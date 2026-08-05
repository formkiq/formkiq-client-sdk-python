# AddDocumentReview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**review_category** | **str** | Review category | 
**review_status** | [**DocumentReviewStatus**](DocumentReviewStatus.md) |  | [optional] 
**required_decisions** | **int** | Number of decisions required to complete the review | 
**comments** | **str** | Review comments | [optional] 

## Example

```python
from formkiq_client.models.add_document_review import AddDocumentReview

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocumentReview from a JSON string
add_document_review_instance = AddDocumentReview.from_json(json)
# print the JSON string representation of the object
print(AddDocumentReview.to_json())

# convert the object into a dict
add_document_review_dict = add_document_review_instance.to_dict()
# create an instance of AddDocumentReview from a dict
add_document_review_from_dict = AddDocumentReview.from_dict(add_document_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


