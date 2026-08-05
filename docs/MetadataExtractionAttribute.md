# MetadataExtractionAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Data Classification Attribute Key | [optional] 
**value** | **str** | Data Classification Attribute Value | [optional] 

## Example

```python
from formkiq_client.models.metadata_extraction_attribute import MetadataExtractionAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataExtractionAttribute from a JSON string
metadata_extraction_attribute_instance = MetadataExtractionAttribute.from_json(json)
# print the JSON string representation of the object
print(MetadataExtractionAttribute.to_json())

# convert the object into a dict
metadata_extraction_attribute_dict = metadata_extraction_attribute_instance.to_dict()
# create an instance of MetadataExtractionAttribute from a dict
metadata_extraction_attribute_from_dict = MetadataExtractionAttribute.from_dict(metadata_extraction_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


