"""Doc runtime hooks for card_network_profile."""

class DocRuntime:
    doc_key = "card_network_profile"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'verify', 'activate', 'disable', 'archive']
