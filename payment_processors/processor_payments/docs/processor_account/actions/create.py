"""Action handler seed for processor_account:create."""

from __future__ import annotations


DOC_ID = "processor_account"
ACTION_ID = "create"
ACTION_RULE = {'allowed_in_states': ['draft', 'verified', 'active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['payment_intent_record', 'processor_payout', 'processor_event_log', 'payment_attempt'], 'borrowed_fields': ['merchant/program context from commerce/payment setup'], 'inferred_roles': ['finance officer']}, 'actors': ['finance officer'], 'action_actors': {'create': ['finance officer'], 'verify': ['finance officer'], 'activate': ['finance officer'], 'archive': ['finance officer']}}

def handle_create(payload: dict, context: dict | None = None) -> dict:
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
