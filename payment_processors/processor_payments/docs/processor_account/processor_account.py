"""Doc runtime hooks for processor_account."""

class DocRuntime:
    doc_key = "processor_account"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'verify', 'activate', 'disable', 'archive']
