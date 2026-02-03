import { CallToolResult } from '@modelcontextprotocol/sdk/types.js';
import { Ok } from 'ts-results-es';
import { z } from 'zod';

import { getConfig } from '../../config.js';
import { useRestApi } from '../../restApiInstance.js';
import { Job } from '../../sdks/tableau/types/job.js';
import { Server } from '../../server.js';
import { getTableauAuthInfo } from '../../server/oauth/getTableauAuthInfo.js';
import { Tool } from '../tool.js';

const paramsSchema = {
  jobId: z.string().describe('The ID of the job to check status for'),
};

/**
 * Helper function to interpret job finish codes
 */
function getFinishCodeDescription(finishCode: number | undefined): string {
  if (finishCode === undefined) {
    return 'In Progress';
  }
  switch (finishCode) {
    case 0:
      return 'Success';
    case 1:
      return 'Failed';
    case 2:
      return 'Cancelled';
    default:
      return `Unknown (${finishCode})`;
  }
}

export const getGetJobStatusTool = (server: Server): Tool<typeof paramsSchema> => {
  const getJobStatusTool = new Tool({
    server,
    name: 'get-job-status',
    description: `Returns the status of an asynchronous job on Tableau Server.

**Use Cases:**
- Check the progress of an extract refresh triggered by refresh-workbook-extract
- Monitor any background job running on Tableau Server

**Response Fields:**
- id: The job ID
- type: The type of job (e.g., "RefreshExtract")
- progress: Percentage complete (0-100), may be undefined while queued
- finishCode: Job result (0 = success, 1 = failed, 2 = cancelled, undefined = in progress)
- status: Human-readable status description
- createdAt: When the job was created
- startedAt: When the job started executing
- completedAt: When the job finished (only present if complete)
- notes: Any error messages or warnings from the job

**Polling Recommendation:**
For extract refreshes, poll every 10-30 seconds until completedAt is present.`,
    paramsSchema,
    annotations: {
      title: 'Get Job Status',
      readOnlyHint: true,
      openWorldHint: false,
    },
    callback: async ({ jobId }, { requestId, authInfo, signal }): Promise<CallToolResult> => {
      const config = getConfig();

      return await getJobStatusTool.logAndExecute<Job>({
        requestId,
        authInfo,
        args: { jobId },
        callback: async () => {
          return new Ok(
            await useRestApi({
              config,
              requestId,
              server,
              jwtScopes: ['tableau:tasks:read'],
              signal,
              authInfo: getTableauAuthInfo(authInfo),
              callback: async (restApi) => {
                return await restApi.jobsMethods.getJob({
                  jobId,
                  siteId: restApi.siteId,
                });
              },
            }),
          );
        },
        constrainSuccessResult: (job) => ({
          type: 'success',
          result: {
            id: job.id,
            type: job.type,
            progress: job.progress,
            finishCode: job.finishCode,
            status: getFinishCodeDescription(job.finishCode),
            createdAt: job.createdAt,
            startedAt: job.startedAt,
            completedAt: job.completedAt,
            notes: job.notes?.note,
            isComplete: job.completedAt !== undefined,
            isSuccess: job.finishCode === 0,
          },
        }),
      });
    },
  });

  return getJobStatusTool;
};
