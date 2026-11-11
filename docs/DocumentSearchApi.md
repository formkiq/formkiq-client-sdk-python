# formkiq_client.DocumentSearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**document_search**](DocumentSearchApi.md#document_search) | **POST** /search | Document search


# **document_search**
> DocumentSearchResponse document_search(document_search_request, site_id=site_id, limit=limit, next=next, previous=previous, projection=projection)

Document search

Document search query request; 

Supports searching DynamoDB for document(s) by a single TAG key and/or value. Value can be "exacted" or "begins_with" matched. Search can be filtered to only check certain documentIds (up to 100 documentIds accepted).

If using Enteprise Composite Keys feature then multiple tag(s) can be searched for.

For attributes defined with dataType JSON, use an attribute criterion's json filter
with a path to compare a nested field. The eq and eqOr operators accept strings,
including inside json filters. Match JSON boolean fields using the strings "true"
or "false". Compare JSON numeric fields using gt, gte, lt, and lte.
Paths support object properties and explicit array positions;
wildcard, recursive, and array any-element matching are not supported.
Multiple conditions on different paths under the same attribute key are supported.
All conditions must match the same document or artifact.

JSON path filtering is applied after candidate records are read and does not reduce
read capacity consumed for those candidates. A stored JSON value does not automatically
create an index for its nested fields. Continue through empty filtered pages until the
next token is absent; candidate and time-budget limits still apply.

If Typesense is enabled, full text search is supported through the "text" parameter. Full text search will look for the text in the "content" and/or document "metadata".

When `documentIds` is supplied, all supplied IDs are checked against the search criteria and all matching documents are returned. The `limit` query parameter is ignored. Up to 100 document IDs are accepted.

Use the `projection` parameter to return matching documents or a count of matching documents. Count responses are capped at 10,000 and indicate when the count was truncated.
Multi-attribute searches requiring additional attribute filtering use a 25-second processing budget
for index batches, attribute filtering, and document loading. The budget starts after index selection and empty-index prechecks. Searches with explicit
`documentIds` or a composite key covering every search attribute are exempt.
The budget is checked before starting each read; an in-flight read is allowed to finish.
If the budget expires, document searches return completed matches with `truncated=true` and a `next` token;
count searches return a partial lower bound with `truncated=true`.

See requestBody examples below for commmon examples.

### Example


```python
import formkiq_client
from formkiq_client.models.document_search_request import DocumentSearchRequest
from formkiq_client.models.document_search_response import DocumentSearchResponse
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
    api_instance = formkiq_client.DocumentSearchApi(api_client)
    document_search_request = {"query":{"attribute":{"key":"category"}}} # DocumentSearchRequest | 
    site_id = 'site_id_example' # str | Site Identifier (optional)
    limit = '10' # str | Limit Results (optional) (default to '10')
    next = 'next_example' # str | Next page of results token (optional)
    previous = 'previous_example' # str | Previous page of results token (optional)
    projection = 'DOCUMENTS' # str | Controls the search response projection. `DOCUMENTS` returns matching documents and pagination tokens. `COUNT` returns `count` and `truncated`, and omits `documents`, `next`, and `previous`. (optional) (default to 'DOCUMENTS')

    try:
        # Document search
        api_response = api_instance.document_search(document_search_request, site_id=site_id, limit=limit, next=next, previous=previous, projection=projection)
        print("The response of DocumentSearchApi->document_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentSearchApi->document_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_search_request** | [**DocumentSearchRequest**](DocumentSearchRequest.md)|  | 
 **site_id** | **str**| Site Identifier | [optional] 
 **limit** | **str**| Limit Results | [optional] [default to &#39;10&#39;]
 **next** | **str**| Next page of results token | [optional] 
 **previous** | **str**| Previous page of results token | [optional] 
 **projection** | **str**| Controls the search response projection. &#x60;DOCUMENTS&#x60; returns matching documents and pagination tokens. &#x60;COUNT&#x60; returns &#x60;count&#x60; and &#x60;truncated&#x60;, and omits &#x60;documents&#x60;, &#x60;next&#x60;, and &#x60;previous&#x60;. | [optional] [default to &#39;DOCUMENTS&#39;]

### Return type

[**DocumentSearchResponse**](DocumentSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  * Access-Control-Allow-Origin -  <br>  * Access-Control-Allow-Methods -  <br>  * Access-Control-Allow-Headers -  <br>  |
**400** | Invalid attribute search value, JSON path, or operator combination. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

