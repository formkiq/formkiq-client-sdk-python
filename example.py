#!/usr/bin/env python3
"""
FormKiQ Python SDK Example
--------------------------

This script demonstrates:
  1) Creating a document inline via FormKiQ (POST /documents)
  2) Reading document metadata (GET /documents/{documentId})
  3) Requesting a presigned S3 upload URL (POST /documents/upload)
  4) Uploading file bytes directly to S3 with the presigned URL (PUT)
  5) Verifying metadata after upload

Requirements:
  pip install git+https://github.com/formkiq/formkiq-client-sdk-python.git requests

Environment variables (optional):
  - FORMKIQ_API_URL  : overrides the API base URL
  - JWT              : overrides the JWT access token
  - SITE_ID          : overrides the site id

Notes:
  - We set the Authorization header explicitly using ApiClient.set_default_header(...)
    because the generated Configuration(access_token=...) isn’t wired (given current spec).
  - Never send your FormKiQ Authorization header to S3 (presigned PUT).
"""

from __future__ import annotations

import os
from typing import Any, Dict, Optional
from pprint import pprint

import requests

import formkiq_client
from formkiq_client.api.documents_api import DocumentsApi
from formkiq_client.rest import ApiException


# ------------------------------------------------------------------------------
# Configuration (edit or use environment variables)
# ------------------------------------------------------------------------------
FORMKIQ_API_URL = os.environ.get("FORMKIQ_API_URL", "https://your-formkiq-api.example.com")
JWT_ACCESS_TOKEN = os.environ.get("JWT", "REPLACE_WITH_ACCESS_TOKEN")
SITE_ID = os.environ.get("SITE_ID", "default")

# Inline document to create
INLINE_DOC = {
    "path": "inbox/hello.txt",
    "contentType": "text/plain",
    "content": "Hello World",
}

# Local file to upload via presigned URL → ends up at path below
UPLOAD_LOCAL_PATH = "example.py"
UPLOAD_DEST_PATH = "example.py"
UPLOAD_CONTENT_TYPE = "text/plain"

# Toggle HTTP debug traces to stdout
DEBUG_HTTP = True
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------------------
def to_dict_safe(obj: Any) -> Any:
    """Return a dict-like view of a model or pass through if already serializable."""
    if hasattr(obj, "to_dict"):
        return obj.to_dict()
    return obj


def build_api_client() -> DocumentsApi:
    """
    Build a DocumentsApi bound to your base URL and JWT.

    We set the Authorization header manually. This is the most reliable method
    with the current generator/spec combination.
    """
    cfg = formkiq_client.Configuration(host=FORMKIQ_API_URL)
    cfg.debug = DEBUG_HTTP

    api_client = formkiq_client.ApiClient(cfg)
    api_client.set_default_header("Authorization", f"Bearer {JWT_ACCESS_TOKEN}")
    return DocumentsApi(api_client)


def add_document_inline(api: DocumentsApi, site_id: str, body: Dict[str, Any]) -> str:
    """
    Create a small document inline (<=5MB depending on config).
    Returns: documentId
    """
    resp = api.add_document(add_document_request=body, site_id=site_id)
    doc_id = getattr(resp, "document_id", None) or getattr(resp, "documentId", None)
    if not doc_id:
        raise RuntimeError("Inline add returned no documentId. Response: %r" % (resp,))
    return doc_id


def get_document_metadata(api: DocumentsApi, site_id: str, document_id: str) -> Dict[str, Any]:
    """Fetch metadata and return as a plain dict for easy printing."""
    meta = api.get_document(document_id=document_id, site_id=site_id)
    return to_dict_safe(meta)


def request_presigned_upload(
    api: DocumentsApi,
    site_id: str,
    dest_path: str,
    content_type: str,
    content_length: int,
) -> Dict[str, Any]:
    """
    Ask FormKiQ for a presigned S3 URL to upload content.

    Returns a dict with:
      - document_id
      - presigned_url
      - required_headers (possibly empty)
    """
    upload_request = {
        "path": dest_path,
        "contentType": content_type,
        "contentLength": content_length,
    }
    resp = api.add_document_upload(add_document_upload_request=upload_request, site_id=site_id)
    # Normalize possible field names
    document_id = getattr(resp, "document_id", None) or getattr(resp, "documentId", None)
    presigned_url = getattr(resp, "upload_url", None) or getattr(resp, "url", None)
    required_headers = getattr(resp, "headers", None) or {}

    if not presigned_url:
        raise RuntimeError(f"Presigned URL missing in upload response: {resp}")

    if not document_id:
        # Some APIs return the doc id in header or different name—adjust if needed
        raise RuntimeError(f"documentId missing in upload response: {resp}")

    return {
        "document_id": document_id,
        "presigned_url": presigned_url,
        "required_headers": required_headers,
    }


def s3_put_bytes(
    url: str,
    data: bytes,
    content_type: str,
    extra_headers: Optional[Dict[str, str]] = None,
) -> None:
    """
    Upload bytes to S3 using the presigned URL.

    IMPORTANT:
      - Do NOT send FormKiQ Authorization headers here.
      - Content-Type must match what was signed.
      - If the presign returned x-amz-* headers, include them verbatim.
    """
    headers = {"Content-Type": content_type}
    headers.update(extra_headers or {})

    resp = requests.put(url, data=data, headers=headers)
    if resp.status_code not in (200, 201):
        raise RuntimeError(f"S3 upload failed: {resp.status_code} {resp.text[:300]}")


# ------------------------------------------------------------------------------
# Main flow
# ------------------------------------------------------------------------------
def main() -> None:
    print("🔧 Using API:", FORMKIQ_API_URL)
    print("🔧 Site     :", SITE_ID)

    api = build_api_client()

    # 1) Add a small document inline
    print("\n① Adding inline document…")
    doc_id = add_document_inline(api, SITE_ID, INLINE_DOC)
    print("✅ Inline documentId:", doc_id)

    # 2) Read metadata
    print("\n② Fetching metadata…")
    meta = get_document_metadata(api, SITE_ID, doc_id)
    pprint(meta)

    # 3) Request presigned URL
    print("\n③ Requesting presigned S3 upload…")
    with open(UPLOAD_LOCAL_PATH, "rb") as fh:
        file_bytes = fh.read()

    presign = request_presigned_upload(
        api=api,
        site_id=SITE_ID,
        dest_path=UPLOAD_DEST_PATH,
        content_type=UPLOAD_CONTENT_TYPE,
        content_length=len(file_bytes),
    )
    print("✅ Upload session")
    print("   documentId    :", presign["document_id"])
    print("   presigned URL :", presign["presigned_url"])
    if presign["required_headers"]:
        print("   S3 headers    :", presign["required_headers"])

    # 4) PUT to S3 (no Authorization header)
    print("\n④ Uploading to S3…")
    s3_put_bytes(
        url=presign["presigned_url"],
        data=file_bytes,
        content_type=UPLOAD_CONTENT_TYPE,
        extra_headers=presign["required_headers"],
    )
    print("✅ S3 upload complete")

    # 5) Verify metadata after upload
    print("\n⑤ Verifying metadata after upload…")
    meta_after = get_document_metadata(api, SITE_ID, presign["document_id"])
    pprint(meta_after)


if __name__ == "__main__":
    try:
        main()
    except ApiException as e:
        # Server returned a non-2xx with a JSON error body
        print("\n❌ API Error")
        # e.body often contains useful JSON; fall back to str(e)
        print(getattr(e, "body", str(e)))
        raise
    except Exception as e:
        print("\n❌ Unexpected Error")
        print(e)
        raise