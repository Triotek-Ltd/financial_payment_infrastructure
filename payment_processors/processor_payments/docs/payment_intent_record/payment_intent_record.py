"""Doc runtime hooks for payment_intent_record."""

class DocRuntime:
    doc_key = "payment_intent_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'confirm', 'cancel', 'succeed', 'fail', 'archive']
