# UpdateDocumentReviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**review** | [**UpdateDocumentReview**](UpdateDocumentReview.md) |  | [optional] 

## Example

```python
from formkiq_client.models.update_document_review_request import UpdateDocumentReviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDocumentReviewRequest from a JSON string
update_document_review_request_instance = UpdateDocumentReviewRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDocumentReviewRequest.to_json())

# convert the object into a dict
update_document_review_request_dict = update_document_review_request_instance.to_dict()
# create an instance of UpdateDocumentReviewRequest from a dict
update_document_review_request_from_dict = UpdateDocumentReviewRequest.from_dict(update_document_review_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


