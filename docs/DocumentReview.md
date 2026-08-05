# DocumentReview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Document Identifier | [optional] 
**artifact_id** | **str** | Artifact Identifier | [optional] 
**review_id** | **str** | Review Identifier | [optional] 
**review_category** | **str** | Review category | [optional] 
**review_status** | [**DocumentReviewStatus**](DocumentReviewStatus.md) |  | [optional] 
**required_decisions** | **int** | Number of decisions required to complete the review | [optional] 
**user_id** | **str** | User who added review | [optional] 
**comments** | **str** | Review comments | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**last_modified_date** | **str** | Last Modified Timestamp | [optional] 

## Example

```python
from formkiq_client.models.document_review import DocumentReview

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentReview from a JSON string
document_review_instance = DocumentReview.from_json(json)
# print the JSON string representation of the object
print(DocumentReview.to_json())

# convert the object into a dict
document_review_dict = document_review_instance.to_dict()
# create an instance of DocumentReview from a dict
document_review_from_dict = DocumentReview.from_dict(document_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


