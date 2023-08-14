<a id="__pageTop"></a>
# formkiq_client.apis.tags.document_search_api.DocumentSearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**document_search**](#document_search) | **post** /search | 

# **document_search**
<a id="document_search"></a>
> DocumentSearchResponse document_search(document_search_request)



Document search query request; documents are searched primarily using a document tag key and optional tag value, or if Typesense is enabled, searches on the document path and versioned metadata is also available. An optional documentIds parameter is also available in the DocumentSearchBody to filter, with up to 100 documentIds accepted.

### Example

```python
import formkiq_client
from formkiq_client.apis.tags import document_search_api
from formkiq_client.model.document_search_request import DocumentSearchRequest
from formkiq_client.model.document_search_response import DocumentSearchResponse
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
    api_instance = document_search_api.DocumentSearchApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = DocumentSearchRequest(
        query=DocumentSearch(
            text="text_example",
            meta=DocumentSearchItemMeta(
                folder="folder_example",
                path="path_example",
                index_type="folder",
                index_filter_begins_with="index_filter_begins_with_example",
            ),
            tag=DocumentSearchItemTag(
                begins_with="begins_with_example",
                eq="eq_example",
                eq_or=[
                    "eq_or_example"
                ],
                key="key_example",
            ),
            document_ids=[
                "document_ids_example"
            ],
        ),
        response_fields=SearchResponseFields(None),
    )
    try:
        api_response = api_instance.document_search(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentSearchApi->document_search: %s\n" % e)

    # example passing only optional values
    query_params = {
        'siteId': "siteId_example",
        'limit': "10",
        'next': "next_example",
        'previous': "previous_example",
    }
    body = DocumentSearchRequest(
        query=DocumentSearch(
            text="text_example",
            meta=DocumentSearchItemMeta(
                folder="folder_example",
                path="path_example",
                index_type="folder",
                index_filter_begins_with="index_filter_begins_with_example",
            ),
            tag=DocumentSearchItemTag(
                begins_with="begins_with_example",
                eq="eq_example",
                eq_or=[
                    "eq_or_example"
                ],
                key="key_example",
            ),
            document_ids=[
                "document_ids_example"
            ],
        ),
        response_fields=SearchResponseFields(None),
    )
    try:
        api_response = api_instance.document_search(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except formkiq_client.ApiException as e:
        print("Exception when calling DocumentSearchApi->document_search: %s\n" % e)
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
[**DocumentSearchRequest**](../../models/DocumentSearchRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
siteId | SiteIdSchema | | optional
limit | LimitSchema | | optional
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#document_search.ApiResponseFor200) | 200 OK

#### document_search.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DocumentSearchResponse**](../../models/DocumentSearchResponse.md) |  | 

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

