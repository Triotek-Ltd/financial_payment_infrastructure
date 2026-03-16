"""Action handler seed for mobile_money_transaction:archive."""

from __future__ import annotations


DOC_ID = "mobile_money_transaction"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': ['initiated', 'pending', 'successful', 'failed', 'settled'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['wallet_provider_profile', 'wallet_reversal_case', 'wallet_settlement', 'payment_attempt'], 'borrowed_fields': ['provider context from wallet_provider_profile', 'checkout/payment context from linked commerce records'], 'inferred_roles': ['finance officer', 'case owner']}, 'actors': ['finance officer', 'case owner'], 'action_actors': {'create': ['finance officer'], 'submit': ['finance officer'], 'confirm': ['case owner'], 'reverse': ['case owner'], 'archive': ['case owner']}}

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
