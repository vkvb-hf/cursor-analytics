import { z } from 'zod';

/**
 * Schema for a Tableau job response
 * @link https://help.tableau.com/current/api/rest_api/en-us/REST/rest_api_ref_jobs_tasks_and_schedules.htm#query_job
 */
export const jobSchema = z.object({
  id: z.string(),
  mode: z.string().optional(),
  type: z.string(),
  progress: z.number().optional(),
  finishCode: z.number().optional(),
  createdAt: z.string().optional(),
  startedAt: z.string().optional(),
  completedAt: z.string().optional(),
  notes: z
    .object({
      note: z.array(z.string()).optional(),
    })
    .optional(),
});

export type Job = z.infer<typeof jobSchema>;

/**
 * Schema for the job response from refresh workbook extract
 */
export const refreshJobSchema = z.object({
  id: z.string(),
  mode: z.string().optional(),
  type: z.string().optional(),
});

export type RefreshJob = z.infer<typeof refreshJobSchema>;
