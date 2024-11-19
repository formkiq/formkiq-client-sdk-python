# formkiq_client.ESignatureApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_docusign_envelopes**](ESignatureApi.md#add_docusign_envelopes) | **POST** /esignature/docusign/{documentId}/envelopes | Create Docusign Envelope request
[**add_docusign_recipient_view**](ESignatureApi.md#add_docusign_recipient_view) | **POST** /esignature/docusign/{documentId}/envelopes/{envelopeId}/views/recipient | Create Docusign Recipient View request
[**add_esignature_docusign_events**](ESignatureApi.md#add_esignature_docusign_events) | **POST** /esignature/docusign/events | Add E-signature event


# **add_docusign_envelopes**
> AddDocusignEnvelopesResponse add_docusign_envelopes(document_id, add_docusign_envelopes_request, site_id=site_id)

Create Docusign Envelope request

DocuSign create Docusign Envelope request; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.add_docusign_envelopes_request import AddDocusignEnvelopesRequest
from formkiq_client.models.add_docusign_envelopes_response import AddDocusignEnvelopesResponse
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
    add_docusign_envelopes_request = formkiq_client.AddDocusignEnvelopesRequest() # AddDocusignEnvelopesRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Create Docusign Envelope request
        api_response = api_instance.add_docusign_envelopes(document_id, add_docusign_envelopes_request, site_id=site_id)
        print("The response of ESignatureApi->add_docusign_envelopes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ESignatureApi->add_docusign_envelopes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **add_docusign_envelopes_request** | [**AddDocusignEnvelopesRequest**](AddDocusignEnvelopesRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**AddDocusignEnvelopesResponse**](AddDocusignEnvelopesResponse.md)

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

# **add_docusign_recipient_view**
> AddDocusignRecipientViewResponse add_docusign_recipient_view(document_id, envelope_id, add_docusign_recipient_view_request, site_id=site_id)

Create Docusign Recipient View request

DocuSign create Docusign Recipient View request; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.add_docusign_recipient_view_request import AddDocusignRecipientViewRequest
from formkiq_client.models.add_docusign_recipient_view_response import AddDocusignRecipientViewResponse
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
    envelope_id = 'envelope_id_example' # str | Docusign Envelope Id
    add_docusign_recipient_view_request = formkiq_client.AddDocusignRecipientViewRequest() # AddDocusignRecipientViewRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Create Docusign Recipient View request
        api_response = api_instance.add_docusign_recipient_view(document_id, envelope_id, add_docusign_recipient_view_request, site_id=site_id)
        print("The response of ESignatureApi->add_docusign_recipient_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ESignatureApi->add_docusign_recipient_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **envelope_id** | **str**| Docusign Envelope Id | 
 **add_docusign_recipient_view_request** | [**AddDocusignRecipientViewRequest**](AddDocusignRecipientViewRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**AddDocusignRecipientViewResponse**](AddDocusignRecipientViewResponse.md)

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
> AddResponse add_esignature_docusign_events()

Add E-signature event

DocuSign callback URL handler; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.add_response import AddResponse
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

[**AddResponse**](AddResponse.md)

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

