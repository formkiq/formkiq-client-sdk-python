# formkiq_client.TagSchemaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_tag_schema**](TagSchemaApi.md#add_tag_schema) | **POST** /tagSchemas | Add tag schemas
[**delete_tag_schema**](TagSchemaApi.md#delete_tag_schema) | **DELETE** /tagSchemas/{tagSchemaId} | Delete tag schema
[**get_tag_schema**](TagSchemaApi.md#get_tag_schema) | **GET** /tagSchemas/{tagSchemaId} | Get tag schema
[**get_tag_schemas**](TagSchemaApi.md#get_tag_schemas) | **GET** /tagSchemas | Get tag schemas


# **add_tag_schema**
> AddTagSchemaResponse add_tag_schema(add_tag_schema_request, site_id=site_id)

Add tag schemas

Creates a new TagSchema; ONLY available with FormKiQ Pro and Enterprise

### Example


```python
import formkiq_client
from formkiq_client.models.add_tag_schema_request import AddTagSchemaRequest
from formkiq_client.models.add_tag_schema_response import AddTagSchemaResponse
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
    api_instance = formkiq_client.TagSchemaApi(api_client)
    add_tag_schema_request = formkiq_client.AddTagSchemaRequest() # AddTagSchemaRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Add tag schemas
        api_response = api_instance.add_tag_schema(add_tag_schema_request, site_id=site_id)
        print("The response of TagSchemaApi->add_tag_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagSchemaApi->add_tag_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_tag_schema_request** | [**AddTagSchemaRequest**](AddTagSchemaRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**AddTagSchemaResponse**](AddTagSchemaResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 201 CREATED |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | 400 BAD REQUEST |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag_schema**
> delete_tag_schema(tag_schema_id, site_id=site_id)

Delete tag schema

Delete a TagSchema; ONLY available with FormKiQ Pro and Enterprise

### Example


```python
import formkiq_client
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
    api_instance = formkiq_client.TagSchemaApi(api_client)
    tag_schema_id = 'tag_schema_id_example' # str | Tag Schema Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Delete tag schema
        api_instance.delete_tag_schema(tag_schema_id, site_id=site_id)
    except Exception as e:
        print("Exception when calling TagSchemaApi->delete_tag_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_schema_id** | **str**| Tag Schema Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_schema**
> GetTagSchemaResponse get_tag_schema(tag_schema_id, site_id=site_id)

Get tag schema

Retrieves a TagSchema's details, i.e., metadata; ONLY available with FormKiQ Pro and Enterprise

### Example


```python
import formkiq_client
from formkiq_client.models.get_tag_schema_response import GetTagSchemaResponse
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
    api_instance = formkiq_client.TagSchemaApi(api_client)
    tag_schema_id = 'tag_schema_id_example' # str | Tag Schema Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Get tag schema
        api_response = api_instance.get_tag_schema(tag_schema_id, site_id=site_id)
        print("The response of TagSchemaApi->get_tag_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagSchemaApi->get_tag_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_schema_id** | **str**| Tag Schema Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**GetTagSchemaResponse**](GetTagSchemaResponse.md)

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

# **get_tag_schemas**
> GetTagSchemasResponse get_tag_schemas(site_id=site_id, limit=limit, next=next, previous=previous)

Get tag schemas

Returns the list of tagSchemas; ONLY available with FormKiQ Pro and Enterprise

### Example


```python
import formkiq_client
from formkiq_client.models.get_tag_schemas_response import GetTagSchemasResponse
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
    api_instance = formkiq_client.TagSchemaApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)
    previous = 'previous_example' # str | Previous page of results token (optional)

    try:
        # Get tag schemas
        api_response = api_instance.get_tag_schemas(site_id=site_id, limit=limit, next=next, previous=previous)
        print("The response of TagSchemaApi->get_tag_schemas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagSchemaApi->get_tag_schemas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **next** | **str**| Next page of results token | [optional] 
 **previous** | **str**| Previous page of results token | [optional] 

### Return type

[**GetTagSchemasResponse**](GetTagSchemasResponse.md)

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

