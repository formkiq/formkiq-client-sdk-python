# NumberingSequence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_key** | **str** | Attribute key where generated values are stored | 
**pattern** | **str** | Number format using supported tokens such as {YEAR} and {SEQUENCE} | 
**start_at** | **int** | First sequence number allocated for a new period | 
**padding** | **int** | Minimum width of the generated sequence number, padded with leading zeroes | 
**reset** | [**NumberingSequenceReset**](NumberingSequenceReset.md) |  | 
**timezone** | **str** | IANA timezone used to determine the active period; defaults to UTC | [optional] [default to 'UTC']
**current_period** | **str** | Active sequence period, or null if no number has been allocated | [optional] [readonly] 
**current_sequence** | **int** | Most recently allocated sequence number, or null if none has been allocated | [optional] [readonly] 
**last_value** | **str** | Most recently generated attribute value, or null if none has been allocated | [optional] [readonly] 

## Example

```python
from formkiq_client.models.numbering_sequence import NumberingSequence

# TODO update the JSON string below
json = "{}"
# create an instance of NumberingSequence from a JSON string
numbering_sequence_instance = NumberingSequence.from_json(json)
# print the JSON string representation of the object
print(NumberingSequence.to_json())

# convert the object into a dict
numbering_sequence_dict = numbering_sequence_instance.to_dict()
# create an instance of NumberingSequence from a dict
numbering_sequence_from_dict = NumberingSequence.from_dict(numbering_sequence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


