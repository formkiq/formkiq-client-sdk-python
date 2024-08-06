# formkiq_client.DocumentOCRApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_document_ocr**](DocumentOCRApi.md#add_document_ocr) | **POST** /documents/{documentId}/ocr | Perform document ocr
[**delete_document_ocr**](DocumentOCRApi.md#delete_document_ocr) | **DELETE** /documents/{documentId}/ocr | Delete document ocr
[**get_document_ocr**](DocumentOCRApi.md#get_document_ocr) | **GET** /documents/{documentId}/ocr | Get document ocr content
[**set_document_ocr**](DocumentOCRApi.md#set_document_ocr) | **PUT** /documents/{documentId}/ocr | Set document ocr result


# **add_document_ocr**
> AddDocumentOcrResponse add_document_ocr(document_id, site_id=site_id, add_document_ocr_request=add_document_ocr_request)

Perform document ocr

Document optical character recognition (OCR) request; extract text and data from a document;   Tesseract available for all editions, but Textract engine and tables and forms options ONLY available with FormKiQ Pro and Enterprise

### Example


```python
import formkiq_client
from formkiq_client.models.add_document_ocr_request import AddDocumentOcrRequest
from formkiq_client.models.add_document_ocr_response import AddDocumentOcrResponse
from formkiq_client.rest import ApiException
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
    api_instance = formkiq_client.DocumentOCRApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    add_document_ocr_request = formkiq_client.AddDocumentOcrRequest() # AddDocumentOcrRequest |  (optional)

    try:
        # Perform document ocr
        api_response = api_instance.add_document_ocr(document_id, site_id=site_id, add_document_ocr_request=add_document_ocr_request)
        print("The response of DocumentOCRApi->add_document_ocr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentOCRApi->add_document_ocr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **add_document_ocr_request** | [**AddDocumentOcrRequest**](AddDocumentOcrRequest.md)|  | [optional] 

### Return type

[**AddDocumentOcrResponse**](AddDocumentOcrResponse.md)

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

# **delete_document_ocr**
> DeleteResponse delete_document_ocr(document_id, site_id=site_id)

Delete document ocr

Delete a document's optical character recognition (OCR) result, if exists;   Tesseract available for all editions, but Textract engine and tables and forms options ONLY available with FormKiQ Pro and Enterprise

### Example


```python
import formkiq_client
from formkiq_client.models.delete_response import DeleteResponse
from formkiq_client.rest import ApiException
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
    api_instance = formkiq_client.DocumentOCRApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Delete document ocr
        api_response = api_instance.delete_document_ocr(document_id, site_id=site_id)
        print("The response of DocumentOCRApi->delete_document_ocr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentOCRApi->delete_document_ocr: %s\n" % e)
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

# **get_document_ocr**
> GetDocumentOcrResponse get_document_ocr(document_id, site_id=site_id, output_type=output_type, content_url=content_url, text=text, share_key=share_key)

Get document ocr content

Get a document's optical character recognition (OCR) result, if exists;   Tesseract available for all editions, but Textract engine and tables and forms options ONLY available with FormKiQ Pro and Enterprise

### Example


```python
import formkiq_client
from formkiq_client.models.get_document_ocr_response import GetDocumentOcrResponse
from formkiq_client.rest import ApiException
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
    api_instance = formkiq_client.DocumentOCRApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    output_type = 'output_type_example' # str | Output Format Type (optional)
    content_url = 'content_url_example' # str | Whether to return a \"contentUrl\", set value to 'true' (deprecated) (optional)
    text = 'text_example' # str | Returns raw 'text' of OCR content. e.g. AWS Textract returns JSON, setting parameter to 'true' converts JSON to Text (deprecated) (optional)
    share_key = 'share_key_example' # str | Share Identifier (optional)

    try:
        # Get document ocr content
        api_response = api_instance.get_document_ocr(document_id, site_id=site_id, output_type=output_type, content_url=content_url, text=text, share_key=share_key)
        print("The response of DocumentOCRApi->get_document_ocr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentOCRApi->get_document_ocr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **output_type** | **str**| Output Format Type | [optional] 
 **content_url** | **str**| Whether to return a \&quot;contentUrl\&quot;, set value to &#39;true&#39; (deprecated) | [optional] 
 **text** | **str**| Returns raw &#39;text&#39; of OCR content. e.g. AWS Textract returns JSON, setting parameter to &#39;true&#39; converts JSON to Text (deprecated) | [optional] 
 **share_key** | **str**| Share Identifier | [optional] 

### Return type

[**GetDocumentOcrResponse**](GetDocumentOcrResponse.md)

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

# **set_document_ocr**
> AddDocumentOcrResponse set_document_ocr(document_id, site_id=site_id, set_document_ocr_request=set_document_ocr_request)

Set document ocr result

Set a document's optical character recognition (OCR) result for a document;   Tesseract available for all editions, but Textract engine and tables and forms options ONLY available with FormKiQ Pro and Enterprise

### Example


```python
import formkiq_client
from formkiq_client.models.add_document_ocr_response import AddDocumentOcrResponse
from formkiq_client.models.set_document_ocr_request import SetDocumentOcrRequest
from formkiq_client.rest import ApiException
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
    api_instance = formkiq_client.DocumentOCRApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    set_document_ocr_request = formkiq_client.SetDocumentOcrRequest() # SetDocumentOcrRequest |  (optional)

    try:
        # Set document ocr result
        api_response = api_instance.set_document_ocr(document_id, site_id=site_id, set_document_ocr_request=set_document_ocr_request)
        print("The response of DocumentOCRApi->set_document_ocr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentOCRApi->set_document_ocr: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **set_document_ocr_request** | [**SetDocumentOcrRequest**](SetDocumentOcrRequest.md)|  | [optional] 

### Return type

[**AddDocumentOcrResponse**](AddDocumentOcrResponse.md)

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

