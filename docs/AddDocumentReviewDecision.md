# AddDocumentReviewDecision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ReviewDecisionType**](ReviewDecisionType.md) |  | 
**decision** | **str** | Review decision | [optional] 
**comment** | **str** | Review decision comment | [optional] 

## Example

```python
from formkiq_client.models.add_document_review_decision import AddDocumentReviewDecision

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentReviewDecision from a JSON string
add_document_review_decision_instance = AddDocumentReviewDecision.from_json(json)
# print the JSON string representation of the object
print(AddDocumentReviewDecision.to_json())

# convert the object into a dict
add_document_review_decision_dict = add_document_review_decision_instance.to_dict()
# create an instance of AddDocumentReviewDecision from a dict
add_document_review_decision_from_dict = AddDocumentReviewDecision.from_dict(add_document_review_decision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


