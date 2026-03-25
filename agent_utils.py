"""
Shared utilities for the Agentic AI Science Playbook.

Every lab imports from this module so setup is consistent across all domains.
Usage:
    from shared.agent_utils import make_client, MODEL
    # or in Colab after cloning the repo:
    import sys; sys.path.insert(0, '/content/agentic-ai-science-playbook')
    from shared.agent_utils import make_client, MODEL
"""

import os
import re
from getpass import getpass
from openai import OpenAI


def make_client(verbose: bool = True) -> tuple["OpenAI", str]:
    """
    Create an OpenAI-compatible client (OpenAI or NVIDIA NIM).

    Environment variables:
        USE_NIM=1           Use NVIDIA NIM instead of OpenAI
        NIM_API_KEY         NIM API key (prompted if missing)
        NIM_MODEL           NIM model ID (default: nvidia/llama-3.3-nemotron-super-49b-v1.5)
        OPENAI_API_KEY      OpenAI API key (prompted if missing)
        OPENAI_MODEL        OpenAI model ID (default: gpt-4o-mini)

    Returns:
        (client, model_id)
    """
    use_nim = (
        os.environ.get("USE_NIM", "").lower() in ("1", "true", "yes")
        or "NIM_API_KEY" in os.environ
    )

    if use_nim:
        if "NIM_API_KEY" not in os.environ:
            os.environ["NIM_API_KEY"] = getpass("Enter your NVIDIA NIM API key: ")
        client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=os.environ["NIM_API_KEY"],
        )
        model = os.environ.get("NIM_MODEL", "nvidia/llama-3.3-nemotron-super-49b-v1.5")
    else:
        if "OPENAI_API_KEY" not in os.environ:
            os.environ["OPENAI_API_KEY"] = getpass("Enter your OpenAI API key: ")
        client = OpenAI()
        model = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")

    if verbose:
        provider = "NVIDIA NIM" if use_nim else "OpenAI"
        print(f"Provider : {provider}")
        print(f"Model    : {model}")

    return client, model


def parse_tool_choice(response_text: str) -> str | None:
    """Extract tool name from 'TOOL: <name>' format."""
    match = re.search(r"TOOL:\s*(\S+)", response_text.strip(), re.IGNORECASE)
    return match.group(1) if match else None


def chat(client: "OpenAI", model: str, messages: list[dict], **kwargs) -> str:
    """Simple one-shot chat call, returns assistant text."""
    defaults = {"temperature": 0.0, "max_tokens": 512}
    defaults.update(kwargs)
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        **defaults,
    )
    return (response.choices[0].message.content or "").strip()
