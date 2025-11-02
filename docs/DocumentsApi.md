# openapi_client.DocumentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_document**](DocumentsApi.md#add_document) | **POST** /documents | Add new document
[**add_document_sync**](DocumentsApi.md#add_document_sync) | **POST** /documents/{documentId}/syncs | Add document sync to service
[**add_document_upload**](DocumentsApi.md#add_document_upload) | **POST** /documents/upload | Add large document
[**compress_documents**](DocumentsApi.md#compress_documents) | **POST** /documents/compress | Compress multiple documents into a .zip file
[**delete_document**](DocumentsApi.md#delete_document) | **DELETE** /documents/{documentId} | Delete document
[**delete_document_checkout_legal_hold**](DocumentsApi.md#delete_document_checkout_legal_hold) | **DELETE** /documents/{documentId}/legalHold | Delete document legal hold checkout
[**delete_published_document_content**](DocumentsApi.md#delete_published_document_content) | **DELETE** /publications/{documentId} | Delete published document&#39;s contents
[**get_document**](DocumentsApi.md#get_document) | **GET** /documents/{documentId} | Get document
[**get_document_content**](DocumentsApi.md#get_document_content) | **GET** /documents/{documentId}/content | Get document&#39;s contents
[**get_document_id_upload**](DocumentsApi.md#get_document_id_upload) | **GET** /documents/{documentId}/upload | Get url to update large document
[**get_document_syncs**](DocumentsApi.md#get_document_syncs) | **GET** /documents/{documentId}/syncs | Get document syncs
[**get_document_upload**](DocumentsApi.md#get_document_upload) | **GET** /documents/upload | Get url to add large document
[**get_document_url**](DocumentsApi.md#get_document_url) | **GET** /documents/{documentId}/url | Get document content url
[**get_documents**](DocumentsApi.md#get_documents) | **GET** /documents | Get Documents listing
[**get_published_document_content**](DocumentsApi.md#get_published_document_content) | **GET** /publications/{documentId} | Get published document&#39;s contents
[**purge_document**](DocumentsApi.md#purge_document) | **DELETE** /documents/{documentId}/purge | Purge document
[**set_document_checkout**](DocumentsApi.md#set_document_checkout) | **PUT** /documents/{documentId}/checkout | Perform document checkout
[**set_document_checkout_legal_hold**](DocumentsApi.md#set_document_checkout_legal_hold) | **PUT** /documents/{documentId}/legalHold | Perform document legal hold checkout
[**set_document_restore**](DocumentsApi.md#set_document_restore) | **PUT** /documents/{documentId}/restore | Restore soft deleted document
[**update_document**](DocumentsApi.md#update_document) | **PATCH** /documents/{documentId} | Update document


# **add_document**
> AddDocumentResponse add_document(add_document_request, site_id=site_id, share_key=share_key)

Add new document

Creates a new document; body may include document content if less than 5 MB.

Returns a unique **documentId** used in subsequent operations.

See POST /documents/{documentId}/tags for adding tags to document schema

See POST /documents/{documentId}/actions for adding actions to document schema

### Example


```python
import openapi_client
from openapi_client.models.add_document_request import AddDocumentRequest
from openapi_client.models.add_document_response import AddDocumentResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentsApi(api_client)
    add_document_request = {"path":"test.txt","contentType":"text/plain","isBase64":false,"content":"This is sample data file","tags":[{"key":"category","value":"sample"},{"key":"players","values":["111","222"]}],"metadata":[{"key":"info","value":"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."}]} # AddDocumentRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)
    share_key = 'share_key_example' # str | Share Identifier (optional)

    try:
        # Add new document
        api_response = api_instance.add_document(add_document_request, site_id=site_id, share_key=share_key)
        print("The response of DocumentsApi->add_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->add_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_document_request** | [**AddDocumentRequest**](AddDocumentRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 
 **share_key** | **str**| Share Identifier | [optional] 

### Return type

[**AddDocumentResponse**](AddDocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 CREATED |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | 400 OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_document_sync**
> AddResponse add_document_sync(document_id, site_id=site_id, add_document_sync_request=add_document_sync_request)

Add document sync to service

Add a document to a service

### Example


```python
import openapi_client
from openapi_client.models.add_document_sync_request import AddDocumentSyncRequest
from openapi_client.models.add_response import AddResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    add_document_sync_request = openapi_client.AddDocumentSyncRequest() # AddDocumentSyncRequest |  (optional)

    try:
        # Add document sync to service
        api_response = api_instance.add_document_sync(document_id, site_id=site_id, add_document_sync_request=add_document_sync_request)
        print("The response of DocumentsApi->add_document_sync:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->add_document_sync: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **add_document_sync_request** | [**AddDocumentSyncRequest**](AddDocumentSyncRequest.md)|  | [optional] 

### Return type

[**AddResponse**](AddResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_document_upload**
> GetDocumentUrlResponse add_document_upload(add_document_upload_request, site_id=site_id, content_length=content_length, duration=duration, share_key=share_key)

Add large document

Returns a URL that can be used to upload document content and create a new document, while allowing metadata to also be sent; this endpoint (whether GET or POST) is required in order to add content that is larger than 5 MB. The POST endpoint allow the adding of document metadata at the same time as the document is created.

### Example


```python
import openapi_client
from openapi_client.models.add_document_upload_request import AddDocumentUploadRequest
from openapi_client.models.get_document_url_response import GetDocumentUrlResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentsApi(api_client)
    add_document_upload_request = {"path":"test.txt","contentType":"text/plain","tags":[{"key":"category","value":"sample"},{"key":"players","values":["111","222"]}],"metadata":[{"key":"info","value":"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."}]} # AddDocumentUploadRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)
    content_length = 56 # int | Indicates the size of the entity-body (optional)
    duration = 56 # int | Indicates the number of hours request is valid for (optional)
    share_key = 'share_key_example' # str | Share Identifier (optional)

    try:
        # Add large document
        api_response = api_instance.add_document_upload(add_document_upload_request, site_id=site_id, content_length=content_length, duration=duration, share_key=share_key)
        print("The response of DocumentsApi->add_document_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->add_document_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_document_upload_request** | [**AddDocumentUploadRequest**](AddDocumentUploadRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 
 **content_length** | **int**| Indicates the size of the entity-body | [optional] 
 **duration** | **int**| Indicates the number of hours request is valid for | [optional] 
 **share_key** | **str**| Share Identifier | [optional] 

### Return type

[**GetDocumentUrlResponse**](GetDocumentUrlResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 CREATED |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compress_documents**
> DocumentsCompressResponse compress_documents(documents_compress_request, site_id=site_id)

Compress multiple documents into a .zip file

Compress documents into an .ZIP archive file, and returns a S3 presigned url for the location of the archive file. The operation is async and processing time depends on the number and size of documents included; a 404 status code is returned until the file is ready.

### Example


```python
import openapi_client
from openapi_client.models.documents_compress_request import DocumentsCompressRequest
from openapi_client.models.documents_compress_response import DocumentsCompressResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentsApi(api_client)
    documents_compress_request = openapi_client.DocumentsCompressRequest() # DocumentsCompressRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Compress multiple documents into a .zip file
        api_response = api_instance.compress_documents(documents_compress_request, site_id=site_id)
        print("The response of DocumentsApi->compress_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->compress_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_compress_request** | [**DocumentsCompressRequest**](DocumentsCompressRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**DocumentsCompressResponse**](DocumentsCompressResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 CREATED |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document**
> DeleteResponse delete_document(document_id, site_id=site_id, soft_delete=soft_delete)

Delete document

Delete a document's details, i.e., metadata, contents, etc

SoftDelete:

The SoftDelete parameter allows for the temporary removal of a document's metadata, attributes, etc from being retrieved from all API requests.

The document can be permanently deleted by calling the DELETE /documents/{documentId} with softDelete=false or restored using the PUT /documents/{documentId}/restore.

Only the GET /documents?deleted=true will return all the soft deleted documents.

### Example


```python
import openapi_client
from openapi_client.models.delete_response import DeleteResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    soft_delete = True # bool | Whether to soft delete document (optional)

    try:
        # Delete document
        api_response = api_instance.delete_document(document_id, site_id=site_id, soft_delete=soft_delete)
        print("The response of DocumentsApi->delete_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->delete_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **soft_delete** | **bool**| Whether to soft delete document | [optional] 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_checkout_legal_hold**
> DeleteResponse delete_document_checkout_legal_hold(document_id, site_id=site_id)

Delete document legal hold checkout

Removes a legal hold checkout for the document; available as an Add-On Module


### Example


```python
import openapi_client
from openapi_client.models.delete_response import DeleteResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Delete document legal hold checkout
        api_response = api_instance.delete_document_checkout_legal_hold(document_id, site_id=site_id)
        print("The response of DocumentsApi->delete_document_checkout_legal_hold:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->delete_document_checkout_legal_hold: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_published_document_content**
> DeleteResponse delete_published_document_content(document_id, site_id=site_id)

Delete published document's contents

Delete a published document's contents. Certain content types, text/*, application/json, and application/x-www-form-urlencoded. return the  "content" field, while all other content types return a 'contentUrl' for retrieving the content.

### Example


```python
import openapi_client
from openapi_client.models.delete_response import DeleteResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Delete published document's contents
        api_response = api_instance.delete_published_document_content(document_id, site_id=site_id)
        print("The response of DocumentsApi->delete_published_document_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->delete_published_document_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> GetDocumentResponse get_document(document_id, site_id=site_id, share_key=share_key)

Get document

Retrieves a document's details, i.e., metadata

### Example


```python
import openapi_client
from openapi_client.models.get_document_response import GetDocumentResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    share_key = 'share_key_example' # str | Share Identifier (optional)

    try:
        # Get document
        api_response = api_instance.get_document(document_id, site_id=site_id, share_key=share_key)
        print("The response of DocumentsApi->get_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->get_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **share_key** | **str**| Share Identifier | [optional] 

### Return type

[**GetDocumentResponse**](GetDocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_content**
> GetDocumentContentResponse get_document_content(document_id, site_id=site_id, version_key=version_key, share_key=share_key)

Get document's contents

Retrieves the content of the document with the specified `documentId`.
- If the content is plain text and under 6 MB, the content will be returned directly.
- If the content is plain text but exceeds 6 MB, an error will be returned.
- For documents not in plain text format, pre-signed S3 URLs will be returned to download the content from S3.
It is recommended to use the `/documents/{documentId}/url` endpoint to retrieve pre-signed S3 URLs for downloading the content.

If the document has a Content-Type of text/, application/json, application/x-www-form-urlencoded the content field will be returned. 
All other Content-Type, the contentUrl field will be returned, which is a S3 Presigned url.


### Example


```python
import openapi_client
from openapi_client.models.get_document_content_response import GetDocumentContentResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    version_key = 'version_key_example' # str | Version Key (version key required URL encoding) (optional)
    share_key = 'share_key_example' # str | Share Identifier (optional)

    try:
        # Get document's contents
        api_response = api_instance.get_document_content(document_id, site_id=site_id, version_key=version_key, share_key=share_key)
        print("The response of DocumentsApi->get_document_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->get_document_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **version_key** | **str**| Version Key (version key required URL encoding) | [optional] 
 **share_key** | **str**| Share Identifier | [optional] 

### Return type

[**GetDocumentContentResponse**](GetDocumentContentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  * Location -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_id_upload**
> GetDocumentUrlResponse get_document_id_upload(document_id, site_id=site_id, checksum_type=checksum_type, checksum=checksum, content_length=content_length, duration=duration, share_key=share_key)

Get url to update large document

Returns a URL that can be used to upload documents for a specific documentId; this endpoint is required in order to add content that is larger than 5 MB. If versions are enabled, this will create a new version of the document.

### Example


```python
import openapi_client
from openapi_client.models.get_document_url_response import GetDocumentUrlResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    checksum_type = 'checksum_type_example' # str | Checksum Type (optional)
    checksum = 'checksum_example' # str | Checksum value (optional)
    content_length = 56 # int | Indicates the size of the entity-body (optional)
    duration = 56 # int | Indicates the number of hours request is valid for (optional)
    share_key = 'share_key_example' # str | Share Identifier (optional)

    try:
        # Get url to update large document
        api_response = api_instance.get_document_id_upload(document_id, site_id=site_id, checksum_type=checksum_type, checksum=checksum, content_length=content_length, duration=duration, share_key=share_key)
        print("The response of DocumentsApi->get_document_id_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->get_document_id_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **checksum_type** | **str**| Checksum Type | [optional] 
 **checksum** | **str**| Checksum value | [optional] 
 **content_length** | **int**| Indicates the size of the entity-body | [optional] 
 **duration** | **int**| Indicates the number of hours request is valid for | [optional] 
 **share_key** | **str**| Share Identifier | [optional] 

### Return type

[**GetDocumentUrlResponse**](GetDocumentUrlResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_syncs**
> GetDocumentSyncResponse get_document_syncs(document_id, site_id=site_id, limit=limit, share_key=share_key)

Get document syncs

Retrieve the document syncs with external services status

### Example


```python
import openapi_client
from openapi_client.models.get_document_sync_response import GetDocumentSyncResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    share_key = 'share_key_example' # str | Share Identifier (optional)

    try:
        # Get document syncs
        api_response = api_instance.get_document_syncs(document_id, site_id=site_id, limit=limit, share_key=share_key)
        print("The response of DocumentsApi->get_document_syncs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->get_document_syncs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **share_key** | **str**| Share Identifier | [optional] 

### Return type

[**GetDocumentSyncResponse**](GetDocumentSyncResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_upload**
> GetDocumentUrlResponse get_document_upload(path=path, site_id=site_id, checksum_type=checksum_type, checksum=checksum, content_length=content_length, duration=duration, share_key=share_key)

Get url to add large document

Returns a URL that can be used to upload document content and create a new document; this endpoint (whether GET or POST) is required in order to add content that is larger than 5 MB

### Example


```python
import openapi_client
from openapi_client.models.get_document_url_response import GetDocumentUrlResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentsApi(api_client)
    path = 'path_example' # str | The upload file's path (optional)
    site_id = 'site_id_example' # str | Site Identifier (optional)
    checksum_type = 'checksum_type_example' # str | Checksum Type (optional)
    checksum = 'checksum_example' # str | Checksum value (optional)
    content_length = 56 # int | Indicates the size of the entity-body (optional)
    duration = 56 # int | Indicates the number of hours request is valid for (optional)
    share_key = 'share_key_example' # str | Share Identifier (optional)

    try:
        # Get url to add large document
        api_response = api_instance.get_document_upload(path=path, site_id=site_id, checksum_type=checksum_type, checksum=checksum, content_length=content_length, duration=duration, share_key=share_key)
        print("The response of DocumentsApi->get_document_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->get_document_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| The upload file&#39;s path | [optional] 
 **site_id** | **str**| Site Identifier | [optional] 
 **checksum_type** | **str**| Checksum Type | [optional] 
 **checksum** | **str**| Checksum value | [optional] 
 **content_length** | **int**| Indicates the size of the entity-body | [optional] 
 **duration** | **int**| Indicates the number of hours request is valid for | [optional] 
 **share_key** | **str**| Share Identifier | [optional] 

### Return type

[**GetDocumentUrlResponse**](GetDocumentUrlResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_url**
> GetDocumentUrlResponse get_document_url(document_id, site_id=site_id, version_key=version_key, duration=duration, share_key=share_key, inline=inline, bypass_watermark=bypass_watermark)

Get document content url

Returns a URL for the document's contents; this URL will expire (the default is 48 hours)

### Example


```python
import openapi_client
from openapi_client.models.get_document_url_response import GetDocumentUrlResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    version_key = 'version_key_example' # str | Version Key (version key required URL encoding) (optional)
    duration = 56 # int | Indicates the number of hours request is valid for (optional)
    share_key = 'share_key_example' # str | Share Identifier (optional)
    inline = False # bool | Set the Content-Disposition to inline (optional) (default to False)
    bypass_watermark = False # bool | Allow the by pass of watermark (only allowed by GOVERN / ADMIN permissions) (optional) (default to False)

    try:
        # Get document content url
        api_response = api_instance.get_document_url(document_id, site_id=site_id, version_key=version_key, duration=duration, share_key=share_key, inline=inline, bypass_watermark=bypass_watermark)
        print("The response of DocumentsApi->get_document_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->get_document_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **version_key** | **str**| Version Key (version key required URL encoding) | [optional] 
 **duration** | **int**| Indicates the number of hours request is valid for | [optional] 
 **share_key** | **str**| Share Identifier | [optional] 
 **inline** | **bool**| Set the Content-Disposition to inline | [optional] [default to False]
 **bypass_watermark** | **bool**| Allow the by pass of watermark (only allowed by GOVERN / ADMIN permissions) | [optional] [default to False]

### Return type

[**GetDocumentUrlResponse**](GetDocumentUrlResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_documents**
> GetDocumentsResponse get_documents(site_id=site_id, action_status=action_status, sync_status=sync_status, deleted=deleted, var_date=var_date, tz=tz, next=next, previous=previous, limit=limit)

Get Documents listing

Returns a list of the most recent documents added, ordered by inserted, descending

### Example


```python
import openapi_client
from openapi_client.models.get_documents_response import GetDocumentsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentsApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier (optional)
    action_status = 'action_status_example' # str | Fetch documents with an action status (optional)
    sync_status = 'sync_status_example' # str | Fetch documents with an sync status (optional)
    deleted = True # bool | Fetch soft deleted documents (optional)
    var_date = 'var_date_example' # str | Fetch documents inserted on a certain date (yyyy-MM-dd) (optional)
    tz = 'tz_example' # str | UTC offset to apply to date parameter (IE: -0600) (optional)
    next = 'next_example' # str | Next page of results token (optional)
    previous = 'previous_example' # str | Previous page of results token (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')

    try:
        # Get Documents listing
        api_response = api_instance.get_documents(site_id=site_id, action_status=action_status, sync_status=sync_status, deleted=deleted, var_date=var_date, tz=tz, next=next, previous=previous, limit=limit)
        print("The response of DocumentsApi->get_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->get_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | [optional] 
 **action_status** | **str**| Fetch documents with an action status | [optional] 
 **sync_status** | **str**| Fetch documents with an sync status | [optional] 
 **deleted** | **bool**| Fetch soft deleted documents | [optional] 
 **var_date** | **str**| Fetch documents inserted on a certain date (yyyy-MM-dd) | [optional] 
 **tz** | **str**| UTC offset to apply to date parameter (IE: -0600) | [optional] 
 **next** | **str**| Next page of results token | [optional] 
 **previous** | **str**| Previous page of results token | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]

### Return type

[**GetDocumentsResponse**](GetDocumentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_published_document_content**
> get_published_document_content(document_id, site_id=site_id)

Get published document's contents

Get a published document's contents. Certain content types, text/*, application/json, and application/x-www-form-urlencoded. return the  "content" field, while all other content types return a 'contentUrl' for retrieving the content.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Get published document's contents
        api_instance.get_published_document_content(document_id, site_id=site_id)
    except Exception as e:
        print("Exception when calling DocumentsApi->get_published_document_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**307** | Temporary Redirect |  * Location -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purge_document**
> DeleteResponse purge_document(document_id, site_id=site_id)

Purge document

Remove all objects from the S3 bucket, including previous versions and current version, and should remove all metadata as well, so that no trace of the document exists outside of the audit logs and any backups. Can only be called be ADMIN or GOVERN.

### Example


```python
import openapi_client
from openapi_client.models.delete_response import DeleteResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Purge document
        api_response = api_instance.purge_document(document_id, site_id=site_id)
        print("The response of DocumentsApi->purge_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->purge_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_document_checkout**
> SetResponse set_document_checkout(document_id, site_id=site_id)

Perform document checkout

Creates a checkout for the document. Fails with **409 Conflict** if the document is already checkedout by another user; available as an Add-On Module


### Example


```python
import openapi_client
from openapi_client.models.set_response import SetResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Perform document checkout
        api_response = api_instance.set_document_checkout(document_id, site_id=site_id)
        print("The response of DocumentsApi->set_document_checkout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->set_document_checkout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**SetResponse**](SetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_document_checkout_legal_hold**
> SetResponse set_document_checkout_legal_hold(document_id, site_id=site_id)

Perform document legal hold checkout

Creates a legal hold checkout for the document. Fails with **409 Conflict** if the document is already checkedout by another user; available as an Add-On Module


### Example


```python
import openapi_client
from openapi_client.models.set_response import SetResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Perform document legal hold checkout
        api_response = api_instance.set_document_checkout_legal_hold(document_id, site_id=site_id)
        print("The response of DocumentsApi->set_document_checkout_legal_hold:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->set_document_checkout_legal_hold: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**SetResponse**](SetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_document_restore**
> SetDocumentRestoreResponse set_document_restore(document_id, site_id=site_id)

Restore soft deleted document

Restores a soft deleted document

### Example


```python
import openapi_client
from openapi_client.models.set_document_restore_response import SetDocumentRestoreResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Restore soft deleted document
        api_response = api_instance.set_document_restore(document_id, site_id=site_id)
        print("The response of DocumentsApi->set_document_restore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->set_document_restore: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**SetDocumentRestoreResponse**](SetDocumentRestoreResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_document**
> AddDocumentResponse update_document(document_id, update_document_request, site_id=site_id, share_key=share_key)

Update document

Update a document's details, i.e., metadata

If no content is specified, the endpoint will return a S3 Presigned that will allow for the uploading of Large document data. 

NOTE:
- provided attributes will overwrite existing matching attribute keys in the document. Attributes not included in the request body will remain unchanged.

### Example


```python
import openapi_client
from openapi_client.models.add_document_response import AddDocumentResponse
from openapi_client.models.update_document_request import UpdateDocumentRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    update_document_request = {"path":"test.txt","contentType":"text/plain","isBase64":false,"content":"This is sample data file","tags":[{"key":"category","value":"sample"},{"key":"players","values":["111","222"]}],"metadata":[{"key":"info","value":"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."}]} # UpdateDocumentRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)
    share_key = 'share_key_example' # str | Share Identifier (optional)

    try:
        # Update document
        api_response = api_instance.update_document(document_id, update_document_request, site_id=site_id, share_key=share_key)
        print("The response of DocumentsApi->update_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->update_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **update_document_request** | [**UpdateDocumentRequest**](UpdateDocumentRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 
 **share_key** | **str**| Share Identifier | [optional] 

### Return type

[**AddDocumentResponse**](AddDocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | 400 OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

