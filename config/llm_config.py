"""
config/llm_config.py
--------------------
Centralised LLM configuration for all agents using AutoGen 0.7+.
Supports OpenAI and Azure OpenAI backends via Client objects.
"""

import os
from typing import Union
from dotenv import load_dotenv

# NEW: Import the specific clients for the 0.7+ architecture
from autogen_ext.models.openai import OpenAIChatCompletionClient, AzureOpenAIChatCompletionClient

load_dotenv()

def get_model_client() -> Union[OpenAIChatCompletionClient, AzureOpenAIChatCompletionClient]:
    """
    Build and return the AutoGen 0.7+ compatible model client.
    Replaces the old dictionary-based get_llm_config.
    """
    use_azure = os.getenv("USE_AZURE_OPENAI", "false").lower() == "true"
    model = os.getenv("LLM_MODEL", "gpt-4o")
    temperature = float(os.getenv("LLM_TEMPERATURE", "0.2"))
    max_tokens = int(os.getenv("LLM_MAX_TOKENS", "4096"))

    if use_azure:
        # NEW: Return the Azure-specific client object
        return AzureOpenAIChatCompletionClient(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01"),
            model_capabilities={
                "vision": True,
                "function_calling": True,
                "json_output": True,
            },
            temperature=temperature,
            max_tokens=max_tokens,
        )
    else:
        # NEW: Return the standard OpenAI client object
        return OpenAIChatCompletionClient(
            model=model,
            api_key=os.getenv("OPENAI_API_KEY"),
            temperature=temperature,
            max_tokens=max_tokens,
        )

def get_max_rounds() -> int:
    return int(os.getenv("MAX_CONVERSATION_ROUNDS", "30"))