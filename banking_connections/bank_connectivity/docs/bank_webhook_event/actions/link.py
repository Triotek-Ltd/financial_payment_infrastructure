"""Action handler seed for bank_webhook_event:link."""

from __future__ import annotations


DOC_ID = "bank_webhook_event"
ACTION_ID = "link"
ACTION_RULE = {'allowed_in_states': ['received', 'normalized', 'linked'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['bank_connection', 'bank_transfer_request', 'settlement_record'], 'borrowed_fields': ['provider/account identity from bank_connection'], 'inferred_roles': ['finance officer']}, 'actors': ['finance officer'], 'action_actors': {'record': ['finance officer'], 'archive': ['finance officer']}}

def handle_link(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = ACTION_RULE.get("transitions_to")
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
