from formkiq_client.paths.configuration.get import ApiForget
from formkiq_client.paths.configuration.patch import ApiForpatch


class Configuration(
    ApiForget,
    ApiForpatch,
):
    pass
