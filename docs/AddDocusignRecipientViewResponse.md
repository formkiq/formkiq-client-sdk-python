# AddDocusignRecipientViewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_url** | **str** | The view URL to be navigated to complete DocuSign signing | [optional] 

## Example

```python
from formkiq_client.models.add_docusign_recipient_view_response import AddDocusignRecipientViewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddDocusignRecipientViewResponse from a JSON string
add_docusign_recipient_view_response_instance = AddDocusignRecipientViewResponse.from_json(json)
# print the JSON string representation of the object
print(AddDocusignRecipientViewResponse.to_json())

# convert the object into a dict
add_docusign_recipient_view_response_dict = add_docusign_recipient_view_response_instance.to_dict()
# create an instance of AddDocusignRecipientViewResponse from a dict
add_docusign_recipient_view_response_from_dict = AddDocusignRecipientViewResponse.from_dict(add_docusign_recipient_view_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


