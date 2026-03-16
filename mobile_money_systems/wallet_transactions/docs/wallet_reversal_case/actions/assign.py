"""Action handler seed for wallet_reversal_case:assign."""

from __future__ import annotations


DOC_ID = "wallet_reversal_case"
ACTION_ID = "assign"
ACTION_RULE = {'allowed_in_states': ['opened', 'investigating', 'rejected'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['mobile_money_transaction', 'wallet_settlement'], 'borrowed_fields': ['transaction identity', 'status from mobile_money_transaction'], 'inferred_roles': ['case owner']}, 'actors': ['case owner'], 'action_actors': {'create': ['case owner'], 'assign': ['case owner'], 'reverse': ['case owner'], 'reject': ['case owner'], 'close': ['case owner'], 'archive': ['case owner']}}

def handle_assign(payload: dict, context: dict | None = None) -> dict:
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
