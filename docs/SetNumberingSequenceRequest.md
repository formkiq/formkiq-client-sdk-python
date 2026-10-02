# SetNumberingSequenceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pattern** | **str** | Number format using supported tokens such as {YEAR} and {SEQUENCE} | 
**start_at** | **int** | First sequence number allocated for a new period | 
**padding** | **int** | Minimum width of the generated sequence number, padded with leading zeroes | 
**reset** | [**NumberingSequenceReset**](NumberingSequenceReset.md) |  | 
**timezone** | **str** | IANA timezone used to determine the active period; defaults to UTC | [optional] [default to 'UTC']

## Example

```python
from formkiq_client.models.set_numbering_sequence_request import SetNumberingSequenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetNumberingSequenceRequest from a JSON string
set_numbering_sequence_request_instance = SetNumberingSequenceRequest.from_json(json)
# print the JSON string representation of the object
print(SetNumberingSequenceRequest.to_json())

# convert the object into a dict
set_numbering_sequence_request_dict = set_numbering_sequence_request_instance.to_dict()
# create an instance of SetNumberingSequenceRequest from a dict
set_numbering_sequence_request_from_dict = SetNumberingSequenceRequest.from_dict(set_numbering_sequence_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


