"""Action registry seed for payment_intent_record."""

from __future__ import annotations


DOC_ID = "payment_intent_record"
ALLOWED_ACTIONS = ['create', 'confirm', 'cancel', 'succeed', 'fail', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['created', 'requires_action', 'processing', 'succeeded', 'failed', 'cancelled'], 'transitions_to': None}, 'confirm': {'allowed_in_states': ['created', 'requires_action', 'processing', 'succeeded', 'failed', 'cancelled'], 'transitions_to': None}, 'cancel': {'allowed_in_states': ['created', 'requires_action', 'processing', 'succeeded', 'failed', 'cancelled'], 'transitions_to': None}, 'succeed': {'allowed_in_states': ['created', 'requires_action', 'processing', 'succeeded', 'failed', 'cancelled'], 'transitions_to': None}, 'fail': {'allowed_in_states': ['created', 'requires_action', 'processing', 'succeeded', 'failed', 'cancelled'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['created', 'requires_action', 'processing', 'succeeded', 'failed', 'cancelled'], 'transitions_to': 'archived'}}

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
