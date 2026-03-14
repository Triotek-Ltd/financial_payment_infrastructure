"""Doc runtime hooks for bank_connection."""

class DocRuntime:
    doc_key = "bank_connection"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'verify', 'activate', 'disable', 'archive']
