# formkiq_client.AntivirusApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**set_antivirus**](AntivirusApi.md#set_antivirus) | **PUT** /documents/{documentId}/antivirus | Antivirus document scan


# **set_antivirus**
> SetAntivirusResponse set_antivirus(document_id, site_id=site_id, share_key=share_key, body=body)

Antivirus document scan

Perform an Anti-Malware / Antivirus scan on a document; ONLY available with FormKiQ Pro and Enterprise

### Example


```python
import time
import os
import formkiq_client
from formkiq_client.models.set_antivirus_response import SetAntivirusResponse
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
    api_instance = formkiq_client.AntivirusApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    share_key = 'share_key_example' # str | Share Identifier (optional)
    body = None # object |  (optional)

    try:
        # Antivirus document scan
        api_response = api_instance.set_antivirus(document_id, site_id=site_id, share_key=share_key, body=body)
        print("The response of AntivirusApi->set_antivirus:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntivirusApi->set_antivirus: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **share_key** | **str**| Share Identifier | [optional] 
 **body** | **object**|  | [optional] 

### Return type

[**SetAntivirusResponse**](SetAntivirusResponse.md)

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

