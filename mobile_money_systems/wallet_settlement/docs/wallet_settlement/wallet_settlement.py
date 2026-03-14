"""Doc runtime hooks for wallet_settlement."""

class DocRuntime:
    doc_key = "wallet_settlement"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'reconcile', 'archive']
