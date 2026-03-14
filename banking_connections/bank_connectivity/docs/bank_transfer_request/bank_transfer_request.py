"""Doc runtime hooks for bank_transfer_request."""

class DocRuntime:
    doc_key = "bank_transfer_request"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'submit', 'review', 'approve', 'release', 'cancel', 'close', 'archive']
