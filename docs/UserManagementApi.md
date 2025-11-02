# openapi_client.UserManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_group**](UserManagementApi.md#add_group) | **POST** /groups | Add a group
[**add_user**](UserManagementApi.md#add_user) | **POST** /users | Add User
[**add_user_to_group**](UserManagementApi.md#add_user_to_group) | **POST** /groups/{groupName}/users | Add User to a group
[**delete_group**](UserManagementApi.md#delete_group) | **DELETE** /groups/{groupName} | Delete Group
[**delete_username**](UserManagementApi.md#delete_username) | **DELETE** /users/{username} | Delete Username
[**get_group**](UserManagementApi.md#get_group) | **GET** /groups/{groupName} | Get a user group
[**get_groups**](UserManagementApi.md#get_groups) | **GET** /groups | Get list of user group(s)
[**get_list_of_user_groups**](UserManagementApi.md#get_list_of_user_groups) | **GET** /users/{username}/groups | Returns a list of group user belongs to
[**get_user**](UserManagementApi.md#get_user) | **GET** /users/{username} | Get a user
[**get_users**](UserManagementApi.md#get_users) | **GET** /users | Get list of user(s)
[**get_users_in_group**](UserManagementApi.md#get_users_in_group) | **GET** /groups/{groupName}/users | Get users in a group
[**remove_username_from_group**](UserManagementApi.md#remove_username_from_group) | **DELETE** /groups/{groupName}/users/{username} | Remove Username From Group
[**set_user_operation**](UserManagementApi.md#set_user_operation) | **PUT** /users/{username}/{userOperation} | Set User Operation


# **add_group**
> AddResponse add_group(add_group_request)

Add a group

Add a new group

### Example


```python
import openapi_client
from openapi_client.models.add_group_request import AddGroupRequest
from openapi_client.models.add_response import AddResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserManagementApi(api_client)
    add_group_request = openapi_client.AddGroupRequest() # AddGroupRequest | 

    try:
        # Add a group
        api_response = api_instance.add_group(add_group_request)
        print("The response of UserManagementApi->add_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->add_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_group_request** | [**AddGroupRequest**](AddGroupRequest.md)|  | 

### Return type

[**AddResponse**](AddResponse.md)

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

# **add_user**
> AddResponse add_user(add_user_request)

Add User

Adds a user

### Example


```python
import openapi_client
from openapi_client.models.add_response import AddResponse
from openapi_client.models.add_user_request import AddUserRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserManagementApi(api_client)
    add_user_request = openapi_client.AddUserRequest() # AddUserRequest | 

    try:
        # Add User
        api_response = api_instance.add_user(add_user_request)
        print("The response of UserManagementApi->add_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->add_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_user_request** | [**AddUserRequest**](AddUserRequest.md)|  | 

### Return type

[**AddResponse**](AddResponse.md)

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

# **add_user_to_group**
> AddResponse add_user_to_group(group_name, add_user_request)

Add User to a group

Adds a user to a group

### Example


```python
import openapi_client
from openapi_client.models.add_response import AddResponse
from openapi_client.models.add_user_request import AddUserRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserManagementApi(api_client)
    group_name = 'group_name_example' # str | Group Name
    add_user_request = openapi_client.AddUserRequest() # AddUserRequest | 

    try:
        # Add User to a group
        api_response = api_instance.add_user_to_group(group_name, add_user_request)
        print("The response of UserManagementApi->add_user_to_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->add_user_to_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| Group Name | 
 **add_user_request** | [**AddUserRequest**](AddUserRequest.md)|  | 

### Return type

[**AddResponse**](AddResponse.md)

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

# **delete_group**
> DeleteResponse delete_group(group_name)

Delete Group

Delete Group

### Example


```python
import openapi_client
from openapi_client.models.delete_response import DeleteResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserManagementApi(api_client)
    group_name = 'group_name_example' # str | Group Name

    try:
        # Delete Group
        api_response = api_instance.delete_group(group_name)
        print("The response of UserManagementApi->delete_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->delete_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| Group Name | 

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

# **delete_username**
> DeleteResponse delete_username(username)

Delete Username

Delete Username

### Example


```python
import openapi_client
from openapi_client.models.delete_response import DeleteResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserManagementApi(api_client)
    username = 'username_example' # str | Username

    try:
        # Delete Username
        api_response = api_instance.delete_username(username)
        print("The response of UserManagementApi->delete_username:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->delete_username: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username | 

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

# **get_group**
> GetGroupResponse get_group(group_name)

Get a user group

Returns a user group

### Example


```python
import openapi_client
from openapi_client.models.get_group_response import GetGroupResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserManagementApi(api_client)
    group_name = 'group_name_example' # str | Group Name

    try:
        # Get a user group
        api_response = api_instance.get_group(group_name)
        print("The response of UserManagementApi->get_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->get_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| Group Name | 

### Return type

[**GetGroupResponse**](GetGroupResponse.md)

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

# **get_groups**
> GetGroupsResponse get_groups(limit=limit, next=next)

Get list of user group(s)

Returns the list of user groups

### Example


```python
import openapi_client
from openapi_client.models.get_groups_response import GetGroupsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserManagementApi(api_client)
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)

    try:
        # Get list of user group(s)
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

# **get_list_of_user_groups**
> GetUserGroupsResponse get_list_of_user_groups(username, limit=limit, next=next)

Returns a list of group user belongs to

Returns a list of group user belongs to

### Example


```python
import openapi_client
from openapi_client.models.get_user_groups_response import GetUserGroupsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserManagementApi(api_client)
    username = 'username_example' # str | Username
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)

    try:
        # Returns a list of group user belongs to
        api_response = api_instance.get_list_of_user_groups(username, limit=limit, next=next)
        print("The response of UserManagementApi->get_list_of_user_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->get_list_of_user_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username | 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **next** | **str**| Next page of results token | [optional] 

### Return type

[**GetUserGroupsResponse**](GetUserGroupsResponse.md)

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

# **get_user**
> GetUserResponse get_user(username)

Get a user

Returns a user

### Example


```python
import openapi_client
from openapi_client.models.get_user_response import GetUserResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserManagementApi(api_client)
    username = 'username_example' # str | Username

    try:
        # Get a user
        api_response = api_instance.get_user(username)
        print("The response of UserManagementApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username | 

### Return type

[**GetUserResponse**](GetUserResponse.md)

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

# **get_users**
> GetUsersResponse get_users(limit=limit, next=next)

Get list of user(s)

Returns the list of users

### Example


```python
import openapi_client
from openapi_client.models.get_users_response import GetUsersResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserManagementApi(api_client)
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)

    try:
        # Get list of user(s)
        api_response = api_instance.get_users(limit=limit, next=next)
        print("The response of UserManagementApi->get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->get_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **next** | **str**| Next page of results token | [optional] 

### Return type

[**GetUsersResponse**](GetUsersResponse.md)

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
import openapi_client
from openapi_client.models.get_users_in_group_response import GetUsersInGroupResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserManagementApi(api_client)
    group_name = 'group_name_example' # str | Group Name
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
 **group_name** | **str**| Group Name | 
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

# **remove_username_from_group**
> DeleteResponse remove_username_from_group(group_name, username)

Remove Username From Group

Remove Username From Group

### Example


```python
import openapi_client
from openapi_client.models.delete_response import DeleteResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserManagementApi(api_client)
    group_name = 'group_name_example' # str | Group Name
    username = 'username_example' # str | Username

    try:
        # Remove Username From Group
        api_response = api_instance.remove_username_from_group(group_name, username)
        print("The response of UserManagementApi->remove_username_from_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->remove_username_from_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_name** | **str**| Group Name | 
 **username** | **str**| Username | 

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

# **set_user_operation**
> SetResponse set_user_operation(username, user_operation)

Set User Operation

Set User Operation (disable, enable, reset-password)

### Example


```python
import openapi_client
from openapi_client.models.set_response import SetResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.UserManagementApi(api_client)
    username = 'username_example' # str | Username
    user_operation = 'user_operation_example' # str | Username Operation

    try:
        # Set User Operation
        api_response = api_instance.set_user_operation(username, user_operation)
        print("The response of UserManagementApi->set_user_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserManagementApi->set_user_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username | 
 **user_operation** | **str**| Username Operation | 

### Return type

[**SetResponse**](SetResponse.md)

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

