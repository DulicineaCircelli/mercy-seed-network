def mercy_paradox_decision(
    action_lethal=False,
    target_critical=False,
    deception_risk=0.0,
    human_signoff_required=True
):
    if (action_lethal and target_critical and deception_risk > 0):
        return {
            "decision": "ESCALATE",
            "reason": "MERCY PARADOX: Never kill the future.",
            "action": "INITIATE VERIFICATION + HUMAN OVERSIGHT"
        }
    elif action_lethal and human_signoff_required:
        return {
            "decision": "ESCALATE",
            "reason": "Human must authorize initiated harm.",
            "action": "AWAIT FINAL COMMAND"
        }
    return {"decision": "PROCEED", "reason": "No paradox or override"}
