# formkiq_client.RulesetsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_rule**](RulesetsApi.md#add_rule) | **POST** /rulesets/{rulesetId}/rules | Add New Rule
[**add_ruleset**](RulesetsApi.md#add_ruleset) | **POST** /rulesets | Add New Ruleset
[**delete_rule**](RulesetsApi.md#delete_rule) | **DELETE** /rulesets/{rulesetId}/rules/{ruleId} | Delete Rule
[**delete_ruleset**](RulesetsApi.md#delete_ruleset) | **DELETE** /rulesets/{rulesetId} | Delete Ruleset
[**get_rule**](RulesetsApi.md#get_rule) | **GET** /rulesets/{rulesetId}/rules/{ruleId} | Get Rule
[**get_rules**](RulesetsApi.md#get_rules) | **GET** /rulesets/{rulesetId}/rules | Get Rules
[**get_ruleset**](RulesetsApi.md#get_ruleset) | **GET** /rulesets/{rulesetId} | Get Ruleset
[**get_rulesets**](RulesetsApi.md#get_rulesets) | **GET** /rulesets | Get Rulesets
[**update_rule**](RulesetsApi.md#update_rule) | **PATCH** /rulesets/{rulesetId}/rules/{ruleId} | Update Rule
[**update_ruleset**](RulesetsApi.md#update_ruleset) | **PATCH** /rulesets/{rulesetId} | Update Ruleset


# **add_rule**
> AddRuleResponse add_rule(ruleset_id, add_rule_request, site_id=site_id)

Add New Rule

Creates a new rule; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.add_rule_request import AddRuleRequest
from formkiq_client.models.add_rule_response import AddRuleResponse
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
    api_instance = formkiq_client.RulesetsApi(api_client)
    ruleset_id = 'ruleset_id_example' # str | Ruleset Identifier
    add_rule_request = formkiq_client.AddRuleRequest() # AddRuleRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Add New Rule
        api_response = api_instance.add_rule(ruleset_id, add_rule_request, site_id=site_id)
        print("The response of RulesetsApi->add_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesetsApi->add_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ruleset_id** | **str**| Ruleset Identifier | 
 **add_rule_request** | [**AddRuleRequest**](AddRuleRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**AddRuleResponse**](AddRuleResponse.md)

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

# **add_ruleset**
> AddRulesetResponse add_ruleset(add_ruleset_request, site_id=site_id)

Add New Ruleset

Creates a new ruleset; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.add_ruleset_request import AddRulesetRequest
from formkiq_client.models.add_ruleset_response import AddRulesetResponse
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
    api_instance = formkiq_client.RulesetsApi(api_client)
    add_ruleset_request = formkiq_client.AddRulesetRequest() # AddRulesetRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Add New Ruleset
        api_response = api_instance.add_ruleset(add_ruleset_request, site_id=site_id)
        print("The response of RulesetsApi->add_ruleset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesetsApi->add_ruleset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_ruleset_request** | [**AddRulesetRequest**](AddRulesetRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**AddRulesetResponse**](AddRulesetResponse.md)

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

# **delete_rule**
> DeleteRuleResponse delete_rule(ruleset_id, rule_id, site_id=site_id)

Delete Rule

Delete Rule; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.delete_rule_response import DeleteRuleResponse
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
    api_instance = formkiq_client.RulesetsApi(api_client)
    ruleset_id = 'ruleset_id_example' # str | Ruleset Identifier
    rule_id = 'rule_id_example' # str | Rule Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Delete Rule
        api_response = api_instance.delete_rule(ruleset_id, rule_id, site_id=site_id)
        print("The response of RulesetsApi->delete_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesetsApi->delete_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ruleset_id** | **str**| Ruleset Identifier | 
 **rule_id** | **str**| Rule Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**DeleteRuleResponse**](DeleteRuleResponse.md)

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

# **delete_ruleset**
> DeleteRulesetResponse delete_ruleset(ruleset_id, site_id=site_id)

Delete Ruleset

Delete Ruleset; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.delete_ruleset_response import DeleteRulesetResponse
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
    api_instance = formkiq_client.RulesetsApi(api_client)
    ruleset_id = 'ruleset_id_example' # str | Ruleset Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Delete Ruleset
        api_response = api_instance.delete_ruleset(ruleset_id, site_id=site_id)
        print("The response of RulesetsApi->delete_ruleset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesetsApi->delete_ruleset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ruleset_id** | **str**| Ruleset Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**DeleteRulesetResponse**](DeleteRulesetResponse.md)

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

# **get_rule**
> GetRuleResponse get_rule(ruleset_id, rule_id, site_id=site_id)

Get Rule

Returns a rule in a ruleset; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.get_rule_response import GetRuleResponse
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
    api_instance = formkiq_client.RulesetsApi(api_client)
    ruleset_id = 'ruleset_id_example' # str | Ruleset Identifier
    rule_id = 'rule_id_example' # str | Rule Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Get Rule
        api_response = api_instance.get_rule(ruleset_id, rule_id, site_id=site_id)
        print("The response of RulesetsApi->get_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesetsApi->get_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ruleset_id** | **str**| Ruleset Identifier | 
 **rule_id** | **str**| Rule Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**GetRuleResponse**](GetRuleResponse.md)

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

# **get_rules**
> GetRulesResponse get_rules(ruleset_id, site_id=site_id, next=next, limit=limit)

Get Rules

Returns a list of rules in a ruleset; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.get_rules_response import GetRulesResponse
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
    api_instance = formkiq_client.RulesetsApi(api_client)
    ruleset_id = 'ruleset_id_example' # str | Ruleset Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    next = 'next_example' # str | Next page of results token (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')

    try:
        # Get Rules
        api_response = api_instance.get_rules(ruleset_id, site_id=site_id, next=next, limit=limit)
        print("The response of RulesetsApi->get_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesetsApi->get_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ruleset_id** | **str**| Ruleset Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **next** | **str**| Next page of results token | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]

### Return type

[**GetRulesResponse**](GetRulesResponse.md)

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

# **get_ruleset**
> GetRulesetResponse get_ruleset(ruleset_id, site_id=site_id)

Get Ruleset

Get a rule sets; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.get_ruleset_response import GetRulesetResponse
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
    api_instance = formkiq_client.RulesetsApi(api_client)
    ruleset_id = 'ruleset_id_example' # str | Ruleset Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Get Ruleset
        api_response = api_instance.get_ruleset(ruleset_id, site_id=site_id)
        print("The response of RulesetsApi->get_ruleset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesetsApi->get_ruleset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ruleset_id** | **str**| Ruleset Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**GetRulesetResponse**](GetRulesetResponse.md)

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

# **get_rulesets**
> GetRulesetsResponse get_rulesets(site_id=site_id, next=next, limit=limit)

Get Rulesets

Returns a list of rule sets; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.get_rulesets_response import GetRulesetsResponse
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
    api_instance = formkiq_client.RulesetsApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier (optional)
    next = 'next_example' # str | Next page of results token (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')

    try:
        # Get Rulesets
        api_response = api_instance.get_rulesets(site_id=site_id, next=next, limit=limit)
        print("The response of RulesetsApi->get_rulesets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesetsApi->get_rulesets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | [optional] 
 **next** | **str**| Next page of results token | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]

### Return type

[**GetRulesetsResponse**](GetRulesetsResponse.md)

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

# **update_rule**
> UpdateRuleResponse update_rule(ruleset_id, rule_id, update_rule_request, site_id=site_id)

Update Rule

Update Rule; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.update_rule_request import UpdateRuleRequest
from formkiq_client.models.update_rule_response import UpdateRuleResponse
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
    api_instance = formkiq_client.RulesetsApi(api_client)
    ruleset_id = 'ruleset_id_example' # str | Ruleset Identifier
    rule_id = 'rule_id_example' # str | Rule Identifier
    update_rule_request = formkiq_client.UpdateRuleRequest() # UpdateRuleRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Update Rule
        api_response = api_instance.update_rule(ruleset_id, rule_id, update_rule_request, site_id=site_id)
        print("The response of RulesetsApi->update_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesetsApi->update_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ruleset_id** | **str**| Ruleset Identifier | 
 **rule_id** | **str**| Rule Identifier | 
 **update_rule_request** | [**UpdateRuleRequest**](UpdateRuleRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**UpdateRuleResponse**](UpdateRuleResponse.md)

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

# **update_ruleset**
> UpdateRulesetResponse update_ruleset(ruleset_id, update_ruleset_request, site_id=site_id)

Update Ruleset

Updates an existing ruleset; available as an Add-On Module

### Example


```python
import formkiq_client
from formkiq_client.models.update_ruleset_request import UpdateRulesetRequest
from formkiq_client.models.update_ruleset_response import UpdateRulesetResponse
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
    api_instance = formkiq_client.RulesetsApi(api_client)
    ruleset_id = 'ruleset_id_example' # str | Ruleset Identifier
    update_ruleset_request = formkiq_client.UpdateRulesetRequest() # UpdateRulesetRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Update Ruleset
        api_response = api_instance.update_ruleset(ruleset_id, update_ruleset_request, site_id=site_id)
        print("The response of RulesetsApi->update_ruleset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RulesetsApi->update_ruleset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ruleset_id** | **str**| Ruleset Identifier | 
 **update_ruleset_request** | [**UpdateRulesetRequest**](UpdateRulesetRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**UpdateRulesetResponse**](UpdateRulesetResponse.md)

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

