# DataClassification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**llm_prompt_entity_name** | **str** | Name of the LLM Prompt Entity | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**content** | **str** | Result content | [optional] 
**user_id** | **str** | UserId that created Result | [optional] 
**attributes** | [**List[DataClassificationAttribute]**](DataClassificationAttribute.md) | Attributes extracted from result content | [optional] 

## Example

```python
from formkiq_client.models.data_classification import DataClassification

# TODO update the JSON string below
json = "{}"
# create an instance of DataClassification from a JSON string
data_classification_instance = DataClassification.from_json(json)
# print the JSON string representation of the object
print(DataClassification.to_json())

# convert the object into a dict
data_classification_dict = data_classification_instance.to_dict()
# create an instance of DataClassification from a dict
data_classification_from_dict = DataClassification.from_dict(data_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


