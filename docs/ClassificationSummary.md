# ClassificationSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of Classification | [optional] 
**user_id** | **str** |  | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 

## Example

```python
from formkiq_client.models.classification_summary import ClassificationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ClassificationSummary from a JSON string
classification_summary_instance = ClassificationSummary.from_json(json)
# print the JSON string representation of the object
print(ClassificationSummary.to_json())

# convert the object into a dict
classification_summary_dict = classification_summary_instance.to_dict()
# create an instance of ClassificationSummary from a dict
classification_summary_from_dict = ClassificationSummary.from_dict(classification_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


