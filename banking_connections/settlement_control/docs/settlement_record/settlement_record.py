"""Doc runtime hooks for settlement_record."""

class DocRuntime:
    doc_key = "settlement_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'settle', 'reconcile', 'archive']
