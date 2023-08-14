# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from formkiq_client.paths.documents_compress import Api

from formkiq_client.paths import PathValues

path = PathValues.DOCUMENTS_COMPRESS