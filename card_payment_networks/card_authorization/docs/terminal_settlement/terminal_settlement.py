"""Doc runtime hooks for terminal_settlement."""

class DocRuntime:
    doc_key = "terminal_settlement"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'reconcile', 'archive']
