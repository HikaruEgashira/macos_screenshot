import os
import sys

from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from mlx_use import Agent
from pydantic import SecretStr
from mlx_use.controller.service import Controller


def set_llm(llm_provider: str, model: str):
    match llm_provider:
        case "OAI":
            api_key = os.getenv("OPENAI_API_KEY")
            return ChatOpenAI(model=model, api_key=SecretStr(api_key))
        case "google":
            api_key = os.getenv("GEMINI_API_KEY")
            return ChatGoogleGenerativeAI(
                model=model, api_key=SecretStr(api_key)
            )
        case "anthropic":
            api_key = os.getenv("ANTHROPIC_API_KEY")
            return ChatAnthropic(
                model_name=model, api_key=SecretStr(api_key)
            )

# Available models:
# google:
#   - gemini-2.0-flash-exp
# OAI:
#   - gpt-4o
#   - gpt-4o-mini
# anthropic:
#   - claude-3-5-haiku-20241022
#   - claude-3-5-sonnet-20241022
llm = set_llm("anthropic", "claude-3-5-sonnet-20241022")

controller = Controller()

task = "calculate how much is 5 X 4 and return the result, then call done."

agent = Agent(
    task=task,
    llm=llm,
    controller=controller,
    use_vision=True,
    max_actions_per_step=1,
)


async def main():
    await agent.run(max_steps=25)


asyncio.run(main())
