"""Action handler seed for wallet_settlement:reconcile."""

from __future__ import annotations


DOC_ID = "wallet_settlement"
ACTION_ID = "reconcile"
ACTION_RULE = {'allowed_in_states': ['pending', 'settled', 'reconciled'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['wallet_provider_profile', 'mobile_money_transaction', 'cash_position_snapshot'], 'borrowed_fields': ['provider identity from wallet_provider_profile'], 'inferred_roles': ['finance officer']}, 'actors': ['finance officer'], 'action_actors': {'record': ['finance officer'], 'review': ['finance officer'], 'reconcile': ['finance officer'], 'archive': ['finance officer']}}

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
