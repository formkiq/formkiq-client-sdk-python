# formkiq_client.UserManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_groups**](UserManagementApi.md#get_groups) | **GET** /groups | Get configured system group(s)
[**get_users_in_group**](UserManagementApi.md#get_users_in_group) | **GET** /groups/{groupName}/users | Get users in a group


# **get_groups**
> GetGroupsResponse get_groups(limit=limit, next=next)

Get configured system group(s)

Returns the list of user groups configured in the application

### Example


```python
import formkiq_client
from formkiq_client.models.get_groups_response import GetGroupsResponse
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
    api_instance = formkiq_client.UserManagementApi(api_client)
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)

    try:
        # Get configured system group(s)
        api_response = api_instance.get_groups(limit=limit, next=next)
        print("The response of UserManagementApi->get_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->get_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **next** | **str**| Next page of results token | [optional] 

### Return type

[**GetGroupsResponse**](GetGroupsResponse.md)

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

# **get_users_in_group**
> GetUsersInGroupResponse get_users_in_group(group_name, limit=limit, next=next)

Get users in a group

Returns the list of users in a group

### Example


```python
import formkiq_client
from formkiq_client.models.get_users_in_group_response import GetUsersInGroupResponse
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
    api_instance = formkiq_client.UserManagementApi(api_client)
    group_name = 'group_name_example' # str | Fetch documents inserted on a certain date (yyyy-MM-dd)
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)

    try:
        # Get users in a group
        api_response = api_instance.get_users_in_group(group_name, limit=limit, next=next)
        print("The response of UserManagementApi->get_users_in_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->get_users_in_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| Fetch documents inserted on a certain date (yyyy-MM-dd) | 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **next** | **str**| Next page of results token | [optional] 

### Return type

[**GetUsersInGroupResponse**](GetUsersInGroupResponse.md)

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

