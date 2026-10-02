# GetNumberingSequencesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | **str** | Next page of results token | [optional] 
**numbering_sequences** | [**List[NumberingSequence]**](NumberingSequence.md) | List of numbering sequences | 

## Example

```python
from formkiq_client.models.get_numbering_sequences_response import GetNumberingSequencesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetNumberingSequencesResponse from a JSON string
get_numbering_sequences_response_instance = GetNumberingSequencesResponse.from_json(json)
# print the JSON string representation of the object
print(GetNumberingSequencesResponse.to_json())

# convert the object into a dict
get_numbering_sequences_response_dict = get_numbering_sequences_response_instance.to_dict()
# create an instance of GetNumberingSequencesResponse from a dict
get_numbering_sequences_response_from_dict = GetNumberingSequencesResponse.from_dict(get_numbering_sequences_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


