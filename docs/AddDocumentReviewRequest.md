# AddDocumentReviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**review** | [**AddDocumentReview**](AddDocumentReview.md) |  | [optional] 

## Example

```python
from formkiq_client.models.add_document_review_request import AddDocumentReviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentReviewRequest from a JSON string
add_document_review_request_instance = AddDocumentReviewRequest.from_json(json)
# print the JSON string representation of the object
print(AddDocumentReviewRequest.to_json())

# convert the object into a dict
add_document_review_request_dict = add_document_review_request_instance.to_dict()
# create an instance of AddDocumentReviewRequest from a dict
add_document_review_request_from_dict = AddDocumentReviewRequest.from_dict(add_document_review_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


