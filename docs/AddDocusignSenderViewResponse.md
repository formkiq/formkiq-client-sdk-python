# AddDocusignSenderViewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_url** | **str** | The URL for the embedded DocuSign sender view | [optional] 

## Example

```python
from formkiq_client.models.add_docusign_sender_view_response import AddDocusignSenderViewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocusignSenderViewResponse from a JSON string
add_docusign_sender_view_response_instance = AddDocusignSenderViewResponse.from_json(json)
# print the JSON string representation of the object
print(AddDocusignSenderViewResponse.to_json())

# convert the object into a dict
add_docusign_sender_view_response_dict = add_docusign_sender_view_response_instance.to_dict()
# create an instance of AddDocusignSenderViewResponse from a dict
add_docusign_sender_view_response_from_dict = AddDocusignSenderViewResponse.from_dict(add_docusign_sender_view_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


