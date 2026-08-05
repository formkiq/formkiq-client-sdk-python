# AddDocumentReviewDecisionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decision_id** | **str** | Decision Identifier | 

## Example

```python
from formkiq_client.models.add_document_review_decision_response import AddDocumentReviewDecisionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentReviewDecisionResponse from a JSON string
add_document_review_decision_response_instance = AddDocumentReviewDecisionResponse.from_json(json)
# print the JSON string representation of the object
print(AddDocumentReviewDecisionResponse.to_json())

# convert the object into a dict
add_document_review_decision_response_dict = add_document_review_decision_response_instance.to_dict()
# create an instance of AddDocumentReviewDecisionResponse from a dict
add_document_review_decision_response_from_dict = AddDocumentReviewDecisionResponse.from_dict(add_document_review_decision_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


