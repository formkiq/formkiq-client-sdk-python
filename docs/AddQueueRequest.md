# AddQueueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Queue name | 

## Example

```python
from openapi_client.models.add_queue_request import AddQueueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddQueueRequest from a JSON string
add_queue_request_instance = AddQueueRequest.from_json(json)
# print the JSON string representation of the object
print(AddQueueRequest.to_json())

# convert the object into a dict
add_queue_request_dict = add_queue_request_instance.to_dict()
# create an instance of AddQueueRequest from a dict
add_queue_request_from_dict = AddQueueRequest.from_dict(add_queue_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


