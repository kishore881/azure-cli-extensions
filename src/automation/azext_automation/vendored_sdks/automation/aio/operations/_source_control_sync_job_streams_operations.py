# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._source_control_sync_job_streams_operations import build_get_request, build_list_by_sync_job_request
from .._vendor import MixinABC
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class SourceControlSyncJobStreamsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.automation.aio.AutomationClient`'s
        :attr:`source_control_sync_job_streams` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    @distributed_trace
    def list_by_sync_job(
        self,
        resource_group_name: str,
        automation_account_name: str,
        source_control_name: str,
        source_control_sync_job_id: str,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable[_models.SourceControlSyncJobStreamsListBySyncJob]:
        """Retrieve a list of sync job streams identified by sync job id.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account.
        :type automation_account_name: str
        :param source_control_name: The source control name.
        :type source_control_name: str
        :param source_control_sync_job_id: The source control sync job id.
        :type source_control_sync_job_id: str
        :param filter: The filter to apply on the operation. Default value is None.
        :type filter: str
        :keyword api_version: Api Version. Default value is "2020-01-13-preview". Note that overriding
         this default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SourceControlSyncJobStreamsListBySyncJob or the
         result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.automation.models.SourceControlSyncJobStreamsListBySyncJob]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2020-01-13-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.SourceControlSyncJobStreamsListBySyncJob]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_sync_job_request(
                    resource_group_name=resource_group_name,
                    automation_account_name=automation_account_name,
                    source_control_name=source_control_name,
                    source_control_sync_job_id=source_control_sync_job_id,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    filter=filter,
                    template_url=self.list_by_sync_job.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_by_sync_job_request(
                    resource_group_name=resource_group_name,
                    automation_account_name=automation_account_name,
                    source_control_name=source_control_name,
                    source_control_sync_job_id=source_control_sync_job_id,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    filter=filter,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("SourceControlSyncJobStreamsListBySyncJob", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_sync_job.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/sourceControls/{sourceControlName}/sourceControlSyncJobs/{sourceControlSyncJobId}/streams"}  # type: ignore

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        automation_account_name: str,
        source_control_name: str,
        source_control_sync_job_id: str,
        stream_id: str,
        **kwargs: Any
    ) -> _models.SourceControlSyncJobStreamById:
        """Retrieve a sync job stream identified by stream id.

        :param resource_group_name: Name of an Azure Resource group.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account.
        :type automation_account_name: str
        :param source_control_name: The source control name.
        :type source_control_name: str
        :param source_control_sync_job_id: The source control sync job id.
        :type source_control_sync_job_id: str
        :param stream_id: The id of the sync job stream.
        :type stream_id: str
        :keyword api_version: Api Version. Default value is "2020-01-13-preview". Note that overriding
         this default value may result in unsupported behavior.
        :paramtype api_version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SourceControlSyncJobStreamById, or the result of cls(response)
        :rtype: ~azure.mgmt.automation.models.SourceControlSyncJobStreamById
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', "2020-01-13-preview"))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.SourceControlSyncJobStreamById]

        
        request = build_get_request(
            resource_group_name=resource_group_name,
            automation_account_name=automation_account_name,
            source_control_name=source_control_name,
            source_control_sync_job_id=source_control_sync_job_id,
            stream_id=stream_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('SourceControlSyncJobStreamById', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/sourceControls/{sourceControlName}/sourceControlSyncJobs/{sourceControlSyncJobId}/streams/{streamId}"}  # type: ignore
