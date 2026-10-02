# formkiq_client.DocumentNotificationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_document_notification**](DocumentNotificationsApi.md#add_document_notification) | **POST** /documents/{documentId}/notifications | Add an ad hoc document notification
[**get_document_notifications**](DocumentNotificationsApi.md#get_document_notifications) | **GET** /documents/{documentId}/notifications | Get document notifications
[**get_user_notifications**](DocumentNotificationsApi.md#get_user_notifications) | **GET** /userNotifications | Get user notifications


# **add_document_notification**
> AddDocumentNotificationResponse add_document_notification(document_id, add_document_notification_request, site_id=site_id, artifact_id=artifact_id)

Add an ad hoc document notification

Queue an ad hoc notification for a document or one of its artifacts

### Example


```python
import formkiq_client
from formkiq_client.models.add_document_notification_request import AddDocumentNotificationRequest
from formkiq_client.models.add_document_notification_response import AddDocumentNotificationResponse
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
    api_instance = formkiq_client.DocumentNotificationsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    add_document_notification_request = formkiq_client.AddDocumentNotificationRequest() # AddDocumentNotificationRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)
    artifact_id = 'artifact_id_example' # str | Artifact Document Identifier (optional)

    try:
        # Add an ad hoc document notification
        api_response = api_instance.add_document_notification(document_id, add_document_notification_request, site_id=site_id, artifact_id=artifact_id)
        print("The response of DocumentNotificationsApi->add_document_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentNotificationsApi->add_document_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **add_document_notification_request** | [**AddDocumentNotificationRequest**](AddDocumentNotificationRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 
 **artifact_id** | **str**| Artifact Document Identifier | [optional] 

### Return type

[**AddDocumentNotificationResponse**](AddDocumentNotificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Notification accepted for delivery |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | Invalid notification request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_notifications**
> GetDocumentNotificationsResponse get_document_notifications(document_id, site_id=site_id, artifact_id=artifact_id, limit=limit, next=next)

Get document notifications

Get notifications attached to a document or one of its artifacts

### Example


```python
import formkiq_client
from formkiq_client.models.get_document_notifications_response import GetDocumentNotificationsResponse
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
    api_instance = formkiq_client.DocumentNotificationsApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    artifact_id = 'artifact_id_example' # str | Artifact Document Identifier (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)

    try:
        # Get document notifications
        api_response = api_instance.get_document_notifications(document_id, site_id=site_id, artifact_id=artifact_id, limit=limit, next=next)
        print("The response of DocumentNotificationsApi->get_document_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentNotificationsApi->get_document_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **artifact_id** | **str**| Artifact Document Identifier | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **next** | **str**| Next page of results token | [optional] 

### Return type

[**GetDocumentNotificationsResponse**](GetDocumentNotificationsResponse.md)

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

# **get_user_notifications**
> GetUserNotificationsResponse get_user_notifications(site_id=site_id, limit=limit, next=next)

Get user notifications

Retrieve notifications where the authenticated user's email is a CC or BCC recipient

### Example


```python
import formkiq_client
from formkiq_client.models.get_user_notifications_response import GetUserNotificationsResponse
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
    api_instance = formkiq_client.DocumentNotificationsApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)

    try:
        # Get user notifications
        api_response = api_instance.get_user_notifications(site_id=site_id, limit=limit, next=next)
        print("The response of DocumentNotificationsApi->get_user_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentNotificationsApi->get_user_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **next** | **str**| Next page of results token | [optional] 

### Return type

[**GetUserNotificationsResponse**](GetUserNotificationsResponse.md)

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

