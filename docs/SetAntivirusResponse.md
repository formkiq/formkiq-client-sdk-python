# SetAntivirusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Antivirus processing message | [optional] 

## Example

```python
from formkiq_client.models.set_antivirus_response import SetAntivirusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetAntivirusResponse from a JSON string
set_antivirus_response_instance = SetAntivirusResponse.from_json(json)
# print the JSON string representation of the object
print(SetAntivirusResponse.to_json())

# convert the object into a dict
set_antivirus_response_dict = set_antivirus_response_instance.to_dict()
# create an instance of SetAntivirusResponse from a dict
set_antivirus_response_form_dict = set_antivirus_response.from_dict(set_antivirus_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


