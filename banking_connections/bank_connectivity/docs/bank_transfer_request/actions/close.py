"""Action handler seed for bank_transfer_request:close."""

from __future__ import annotations


DOC_ID = "bank_transfer_request"
ACTION_ID = "close"
ACTION_RULE = {'allowed_in_states': ['draft', 'approved', 'submitted', 'completed', 'failed'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['bank_connection', 'settlement_record', 'supplier_payment', 'treasury_movement'], 'borrowed_fields': ['source account', 'institution from bank_connection'], 'inferred_roles': ['procurement officer', 'finance officer']}, 'actors': ['procurement officer', 'finance officer'], 'action_actors': {'create': ['procurement officer'], 'submit': ['procurement officer'], 'review': ['finance officer'], 'approve': ['finance officer'], 'cancel': ['procurement officer'], 'close': ['procurement officer'], 'archive': ['procurement officer']}}

def handle_close(payload: dict, context: dict | None = None) -> dict:
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
