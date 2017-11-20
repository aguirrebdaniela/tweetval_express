"""Generated client library for cloudscheduler version v1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.cloudscheduler.v1beta1 import cloudscheduler_v1beta1_messages as messages


class CloudschedulerV1beta1(base_api.BaseApiClient):
  """Generated client library for service cloudscheduler version v1beta1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://cloudscheduler.googleapis.com/'

  _PACKAGE = u'cloudscheduler'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1beta1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'CloudschedulerV1beta1'
  _URL_VERSION = u'v1beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new cloudscheduler handle."""
    url = url or self.BASE_URL
    super(CloudschedulerV1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.projects_locations_jobs = self.ProjectsLocationsJobsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsJobsService(base_api.BaseApiService):
    """Service class for the projects_locations_jobs resource."""

    _NAME = u'projects_locations_jobs'

    def __init__(self, client):
      super(CloudschedulerV1beta1.ProjectsLocationsJobsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a job.

      Args:
        request: (CloudschedulerProjectsLocationsJobsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/jobs',
        http_method=u'POST',
        method_id=u'cloudscheduler.projects.locations.jobs.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1beta1/{+parent}/jobs',
        request_field=u'job',
        request_type_name=u'CloudschedulerProjectsLocationsJobsCreateRequest',
        response_type_name=u'Job',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes a job.

      Args:
        request: (CloudschedulerProjectsLocationsJobsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/jobs/{jobsId}',
        http_method=u'DELETE',
        method_id=u'cloudscheduler.projects.locations.jobs.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'CloudschedulerProjectsLocationsJobsDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets a job.

      Args:
        request: (CloudschedulerProjectsLocationsJobsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/jobs/{jobsId}',
        http_method=u'GET',
        method_id=u'cloudscheduler.projects.locations.jobs.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'responseView'],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'CloudschedulerProjectsLocationsJobsGetRequest',
        response_type_name=u'Job',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists jobs.

ListJobsRequest.filter can be used to specify a subset of
jobs. ListJobsRequest.response_view controls the subset of
information returned. By default response_view is
Job.View.BASIC; not all information is returned by default
due to performance considerations.

      Args:
        request: (CloudschedulerProjectsLocationsJobsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListJobsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/jobs',
        http_method=u'GET',
        method_id=u'cloudscheduler.projects.locations.jobs.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken', u'responseView'],
        relative_path=u'v1beta1/{+parent}/jobs',
        request_field='',
        request_type_name=u'CloudschedulerProjectsLocationsJobsListRequest',
        response_type_name=u'ListJobsResponse',
        supports_download=False,
    )

    def Run(self, request, global_params=None):
      """Forces a job to run now.

When this method is called, Cloud Scheduler will immediately attempt the
job. The attempt will be counted in the job's Job.total_attempt_count.

The job's Execution.schedule_time is not modified, so the job
will also be attempted according to its existing
Execution.schedule_time.

      Args:
        request: (CloudschedulerProjectsLocationsJobsRunRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Run')
      return self._RunMethod(
          config, request, global_params=global_params)

    Run.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}/jobs/{jobsId}:run',
        http_method=u'POST',
        method_id=u'cloudscheduler.projects.locations.jobs.run',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}:run',
        request_field=u'runJobRequest',
        request_type_name=u'CloudschedulerProjectsLocationsJobsRunRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = u'projects_locations'

    def __init__(self, client):
      super(CloudschedulerV1beta1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      """Get information about a location.

      Args:
        request: (CloudschedulerProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations/{locationsId}',
        http_method=u'GET',
        method_id=u'cloudscheduler.projects.locations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1beta1/{+name}',
        request_field='',
        request_type_name=u'CloudschedulerProjectsLocationsGetRequest',
        response_type_name=u'Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists information about the supported locations for this service.

      Args:
        request: (CloudschedulerProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1beta1/projects/{projectsId}/locations',
        http_method=u'GET',
        method_id=u'cloudscheduler.projects.locations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1beta1/{+name}/locations',
        request_field='',
        request_type_name=u'CloudschedulerProjectsLocationsListRequest',
        response_type_name=u'ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(CloudschedulerV1beta1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }