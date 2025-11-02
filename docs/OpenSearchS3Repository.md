# OpenSearchS3Repository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | **str** | Name of the Repository | [optional] 
**bucket** | **str** | Name of the S3 bucket | [optional] 

## Example

```python
from openapi_client.models.open_search_s3_repository import OpenSearchS3Repository

# TODO update the JSON string below
json = "{}"
# create an instance of OpenSearchS3Repository from a JSON string
open_search_s3_repository_instance = OpenSearchS3Repository.from_json(json)
# print the JSON string representation of the object
print(OpenSearchS3Repository.to_json())

# convert the object into a dict
open_search_s3_repository_dict = open_search_s3_repository_instance.to_dict()
# create an instance of OpenSearchS3Repository from a dict
open_search_s3_repository_from_dict = OpenSearchS3Repository.from_dict(open_search_s3_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


