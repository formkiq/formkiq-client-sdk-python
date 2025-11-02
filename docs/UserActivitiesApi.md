# formkiq_client.UserActivitiesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_document_user_activities**](UserActivitiesApi.md#get_document_user_activities) | **GET** /documents/{documentId}/userActivities | Get user activities for a document
[**get_resource_activities**](UserActivitiesApi.md#get_resource_activities) | **GET** /activities | Get resource activities
[**get_user_activities**](UserActivitiesApi.md#get_user_activities) | **GET** /userActivities | Get user activities


# **get_document_user_activities**
> GetUserActivitesResponse get_document_user_activities(document_id, site_id=site_id, next=next, limit=limit)

Get user activities for a document

Retrieve a user's activities for a document

### Example


```python
import formkiq_client
from formkiq_client.models.get_user_activites_response import GetUserActivitesResponse
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
    api_instance = formkiq_client.UserActivitiesApi(api_client)
    document_id = 'document_id_example' # str | Document Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    next = 'next_example' # str | Next page of results token (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')

    try:
        # Get user activities for a document
        api_response = api_instance.get_document_user_activities(document_id, site_id=site_id, next=next, limit=limit)
        print("The response of UserActivitiesApi->get_document_user_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserActivitiesApi->get_document_user_activities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Document Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **next** | **str**| Next page of results token | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]

### Return type

[**GetUserActivitesResponse**](GetUserActivitesResponse.md)

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

# **get_resource_activities**
> GetActivitesResponse get_resource_activities(site_id=site_id, document_id=document_id, entity_type_id=entity_type_id, namespace=namespace, entity_id=entity_id, start=start, end=end, sort=sort, next=next, limit=limit, user_id=user_id)

Get resource activities

Retrieve an resource activities

### Example


```python
import formkiq_client
from formkiq_client.models.get_activites_response import GetActivitesResponse
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
    api_instance = formkiq_client.UserActivitiesApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier (optional)
    document_id = 'document_id_example' # str | Document Identifier (optional)
    entity_type_id = 'entity_type_id_example' # str | EntityType Identifier (optional)
    namespace = 'namespace_example' # str | Namespace Identifier (optional)
    entity_id = 'entity_id_example' # str | Entity Identifier (optional)
    start = '2013-10-20T19:20:30+01:00' # datetime | Start of date-time range (UTC) (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime | End of date-time range (UTC) (optional)
    sort = 'sort_example' # str | Sort order (default DESC) (optional)
    next = 'next_example' # str | Next page of results token (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    user_id = 'user_id_example' # str | Fetch specific user activities (optional)

    try:
        # Get resource activities
        api_response = api_instance.get_resource_activities(site_id=site_id, document_id=document_id, entity_type_id=entity_type_id, namespace=namespace, entity_id=entity_id, start=start, end=end, sort=sort, next=next, limit=limit, user_id=user_id)
        print("The response of UserActivitiesApi->get_resource_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserActivitiesApi->get_resource_activities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | [optional] 
 **document_id** | **str**| Document Identifier | [optional] 
 **entity_type_id** | **str**| EntityType Identifier | [optional] 
 **namespace** | **str**| Namespace Identifier | [optional] 
 **entity_id** | **str**| Entity Identifier | [optional] 
 **start** | **datetime**| Start of date-time range (UTC) | [optional] 
 **end** | **datetime**| End of date-time range (UTC) | [optional] 
 **sort** | **str**| Sort order (default DESC) | [optional] 
 **next** | **str**| Next page of results token | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **user_id** | **str**| Fetch specific user activities | [optional] 

### Return type

[**GetActivitesResponse**](GetActivitesResponse.md)

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

# **get_user_activities**
> GetUserActivitesResponse get_user_activities(site_id=site_id, next=next, limit=limit, user_id=user_id)

Get user activities

Retrieve a user's activities

### Example


```python
import formkiq_client
from formkiq_client.models.get_user_activites_response import GetUserActivitesResponse
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
    api_instance = formkiq_client.UserActivitiesApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier (optional)
    next = 'next_example' # str | Next page of results token (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    user_id = 'user_id_example' # str | Fetch specific user activities (optional)

    try:
        # Get user activities
        api_response = api_instance.get_user_activities(site_id=site_id, next=next, limit=limit, user_id=user_id)
        print("The response of UserActivitiesApi->get_user_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserActivitiesApi->get_user_activities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | [optional] 
 **next** | **str**| Next page of results token | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **user_id** | **str**| Fetch specific user activities | [optional] 

### Return type

[**GetUserActivitesResponse**](GetUserActivitesResponse.md)

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

