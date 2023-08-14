<a id="__pageTop"></a>
# formkiq_client.apis.tags.document_versions_api.DocumentVersionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_document_version**](#delete_document_version) | **delete** /documents/{documentId}/versions/{versionKey} | 
[**get_document_versions**](#get_document_versions) | **get** /documents/{documentId}/versions | 
[**set_document_version**](#set_document_version) | **put** /documents/{documentId}/versions | 

# **delete_document_version**
<a id="delete_document_version"></a>
> delete_document_version(document_idversion_key)



Delete a specific previous document version; ONLY available with FormKiQ Pro and Enterprise

### Example

```python
import formkiq_client
from formkiq_client.apis.tags import document_versions_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = document_versions_api.DocumentVersionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'documentId': "documentId_example",
        'versionKey': "versionKey_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.delete_document_version(
            path_params=path_params,
            query_params=query_params,
        )
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentVersionsApi->delete_document_version: %s\n" % e)

    # example passing only optional values
    path_params = {
        'documentId': "documentId_example",
        'versionKey': "versionKey_example",
    }
    query_params = {
        'shareKey': "shareKey_example",
    }
    try:
        api_response = api_instance.delete_document_version(
            path_params=path_params,
            query_params=query_params,
        )
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentVersionsApi->delete_document_version: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
shareKey | ShareKeySchema | | optional


# ShareKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
documentId | DocumentIdSchema | | 
versionKey | VersionKeySchema | | 

# DocumentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# VersionKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_document_version.ApiResponseFor200) | 200 OK

#### delete_document_version.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | ResponseHeadersFor200 |  |
#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional
Access-Control-Allow-Methods | AccessControlAllowMethodsSchema | | optional
Access-Control-Allow-Headers | AccessControlAllowHeadersSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AccessControlAllowMethodsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AccessControlAllowHeadersSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_document_versions**
<a id="get_document_versions"></a>
> GetDocumentVersionsResponse get_document_versions(document_id)



Get a listing of document content and metadata versions; ONLY available with FormKiQ Pro and Enterprise

### Example

```python
import formkiq_client
from formkiq_client.apis.tags import document_versions_api
from formkiq_client.model.get_document_versions_response import GetDocumentVersionsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = document_versions_api.DocumentVersionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'documentId': "documentId_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.get_document_versions(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentVersionsApi->get_document_versions: %s\n" % e)

    # example passing only optional values
    path_params = {
        'documentId': "documentId_example",
    }
    query_params = {
        'siteId': "siteId_example",
        'shareKey': "shareKey_example",
        'next': "next_example",
    }
    try:
        api_response = api_instance.get_document_versions(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentVersionsApi->get_document_versions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
siteId | SiteIdSchema | | optional
shareKey | ShareKeySchema | | optional
next | NextSchema | | optional


# SiteIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ShareKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NextSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
documentId | DocumentIdSchema | | 

# DocumentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_document_versions.ApiResponseFor200) | 200 OK

#### get_document_versions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetDocumentVersionsResponse**](../../models/GetDocumentVersionsResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional
Access-Control-Allow-Methods | AccessControlAllowMethodsSchema | | optional
Access-Control-Allow-Headers | AccessControlAllowHeadersSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AccessControlAllowMethodsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AccessControlAllowHeadersSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **set_document_version**
<a id="set_document_version"></a>
> SetDocumentVersionResponse set_document_version(document_idset_document_version_request)



Set document to a previous document version; ONLY available with FormKiQ Pro and Enterprise

### Example

```python
import formkiq_client
from formkiq_client.apis.tags import document_versions_api
from formkiq_client.model.set_document_version_response import SetDocumentVersionResponse
from formkiq_client.model.validation_errors_response import ValidationErrorsResponse
from formkiq_client.model.set_document_version_request import SetDocumentVersionRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = document_versions_api.DocumentVersionsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'documentId': "documentId_example",
    }
    query_params = {
    }
    body = SetDocumentVersionRequest(
        version_key="version_key_example",
    )
    try:
        api_response = api_instance.set_document_version(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentVersionsApi->set_document_version: %s\n" % e)

    # example passing only optional values
    path_params = {
        'documentId': "documentId_example",
    }
    query_params = {
        'siteId': "siteId_example",
    }
    body = SetDocumentVersionRequest(
        version_key="version_key_example",
    )
    try:
        api_response = api_instance.set_document_version(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentVersionsApi->set_document_version: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SetDocumentVersionRequest**](../../models/SetDocumentVersionRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
siteId | SiteIdSchema | | optional


# SiteIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
documentId | DocumentIdSchema | | 

# DocumentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#set_document_version.ApiResponseFor200) | 200 OK
400 | [ApiResponseFor400](#set_document_version.ApiResponseFor400) | 400 OK

#### set_document_version.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SetDocumentVersionResponse**](../../models/SetDocumentVersionResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Access-Control-Allow-Origin | AccessControlAllowOriginSchema | | optional
Access-Control-Allow-Methods | AccessControlAllowMethodsSchema | | optional
Access-Control-Allow-Headers | AccessControlAllowHeadersSchema | | optional

# AccessControlAllowOriginSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AccessControlAllowMethodsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AccessControlAllowHeadersSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### set_document_version.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidationErrorsResponse**](../../models/ValidationErrorsResponse.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

