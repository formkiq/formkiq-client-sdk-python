# DocumentCertification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Certificate alias. | 
**source_type** | [**DocumentCertificationType**](DocumentCertificationType.md) |  | [optional] 
**aws_secrets_manager** | [**DocumentCertificationAwsSecretsManager**](DocumentCertificationAwsSecretsManager.md) |  | [optional] 

## Example

```python
from formkiq_client.models.document_certification import DocumentCertification

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCertification from a JSON string
document_certification_instance = DocumentCertification.from_json(json)
# print the JSON string representation of the object
print(DocumentCertification.to_json())

# convert the object into a dict
document_certification_dict = document_certification_instance.to_dict()
# create an instance of DocumentCertification from a dict
document_certification_from_dict = DocumentCertification.from_dict(document_certification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


