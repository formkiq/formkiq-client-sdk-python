# DocumentConfigContentTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowlist** | **List[str]** |  | [optional] 
**denylist** | **List[str]** |  | [optional] 

## Example

```python
from formkiq_client.models.document_config_content_types import DocumentConfigContentTypes

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentConfigContentTypes from a JSON string
document_config_content_types_instance = DocumentConfigContentTypes.from_json(json)
# print the JSON string representation of the object
print(DocumentConfigContentTypes.to_json())

# convert the object into a dict
document_config_content_types_dict = document_config_content_types_instance.to_dict()
# create an instance of DocumentConfigContentTypes from a dict
document_config_content_types_from_dict = DocumentConfigContentTypes.from_dict(document_config_content_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


