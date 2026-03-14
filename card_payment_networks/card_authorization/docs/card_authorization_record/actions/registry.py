"""Action registry seed for card_authorization_record."""

from __future__ import annotations


DOC_ID = "card_authorization_record"
ALLOWED_ACTIONS = ['create', 'authorize', 'capture', 'void', 'settle', 'reverse', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['initiated', 'authorized', 'captured', 'failed', 'settled'], 'transitions_to': None}, 'authorize': {'allowed_in_states': ['initiated', 'authorized', 'captured', 'failed', 'settled'], 'transitions_to': None}, 'capture': {'allowed_in_states': ['initiated', 'authorized', 'captured', 'failed', 'settled'], 'transitions_to': None}, 'void': {'allowed_in_states': ['initiated', 'authorized', 'captured', 'failed', 'settled'], 'transitions_to': None}, 'settle': {'allowed_in_states': ['initiated', 'authorized', 'captured', 'failed', 'settled'], 'transitions_to': None}, 'reverse': {'allowed_in_states': ['initiated', 'authorized', 'captured', 'failed', 'settled'], 'transitions_to': 'reversed'}, 'archive': {'allowed_in_states': ['initiated', 'authorized', 'captured', 'failed', 'settled'], 'transitions_to': 'archived'}}

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
