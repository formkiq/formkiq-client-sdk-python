# UpdateDocumentReview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**review_status** | [**DocumentReviewStatus**](DocumentReviewStatus.md) |  | [optional] 
**required_decisions** | **int** | Number of decisions required to complete the review | [optional] 
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


