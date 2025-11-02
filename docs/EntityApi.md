# openapi_client.EntityApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_entity**](EntityApi.md#add_entity) | **POST** /entities/{entityTypeId} | Add New Entity
[**add_entity_type**](EntityApi.md#add_entity_type) | **POST** /entityTypes | Add New EntityType
[**delete_entity**](EntityApi.md#delete_entity) | **DELETE** /entities/{entityTypeId}/{entityId} | Deletes Entity
[**delete_entity_type**](EntityApi.md#delete_entity_type) | **DELETE** /entityTypes/{entityTypeId} | Deletes Entity Type
[**get_entities**](EntityApi.md#get_entities) | **GET** /entities/{entityTypeId} | Get Entities
[**get_entity**](EntityApi.md#get_entity) | **GET** /entities/{entityTypeId}/{entityId} | Get Entity
[**get_entity_type**](EntityApi.md#get_entity_type) | **GET** /entityTypes/{entityTypeId} | Get EntityType
[**get_entity_types**](EntityApi.md#get_entity_types) | **GET** /entityTypes | Get EntityTypes
[**update_entity**](EntityApi.md#update_entity) | **PATCH** /entities/{entityTypeId}/{entityId} | Update Entity


# **add_entity**
> AddEntityResponse add_entity(entity_type_id, add_entity_request, site_id=site_id, namespace=namespace)

Add New Entity

Creates a Entity

### Example


```python
import openapi_client
from openapi_client.models.add_entity_request import AddEntityRequest
from openapi_client.models.add_entity_response import AddEntityResponse
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
    api_instance = openapi_client.EntityApi(api_client)
    entity_type_id = 'entity_type_id_example' # str | EntityType Identifier
    add_entity_request = openapi_client.AddEntityRequest() # AddEntityRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)
    namespace = 'namespace_example' # str | Namespace Identifier (optional)

    try:
        # Add New Entity
        api_response = api_instance.add_entity(entity_type_id, add_entity_request, site_id=site_id, namespace=namespace)
        print("The response of EntityApi->add_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->add_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type_id** | **str**| EntityType Identifier | 
 **add_entity_request** | [**AddEntityRequest**](AddEntityRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 
 **namespace** | **str**| Namespace Identifier | [optional] 

### Return type

[**AddEntityResponse**](AddEntityResponse.md)

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

# **add_entity_type**
> AddEntityTypeResponse add_entity_type(add_entity_type_request, site_id=site_id)

Add New EntityType

Creates a Entity Type

### Example


```python
import openapi_client
from openapi_client.models.add_entity_type_request import AddEntityTypeRequest
from openapi_client.models.add_entity_type_response import AddEntityTypeResponse
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
    api_instance = openapi_client.EntityApi(api_client)
    add_entity_type_request = openapi_client.AddEntityTypeRequest() # AddEntityTypeRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Add New EntityType
        api_response = api_instance.add_entity_type(add_entity_type_request, site_id=site_id)
        print("The response of EntityApi->add_entity_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->add_entity_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_entity_type_request** | [**AddEntityTypeRequest**](AddEntityTypeRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 

### Return type

[**AddEntityTypeResponse**](AddEntityTypeResponse.md)

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

# **delete_entity**
> DeleteResponse delete_entity(entity_type_id, entity_id, site_id=site_id)

Deletes Entity

Deletes Entity

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
    api_instance = openapi_client.EntityApi(api_client)
    entity_type_id = 'entity_type_id_example' # str | EntityType Identifier
    entity_id = 'entity_id_example' # str | Entity Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Deletes Entity
        api_response = api_instance.delete_entity(entity_type_id, entity_id, site_id=site_id)
        print("The response of EntityApi->delete_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->delete_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type_id** | **str**| EntityType Identifier | 
 **entity_id** | **str**| Entity Identifier | 
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

# **delete_entity_type**
> DeleteResponse delete_entity_type(entity_type_id, site_id=site_id)

Deletes Entity Type

Deletes Entity Type

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
    api_instance = openapi_client.EntityApi(api_client)
    entity_type_id = 'entity_type_id_example' # str | EntityType Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)

    try:
        # Deletes Entity Type
        api_response = api_instance.delete_entity_type(entity_type_id, site_id=site_id)
        print("The response of EntityApi->delete_entity_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->delete_entity_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type_id** | **str**| EntityType Identifier | 
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

# **get_entities**
> GetEntitiesResponse get_entities(entity_type_id, site_id=site_id, namespace=namespace, next=next, limit=limit)

Get Entities

Returns a list of entities

### Example


```python
import openapi_client
from openapi_client.models.get_entities_response import GetEntitiesResponse
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
    api_instance = openapi_client.EntityApi(api_client)
    entity_type_id = 'entity_type_id_example' # str | EntityType Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    namespace = 'namespace_example' # str | Namespace Identifier (optional)
    next = 'next_example' # str | Next page of results token (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')

    try:
        # Get Entities
        api_response = api_instance.get_entities(entity_type_id, site_id=site_id, namespace=namespace, next=next, limit=limit)
        print("The response of EntityApi->get_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->get_entities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type_id** | **str**| EntityType Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **namespace** | **str**| Namespace Identifier | [optional] 
 **next** | **str**| Next page of results token | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]

### Return type

[**GetEntitiesResponse**](GetEntitiesResponse.md)

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

# **get_entity**
> GetEntityResponse get_entity(entity_type_id, entity_id, site_id=site_id, namespace=namespace)

Get Entity

Returns a entity

### Example


```python
import openapi_client
from openapi_client.models.get_entity_response import GetEntityResponse
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
    api_instance = openapi_client.EntityApi(api_client)
    entity_type_id = 'entity_type_id_example' # str | EntityType Identifier
    entity_id = 'entity_id_example' # str | Entity Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    namespace = 'namespace_example' # str | Namespace Identifier (optional)

    try:
        # Get Entity
        api_response = api_instance.get_entity(entity_type_id, entity_id, site_id=site_id, namespace=namespace)
        print("The response of EntityApi->get_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->get_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type_id** | **str**| EntityType Identifier | 
 **entity_id** | **str**| Entity Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **namespace** | **str**| Namespace Identifier | [optional] 

### Return type

[**GetEntityResponse**](GetEntityResponse.md)

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

# **get_entity_type**
> GetEntityTypeResponse get_entity_type(entity_type_id, site_id=site_id, namespace=namespace)

Get EntityType

Returns a entity type

### Example


```python
import openapi_client
from openapi_client.models.get_entity_type_response import GetEntityTypeResponse
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
    api_instance = openapi_client.EntityApi(api_client)
    entity_type_id = 'entity_type_id_example' # str | EntityType Identifier
    site_id = 'site_id_example' # str | Site Identifier (optional)
    namespace = 'namespace_example' # str | Namespace Identifier (optional)

    try:
        # Get EntityType
        api_response = api_instance.get_entity_type(entity_type_id, site_id=site_id, namespace=namespace)
        print("The response of EntityApi->get_entity_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->get_entity_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type_id** | **str**| EntityType Identifier | 
 **site_id** | **str**| Site Identifier | [optional] 
 **namespace** | **str**| Namespace Identifier | [optional] 

### Return type

[**GetEntityTypeResponse**](GetEntityTypeResponse.md)

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

# **get_entity_types**
> GetEntityTypesResponse get_entity_types(site_id=site_id, namespace=namespace, next=next, limit=limit)

Get EntityTypes

Returns a list of entity types

### Example


```python
import openapi_client
from openapi_client.models.get_entity_types_response import GetEntityTypesResponse
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
    api_instance = openapi_client.EntityApi(api_client)
    site_id = 'site_id_example' # str | Site Identifier (optional)
    namespace = 'namespace_example' # str | Namespace Identifier (optional)
    next = 'next_example' # str | Next page of results token (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')

    try:
        # Get EntityTypes
        api_response = api_instance.get_entity_types(site_id=site_id, namespace=namespace, next=next, limit=limit)
        print("The response of EntityApi->get_entity_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->get_entity_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| Site Identifier | [optional] 
 **namespace** | **str**| Namespace Identifier | [optional] 
 **next** | **str**| Next page of results token | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]

### Return type

[**GetEntityTypesResponse**](GetEntityTypesResponse.md)

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

# **update_entity**
> UpdateResponse update_entity(entity_type_id, entity_id, update_entity_request, site_id=site_id, namespace=namespace)

Update Entity

Updates a Entity

### Example


```python
import openapi_client
from openapi_client.models.update_entity_request import UpdateEntityRequest
from openapi_client.models.update_response import UpdateResponse
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
    api_instance = openapi_client.EntityApi(api_client)
    entity_type_id = 'entity_type_id_example' # str | EntityType Identifier
    entity_id = 'entity_id_example' # str | Entity Identifier
    update_entity_request = openapi_client.UpdateEntityRequest() # UpdateEntityRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)
    namespace = 'namespace_example' # str | Namespace Identifier (optional)

    try:
        # Update Entity
        api_response = api_instance.update_entity(entity_type_id, entity_id, update_entity_request, site_id=site_id, namespace=namespace)
        print("The response of EntityApi->update_entity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityApi->update_entity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type_id** | **str**| EntityType Identifier | 
 **entity_id** | **str**| Entity Identifier | 
 **update_entity_request** | [**UpdateEntityRequest**](UpdateEntityRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 
 **namespace** | **str**| Namespace Identifier | [optional] 

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
**400** | 400 OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

