# DocusignRecipientView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_url** | **str** | Identifies the return point after sending the envelope | [optional] 
**recipient_id** | **str** | A reference used to map recipients to other objects, such as specific document tabs. | [optional] 
**user_name** | **str** | The username of the recipient. You can use either email and userName. | [optional] 
**client_user_id** | **str** | Specifies unique identifier for signer | [optional] 
**email** | **str** | Specifies the email of the recipient | [optional] 
**frame_ancestors** | **List[str]** | An array of ancestors that can embed the frame. Include the domain where the envelope will be embedded and the same URL as messageOrigins. | [optional] 
**message_origins** | **List[str]** | The originating domain for the signature request message | [optional] 

## Example

```python
from openapi_client.models.docusign_recipient_view import DocusignRecipientView

# TODO update the JSON string below
json = "{}"
# create an instance of DocusignRecipientView from a JSON string
docusign_recipient_view_instance = DocusignRecipientView.from_json(json)
# print the JSON string representation of the object
print(DocusignRecipientView.to_json())

# convert the object into a dict
docusign_recipient_view_dict = docusign_recipient_view_instance.to_dict()
# create an instance of DocusignRecipientView from a dict
docusign_recipient_view_from_dict = DocusignRecipientView.from_dict(docusign_recipient_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


