# formkiq_client.ESignatureApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_docusign_envelope_reminders**](ESignatureApi.md#add_docusign_envelope_reminders) | **POST** /esignature/docusign/{documentId}/envelopes/{envelopeId}/reminders | Request DocuSign signing reminders
[**add_docusign_envelopes**](ESignatureApi.md#add_docusign_envelopes) | **POST** /esignature/docusign/{documentId}/envelopes | Create Docusign Envelope request
[**add_docusign_recipient_view**](ESignatureApi.md#add_docusign_recipient_view) | **POST** /esignature/docusign/{documentId}/envelopes/{envelopeId}/views/recipient | Create Docusign Recipient View request
[**add_docusign_sender_view**](ESignatureApi.md#add_docusign_sender_view) | **POST** /esignature/docusign/{documentId}/envelopes/{envelopeId}/views/sender | Create Docusign Sender View request
[**add_esignature_docusign_events**](ESignatureApi.md#add_esignature_docusign_events) | **POST** /esignature/docusign/events | Add E-signature event
[**get_docusign_envelope**](ESignatureApi.md#get_docusign_envelope) | **GET** /esignature/docusign/{documentId}/envelopes/{envelopeId} | Get Docusign envelope and recipient status
[**void_docusign_envelope**](ESignatureApi.md#void_docusign_envelope) | **POST** /esignature/docusign/{documentId}/envelopes/{envelopeId}/void | Void a DocuSign envelope


# **add_docusign_envelope_reminders**
> AddDocusignEnvelopeRemindersResponse add_docusign_envelope_reminders(document_id, envelope_id, site_id=site_id, artifact_id=artifact_id, environment=environment, add_docusign_envelope_reminders_request=add_docusign_envelope_reminders_request)

Request DocuSign signing reminders

Resends signing notifications for an in-progress DocuSign envelope; available as an Add-On Module. With no request body or an empty object, DocuSign reminds all eligible recipients at the current routing step. Supply recipientIds to remind only the selected eligible signers. Obtain IDs from recipients.signers[].recipientId in GET /esignature/docusign/{documentId}/envelopes/{envelopeId}. Every selected signer must still be awaiting action at the current routing step when this request is processed. Validate the entire selection before issuing a resend. Completed and future-step signers cannot be targeted. Invalid targeted requests never fall back to reminding all recipients. Recipient notification settings are respected; this operation does not send FormKiQ notifications to embedded-only or email-suppressed signers. Requires write access to the selected document or artifact and a matching stored envelope ID. The operation resends the existing invitation without changing recipients, documents, routing, or automatic reminder settings. Targeted responses report each selected recipient's acceptance or failure, with no overall status. Acceptance does not confirm notification delivery. Do not automatically retry after a timeout because the reminder may already have been requested.

### Example


```python
import formkiq_client
from formkiq_client.models.add_docusign_envelope_reminders_request import AddDocusignEnvelopeRemindersRequest
from formkiq_client.models.add_docusign_envelope_reminders_response import AddDocusignEnvelopeRemindersResponse
from formkiq_client.models.docusign_environment import DocusignEnvironment
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
    site_id = 'site_id_example' # str | Site Identifier (optional)
    artifact_id = 'artifact_id_example' # str | Artifact Document Identifier (optional)
    environment = formkiq_client.DocusignEnvironment() # DocusignEnvironment | DocuSign environment. Defaults to the site's docusignEnvironment; required when the site has no default. Use the environment in which the envelope was created. (optional)
    add_docusign_envelope_reminders_request = {} # AddDocusignEnvelopeRemindersRequest |  (optional)

    try:
        # Request DocuSign signing reminders
        api_response = api_instance.add_docusign_envelope_reminders(document_id, envelope_id, site_id=site_id, artifact_id=artifact_id, environment=environment, add_docusign_envelope_reminders_request=add_docusign_envelope_reminders_request)
        print("The response of ESignatureApi->add_docusign_envelope_reminders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ESignatureApi->add_docusign_envelope_reminders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **envelope_id** | **str**| Docusign Envelope Id | 
 **site_id** | **str**| Site Identifier | [optional] 
 **artifact_id** | **str**| Artifact Document Identifier | [optional] 
 **environment** | [**DocusignEnvironment**](.md)| DocuSign environment. Defaults to the site&#39;s docusignEnvironment; required when the site has no default. Use the environment in which the envelope was created. | [optional] 
 **add_docusign_envelope_reminders_request** | [**AddDocusignEnvelopeRemindersRequest**](AddDocusignEnvelopeRemindersRequest.md)|  | [optional] 

### Return type

[**AddDocusignEnvelopeRemindersResponse**](AddDocusignEnvelopeRemindersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reminder request processed. For targeted requests, inspect each entry in recipients for acceptance or failure; HTTP 200 does not mean all selected recipients succeeded. An envelope-wide request returns an empty object when DocuSign accepts it, because individual recipient outcomes are not returned. Acceptance does not confirm delivery. |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | Invalid parameters, missing DocuSign configuration, ineligible envelope state, or unknown or ineligible signers. Null or empty recipientIds arrays, duplicate IDs, and null, blank, or non-string entries are rejected. The singular recipientId field is not accepted. Draft and terminal envelopes cannot be reminded. |  -  |
**401** | Authentication required |  -  |
**403** | Write access to the selected document or artifact is denied |  -  |
**404** | Document, artifact, or associated DocuSign envelope not found |  -  |
**429** | DocuSign rate limit exceeded |  -  |
**502** | DocuSign authentication failure, upstream error, or invalid response |  -  |
**504** | DocuSign request timed out; reminder delivery outcome is unknown |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_docusign_envelopes**
> AddDocusignEnvelopesResponse add_docusign_envelopes(document_id, add_docusign_envelopes_request, site_id=site_id, artifact_id=artifact_id)

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
    artifact_id = 'artifact_id_example' # str | Artifact Document Identifier (optional)

    try:
        # Create Docusign Envelope request
        api_response = api_instance.add_docusign_envelopes(document_id, add_docusign_envelopes_request, site_id=site_id, artifact_id=artifact_id)
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
 **artifact_id** | **str**| Artifact Document Identifier | [optional] 

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
> AddDocusignRecipientViewResponse add_docusign_recipient_view(document_id, envelope_id, add_docusign_recipient_view_request, site_id=site_id, artifact_id=artifact_id)

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
    artifact_id = 'artifact_id_example' # str | Artifact Document Identifier (optional)

    try:
        # Create Docusign Recipient View request
        api_response = api_instance.add_docusign_recipient_view(document_id, envelope_id, add_docusign_recipient_view_request, site_id=site_id, artifact_id=artifact_id)
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
 **artifact_id** | **str**| Artifact Document Identifier | [optional] 

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

# **add_docusign_sender_view**
> AddDocusignSenderViewResponse add_docusign_sender_view(document_id, envelope_id, add_docusign_sender_view_request, site_id=site_id, artifact_id=artifact_id)

Create Docusign Sender View request

DocuSign create Docusign Sender View request; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.add_docusign_sender_view_request import AddDocusignSenderViewRequest
from formkiq_client.models.add_docusign_sender_view_response import AddDocusignSenderViewResponse
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
    add_docusign_sender_view_request = {"returnUrl":"https://console.example.com/agreements/123/esignature"} # AddDocusignSenderViewRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)
    artifact_id = 'artifact_id_example' # str | Artifact Document Identifier (optional)

    try:
        # Create Docusign Sender View request
        api_response = api_instance.add_docusign_sender_view(document_id, envelope_id, add_docusign_sender_view_request, site_id=site_id, artifact_id=artifact_id)
        print("The response of ESignatureApi->add_docusign_sender_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ESignatureApi->add_docusign_sender_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **envelope_id** | **str**| Docusign Envelope Id | 
 **add_docusign_sender_view_request** | [**AddDocusignSenderViewRequest**](AddDocusignSenderViewRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 
 **artifact_id** | **str**| Artifact Document Identifier | [optional] 

### Return type

[**AddDocusignSenderViewResponse**](AddDocusignSenderViewResponse.md)

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

# **get_docusign_envelope**
> GetDocusignEnvelopeResponse get_docusign_envelope(document_id, envelope_id, site_id=site_id, artifact_id=artifact_id, environment=environment)

Get Docusign envelope and recipient status

Retrieves the DocuSign envelope using include=recipients and returns the DocuSign response directly, including envelope status and recipient routing information. No FormKiQ fields or wrapper are added. The envelope must be associated with the selected document or artifact. This read-only operation does not update document attributes or download the signed document. Available as an Add-On Module. Repeated status polling must be at least 15 minutes apart. Use recipients.signers[].recipientId from this response as entries in the optional recipientIds array in POST /esignature/docusign/{documentId}/envelopes/{envelopeId}/reminders to request reminders for selected signers.

### Example


```python
import formkiq_client
from formkiq_client.models.docusign_environment import DocusignEnvironment
from formkiq_client.models.get_docusign_envelope_response import GetDocusignEnvelopeResponse
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
    site_id = 'site_id_example' # str | Site Identifier (optional)
    artifact_id = 'artifact_id_example' # str | Artifact Document Identifier (optional)
    environment = formkiq_client.DocusignEnvironment() # DocusignEnvironment | DocuSign environment. Defaults to the site's docusignEnvironment; required when the site has no default. Use the environment in which the envelope was created. (optional)

    try:
        # Get Docusign envelope and recipient status
        api_response = api_instance.get_docusign_envelope(document_id, envelope_id, site_id=site_id, artifact_id=artifact_id, environment=environment)
        print("The response of ESignatureApi->get_docusign_envelope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ESignatureApi->get_docusign_envelope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **envelope_id** | **str**| Docusign Envelope Id | 
 **site_id** | **str**| Site Identifier | [optional] 
 **artifact_id** | **str**| Artifact Document Identifier | [optional] 
 **environment** | [**DocusignEnvironment**](.md)| DocuSign environment. Defaults to the site&#39;s docusignEnvironment; required when the site has no default. Use the environment in which the envelope was created. | [optional] 

### Return type

[**GetDocusignEnvelopeResponse**](GetDocusignEnvelopeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DocuSign envelope with recipients |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | Invalid parameters or missing DocuSign configuration |  -  |
**401** | Authentication required |  -  |
**403** | Access to the selected document or artifact is denied |  -  |
**404** | Document, artifact, or associated DocuSign envelope not found |  -  |
**429** | Envelope polling or DocuSign rate limit exceeded |  * Retry-After - Seconds to wait before another lookup <br>  |
**502** | DocuSign authentication failure, upstream error, or invalid response |  -  |
**504** | DocuSign request timed out |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_docusign_envelope**
> VoidDocusignEnvelopeResponse void_docusign_envelope(document_id, envelope_id, void_docusign_envelope_request, site_id=site_id, artifact_id=artifact_id, environment=environment)

Void a DocuSign envelope

Cancels an in-progress DocuSign envelope; available as an Add-On Module. Requires write access to the selected document or artifact and a matching stored envelope ID. Calls DocuSign's envelope update API, PUT /restapi/v2.1/accounts/{accountId}/envelopes/{envelopeId}, with status set to voided and the supplied voidedReason. DocuSign notifies recipients that the envelope was voided, including the supplied reason. Only sent or delivered envelopes can be voided. If the envelope is already voided, returns its current state without another update or changing its original reason. Voiding cannot be undone. The existing envelope-voided callback updates the stored FormKiQ status. After a timeout, the outcome is unknown; check the existing GET envelope status endpoint before attempting the operation again.

### Example


```python
import formkiq_client
from formkiq_client.models.docusign_environment import DocusignEnvironment
from formkiq_client.models.void_docusign_envelope_request import VoidDocusignEnvelopeRequest
from formkiq_client.models.void_docusign_envelope_response import VoidDocusignEnvelopeResponse
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
    void_docusign_envelope_request = {"voidedReason":"Document has been replaced."} # VoidDocusignEnvelopeRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)
    artifact_id = 'artifact_id_example' # str | Artifact Document Identifier (optional)
    environment = formkiq_client.DocusignEnvironment() # DocusignEnvironment | DocuSign environment. Defaults to the site's docusignEnvironment; required when the site has no default. Use the environment in which the envelope was created. (optional)

    try:
        # Void a DocuSign envelope
        api_response = api_instance.void_docusign_envelope(document_id, envelope_id, void_docusign_envelope_request, site_id=site_id, artifact_id=artifact_id, environment=environment)
        print("The response of ESignatureApi->void_docusign_envelope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ESignatureApi->void_docusign_envelope: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **envelope_id** | **str**| Docusign Envelope Id | 
 **void_docusign_envelope_request** | [**VoidDocusignEnvelopeRequest**](VoidDocusignEnvelopeRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 
 **artifact_id** | **str**| Artifact Document Identifier | [optional] 
 **environment** | [**DocusignEnvironment**](.md)| DocuSign environment. Defaults to the site&#39;s docusignEnvironment; required when the site has no default. Use the environment in which the envelope was created. | [optional] 

### Return type

[**VoidDocusignEnvelopeResponse**](VoidDocusignEnvelopeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DocuSign envelope voided successfully |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | Invalid parameters, missing, blank, or overlong voidedReason, missing DocuSign configuration, or an envelope that is not eligible to be voided. |  -  |
**401** | Authentication required |  -  |
**403** | Write access to the selected document or artifact is denied |  -  |
**404** | Document, artifact, or associated DocuSign envelope not found |  -  |
**429** | DocuSign rate limit exceeded |  -  |
**502** | DocuSign authentication failure, upstream error, or invalid response |  -  |
**504** | DocuSign request timed out; the void operation outcome is unknown |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

