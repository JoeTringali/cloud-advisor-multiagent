"""
config/llm_config.py
--------------------
Centralised LLM configuration for all agents.
Supports OpenAI and Azure OpenAI backends.
"""

import os
from dotenv import load_dotenv

load_dotenv()


def get_llm_config() -> dict:
    """
    Build and return the AutoGen-compatible llm_config dictionary.
    Reads credentials from environment variables.
    """
    use_azure = os.getenv("USE_AZURE_OPENAI", "false").lower() == "true"
    model = os.getenv("LLM_MODEL", "gpt-4o")
    temperature = float(os.getenv("LLM_TEMPERATURE", "0.2"))
    max_tokens = int(os.getenv("LLM_MAX_TOKENS", "4096"))

    if use_azure:
        config_list = [
            {
                "model": os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o"),
                "api_type": "azure",
                "api_key": os.getenv("AZURE_OPENAI_API_KEY"),
                "base_url": os.getenv("AZURE_OPENAI_ENDPOINT"),
                "api_version": os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01"),
            }
        ]
    else:
        config_list = [
            {
                "model": model,
                "api_key": os.getenv("OPENAI_API_KEY"),
            }
        ]

    return {
        "config_list": config_list,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "cache_seed": None,  # Set to an int to enable caching for dev/testing
    }


def get_max_rounds() -> int:
    return int(os.getenv("MAX_CONVERSATION_ROUNDS", "30"))
