import { CallToolResult } from '@modelcontextprotocol/sdk/types.js';
import { Err, Ok } from 'ts-results-es';
import { z } from 'zod';

import { getConfig } from '../../config.js';
import { useRestApi } from '../../restApiInstance.js';
import { RefreshJob } from '../../sdks/tableau/types/job.js';
import { Server } from '../../server.js';
import { getTableauAuthInfo } from '../../server/oauth/getTableauAuthInfo.js';
import { resourceAccessChecker } from '../resourceAccessChecker.js';
import { Tool } from '../tool.js';

const paramsSchema = {
  workbookId: z.string().describe('The ID of the workbook to refresh'),
};

export type RefreshWorkbookExtractError = {
  type: 'workbook-not-allowed' | 'refresh-failed';
  message: string;
};

export const getRefreshWorkbookExtractTool = (server: Server): Tool<typeof paramsSchema> => {
  const refreshTool = new Tool({
    server,
    name: 'refresh-workbook-extract',
    description: `Triggers an extract refresh for the specified workbook. Returns a job ID that can be used to track the refresh status using the get-job-status tool.

**Important:** This is an asynchronous operation. The tool returns immediately with a job ID. The actual refresh runs in the background on Tableau Server.

**Requirements:**
- The workbook must have extracts (embedded data sources with extracts)
- The user must have permission to refresh the workbook

**Response:**
- jobId: The ID of the refresh job
- mode: The job mode (typically "Asynchronous")
- type: The job type (typically "RefreshExtract")

**Next Steps:**
After triggering a refresh, use the get-job-status tool with the returned jobId to check:
- progress: Percentage complete (0-100)
- finishCode: 0 = success, other values indicate errors
- completedAt: When the job finished`,
    paramsSchema,
    annotations: {
      title: 'Refresh Workbook Extract',
      readOnlyHint: false, // This is a WRITE operation
      openWorldHint: false,
    },
    callback: async ({ workbookId }, { requestId, authInfo, signal }): Promise<CallToolResult> => {
      const config = getConfig();

      return await refreshTool.logAndExecute<RefreshJob, RefreshWorkbookExtractError>({
        requestId,
        authInfo,
        args: { workbookId },
        callback: async () => {
          // Check if workbook is allowed
          const isWorkbookAllowedResult = await resourceAccessChecker.isWorkbookAllowed({
            workbookId,
            restApiArgs: { config, requestId, server, signal },
          });

          if (!isWorkbookAllowedResult.allowed) {
            return new Err({
              type: 'workbook-not-allowed',
              message: isWorkbookAllowedResult.message,
            });
          }

          return new Ok(
            await useRestApi({
              config,
              requestId,
              server,
              jwtScopes: ['tableau:tasks:run'],
              signal,
              authInfo: getTableauAuthInfo(authInfo),
              callback: async (restApi) => {
                return await restApi.workbooksMethods.refreshWorkbookExtract({
                  workbookId,
                  siteId: restApi.siteId,
                });
              },
            }),
          );
        },
        constrainSuccessResult: (result) => ({
          type: 'success',
          result: {
            jobId: result.id,
            mode: result.mode,
            type: result.type,
            message: `Extract refresh triggered successfully. Use get-job-status with jobId "${result.id}" to check progress.`,
          },
        }),
        getErrorText: (error: RefreshWorkbookExtractError) => {
          switch (error.type) {
            case 'workbook-not-allowed':
              return error.message;
            case 'refresh-failed':
              return `Failed to trigger extract refresh: ${error.message}`;
          }
        },
      });
    },
  });

  return refreshTool;
};
