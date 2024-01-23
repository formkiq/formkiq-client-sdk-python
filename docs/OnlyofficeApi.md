# formkiq_client.OnlyofficeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**only_office_document_edit**](OnlyofficeApi.md#only_office_document_edit) | **POST** /onlyoffice/{documentId}/edit | Edit onlyoffice document
[**only_office_document_new**](OnlyofficeApi.md#only_office_document_new) | **POST** /onlyoffice/new | Create onlyoffice document
[**only_office_document_save**](OnlyofficeApi.md#only_office_document_save) | **POST** /onlyoffice/{documentId}/save | Save onlyoffice document


# **only_office_document_edit**
> OnlyOfficeDocumentResponse only_office_document_edit(document_id, body, site_id=site_id)

Edit onlyoffice document

Provide ONLYOFFICE integration for editing documents; ONLY available with FormKiQ Enterprise

### Example


```python
import time
import os
import formkiq_client
from formkiq_client.models.only_office_document_response import OnlyOfficeDocumentResponse
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
    api_instance = formkiq_client.OnlyofficeApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    body = None # object | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Edit onlyoffice document
        api_response = api_instance.only_office_document_edit(document_id, body, site_id=site_id)
        print("The response of OnlyofficeApi->only_office_document_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnlyofficeApi->only_office_document_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **body** | **object**|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**OnlyOfficeDocumentResponse**](OnlyOfficeDocumentResponse.md)

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

# **only_office_document_new**
> OnlyOfficeDocumentResponse only_office_document_new(only_office_document_new_request, site_id=site_id)

Create onlyoffice document

Provide ONLYOFFICE integration for the creation of new documents; ONLY available with FormKiQ Enterprise

### Example


```python
import time
import os
import formkiq_client
from formkiq_client.models.only_office_document_new_request import OnlyOfficeDocumentNewRequest
from formkiq_client.models.only_office_document_response import OnlyOfficeDocumentResponse
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
    api_instance = formkiq_client.OnlyofficeApi(api_client)
    only_office_document_new_request = formkiq_client.OnlyOfficeDocumentNewRequest() # OnlyOfficeDocumentNewRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Create onlyoffice document
        api_response = api_instance.only_office_document_new(only_office_document_new_request, site_id=site_id)
        print("The response of OnlyofficeApi->only_office_document_new:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnlyofficeApi->only_office_document_new: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **only_office_document_new_request** | [**OnlyOfficeDocumentNewRequest**](OnlyOfficeDocumentNewRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**OnlyOfficeDocumentResponse**](OnlyOfficeDocumentResponse.md)

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

# **only_office_document_save**
> OnlyOfficeDocumentSaveResponse only_office_document_save(document_id, site_id=site_id)

Save onlyoffice document

Save an updated document for ONLYOFFICE integration. ONLY available with FormKiQ Enterprise

### Example


```python
import time
import os
import formkiq_client
from formkiq_client.models.only_office_document_save_response import OnlyOfficeDocumentSaveResponse
from formkiq_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = formkiq_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with formkiq_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formkiq_client.OnlyofficeApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Save onlyoffice document
        api_response = api_instance.only_office_document_save(document_id, site_id=site_id)
        print("The response of OnlyofficeApi->only_office_document_save:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnlyofficeApi->only_office_document_save: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**OnlyOfficeDocumentSaveResponse**](OnlyOfficeDocumentSaveResponse.md)

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

