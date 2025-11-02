# openapi_client.SchemasApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_classification**](SchemasApi.md#add_classification) | **POST** /sites/{siteId}/classifications | Add Classification
[**delete_classification**](SchemasApi.md#delete_classification) | **DELETE** /sites/{siteId}/classifications/{classificationId} | Delete Classification
[**get_classification**](SchemasApi.md#get_classification) | **GET** /sites/{siteId}/classifications/{classificationId} | Get Classification
[**get_classification_attribute_allowed_values**](SchemasApi.md#get_classification_attribute_allowed_values) | **GET** /sites/{siteId}/classifications/{classificationId}/attributes/{key}/allowedValues | Get Classification&#39;s Attribute Allowed Values
[**get_sites_classifications**](SchemasApi.md#get_sites_classifications) | **GET** /sites/{siteId}/classifications | Get Sites Classifications
[**get_sites_schema**](SchemasApi.md#get_sites_schema) | **GET** /sites/{siteId}/schema/document | Get Sites Schema
[**get_sites_schema_attribute_allowed_values**](SchemasApi.md#get_sites_schema_attribute_allowed_values) | **GET** /sites/{siteId}/schema/document/attributes/{key}/allowedValues | Get Attribute Allowed Values
[**set_classification**](SchemasApi.md#set_classification) | **PUT** /sites/{siteId}/classifications/{classificationId} | Set Classification
[**set_sites_schema**](SchemasApi.md#set_sites_schema) | **PUT** /sites/{siteId}/schema/document | Set Sites Schema


# **add_classification**
> AddClassificationResponse add_classification(site_id, add_classification_request)

Add Classification

Add Classification

### Example


```python
import openapi_client
from openapi_client.models.add_classification_request import AddClassificationRequest
from openapi_client.models.add_classification_response import AddClassificationResponse
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
    api_instance = openapi_client.SchemasApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    add_classification_request = openapi_client.AddClassificationRequest() # AddClassificationRequest | 

    try:
        # Add Classification
        api_response = api_instance.add_classification(site_id, add_classification_request)
        print("The response of SchemasApi->add_classification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemasApi->add_classification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **add_classification_request** | [**AddClassificationRequest**](AddClassificationRequest.md)|  | 

### Return type

[**AddClassificationResponse**](AddClassificationResponse.md)

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

# **delete_classification**
> DeleteResponse delete_classification(site_id, classification_id)

Delete Classification

Delete Classification

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
    api_instance = openapi_client.SchemasApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    classification_id = 'classification_id_example' # str | Classification Identifier

    try:
        # Delete Classification
        api_response = api_instance.delete_classification(site_id, classification_id)
        print("The response of SchemasApi->delete_classification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemasApi->delete_classification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **classification_id** | **str**| Classification Identifier | 

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

# **get_classification**
> GetClassificationResponse get_classification(site_id, classification_id, locale=locale)

Get Classification

Get Classification

### Example


```python
import openapi_client
from openapi_client.models.get_classification_response import GetClassificationResponse
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
    api_instance = openapi_client.SchemasApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    classification_id = 'classification_id_example' # str | Classification Identifier
    locale = 'locale_example' # str | Site Locale (ISO 639 / ISO 3166) (optional)

    try:
        # Get Classification
        api_response = api_instance.get_classification(site_id, classification_id, locale=locale)
        print("The response of SchemasApi->get_classification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemasApi->get_classification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **classification_id** | **str**| Classification Identifier | 
 **locale** | **str**| Site Locale (ISO 639 / ISO 3166) | [optional] 

### Return type

[**GetClassificationResponse**](GetClassificationResponse.md)

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

# **get_classification_attribute_allowed_values**
> GetAttributeAllowedValuesResponse get_classification_attribute_allowed_values(site_id, classification_id, key, locale=locale)

Get Classification's Attribute Allowed Values

Returns an attribute's allowed values that spans for a specific classifications and site schema

### Example


```python
import openapi_client
from openapi_client.models.get_attribute_allowed_values_response import GetAttributeAllowedValuesResponse
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
    api_instance = openapi_client.SchemasApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    classification_id = 'classification_id_example' # str | Classification Identifier
    key = 'key_example' # str | Key Identifier
    locale = 'locale_example' # str | Site Locale (ISO 639 / ISO 3166) (optional)

    try:
        # Get Classification's Attribute Allowed Values
        api_response = api_instance.get_classification_attribute_allowed_values(site_id, classification_id, key, locale=locale)
        print("The response of SchemasApi->get_classification_attribute_allowed_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemasApi->get_classification_attribute_allowed_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **classification_id** | **str**| Classification Identifier | 
 **key** | **str**| Key Identifier | 
 **locale** | **str**| Site Locale (ISO 639 / ISO 3166) | [optional] 

### Return type

[**GetAttributeAllowedValuesResponse**](GetAttributeAllowedValuesResponse.md)

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

# **get_sites_classifications**
> GetClassificationsResponse get_sites_classifications(site_id, limit=limit, next=next)

Get Sites Classifications

Gets Sites Classifications

### Example


```python
import openapi_client
from openapi_client.models.get_classifications_response import GetClassificationsResponse
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
    api_instance = openapi_client.SchemasApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)

    try:
        # Get Sites Classifications
        api_response = api_instance.get_sites_classifications(site_id, limit=limit, next=next)
        print("The response of SchemasApi->get_sites_classifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemasApi->get_sites_classifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **next** | **str**| Next page of results token | [optional] 

### Return type

[**GetClassificationsResponse**](GetClassificationsResponse.md)

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

# **get_sites_schema**
> GetSitesSchemaResponse get_sites_schema(site_id, locale=locale)

Get Sites Schema

Gets Sites schema

### Example


```python
import openapi_client
from openapi_client.models.get_sites_schema_response import GetSitesSchemaResponse
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
    api_instance = openapi_client.SchemasApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    locale = 'locale_example' # str | Site Locale (ISO 639 / ISO 3166) (optional)

    try:
        # Get Sites Schema
        api_response = api_instance.get_sites_schema(site_id, locale=locale)
        print("The response of SchemasApi->get_sites_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemasApi->get_sites_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **locale** | **str**| Site Locale (ISO 639 / ISO 3166) | [optional] 

### Return type

[**GetSitesSchemaResponse**](GetSitesSchemaResponse.md)

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

# **get_sites_schema_attribute_allowed_values**
> GetAttributeAllowedValuesResponse get_sites_schema_attribute_allowed_values(site_id, key, locale=locale)

Get Attribute Allowed Values

Returns an attribute's allowed values from the site schema

### Example


```python
import openapi_client
from openapi_client.models.get_attribute_allowed_values_response import GetAttributeAllowedValuesResponse
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
    api_instance = openapi_client.SchemasApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    key = 'key_example' # str | Key Identifier
    locale = 'locale_example' # str | Site Locale (ISO 639 / ISO 3166) (optional)

    try:
        # Get Attribute Allowed Values
        api_response = api_instance.get_sites_schema_attribute_allowed_values(site_id, key, locale=locale)
        print("The response of SchemasApi->get_sites_schema_attribute_allowed_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemasApi->get_sites_schema_attribute_allowed_values: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **key** | **str**| Key Identifier | 
 **locale** | **str**| Site Locale (ISO 639 / ISO 3166) | [optional] 

### Return type

[**GetAttributeAllowedValuesResponse**](GetAttributeAllowedValuesResponse.md)

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

# **set_classification**
> SetResponse set_classification(site_id, classification_id, set_classification_request)

Set Classification

Sets Classification

### Example


```python
import openapi_client
from openapi_client.models.set_classification_request import SetClassificationRequest
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
    api_instance = openapi_client.SchemasApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    classification_id = 'classification_id_example' # str | Classification Identifier
    set_classification_request = openapi_client.SetClassificationRequest() # SetClassificationRequest | 

    try:
        # Set Classification
        api_response = api_instance.set_classification(site_id, classification_id, set_classification_request)
        print("The response of SchemasApi->set_classification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemasApi->set_classification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **classification_id** | **str**| Classification Identifier | 
 **set_classification_request** | [**SetClassificationRequest**](SetClassificationRequest.md)|  | 

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
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | 400 OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_sites_schema**
> SetResponse set_sites_schema(site_id, set_sites_schema_request)

Set Sites Schema

Sets Sites schema

### Example


```python
import openapi_client
from openapi_client.models.set_response import SetResponse
from openapi_client.models.set_sites_schema_request import SetSitesSchemaRequest
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
    api_instance = openapi_client.SchemasApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier
    set_sites_schema_request = openapi_client.SetSitesSchemaRequest() # SetSitesSchemaRequest | 

    try:
        # Set Sites Schema
        api_response = api_instance.set_sites_schema(site_id, set_sites_schema_request)
        print("The response of SchemasApi->set_sites_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemasApi->set_sites_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | 
 **set_sites_schema_request** | [**SetSitesSchemaRequest**](SetSitesSchemaRequest.md)|  | 

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
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | 400 OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

