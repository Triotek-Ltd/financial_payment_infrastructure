"""Action registry seed for bank_transfer_request."""

from __future__ import annotations


DOC_ID = "bank_transfer_request"
ALLOWED_ACTIONS = ['create', 'submit', 'review', 'approve', 'release', 'cancel', 'close', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'approved', 'submitted', 'completed', 'failed'], 'transitions_to': None}, 'submit': {'allowed_in_states': ['draft', 'approved', 'submitted', 'completed', 'failed'], 'transitions_to': 'submitted'}, 'review': {'allowed_in_states': ['draft', 'approved', 'submitted', 'completed', 'failed'], 'transitions_to': None}, 'approve': {'allowed_in_states': ['draft', 'approved', 'submitted', 'completed', 'failed'], 'transitions_to': 'approved'}, 'release': {'allowed_in_states': ['draft', 'approved', 'submitted', 'completed', 'failed'], 'transitions_to': None}, 'cancel': {'allowed_in_states': ['draft', 'approved', 'submitted', 'completed', 'failed'], 'transitions_to': None}, 'close': {'allowed_in_states': ['draft', 'approved', 'submitted', 'completed', 'failed'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['draft', 'approved', 'submitted', 'completed', 'failed'], 'transitions_to': 'archived'}}

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
