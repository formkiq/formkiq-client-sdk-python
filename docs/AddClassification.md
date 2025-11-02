# AddClassification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of Classification | [optional] 
**attributes** | [**SetSchemaAttributes**](SetSchemaAttributes.md) |  | [optional] 

## Example

```python
from openapi_client.models.add_classification import AddClassification

# TODO update the JSON string below
json = "{}"
# create an instance of AddClassification from a JSON string
add_classification_instance = AddClassification.from_json(json)
# print the JSON string representation of the object
print(AddClassification.to_json())

# convert the object into a dict
add_classification_dict = add_classification_instance.to_dict()
# create an instance of AddClassification from a dict
add_classification_from_dict = AddClassification.from_dict(add_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


