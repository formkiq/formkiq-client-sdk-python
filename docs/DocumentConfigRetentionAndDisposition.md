# DocumentConfigRetentionAndDisposition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disposition_action** | [**DocumentConfigDispositionAction**](DocumentConfigDispositionAction.md) |  | [optional] [default to DocumentConfigDispositionAction.SOFT_DELETE]
**soft_delete_retention_in_days** | **int** | Number of days to retain soft deleted documents before permanent deletion. Use -1 to retain soft deleted documents until trash is cleared manually. | [optional] [default to -1]

## Example

```python
from formkiq_client.models.document_config_retention_and_disposition import DocumentConfigRetentionAndDisposition

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentConfigRetentionAndDisposition from a JSON string
document_config_retention_and_disposition_instance = DocumentConfigRetentionAndDisposition.from_json(json)
# print the JSON string representation of the object
print(DocumentConfigRetentionAndDisposition.to_json())

# convert the object into a dict
document_config_retention_and_disposition_dict = document_config_retention_and_disposition_instance.to_dict()
# create an instance of DocumentConfigRetentionAndDisposition from a dict
document_config_retention_and_disposition_from_dict = DocumentConfigRetentionAndDisposition.from_dict(document_config_retention_and_disposition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


