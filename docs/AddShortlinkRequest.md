# AddShortlinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_url** | **str** | Target URL for the shortlink | 
**slug** | **str** | Shortlink slug | 

## Example

```python
from formkiq_client.models.add_shortlink_request import AddShortlinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddShortlinkRequest from a JSON string
add_shortlink_request_instance = AddShortlinkRequest.from_json(json)
# print the JSON string representation of the object
print(AddShortlinkRequest.to_json())

# convert the object into a dict
add_shortlink_request_dict = add_shortlink_request_instance.to_dict()
# create an instance of AddShortlinkRequest from a dict
add_shortlink_request_from_dict = AddShortlinkRequest.from_dict(add_shortlink_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


