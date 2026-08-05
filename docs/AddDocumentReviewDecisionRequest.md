# AddDocumentReviewDecisionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decision** | [**AddDocumentReviewDecision**](AddDocumentReviewDecision.md) |  | 

## Example

```python
from formkiq_client.models.add_document_review_decision_request import AddDocumentReviewDecisionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentReviewDecisionRequest from a JSON string
add_document_review_decision_request_instance = AddDocumentReviewDecisionRequest.from_json(json)
# print the JSON string representation of the object
print(AddDocumentReviewDecisionRequest.to_json())

# convert the object into a dict
add_document_review_decision_request_dict = add_document_review_decision_request_instance.to_dict()
# create an instance of AddDocumentReviewDecisionRequest from a dict
add_document_review_decision_request_from_dict = AddDocumentReviewDecisionRequest.from_dict(add_document_review_decision_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


