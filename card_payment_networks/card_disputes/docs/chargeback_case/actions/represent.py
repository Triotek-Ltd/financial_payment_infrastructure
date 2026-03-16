"""Action handler seed for chargeback_case:represent."""

from __future__ import annotations


DOC_ID = "chargeback_case"
ACTION_ID = "represent"
ACTION_RULE = {'allowed_in_states': ['opened', 'evidence_requested', 'represented', 'won', 'lost'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['card_authorization_record', 'refund_case', 'payment_log_entry'], 'borrowed_fields': ['authorization', 'transaction context from card_authorization_record'], 'inferred_roles': ['approver', 'finance officer', 'case owner']}, 'actors': ['approver', 'finance officer', 'case owner'], 'action_actors': {'create': ['approver'], 'assign': ['approver'], 'close': ['case owner'], 'archive': ['case owner']}}

def handle_represent(payload: dict, context: dict | None = None) -> dict:
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
