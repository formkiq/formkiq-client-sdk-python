from formkiq_client.paths.webhooks_webhook_id.get import ApiForget
from formkiq_client.paths.webhooks_webhook_id.delete import ApiFordelete
from formkiq_client.paths.webhooks_webhook_id.patch import ApiForpatch


class WebhooksWebhookId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
