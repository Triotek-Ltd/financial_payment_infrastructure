"""Doc runtime hooks for mobile_money_transaction."""

class DocRuntime:
    doc_key = "mobile_money_transaction"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'submit', 'confirm', 'reverse', 'settle', 'archive']
