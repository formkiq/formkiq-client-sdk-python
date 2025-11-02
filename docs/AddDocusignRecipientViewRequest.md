# AddDocusignRecipientViewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | [**DocusignEnvironment**](DocusignEnvironment.md) |  | 
**recipient_view** | [**DocusignRecipientView**](DocusignRecipientView.md) |  | 

## Example

```python
from openapi_client.models.add_docusign_recipient_view_request import AddDocusignRecipientViewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocusignRecipientViewRequest from a JSON string
add_docusign_recipient_view_request_instance = AddDocusignRecipientViewRequest.from_json(json)
# print the JSON string representation of the object
print(AddDocusignRecipientViewRequest.to_json())

# convert the object into a dict
add_docusign_recipient_view_request_dict = add_docusign_recipient_view_request_instance.to_dict()
# create an instance of AddDocusignRecipientViewRequest from a dict
add_docusign_recipient_view_request_from_dict = AddDocusignRecipientViewRequest.from_dict(add_docusign_recipient_view_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


