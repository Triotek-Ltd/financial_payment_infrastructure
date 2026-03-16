"""Action handler seed for settlement_record:review."""

from __future__ import annotations


DOC_ID = "settlement_record"
ACTION_ID = "review"
ACTION_RULE = {'allowed_in_states': ['pending', 'settled', 'reconciled'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['bank_connection', 'bank_transfer_request', 'treasury_movement', 'cash_position_snapshot'], 'borrowed_fields': ['source account', 'institution from bank_connection'], 'inferred_roles': ['finance officer']}, 'actors': ['finance officer'], 'action_actors': {'create': ['finance officer'], 'review': ['finance officer'], 'reconcile': ['finance officer'], 'archive': ['finance officer']}}

def handle_review(payload: dict, context: dict | None = None) -> dict:
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
