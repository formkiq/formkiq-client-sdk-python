<a id="__pageTop"></a>
# formkiq_client.apis.tags.document_tags_api.DocumentTagsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_document_tags**](#add_document_tags) | **post** /documents/{documentId}/tags | 
[**delete_document_tag**](#delete_document_tag) | **delete** /documents/{documentId}/tags/{tagKey} | 
[**delete_document_tag_and_value**](#delete_document_tag_and_value) | **delete** /documents/{documentId}/tags/{tagKey}/{tagValue} | 
[**get_document_tag**](#get_document_tag) | **get** /documents/{documentId}/tags/{tagKey} | 
[**get_document_tags**](#get_document_tags) | **get** /documents/{documentId}/tags | 
[**set_document_tag**](#set_document_tag) | **put** /documents/{documentId}/tags/{tagKey} | 
[**set_document_tags**](#set_document_tags) | **put** /documents/{documentId}/tags | 
[**update_document_tags**](#update_document_tags) | **patch** /documents/{documentId}/tags | 
[**update_matching_document_tags**](#update_matching_document_tags) | **patch** /documents/tags | 

# **add_document_tags**
<a id="add_document_tags"></a>
> add_document_tags(document_idadd_document_tags_request)



Add multiple tags to a document; this endpoint also accepts a different body parameter for adding a single tag

### Example

```python
import formkiq_client
from formkiq_client.apis.tags import document_tags_api
from formkiq_client.model.add_document_tags_request import AddDocumentTagsRequest
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
    api_instance = document_tags_api.DocumentTagsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'documentId': "documentId_example",
    }
    query_params = {
    }
    body = AddDocumentTagsRequest(
        tags=[
            AddDocumentTag(
                key="key_example",
                value="value_example",
                values=[
                    "values_example"
                ],
            )
        ],
    )
    try:
        api_response = api_instance.add_document_tags(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentTagsApi->add_document_tags: %s\n" % e)

    # example passing only optional values
    path_params = {
        'documentId': "documentId_example",
    }
    query_params = {
        'siteId': "siteId_example",
    }
    body = AddDocumentTagsRequest(
        tags=[
            AddDocumentTag(
                key="key_example",
                value="value_example",
                values=[
                    "values_example"
                ],
            )
        ],
    )
    try:
        api_response = api_instance.add_document_tags(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentTagsApi->add_document_tags: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AddDocumentTagsRequest**](../../models/AddDocumentTagsRequest.md) |  | 


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
201 | [ApiResponseFor201](#add_document_tags.ApiResponseFor201) | 200 OK

#### add_document_tags.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | ResponseHeadersFor201 |  |
#### ResponseHeadersFor201

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

# **delete_document_tag**
<a id="delete_document_tag"></a>
> delete_document_tag(document_idtag_key)



Delete a document tag by using its key

### Example

```python
import formkiq_client
from formkiq_client.apis.tags import document_tags_api
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
    api_instance = document_tags_api.DocumentTagsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'documentId': "documentId_example",
        'tagKey': "tagKey_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.delete_document_tag(
            path_params=path_params,
            query_params=query_params,
        )
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentTagsApi->delete_document_tag: %s\n" % e)

    # example passing only optional values
    path_params = {
        'documentId': "documentId_example",
        'tagKey': "tagKey_example",
    }
    query_params = {
        'siteId': "siteId_example",
    }
    try:
        api_response = api_instance.delete_document_tag(
            path_params=path_params,
            query_params=query_params,
        )
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentTagsApi->delete_document_tag: %s\n" % e)
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
tagKey | TagKeySchema | | 

# DocumentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TagKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_document_tag.ApiResponseFor200) | 200 OK

#### delete_document_tag.ApiResponseFor200
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

# **delete_document_tag_and_value**
<a id="delete_document_tag_and_value"></a>
> delete_document_tag_and_value(document_idtag_keytag_value)



Delete a specific document tag's key/value combination; the request will be ignored if there is no valid key/value combination found

### Example

```python
import formkiq_client
from formkiq_client.apis.tags import document_tags_api
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
    api_instance = document_tags_api.DocumentTagsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'documentId': "documentId_example",
        'tagKey': "tagKey_example",
        'tagValue': "tagValue_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.delete_document_tag_and_value(
            path_params=path_params,
            query_params=query_params,
        )
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentTagsApi->delete_document_tag_and_value: %s\n" % e)

    # example passing only optional values
    path_params = {
        'documentId': "documentId_example",
        'tagKey': "tagKey_example",
        'tagValue': "tagValue_example",
    }
    query_params = {
        'siteId': "siteId_example",
        'shareKey': "shareKey_example",
    }
    try:
        api_response = api_instance.delete_document_tag_and_value(
            path_params=path_params,
            query_params=query_params,
        )
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentTagsApi->delete_document_tag_and_value: %s\n" % e)
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
siteId | SiteIdSchema | | optional
shareKey | ShareKeySchema | | optional


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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
documentId | DocumentIdSchema | | 
tagKey | TagKeySchema | | 
tagValue | TagValueSchema | | 

# DocumentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TagKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TagValueSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_document_tag_and_value.ApiResponseFor200) | 200 OK

#### delete_document_tag_and_value.ApiResponseFor200
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

# **get_document_tag**
<a id="get_document_tag"></a>
> GetDocumentTagResponse get_document_tag(document_idtag_key)



Get a document tag by using its key

### Example

```python
import formkiq_client
from formkiq_client.apis.tags import document_tags_api
from formkiq_client.model.get_document_tag_response import GetDocumentTagResponse
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
    api_instance = document_tags_api.DocumentTagsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'documentId': "documentId_example",
        'tagKey': "tagKey_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.get_document_tag(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentTagsApi->get_document_tag: %s\n" % e)

    # example passing only optional values
    path_params = {
        'documentId': "documentId_example",
        'tagKey': "tagKey_example",
    }
    query_params = {
        'siteId': "siteId_example",
        'shareKey': "shareKey_example",
    }
    try:
        api_response = api_instance.get_document_tag(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentTagsApi->get_document_tag: %s\n" % e)
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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
documentId | DocumentIdSchema | | 
tagKey | TagKeySchema | | 

# DocumentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TagKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_document_tag.ApiResponseFor200) | 200 OK

#### get_document_tag.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetDocumentTagResponse**](../../models/GetDocumentTagResponse.md) |  | 

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

# **get_document_tags**
<a id="get_document_tags"></a>
> GetDocumentTagsResponse get_document_tags(document_id)



Get a listing of a document's tags

### Example

```python
import formkiq_client
from formkiq_client.apis.tags import document_tags_api
from formkiq_client.model.get_document_tags_response import GetDocumentTagsResponse
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
    api_instance = document_tags_api.DocumentTagsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'documentId': "documentId_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.get_document_tags(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentTagsApi->get_document_tags: %s\n" % e)

    # example passing only optional values
    path_params = {
        'documentId': "documentId_example",
    }
    query_params = {
        'siteId': "siteId_example",
        'limit': "10",
        'shareKey': "shareKey_example",
        'next': "next_example",
        'previous': "previous_example",
    }
    try:
        api_response = api_instance.get_document_tags(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentTagsApi->get_document_tags: %s\n" % e)
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
limit | LimitSchema | | optional
shareKey | ShareKeySchema | | optional
next | NextSchema | | optional
previous | PreviousSchema | | optional


# SiteIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "10"

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

# PreviousSchema

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
200 | [ApiResponseFor200](#get_document_tags.ApiResponseFor200) | 200 OK

#### get_document_tags.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetDocumentTagsResponse**](../../models/GetDocumentTagsResponse.md) |  | 

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

# **set_document_tag**
<a id="set_document_tag"></a>
> set_document_tag(document_idtag_keyset_document_tag_key_request)



Update any and all values of a document tag, by using its key; you can supply one tag value or a list of tag values in the request body

### Example

```python
import formkiq_client
from formkiq_client.apis.tags import document_tags_api
from formkiq_client.model.set_document_tag_key_request import SetDocumentTagKeyRequest
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
    api_instance = document_tags_api.DocumentTagsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'documentId': "documentId_example",
        'tagKey': "tagKey_example",
    }
    query_params = {
    }
    body = SetDocumentTagKeyRequest(
        value="value_example",
        values=[
            "values_example"
        ],
    )
    try:
        api_response = api_instance.set_document_tag(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentTagsApi->set_document_tag: %s\n" % e)

    # example passing only optional values
    path_params = {
        'documentId': "documentId_example",
        'tagKey': "tagKey_example",
    }
    query_params = {
        'siteId': "siteId_example",
    }
    body = SetDocumentTagKeyRequest(
        value="value_example",
        values=[
            "values_example"
        ],
    )
    try:
        api_response = api_instance.set_document_tag(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentTagsApi->set_document_tag: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SetDocumentTagKeyRequest**](../../models/SetDocumentTagKeyRequest.md) |  | 


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
tagKey | TagKeySchema | | 

# DocumentIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TagKeySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#set_document_tag.ApiResponseFor200) | 200 OK

#### set_document_tag.ApiResponseFor200
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

# **set_document_tags**
<a id="set_document_tags"></a>
> set_document_tags(document_idadd_document_tags_request)



Set multiple tags to a document; this endpoint also accepts a different body parameter for setting a single tag

### Example

```python
import formkiq_client
from formkiq_client.apis.tags import document_tags_api
from formkiq_client.model.add_document_tags_request import AddDocumentTagsRequest
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
    api_instance = document_tags_api.DocumentTagsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'documentId': "documentId_example",
    }
    query_params = {
    }
    body = AddDocumentTagsRequest(
        tags=[
            AddDocumentTag(
                key="key_example",
                value="value_example",
                values=[
                    "values_example"
                ],
            )
        ],
    )
    try:
        api_response = api_instance.set_document_tags(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentTagsApi->set_document_tags: %s\n" % e)

    # example passing only optional values
    path_params = {
        'documentId': "documentId_example",
    }
    query_params = {
        'siteId': "siteId_example",
    }
    body = AddDocumentTagsRequest(
        tags=[
            AddDocumentTag(
                key="key_example",
                value="value_example",
                values=[
                    "values_example"
                ],
            )
        ],
    )
    try:
        api_response = api_instance.set_document_tags(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentTagsApi->set_document_tags: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AddDocumentTagsRequest**](../../models/AddDocumentTagsRequest.md) |  | 


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
200 | [ApiResponseFor200](#set_document_tags.ApiResponseFor200) | 200 OK

#### set_document_tags.ApiResponseFor200
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

# **update_document_tags**
<a id="update_document_tags"></a>
> update_document_tags(document_idadd_document_tags_request)



Updates multiple tags to a document; this endpoint also accepts a different body parameter for updating a single tag

### Example

```python
import formkiq_client
from formkiq_client.apis.tags import document_tags_api
from formkiq_client.model.add_document_tags_request import AddDocumentTagsRequest
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
    api_instance = document_tags_api.DocumentTagsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'documentId': "documentId_example",
    }
    query_params = {
    }
    body = AddDocumentTagsRequest(
        tags=[
            AddDocumentTag(
                key="key_example",
                value="value_example",
                values=[
                    "values_example"
                ],
            )
        ],
    )
    try:
        api_response = api_instance.update_document_tags(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentTagsApi->update_document_tags: %s\n" % e)

    # example passing only optional values
    path_params = {
        'documentId': "documentId_example",
    }
    query_params = {
        'siteId': "siteId_example",
    }
    body = AddDocumentTagsRequest(
        tags=[
            AddDocumentTag(
                key="key_example",
                value="value_example",
                values=[
                    "values_example"
                ],
            )
        ],
    )
    try:
        api_response = api_instance.update_document_tags(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentTagsApi->update_document_tags: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AddDocumentTagsRequest**](../../models/AddDocumentTagsRequest.md) |  | 


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
200 | [ApiResponseFor200](#update_document_tags.ApiResponseFor200) | 200 OK

#### update_document_tags.ApiResponseFor200
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

# **update_matching_document_tags**
<a id="update_matching_document_tags"></a>
> UpdateMatchingDocumentTagsResponse update_matching_document_tags(update_matching_document_tags_request)



This API request allows the adding/updating of multiple document tag(s) based on document(s) that have the matching tag.

### Example

```python
import formkiq_client
from formkiq_client.apis.tags import document_tags_api
from formkiq_client.model.update_matching_document_tags_request import UpdateMatchingDocumentTagsRequest
from formkiq_client.model.update_matching_document_tags_response import UpdateMatchingDocumentTagsResponse
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
    api_instance = document_tags_api.DocumentTagsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = UpdateMatchingDocumentTagsRequest(
        match=dict(
            tag=MatchDocumentTag(
                key="key_example",
                begins_with="begins_with_example",
                eq="eq_example",
            ),
        ),
        update=dict(
            tags=[
                AddDocumentTag(
                    key="key_example",
                    value="value_example",
                    values=[
                        "values_example"
                    ],
                )
            ],
        ),
    )
    try:
        api_response = api_instance.update_matching_document_tags(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentTagsApi->update_matching_document_tags: %s\n" % e)

    # example passing only optional values
    query_params = {
        'siteId': "siteId_example",
    }
    body = UpdateMatchingDocumentTagsRequest(
        match=dict(
            tag=MatchDocumentTag(
                key="key_example",
                begins_with="begins_with_example",
                eq="eq_example",
            ),
        ),
        update=dict(
            tags=[
                AddDocumentTag(
                    key="key_example",
                    value="value_example",
                    values=[
                        "values_example"
                    ],
                )
            ],
        ),
    )
    try:
        api_response = api_instance.update_matching_document_tags(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentTagsApi->update_matching_document_tags: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateMatchingDocumentTagsRequest**](../../models/UpdateMatchingDocumentTagsRequest.md) |  | 


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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_matching_document_tags.ApiResponseFor200) | 200 OK

#### update_matching_document_tags.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateMatchingDocumentTagsResponse**](../../models/UpdateMatchingDocumentTagsResponse.md) |  | 

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

