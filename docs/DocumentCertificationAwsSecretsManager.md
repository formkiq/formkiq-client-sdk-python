# DocumentCertificationAwsSecretsManager


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_arn** | **str** | Aws Secrets Manager Certificate ARN | 
**password_arn** | **str** | Aws Secrets Manager Password ARN | 

## Example

```python
from formkiq_client.models.document_certification_aws_secrets_manager import DocumentCertificationAwsSecretsManager

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCertificationAwsSecretsManager from a JSON string
document_certification_aws_secrets_manager_instance = DocumentCertificationAwsSecretsManager.from_json(json)
# print the JSON string representation of the object
print(DocumentCertificationAwsSecretsManager.to_json())

# convert the object into a dict
document_certification_aws_secrets_manager_dict = document_certification_aws_secrets_manager_instance.to_dict()
# create an instance of DocumentCertificationAwsSecretsManager from a dict
document_certification_aws_secrets_manager_from_dict = DocumentCertificationAwsSecretsManager.from_dict(document_certification_aws_secrets_manager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


