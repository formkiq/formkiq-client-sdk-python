# GetQueuesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**queues** | [**List[Queue]**](Queue.md) | List of queues | [optional] 

## Example

```python
from openapi_client.models.get_queues_response import GetQueuesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetQueuesResponse from a JSON string
get_queues_response_instance = GetQueuesResponse.from_json(json)
# print the JSON string representation of the object
print(GetQueuesResponse.to_json())

# convert the object into a dict
get_queues_response_dict = get_queues_response_instance.to_dict()
# create an instance of GetQueuesResponse from a dict
get_queues_response_from_dict = GetQueuesResponse.from_dict(get_queues_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


