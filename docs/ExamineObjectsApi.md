# formkiq_client.ExamineObjectsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_examine_pdf**](ExamineObjectsApi.md#get_examine_pdf) | **GET** /objects/examine/{id}/pdf | Add Examine Pdf
[**get_examine_pdf_url**](ExamineObjectsApi.md#get_examine_pdf_url) | **GET** /objects/examine/pdf | Add Examine Pdf


# **get_examine_pdf**
> GetExaminePdfResponse get_examine_pdf(id, site_id=site_id)

Add Examine Pdf

Get PDF details  File must have been uploaded previously using the GET /objects/examine/pdf API.

### Example


```python
import formkiq_client
from formkiq_client.models.get_examine_pdf_response import GetExaminePdfResponse
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
    api_instance = formkiq_client.ExamineObjectsApi(api_client)
    id = 'id_example' # str | Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Add Examine Pdf
        api_response = api_instance.get_examine_pdf(id, site_id=site_id)
        print("The response of ExamineObjectsApi->get_examine_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExamineObjectsApi->get_examine_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**GetExaminePdfResponse**](GetExaminePdfResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_examine_pdf_url**
> GetExaminePdfUrlResponse get_examine_pdf_url(site_id=site_id)

Add Examine Pdf

Get Signed URL for PDF Object Upload of a document to be examined by calling GET /objects/examine/{id}/pdf

### Example


```python
import formkiq_client
from formkiq_client.models.get_examine_pdf_url_response import GetExaminePdfUrlResponse
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
    api_instance = formkiq_client.ExamineObjectsApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Add Examine Pdf
        api_response = api_instance.get_examine_pdf_url(site_id=site_id)
        print("The response of ExamineObjectsApi->get_examine_pdf_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExamineObjectsApi->get_examine_pdf_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**GetExaminePdfUrlResponse**](GetExaminePdfUrlResponse.md)

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

