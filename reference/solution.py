#!/usr/bin/env python3
"""Agent ready for live calls with authentication.

Lab 1.4 Deliverable: Production-ready agent configured for live calls
with basic authentication, prompts, and voice settings.

Environment variables:
    SWML_BASIC_AUTH_USER: Basic auth username (auto-detected by SDK)
    SWML_BASIC_AUTH_PASSWORD: Basic auth password (auto-detected by SDK)
"""

from signalwire_agents import AgentBase

agent = AgentBase(
    name="live-agent",
    route="/agent"
)

# Prompt configuration
agent.prompt_add_section(
    "Role",
    "You are a friendly training assistant for SignalWire. "
    "Greet callers warmly and have a brief conversation. "
    "Ask them what they're learning about today."
)

agent.prompt_add_section(
    "Guidelines",
    bullets=[
        "Keep responses brief - this is a phone call",
        "Be enthusiastic about voice AI",
        "If asked about SignalWire, say you're a demo agent"
    ]
)

# Voice configuration
agent.add_language("English", "en-US", "rime.spore")

if __name__ == "__main__":
    agent.run()
