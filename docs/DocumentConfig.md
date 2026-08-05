# DocumentConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_types** | [**DocumentConfigContentTypes**](DocumentConfigContentTypes.md) |  | [optional] 
**retention_and_disposition** | [**DocumentConfigRetentionAndDisposition**](DocumentConfigRetentionAndDisposition.md) |  | [optional] 

## Example

```python
from formkiq_client.models.document_config import DocumentConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentConfig from a JSON string
document_config_instance = DocumentConfig.from_json(json)
# print the JSON string representation of the object
print(DocumentConfig.to_json())

# convert the object into a dict
document_config_dict = document_config_instance.to_dict()
# create an instance of DocumentConfig from a dict
document_config_from_dict = DocumentConfig.from_dict(document_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


