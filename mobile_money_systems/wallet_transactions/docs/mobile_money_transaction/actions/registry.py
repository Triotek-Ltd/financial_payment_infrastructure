"""Action registry seed for mobile_money_transaction."""

from __future__ import annotations


DOC_ID = "mobile_money_transaction"
ALLOWED_ACTIONS = ['create', 'submit', 'confirm', 'reverse', 'settle', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['initiated', 'pending', 'successful', 'failed', 'settled'], 'transitions_to': None}, 'submit': {'allowed_in_states': ['initiated', 'pending', 'successful', 'failed', 'settled'], 'transitions_to': None}, 'confirm': {'allowed_in_states': ['initiated', 'pending', 'successful', 'failed', 'settled'], 'transitions_to': None}, 'reverse': {'allowed_in_states': ['initiated', 'pending', 'successful', 'failed', 'settled'], 'transitions_to': 'reversed'}, 'settle': {'allowed_in_states': ['initiated', 'pending', 'successful', 'failed', 'settled'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['initiated', 'pending', 'successful', 'failed', 'settled'], 'transitions_to': 'archived'}}

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
