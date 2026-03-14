"""Doc runtime hooks for wallet_provider_profile."""

class DocRuntime:
    doc_key = "wallet_provider_profile"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'verify', 'activate', 'disable', 'archive']
