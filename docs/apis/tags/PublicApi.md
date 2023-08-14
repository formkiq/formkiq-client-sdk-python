<a id="__pageTop"></a>
# formkiq_client.apis.tags.public_api.PublicApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_add_document**](#public_add_document) | **post** /public/documents | 
[**public_add_webhook**](#public_add_webhook) | **post** /public/webhooks/{webhooks+} | 

# **public_add_document**
<a id="public_add_document"></a>
> DocumentId public_add_document(add_document_request)



Allow unauthenticated creation of new documents; must be enabled during installation (disabled by default)

### Example

```python
import formkiq_client
from formkiq_client.apis.tags import public_api
from formkiq_client.model.document_id import DocumentId
from formkiq_client.model.add_document_request import AddDocumentRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = AddDocumentRequest(
        tag_schema_id="tag_schema_id_example",
        path="path_example",
        content_type="content_type_example",
        is_base64=True,
        content="content_example",
        tags=[
            AddDocumentTag(
                key="key_example",
                value="value_example",
                values=[
                    "values_example"
                ],
            )
        ],
        metadata=[
            AddDocumentMetadata(
                key="key_example",
                value="value_example",
                values=[
                    "values_example"
                ],
            )
        ],
        actions=[
            AddAction(
                type="OCR",
                parameters=AddActionParameters(
                    ocr_parse_types="ocr_parse_types_example",
                    add_pdf_detected_characters_as_text=True,
                    url="url_example",
                    character_max="character_max_example",
                    engine="chatgpt",
                    tags="tags_example",
                ),
            )
        ],
        documents=[
            AddChildDocument(
                path="path_example",
                content_type="content_type_example",
                is_base64=True,
                content="content_example",
            )
        ],
    )
    try:
        api_response = api_instance.public_add_document(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except formkiq_client.ApiException as e:
        print("Exception when calling PublicApi->public_add_document: %s\n" % e)

    # example passing only optional values
    query_params = {
        'siteId': "siteId_example",
    }
    body = AddDocumentRequest(
        tag_schema_id="tag_schema_id_example",
        path="path_example",
        content_type="content_type_example",
        is_base64=True,
        content="content_example",
        tags=[
            AddDocumentTag(
                key="key_example",
                value="value_example",
                values=[
                    "values_example"
                ],
            )
        ],
        metadata=[
            AddDocumentMetadata(
                key="key_example",
                value="value_example",
                values=[
                    "values_example"
                ],
            )
        ],
        actions=[
            AddAction(
                type="OCR",
                parameters=AddActionParameters(
                    ocr_parse_types="ocr_parse_types_example",
                    add_pdf_detected_characters_as_text=True,
                    url="url_example",
                    character_max="character_max_example",
                    engine="chatgpt",
                    tags="tags_example",
                ),
            )
        ],
        documents=[
            AddChildDocument(
                path="path_example",
                content_type="content_type_example",
                is_base64=True,
                content="content_example",
            )
        ],
    )
    try:
        api_response = api_instance.public_add_document(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except formkiq_client.ApiException as e:
        print("Exception when calling PublicApi->public_add_document: %s\n" % e)
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
[**AddDocumentRequest**](../../models/AddDocumentRequest.md) |  | 


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
201 | [ApiResponseFor201](#public_add_document.ApiResponseFor201) | 201 CREATED

#### public_add_document.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor201 |  |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DocumentId**](../../models/DocumentId.md) |  | 

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

# **public_add_webhook**
<a id="public_add_webhook"></a>
> DocumentId public_add_webhook(webhooksbody)



Receive an incoming public post to a specified webhook and creates a document based on the data sent; must be enabled during installation (disabled by default)

### Example

```python
import formkiq_client
from formkiq_client.apis.tags import public_api
from formkiq_client.model.document_id import DocumentId
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'webhooks+': "webhooks+_example",
    }
    query_params = {
    }
    body = dict()
    try:
        api_response = api_instance.public_add_webhook(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except formkiq_client.ApiException as e:
        print("Exception when calling PublicApi->public_add_webhook: %s\n" % e)

    # example passing only optional values
    path_params = {
        'webhooks+': "webhooks+_example",
    }
    query_params = {
        'siteId': "siteId_example",
    }
    body = dict()
    try:
        api_response = api_instance.public_add_webhook(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except formkiq_client.ApiException as e:
        print("Exception when calling PublicApi->public_add_webhook: %s\n" % e)
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

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

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
webhooks+ | WebhooksSchema | | 

# WebhooksSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#public_add_webhook.ApiResponseFor200) | 200 OK

#### public_add_webhook.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DocumentId**](../../models/DocumentId.md) |  | 

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

