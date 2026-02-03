import { Zodios } from '@zodios/core';

import { AxiosRequestConfig } from '../../../utils/axios.js';
import { jobsApis } from '../apis/jobsApi.js';
import { Credentials } from '../types/credentials.js';
import { Job } from '../types/job.js';
import AuthenticatedMethods from './authenticatedMethods.js';

/**
 * Jobs methods of the Tableau Server REST API
 *
 * @export
 * @class JobsMethods
 * @link https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_ref_jobs_tasks_and_schedules.htm
 */
export default class JobsMethods extends AuthenticatedMethods<typeof jobsApis> {
  constructor(baseUrl: string, creds: Credentials, axiosConfig: AxiosRequestConfig) {
    super(new Zodios(baseUrl, jobsApis, { axiosConfig }), creds);
  }

  /**
   * Returns status information about an asynchronous job.
   *
   * Required scopes: `tableau:tasks:read`
   *
   * @param {string} jobId The ID of the job to get status for.
   * @param {string} siteId - The Tableau site ID
   * @link https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_ref_jobs_tasks_and_schedules.htm#query_job
   */
  getJob = async ({
    jobId,
    siteId,
  }: {
    jobId: string;
    siteId: string;
  }): Promise<Job> => {
    return (
      await this._apiClient.getJob({
        params: { siteId, jobId },
        ...this.authHeader,
      })
    ).job;
  };
}
