# PromoteDocumentArtifactRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact_id** | **str** | Artifact Document Identifier. Omit to clear the promoted artifact. | [optional] 

## Example

```python
from formkiq_client.models.promote_document_artifact_request import PromoteDocumentArtifactRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PromoteDocumentArtifactRequest from a JSON string
promote_document_artifact_request_instance = PromoteDocumentArtifactRequest.from_json(json)
# print the JSON string representation of the object
print(PromoteDocumentArtifactRequest.to_json())

# convert the object into a dict
promote_document_artifact_request_dict = promote_document_artifact_request_instance.to_dict()
# create an instance of PromoteDocumentArtifactRequest from a dict
promote_document_artifact_request_from_dict = PromoteDocumentArtifactRequest.from_dict(promote_document_artifact_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


