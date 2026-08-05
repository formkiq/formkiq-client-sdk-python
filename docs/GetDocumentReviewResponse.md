# GetDocumentReviewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**review** | [**DocumentReview**](DocumentReview.md) |  | [optional] 

## Example

```python
from formkiq_client.models.get_document_review_response import GetDocumentReviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentReviewResponse from a JSON string
get_document_review_response_instance = GetDocumentReviewResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocumentReviewResponse.to_json())

# convert the object into a dict
get_document_review_response_dict = get_document_review_response_instance.to_dict()
# create an instance of GetDocumentReviewResponse from a dict
get_document_review_response_from_dict = GetDocumentReviewResponse.from_dict(get_document_review_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


