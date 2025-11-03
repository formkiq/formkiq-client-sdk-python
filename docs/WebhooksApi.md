# formkiq_client.WebhooksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_webhook**](WebhooksApi.md#add_webhook) | **POST** /webhooks | Add webhook
[**add_webhook_document**](WebhooksApi.md#add_webhook_document) | **POST** /private/webhooks/{webhooks+} | Add webhook
[**add_webhook_tag**](WebhooksApi.md#add_webhook_tag) | **POST** /webhooks/{webhookId}/tags | Add webhook tag
[**delete_webhook**](WebhooksApi.md#delete_webhook) | **DELETE** /webhooks/{webhookId} | Delete webhook
[**get_webhook**](WebhooksApi.md#get_webhook) | **GET** /webhooks/{webhookId} | Get webhook
[**get_webhook_tags**](WebhooksApi.md#get_webhook_tags) | **GET** /webhooks/{webhookId}/tags | Get webhook tags
[**get_webhooks**](WebhooksApi.md#get_webhooks) | **GET** /webhooks | Get webhooks
[**update_webhook**](WebhooksApi.md#update_webhook) | **PATCH** /webhooks/{webhookId} | Update webhook


# **add_webhook**
> AddWebhookResponse add_webhook(add_webhook_request, site_id=site_id)

Add webhook

Create a new webhook; once created, a webhook's id can be provided to an external service, allowing data to be sent, received, and processed via that webhook

### Example


```python
import formkiq_client
from formkiq_client.models.add_webhook_request import AddWebhookRequest
from formkiq_client.models.add_webhook_response import AddWebhookResponse
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
    api_instance = formkiq_client.WebhooksApi(api_client)
    add_webhook_request = formkiq_client.AddWebhookRequest() # AddWebhookRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Add webhook
        api_response = api_instance.add_webhook(add_webhook_request, site_id=site_id)
        print("The response of WebhooksApi->add_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->add_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_webhook_request** | [**AddWebhookRequest**](AddWebhookRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**AddWebhookResponse**](AddWebhookResponse.md)

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

# **add_webhook_document**
> DocumentId add_webhook_document(webhooks, body, site_id=site_id)

Add webhook

Receive an incoming private webhook and creates a document based on the webhook's body; requires authentication

### Example


```python
import formkiq_client
from formkiq_client.models.document_id import DocumentId
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
    api_instance = formkiq_client.WebhooksApi(api_client)
    webhooks = 'webhooks_example' # str | Web Hook Param
    body = None # object | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Add webhook
        api_response = api_instance.add_webhook_document(webhooks, body, site_id=site_id)
        print("The response of WebhooksApi->add_webhook_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->add_webhook_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhooks** | **str**| Web Hook Param | 
 **body** | **object**|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**DocumentId**](DocumentId.md)

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

# **add_webhook_tag**
> add_webhook_tag(webhook_id, add_webhook_tag_request, site_id=site_id)

Add webhook tag

Add a tag to a webhook

### Example


```python
import formkiq_client
from formkiq_client.models.add_webhook_tag_request import AddWebhookTagRequest
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
    api_instance = formkiq_client.WebhooksApi(api_client)
    webhook_id = 'webhook_id_example' # str | Web Hook Param
    add_webhook_tag_request = {"key":"category"} # AddWebhookTagRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Add webhook tag
        api_instance.add_webhook_tag(webhook_id, add_webhook_tag_request, site_id=site_id)
    except Exception as e:
        print("Exception when calling WebhooksApi->add_webhook_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| Web Hook Param | 
 **add_webhook_tag_request** | [**AddWebhookTagRequest**](AddWebhookTagRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook**
> DeleteResponse delete_webhook(webhook_id, site_id=site_id)

Delete webhook

Delete a webhook; this will disable sending, receiving, or processing of data from external services to this webhook

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
    api_instance = formkiq_client.WebhooksApi(api_client)
    webhook_id = 'webhook_id_example' # str | Web Hook Param
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Delete webhook
        api_response = api_instance.delete_webhook(webhook_id, site_id=site_id)
        print("The response of WebhooksApi->delete_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->delete_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| Web Hook Param | 
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

# **get_webhook**
> GetWebhookResponse get_webhook(webhook_id, site_id=site_id)

Get webhook

Return a webhook's details, i.e., its metadata

### Example


```python
import formkiq_client
from formkiq_client.models.get_webhook_response import GetWebhookResponse
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
    api_instance = formkiq_client.WebhooksApi(api_client)
    webhook_id = 'webhook_id_example' # str | Web Hook Param
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Get webhook
        api_response = api_instance.get_webhook(webhook_id, site_id=site_id)
        print("The response of WebhooksApi->get_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| Web Hook Param | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**GetWebhookResponse**](GetWebhookResponse.md)

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

# **get_webhook_tags**
> GetWebhookTagsResponse get_webhook_tags(webhook_id, site_id=site_id)

Get webhook tags

Get a webhook's tags

### Example


```python
import formkiq_client
from formkiq_client.models.get_webhook_tags_response import GetWebhookTagsResponse
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
    api_instance = formkiq_client.WebhooksApi(api_client)
    webhook_id = 'webhook_id_example' # str | Web Hook Param
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Get webhook tags
        api_response = api_instance.get_webhook_tags(webhook_id, site_id=site_id)
        print("The response of WebhooksApi->get_webhook_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_webhook_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| Web Hook Param | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**GetWebhookTagsResponse**](GetWebhookTagsResponse.md)

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

# **get_webhooks**
> GetWebhooksResponse get_webhooks(site_id=site_id, next=next, limit=limit)

Get webhooks

Return a list of webhooks; each webhook's id can be provided to an external service, allowing data to be sent, received, and processed via that webhook

### Example


```python
import formkiq_client
from formkiq_client.models.get_webhooks_response import GetWebhooksResponse
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
    api_instance = formkiq_client.WebhooksApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier (optional)
    next = 'next_example' # str | Next page of results token (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')

    try:
        # Get webhooks
        api_response = api_instance.get_webhooks(site_id=site_id, next=next, limit=limit)
        print("The response of WebhooksApi->get_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | [optional] 
 **next** | **str**| Next page of results token | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]

### Return type

[**GetWebhooksResponse**](GetWebhooksResponse.md)

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

# **update_webhook**
> UpdateResponse update_webhook(webhook_id, add_webhook_request, site_id=site_id)

Update webhook

Updates a webhook's details, i.e., its metadata

### Example


```python
import formkiq_client
from formkiq_client.models.add_webhook_request import AddWebhookRequest
from formkiq_client.models.update_response import UpdateResponse
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
    api_instance = formkiq_client.WebhooksApi(api_client)
    webhook_id = 'webhook_id_example' # str | Web Hook Param
    add_webhook_request = formkiq_client.AddWebhookRequest() # AddWebhookRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Update webhook
        api_response = api_instance.update_webhook(webhook_id, add_webhook_request, site_id=site_id)
        print("The response of WebhooksApi->update_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->update_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| Web Hook Param | 
 **add_webhook_request** | [**AddWebhookRequest**](AddWebhookRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**UpdateResponse**](UpdateResponse.md)

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

