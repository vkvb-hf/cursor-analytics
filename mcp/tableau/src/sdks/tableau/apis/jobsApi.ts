import { makeApi, makeEndpoint, ZodiosEndpointDefinitions } from '@zodios/core';
import { z } from 'zod';

import { jobSchema } from '../types/job.js';

/**
 * Get job endpoint
 * @link https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_ref_jobs_tasks_and_schedules.htm#query_job
 */
const getJobEndpoint = makeEndpoint({
  method: 'get',
  path: '/sites/:siteId/jobs/:jobId',
  alias: 'getJob',
  description: 'Returns status information about an asynchronous job.',
  response: z.object({ job: jobSchema }),
});

const jobsApi = makeApi([getJobEndpoint]);

export const jobsApis = [...jobsApi] as const satisfies ZodiosEndpointDefinitions;
