from formkiq_client.paths.configuration_api_keys.get import ApiForget
from formkiq_client.paths.configuration_api_keys.post import ApiForpost


class ConfigurationApiKeys(
    ApiForget,
    ApiForpost,
):
    pass
