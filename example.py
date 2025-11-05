#!/usr/bin/env python3

from pprint import pprint
import formkiq_client
from formkiq_client.api.documents_api import DocumentsApi
from formkiq_client.rest import ApiException

# -------------------------------------------------------------------
# REQUIRED: Set your FormKiQ API URL + JWT access token
# -------------------------------------------------------------------
FORMKIQ_API_URL = "FORMKIQ_API_URL"         # ← CHANGE THIS
JWT_ACCESS_TOKEN = "YOUR_JWT_ACCESS_TOKEN"  # ← CHANGE THIS
SITE_ID = "default"
# -------------------------------------------------------------------

# Configure the SDK client
configuration = formkiq_client.Configuration(host=FORMKIQ_API_URL,access_token=JWT_ACCESS_TOKEN)
configuration.debug = True

# Document body matches AddDocumentRequest schema
document = {
    "path": "inbox/hello.txt",     # Path within FormKiQ
    "contentType": "text/plain",   # MIME type
    "content": "Hello World"       # Text content (SDK auto base64-encodes if needed)
}

try:
    with formkiq_client.ApiClient(configuration) as api_client:
        api_client.set_default_header("Authorization", f"Bearer {JWT_ACCESS_TOKEN}")
        api = DocumentsApi(api_client)
        response = api.add_document(add_document_request=document, site_id=SITE_ID)

        print("\n✅ Document Added Successfully!")
        print("DocumentId:", response.document_id)
        pprint(response)

        meta = api.get_document(document_id=response.document_id, site_id=SITE_ID)

        print("\n📝 Document Metadata Retrieved Successfully!")
        pprint(meta.to_dict() if hasattr(meta, "to_dict") else meta)

        upload_request = {
            "path": "document.py",
            "contentType": "text/plain"
        }
        init_resp = api.add_document_upload(add_document_upload_request=upload_request, site_id=SITE_ID)
        print("\n✅ Document Added Successfully with Presigned Url!")
        pprint(init_resp);
        # presigned_url = getattr(init_resp.data, "url", None)
        # print("Upload URL:", presigned_url)

except ApiException as e:
    print("\n❌ API Error:")
    print(e)
except Exception as e:
    print("\n❌ Unexpected Error:")
    print(e)
