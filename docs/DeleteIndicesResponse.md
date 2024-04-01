# DeleteIndicesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | response message | [optional] 

## Example

```python
from formkiq_client.models.delete_indices_response import DeleteIndicesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteIndicesResponse from a JSON string
delete_indices_response_instance = DeleteIndicesResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteIndicesResponse.to_json())

# convert the object into a dict
delete_indices_response_dict = delete_indices_response_instance.to_dict()
# create an instance of DeleteIndicesResponse from a dict
delete_indices_response_form_dict = delete_indices_response.from_dict(delete_indices_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


