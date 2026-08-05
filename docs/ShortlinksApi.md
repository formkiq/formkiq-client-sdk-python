# formkiq_client.ShortlinksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_shortlink**](ShortlinksApi.md#add_shortlink) | **POST** /shortlinks | Add shortlink


# **add_shortlink**
> AddShortlinkResponse add_shortlink(add_shortlink_request)

Add shortlink

Create a shortlink for a target URL

### Example


```python
import formkiq_client
from formkiq_client.models.add_shortlink_request import AddShortlinkRequest
from formkiq_client.models.add_shortlink_response import AddShortlinkResponse
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
    api_instance = formkiq_client.ShortlinksApi(api_client)
    add_shortlink_request = formkiq_client.AddShortlinkRequest() # AddShortlinkRequest | 

    try:
        # Add shortlink
        api_response = api_instance.add_shortlink(add_shortlink_request)
        print("The response of ShortlinksApi->add_shortlink:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShortlinksApi->add_shortlink: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_shortlink_request** | [**AddShortlinkRequest**](AddShortlinkRequest.md)|  | 

### Return type

[**AddShortlinkResponse**](AddShortlinkResponse.md)

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

