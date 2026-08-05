# AddShortlinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Shortlink URL | [optional] 

## Example

```python
from formkiq_client.models.add_shortlink_response import AddShortlinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddShortlinkResponse from a JSON string
add_shortlink_response_instance = AddShortlinkResponse.from_json(json)
# print the JSON string representation of the object
print(AddShortlinkResponse.to_json())

# convert the object into a dict
add_shortlink_response_dict = add_shortlink_response_instance.to_dict()
# create an instance of AddShortlinkResponse from a dict
add_shortlink_response_from_dict = AddShortlinkResponse.from_dict(add_shortlink_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


