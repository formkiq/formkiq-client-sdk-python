# DocusignSigningTabs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sign_here_tabs** | [**List[DocusignSignHereTabs]**](DocusignSignHereTabs.md) | A list of Sign Here tabs | [optional] 

## Example

```python
from openapi_client.models.docusign_signing_tabs import DocusignSigningTabs

# TODO update the JSON string below
json = "{}"
# create an instance of DocusignSigningTabs from a JSON string
docusign_signing_tabs_instance = DocusignSigningTabs.from_json(json)
# print the JSON string representation of the object
print(DocusignSigningTabs.to_json())

# convert the object into a dict
docusign_signing_tabs_dict = docusign_signing_tabs_instance.to_dict()
# create an instance of DocusignSigningTabs from a dict
docusign_signing_tabs_from_dict = DocusignSigningTabs.from_dict(docusign_signing_tabs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


