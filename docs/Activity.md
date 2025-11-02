# Activity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | Resource of Activity | [optional] 
**type** | **str** | Type of Activity | [optional] 
**source** | **str** | The Source of the activity | [optional] 
**source_ip_address** | **str** | The Source IP address of the user | [optional] 
**message** | **str** | The activity message | [optional] 
**status** | [**ActivityStatus**](ActivityStatus.md) |  | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**user_id** | **str** | User who added document | [optional] 
**document_id** | **object** | Document Identifier | [optional] 
**attribute_key** | **object** | Document Attribute Key | [optional] 
**entity_type_id** | **str** | Entity Type Identifier | [optional] 
**entity_id** | **str** | Entity Identifier | [optional] 
**changes** | [**Dict[str, UserActivityChanges]**](UserActivityChanges.md) |  | [optional] 

## Example

```python
from openapi_client.model.activity import Activity

# TODO update the JSON string below
json = "{}"
# create an instance of Activity from a JSON string
activity_instance = Activity.from_json(json)
# print the JSON string representation of the object
print(Activity.to_json())

# convert the object into a dict
activity_dict = activity_instance.to_dict()
# create an instance of Activity from a dict
activity_from_dict = Activity.from_dict(activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


