"""Action handler seed for card_network_profile:verify."""

from __future__ import annotations


DOC_ID = "card_network_profile"
ACTION_ID = "verify"
ACTION_RULE = {'allowed_in_states': ['draft', 'verified', 'active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['card_authorization_record', 'chargeback_case', 'terminal_settlement', 'payment_log_entry'], 'borrowed_fields': ['merchant context from commerce/payment config where linked'], 'inferred_roles': ['approver', 'finance officer', 'case owner']}, 'actors': ['approver', 'finance officer', 'case owner'], 'action_actors': {'create': ['approver'], 'verify': ['finance officer'], 'activate': ['case owner'], 'archive': ['case owner']}}

def handle_verify(payload: dict, context: dict | None = None) -> dict:
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
