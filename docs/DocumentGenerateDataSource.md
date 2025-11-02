# DocumentGenerateDataSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The data source name | [optional] 
**document_id** | **str** | Document Identifier of the data source document | 
**data_root** | **str** | The default JSON object path for the data object | [optional] [default to 'data']

## Example

```python
from openapi_client.models.document_generate_data_source import DocumentGenerateDataSource

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentGenerateDataSource from a JSON string
document_generate_data_source_instance = DocumentGenerateDataSource.from_json(json)
# print the JSON string representation of the object
print(DocumentGenerateDataSource.to_json())

# convert the object into a dict
document_generate_data_source_dict = document_generate_data_source_instance.to_dict()
# create an instance of DocumentGenerateDataSource from a dict
document_generate_data_source_from_dict = DocumentGenerateDataSource.from_dict(document_generate_data_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


