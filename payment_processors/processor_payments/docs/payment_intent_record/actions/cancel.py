"""Action handler seed for payment_intent_record:cancel."""

from __future__ import annotations


DOC_ID = "payment_intent_record"
ACTION_ID = "cancel"
ACTION_RULE = {'allowed_in_states': ['created', 'requires_action', 'processing', 'succeeded', 'failed', 'cancelled'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['processor_account', 'processor_event_log', 'processor_payout', 'payment_attempt'], 'borrowed_fields': ['account context from processor_account', 'checkout/payment context from payment_attempt'], 'inferred_roles': ['finance officer']}, 'actors': ['finance officer'], 'action_actors': {'create': ['finance officer'], 'confirm': ['finance officer'], 'cancel': ['finance officer'], 'archive': ['finance officer']}}

def handle_cancel(payload: dict, context: dict | None = None) -> dict:
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
