# formkiq_client.ESignatureApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_esignature_docusign**](ESignatureApi.md#add_esignature_docusign) | **POST** /esignature/docusign/{documentId} | Create E-signature request
[**add_esignature_docusign_events**](ESignatureApi.md#add_esignature_docusign_events) | **POST** /esignature/docusign/events | Add E-signature event
[**get_esignature_docusign_config**](ESignatureApi.md#get_esignature_docusign_config) | **GET** /esignature/docusign/config | Get E-signature config
[**set_esignature_docusign_config**](ESignatureApi.md#set_esignature_docusign_config) | **PUT** /esignature/docusign/config | Set E-signature config


# **add_esignature_docusign**
> AddEsignatureDocusignResponse add_esignature_docusign(document_id, add_esignature_docusign_request, site_id=site_id)

Create E-signature request

Create a DocuSign E-Signature request; ONLY available with FormKiQ Enterprise

### Example


```python
import time
import os
import formkiq_client
from formkiq_client.models.add_esignature_docusign_request import AddEsignatureDocusignRequest
from formkiq_client.models.add_esignature_docusign_response import AddEsignatureDocusignResponse
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
    api_instance = formkiq_client.ESignatureApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    add_esignature_docusign_request = formkiq_client.AddEsignatureDocusignRequest() # AddEsignatureDocusignRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Create E-signature request
        api_response = api_instance.add_esignature_docusign(document_id, add_esignature_docusign_request, site_id=site_id)
        print("The response of ESignatureApi->add_esignature_docusign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ESignatureApi->add_esignature_docusign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **add_esignature_docusign_request** | [**AddEsignatureDocusignRequest**](AddEsignatureDocusignRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**AddEsignatureDocusignResponse**](AddEsignatureDocusignResponse.md)

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

# **add_esignature_docusign_events**
> AddEsignatureDocusignResponse add_esignature_docusign_events()

Add E-signature event

DocuSign callback URL handler; ONLY available with FormKiQ Enterprise

### Example


```python
import time
import os
import formkiq_client
from formkiq_client.models.add_esignature_docusign_response import AddEsignatureDocusignResponse
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
    api_instance = formkiq_client.ESignatureApi(api_client)

    try:
        # Add E-signature event
        api_response = api_instance.add_esignature_docusign_events()
        print("The response of ESignatureApi->add_esignature_docusign_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ESignatureApi->add_esignature_docusign_events: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AddEsignatureDocusignResponse**](AddEsignatureDocusignResponse.md)

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

# **get_esignature_docusign_config**
> GetEsignatureDocusignConfigResponse get_esignature_docusign_config(site_id=site_id)

Get E-signature config

Get DocuSign configuration info; ONLY available with FormKiQ Enterprise

### Example


```python
import time
import os
import formkiq_client
from formkiq_client.models.get_esignature_docusign_config_response import GetEsignatureDocusignConfigResponse
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
    api_instance = formkiq_client.ESignatureApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Get E-signature config
        api_response = api_instance.get_esignature_docusign_config(site_id=site_id)
        print("The response of ESignatureApi->get_esignature_docusign_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ESignatureApi->get_esignature_docusign_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**GetEsignatureDocusignConfigResponse**](GetEsignatureDocusignConfigResponse.md)

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

# **set_esignature_docusign_config**
> SetEsignatureDocusignConfigResponse set_esignature_docusign_config(set_esignature_docusign_config_request, site_id=site_id)

Set E-signature config

Set DocuSign configuration, required for integration; ONLY available with FormKiQ Enterprise

### Example


```python
import time
import os
import formkiq_client
from formkiq_client.models.set_esignature_docusign_config_request import SetEsignatureDocusignConfigRequest
from formkiq_client.models.set_esignature_docusign_config_response import SetEsignatureDocusignConfigResponse
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
    api_instance = formkiq_client.ESignatureApi(api_client)
    set_esignature_docusign_config_request = formkiq_client.SetEsignatureDocusignConfigRequest() # SetEsignatureDocusignConfigRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Set E-signature config
        api_response = api_instance.set_esignature_docusign_config(set_esignature_docusign_config_request, site_id=site_id)
        print("The response of ESignatureApi->set_esignature_docusign_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ESignatureApi->set_esignature_docusign_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_esignature_docusign_config_request** | [**SetEsignatureDocusignConfigRequest**](SetEsignatureDocusignConfigRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**SetEsignatureDocusignConfigResponse**](SetEsignatureDocusignConfigResponse.md)

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

