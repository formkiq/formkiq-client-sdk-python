# formkiq_client.AccessControlApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_opa_access_policy_items**](AccessControlApi.md#delete_opa_access_policy_items) | **DELETE** /sites/{siteId}/opa/accessPolicy/policyItems | Delete OPA Access Policy Items
[**get_opa_access_policies**](AccessControlApi.md#get_opa_access_policies) | **GET** /sites/opa/accessPolicies | Get OPAs Access Policies
[**get_opa_access_policy**](AccessControlApi.md#get_opa_access_policy) | **GET** /sites/{siteId}/opa/accessPolicy | Get OPA Access Policy
[**get_opa_access_policy_items**](AccessControlApi.md#get_opa_access_policy_items) | **GET** /sites/{siteId}/opa/accessPolicy/policyItems | Get OPA Access Policy Items
[**set_opa_access_policy_items**](AccessControlApi.md#set_opa_access_policy_items) | **PUT** /sites/{siteId}/opa/accessPolicy/policyItems | Set opa access policy items, can only be requested with ADMIN privileges


# **delete_opa_access_policy_items**
> DeleteResponse delete_opa_access_policy_items(site_id)

Delete OPA Access Policy Items

Delete OPA Access Policy Items

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
    api_instance = formkiq_client.AccessControlApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier

    try:
        # Delete OPA Access Policy Items
        api_response = api_instance.delete_opa_access_policy_items(site_id)
        print("The response of AccessControlApi->delete_opa_access_policy_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->delete_opa_access_policy_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 

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

# **get_opa_access_policies**
> GetOpaAccessPoliciesResponse get_opa_access_policies()

Get OPAs Access Policies

Returns a list of OPA Access Policies, can only be requested with ADMIN privileges

### Example


```python
import formkiq_client
from formkiq_client.models.get_opa_access_policies_response import GetOpaAccessPoliciesResponse
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
    api_instance = formkiq_client.AccessControlApi(api_client)

    try:
        # Get OPAs Access Policies
        api_response = api_instance.get_opa_access_policies()
        print("The response of AccessControlApi->get_opa_access_policies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->get_opa_access_policies: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetOpaAccessPoliciesResponse**](GetOpaAccessPoliciesResponse.md)

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

# **get_opa_access_policy**
> GetOpaAccessPolicyResponse get_opa_access_policy(site_id)

Get OPA Access Policy

Returns OPA Access Policy, can only be requested with ADMIN privileges

### Example


```python
import formkiq_client
from formkiq_client.models.get_opa_access_policy_response import GetOpaAccessPolicyResponse
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
    api_instance = formkiq_client.AccessControlApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier

    try:
        # Get OPA Access Policy
        api_response = api_instance.get_opa_access_policy(site_id)
        print("The response of AccessControlApi->get_opa_access_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->get_opa_access_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 

### Return type

[**GetOpaAccessPolicyResponse**](GetOpaAccessPolicyResponse.md)

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

# **get_opa_access_policy_items**
> GetOpaAccessPolicyItemsResponse get_opa_access_policy_items(site_id)

Get OPA Access Policy Items

Returns OPA Access Policy Items, can only be requested with ADMIN privileges

### Example


```python
import formkiq_client
from formkiq_client.models.get_opa_access_policy_items_response import GetOpaAccessPolicyItemsResponse
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
    api_instance = formkiq_client.AccessControlApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier

    try:
        # Get OPA Access Policy Items
        api_response = api_instance.get_opa_access_policy_items(site_id)
        print("The response of AccessControlApi->get_opa_access_policy_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->get_opa_access_policy_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 

### Return type

[**GetOpaAccessPolicyItemsResponse**](GetOpaAccessPolicyItemsResponse.md)

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

# **set_opa_access_policy_items**
> SetResponse set_opa_access_policy_items(site_id, set_opa_access_policy_items_request)

Set opa access policy items, can only be requested with ADMIN privileges

Sets opa access policy items

### Example


```python
import formkiq_client
from formkiq_client.models.set_opa_access_policy_items_request import SetOpaAccessPolicyItemsRequest
from formkiq_client.models.set_response import SetResponse
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
    api_instance = formkiq_client.AccessControlApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    set_opa_access_policy_items_request = formkiq_client.SetOpaAccessPolicyItemsRequest() # SetOpaAccessPolicyItemsRequest | 

    try:
        # Set opa access policy items, can only be requested with ADMIN privileges
        api_response = api_instance.set_opa_access_policy_items(site_id, set_opa_access_policy_items_request)
        print("The response of AccessControlApi->set_opa_access_policy_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccessControlApi->set_opa_access_policy_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **set_opa_access_policy_items_request** | [**SetOpaAccessPolicyItemsRequest**](SetOpaAccessPolicyItemsRequest.md)|  | 

### Return type

[**SetResponse**](SetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 CREATED |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | 400 OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

