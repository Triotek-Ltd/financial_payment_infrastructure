"""Doc runtime hooks for wallet_reversal_case."""

class DocRuntime:
    doc_key = "wallet_reversal_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'investigate', 'reverse', 'reject', 'close', 'archive']
