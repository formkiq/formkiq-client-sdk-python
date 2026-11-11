# DeleteType

DELETE action deletion mode.  CONTENT_ONLY removes the current S3 object while preserving document metadata, attributes, tags, malware scan results, and workflow history. Existing S3 versions are retained. Use this mode in a workflow when infected content must be removed while retaining its metadata and scan results.

## Enum

* `SOFT_DELETE` (value: `'SOFT_DELETE'`)

* `HARD_DELETE` (value: `'HARD_DELETE'`)

* `PURGE` (value: `'PURGE'`)

* `CONTENT_ONLY` (value: `'CONTENT_ONLY'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


