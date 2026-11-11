# UpdateDocumentReview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**review_status** | [**DocumentReviewStatus**](DocumentReviewStatus.md) |  | [optional] 
**required_decisions** | **int** | Number of decision records matching countedDecisionTypes required to complete the review. Changes apply when subsequent counted decisions are submitted. | [optional] 
**counted_decision_types** | [**List[ReviewDecisionType]**](ReviewDecisionType.md) | Replacement types of decision records that count toward requiredDecisions. Omission or null preserves the effective current policy; it does not reset it to [APPROVAL]. Changes apply when subsequent counted decisions are submitted, counting existing records against the updated policy. This does not restrict submissions. Empty arrays, duplicate entries, unknown types, and non-string entries are rejected. | [optional] 
**comments** | **str** | Review comments | [optional] 

## Example

```python
from formkiq_client.models.update_document_review import UpdateDocumentReview

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDocumentReview from a JSON string
update_document_review_instance = UpdateDocumentReview.from_json(json)
# print the JSON string representation of the object
print(UpdateDocumentReview.to_json())

# convert the object into a dict
update_document_review_dict = update_document_review_instance.to_dict()
# create an instance of UpdateDocumentReview from a dict
update_document_review_from_dict = UpdateDocumentReview.from_dict(update_document_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


