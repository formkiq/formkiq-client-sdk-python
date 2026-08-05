# MetadataExtraction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**llm_prompt_entity_name** | **str** | Name of the LLM Prompt Entity | [optional] 
**inserted_date** | **str** | Inserted Timestamp | [optional] 
**content** | **str** | Result content | [optional] 
**user_id** | **str** | UserId that created Result | [optional] 
**attributes** | [**List[MetadataExtractionAttribute]**](MetadataExtractionAttribute.md) | Attributes extracted from result content | [optional] 

## Example

```python
from formkiq_client.models.metadata_extraction import MetadataExtraction

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataExtraction from a JSON string
metadata_extraction_instance = MetadataExtraction.from_json(json)
# print the JSON string representation of the object
print(MetadataExtraction.to_json())

# convert the object into a dict
metadata_extraction_dict = metadata_extraction_instance.to_dict()
# create an instance of MetadataExtraction from a dict
metadata_extraction_from_dict = MetadataExtraction.from_dict(metadata_extraction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


