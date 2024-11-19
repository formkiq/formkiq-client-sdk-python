# AddActionParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ocr_parse_types** | **str** | OCR: Parse types - TEXT, FORMS, TABLES | [optional] 
**ocr_engine** | [**OcrEngine**](OcrEngine.md) |  | [optional] 
**ocr_output_type** | [**OcrOutputType**](OcrOutputType.md) |  | [optional] 
**ocr_number_of_pages** | **str** | Number of pages to OCR (from start) (-1 all) | [optional] 
**add_pdf_detected_characters_as_text** | **str** | OCR: For the rewriting of the PDF document, converting any image text to searchable text | [optional] 
**url** | **str** | Webhook: Callback URL | [optional] 
**character_max** | **str** | Fulltext: Maximum number of characters (-1 unlimited, Typesense defaults to 2048 characters) | [optional] 
**engine** | **str** | DocumentTagging: Engine to use for document tagging generation | [optional] 
**notification_type** | **str** | Notification Type | [optional] 
**notification_to_cc** | **str** | Who to carbon copy on the notification to (comma-delimited list) | [optional] 
**notification_to_bcc** | **str** | Who to blind carbon copy on the notification to (comma-delimited list) | [optional] 
**notification_subject** | **str** | Subject of the notification | [optional] 
**notification_text** | **str** | Text of the notification | [optional] 
**notification_html** | **str** | Html of the notification | [optional] 
**tags** | **str** | DocumentTagging: Comma-deliminted list of keywords to generate tags for | [optional] 
**mapping_id** | **str** | Id of Mapping | [optional] 
**event_bus_name** | **str** | The name or ARN of the event bus to receive the event | [optional] 

## Example

```python
from formkiq_client.models.add_action_parameters import AddActionParameters

# TODO update the JSON string below
json = "{}"
# create an instance of AddActionParameters from a JSON string
add_action_parameters_instance = AddActionParameters.from_json(json)
# print the JSON string representation of the object
print(AddActionParameters.to_json())

# convert the object into a dict
add_action_parameters_dict = add_action_parameters_instance.to_dict()
# create an instance of AddActionParameters from a dict
add_action_parameters_from_dict = AddActionParameters.from_dict(add_action_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


