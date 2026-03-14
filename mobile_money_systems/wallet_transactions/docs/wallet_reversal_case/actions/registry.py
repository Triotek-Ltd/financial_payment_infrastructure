"""Action registry seed for wallet_reversal_case."""

from __future__ import annotations


DOC_ID = "wallet_reversal_case"
ALLOWED_ACTIONS = ['create', 'assign', 'investigate', 'reverse', 'reject', 'close', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['opened', 'investigating', 'rejected'], 'transitions_to': None}, 'assign': {'allowed_in_states': ['opened', 'investigating', 'rejected'], 'transitions_to': None}, 'investigate': {'allowed_in_states': ['opened', 'investigating', 'rejected'], 'transitions_to': None}, 'reverse': {'allowed_in_states': ['opened', 'investigating', 'rejected'], 'transitions_to': 'reversed'}, 'reject': {'allowed_in_states': ['opened', 'investigating', 'rejected'], 'transitions_to': 'rejected'}, 'close': {'allowed_in_states': ['opened', 'investigating', 'rejected'], 'transitions_to': 'closed'}, 'archive': {'allowed_in_states': ['opened', 'investigating', 'rejected'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'

def get_action_handler_name(action_id: str) -> str:
    return f"handle_{action_id}"

def get_action_module_path(action_id: str) -> str:
    return f"actions/{action_id}.py"

def action_contract(action_id: str) -> dict:
    return {
        "state_field": STATE_FIELD,
        "rule": ACTION_RULES.get(action_id, {}),
    }
