# DocumentReviewDecision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document Identifier | [optional] 
**artifact_id** | **str** | Artifact Identifier | [optional] 
**review_id** | **str** | Review Identifier | [optional] 
**decision_id** | **str** | Decision Identifier | [optional] 
**type** | [**ReviewDecisionType**](ReviewDecisionType.md) |  | [optional] 
**decision** | **str** | Review decision | [optional] 
**comment** | **str** | Review decision comment | [optional] 
**user_id** | **str** | User who added decision | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 

## Example

```python
from formkiq_client.models.document_review_decision import DocumentReviewDecision

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentReviewDecision from a JSON string
document_review_decision_instance = DocumentReviewDecision.from_json(json)
# print the JSON string representation of the object
print(DocumentReviewDecision.to_json())

# convert the object into a dict
document_review_decision_dict = document_review_decision_instance.to_dict()
# create an instance of DocumentReviewDecision from a dict
document_review_decision_from_dict = DocumentReviewDecision.from_dict(document_review_decision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


