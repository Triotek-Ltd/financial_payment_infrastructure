"""Doc runtime hooks for processor_event_log."""

class DocRuntime:
    doc_key = "processor_event_log"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'normalize', 'apply', 'ignore', 'archive']
