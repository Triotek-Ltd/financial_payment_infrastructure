"""Action handler seed for terminal_settlement:reconcile."""

from __future__ import annotations


DOC_ID = "terminal_settlement"
ACTION_ID = "reconcile"
ACTION_RULE = {'allowed_in_states': ['open', 'settled', 'reconciled'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['card_authorization_record', 'card_network_profile', 'settlement_record'], 'borrowed_fields': ['merchant/terminal context from card_network_profile'], 'inferred_roles': ['approver', 'finance officer']}, 'actors': ['approver', 'finance officer'], 'action_actors': {'record': ['approver'], 'review': ['finance officer'], 'reconcile': ['finance officer'], 'archive': ['approver']}}

def handle_reconcile(payload: dict, context: dict | None = None) -> dict:
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
