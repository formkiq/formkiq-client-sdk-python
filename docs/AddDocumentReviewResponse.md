# AddDocumentReviewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**review_id** | **str** | Review Identifier | 

## Example

```python
from formkiq_client.models.add_document_review_response import AddDocumentReviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentReviewResponse from a JSON string
add_document_review_response_instance = AddDocumentReviewResponse.from_json(json)
# print the JSON string representation of the object
print(AddDocumentReviewResponse.to_json())

# convert the object into a dict
add_document_review_response_dict = add_document_review_response_instance.to_dict()
# create an instance of AddDocumentReviewResponse from a dict
add_document_review_response_from_dict = AddDocumentReviewResponse.from_dict(add_document_review_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


