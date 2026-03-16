"""Action handler seed for processor_event_log:ignore."""

from __future__ import annotations


DOC_ID = "processor_event_log"
ACTION_ID = "ignore"
ACTION_RULE = {'allowed_in_states': ['received', 'normalized', 'applied', 'ignored'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['processor_account', 'payment_intent_record', 'processor_payout'], 'borrowed_fields': ['provider/account identity from processor_account'], 'inferred_roles': ['finance officer']}, 'actors': ['finance officer'], 'action_actors': {'record': ['finance officer'], 'archive': ['finance officer']}}

def handle_ignore(payload: dict, context: dict | None = None) -> dict:
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
