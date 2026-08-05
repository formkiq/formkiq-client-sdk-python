# GetDocumentReviewsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**reviews** | [**List[DocumentReview]**](DocumentReview.md) | List of document reviews | [optional] 

## Example

```python
from formkiq_client.models.get_document_reviews_response import GetDocumentReviewsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentReviewsResponse from a JSON string
get_document_reviews_response_instance = GetDocumentReviewsResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocumentReviewsResponse.to_json())

# convert the object into a dict
get_document_reviews_response_dict = get_document_reviews_response_instance.to_dict()
# create an instance of GetDocumentReviewsResponse from a dict
get_document_reviews_response_from_dict = GetDocumentReviewsResponse.from_dict(get_document_reviews_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


