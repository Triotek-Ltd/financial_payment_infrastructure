"""Doc runtime hooks for chargeback_case."""

class DocRuntime:
    doc_key = "chargeback_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'represent', 'accept', 'close', 'archive']
