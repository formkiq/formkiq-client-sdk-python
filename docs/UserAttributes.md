# UserAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Address of user | [optional] 
**birthdate** | **str** | Birthdate of user | [optional] 
**family_name** | **str** | Family name of user | [optional] 
**gender** | **str** | Gender of user | [optional] 
**given_name** | **str** | Given name of user | [optional] 
**locale** | **str** | Locale of user | [optional] 
**middle_name** | **str** | Middle name of user | [optional] 
**name** | **str** | Name of user | [optional] 
**nickname** | **str** | Nickname of user | [optional] 
**phone_number** | **str** | Phone number of user | [optional] 
**picture** | **str** | Picture of user | [optional] 
**preferred_username** | **str** | Preferred username of user | [optional] 
**profile** | **str** | Profile of user | [optional] 
**zoneinfo** | **str** | Zoneinfo of user | [optional] 
**updated_at** | **str** | Updated at date of user | [optional] 
**website** | **str** | Website of user | [optional] 

## Example

```python
from openapi_client.model.user_attributes import UserAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UserAttributes from a JSON string
user_attributes_instance = UserAttributes.from_json(json)
# print the JSON string representation of the object
print(UserAttributes.to_json())

# convert the object into a dict
user_attributes_dict = user_attributes_instance.to_dict()
# create an instance of UserAttributes from a dict
user_attributes_from_dict = UserAttributes.from_dict(user_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


