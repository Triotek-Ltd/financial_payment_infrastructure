"""Doc runtime hooks for card_authorization_record."""

class DocRuntime:
    doc_key = "card_authorization_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'authorize', 'capture', 'void', 'settle', 'reverse', 'archive']
