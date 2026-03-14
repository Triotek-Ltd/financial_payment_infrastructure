"""Doc runtime hooks for processor_payout."""

class DocRuntime:
    doc_key = "processor_payout"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'confirm_arrival', 'reconcile', 'archive']
