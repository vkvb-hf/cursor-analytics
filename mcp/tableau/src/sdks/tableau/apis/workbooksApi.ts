import { makeApi, makeEndpoint, ZodiosEndpointDefinitions } from '@zodios/core';
import { z } from 'zod';

import { paginationSchema } from '../types/pagination.js';
import { workbookSchema } from '../types/workbook.js';
import { refreshJobSchema } from '../types/job.js';
import { paginationParameters } from './paginationParameters.js';

const getWorkbookEndpoint = makeEndpoint({
  method: 'get',
  path: '/sites/:siteId/workbooks/:workbookId',
  alias: 'getWorkbook',
  description:
    'Returns information about the specified workbook, including information about views and tags.',
  response: z.object({ workbook: workbookSchema }),
});

const queryWorkbooksForSiteEndpoint = makeEndpoint({
  method: 'get',
  path: '/sites/:siteId/workbooks',
  alias: 'queryWorkbooksForSite',
  description: 'Returns the workbooks on a site.',
  parameters: [
    ...paginationParameters,
    {
      name: 'siteId',
      type: 'Path',
      schema: z.string(),
    },
    {
      name: 'filter',
      type: 'Query',
      schema: z.string().optional(),
      description:
        'An expression that lets you specify a subset of workbooks to return. You can filter on predefined fields such as name, tags, and createdAt. You can include multiple filter expressions.',
    },
  ],
  response: z.object({
    pagination: paginationSchema,
    workbooks: z.object({
      workbook: z.optional(z.array(workbookSchema)),
    }),
  }),
});

/**
 * Refresh workbook extract endpoint
 * @link https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_ref_extract_and_encryption.htm#update_workbook_now
 */
const refreshWorkbookExtractEndpoint = makeEndpoint({
  method: 'post',
  path: '/sites/:siteId/workbooks/:workbookId/refresh',
  alias: 'refreshWorkbookExtract',
  description: 'Initiates a refresh of the extracts in a workbook. This is an asynchronous operation.',
  requestFormat: 'json',
  parameters: [
    {
      name: 'body',
      type: 'Body',
      schema: z.object({}).optional(),
    },
  ],
  response: z.object({ job: refreshJobSchema }),
});

const workbooksApi = makeApi([queryWorkbooksForSiteEndpoint, getWorkbookEndpoint, refreshWorkbookExtractEndpoint]);

export const workbooksApis = [...workbooksApi] as const satisfies ZodiosEndpointDefinitions;
