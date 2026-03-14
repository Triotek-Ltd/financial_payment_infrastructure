"""Action registry seed for bank_webhook_event."""

from __future__ import annotations


DOC_ID = "bank_webhook_event"
ALLOWED_ACTIONS = ['record', 'normalize', 'link', 'archive']
ACTION_RULES = {'record': {'allowed_in_states': ['received', 'normalized', 'linked'], 'transitions_to': None}, 'normalize': {'allowed_in_states': ['received', 'normalized', 'linked'], 'transitions_to': None}, 'link': {'allowed_in_states': ['received', 'normalized', 'linked'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['received', 'normalized', 'linked'], 'transitions_to': 'archived'}}

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
