"""Action handler seed for card_authorization_record:archive."""

from __future__ import annotations


DOC_ID = "card_authorization_record"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': ['initiated', 'authorized', 'captured', 'failed', 'settled'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['card_network_profile', 'chargeback_case', 'terminal_settlement', 'payment_attempt'], 'borrowed_fields': ['merchant', 'processor context from card_network_profile', 'checkout/payment context from payment_attempt'], 'inferred_roles': ['approver', 'finance officer', 'case owner']}, 'actors': ['approver', 'finance officer', 'case owner'], 'action_actors': {'create': ['approver'], 'reverse': ['case owner'], 'archive': ['case owner']}}

def handle_archive(payload: dict, context: dict | None = None) -> dict:
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
