# GetDocumentReviewDecisionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**decisions** | [**List[DocumentReviewDecision]**](DocumentReviewDecision.md) | List of document review decisions | [optional] 

## Example

```python
from formkiq_client.models.get_document_review_decisions_response import GetDocumentReviewDecisionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDocumentReviewDecisionsResponse from a JSON string
get_document_review_decisions_response_instance = GetDocumentReviewDecisionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetDocumentReviewDecisionsResponse.to_json())

# convert the object into a dict
get_document_review_decisions_response_dict = get_document_review_decisions_response_instance.to_dict()
# create an instance of GetDocumentReviewDecisionsResponse from a dict
get_document_review_decisions_response_from_dict = GetDocumentReviewDecisionsResponse.from_dict(get_document_review_decisions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


