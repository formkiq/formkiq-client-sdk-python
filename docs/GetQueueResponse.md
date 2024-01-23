# GetQueueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Queue name | [optional] 

## Example

```python
from formkiq_client.models.get_queue_response import GetQueueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetQueueResponse from a JSON string
get_queue_response_instance = GetQueueResponse.from_json(json)
# print the JSON string representation of the object
print GetQueueResponse.to_json()

# convert the object into a dict
get_queue_response_dict = get_queue_response_instance.to_dict()
# create an instance of GetQueueResponse from a dict
get_queue_response_form_dict = get_queue_response.from_dict(get_queue_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


