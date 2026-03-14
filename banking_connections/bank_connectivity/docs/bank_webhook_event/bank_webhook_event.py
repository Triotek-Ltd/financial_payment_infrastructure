"""Doc runtime hooks for bank_webhook_event."""

class DocRuntime:
    doc_key = "bank_webhook_event"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'normalize', 'link', 'archive']
