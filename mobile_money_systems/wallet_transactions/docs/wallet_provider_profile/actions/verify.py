"""Action handler seed for wallet_provider_profile:verify."""

from __future__ import annotations


DOC_ID = "wallet_provider_profile"
ACTION_ID = "verify"
ACTION_RULE = {'allowed_in_states': ['draft', 'verified', 'active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['mobile_money_transaction', 'wallet_reversal_case', 'wallet_settlement'], 'borrowed_fields': ['merchant/account context from finance/integration setup where linked'], 'inferred_roles': ['case owner']}, 'actors': ['case owner'], 'action_actors': {'create': ['case owner'], 'verify': ['case owner'], 'activate': ['case owner'], 'archive': ['case owner']}}

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
