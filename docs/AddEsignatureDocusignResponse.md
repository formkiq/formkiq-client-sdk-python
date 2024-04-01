# AddEsignatureDocusignResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect_url** | **str** | Redirect Url to complete DocuSign workflow | [optional] 
**message** | **str** | Result message | [optional] 

## Example

```python
from formkiq_client.models.add_esignature_docusign_response import AddEsignatureDocusignResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddEsignatureDocusignResponse from a JSON string
add_esignature_docusign_response_instance = AddEsignatureDocusignResponse.from_json(json)
# print the JSON string representation of the object
print(AddEsignatureDocusignResponse.to_json())

# convert the object into a dict
add_esignature_docusign_response_dict = add_esignature_docusign_response_instance.to_dict()
# create an instance of AddEsignatureDocusignResponse from a dict
add_esignature_docusign_response_form_dict = add_esignature_docusign_response.from_dict(add_esignature_docusign_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


