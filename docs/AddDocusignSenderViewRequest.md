# AddDocusignSenderViewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | [**DocusignEnvironment**](DocusignEnvironment.md) |  | [optional] 
**return_url** | **str** | The URL to which the sender is redirected after exiting the sender view | 

## Example

```python
from formkiq_client.models.add_docusign_sender_view_request import AddDocusignSenderViewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocusignSenderViewRequest from a JSON string
add_docusign_sender_view_request_instance = AddDocusignSenderViewRequest.from_json(json)
# print the JSON string representation of the object
print(AddDocusignSenderViewRequest.to_json())

# convert the object into a dict
add_docusign_sender_view_request_dict = add_docusign_sender_view_request_instance.to_dict()
# create an instance of AddDocusignSenderViewRequest from a dict
add_docusign_sender_view_request_from_dict = AddDocusignSenderViewRequest.from_dict(add_docusign_sender_view_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


