import sys
from webhook import DiscordWebhookTool
from langchain import LLMMathChain, SerpAPIWrapper
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from typing import Optional, Type
from dhooks import Webhook

from langchain.callbacks.manager import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun
from langchain.tools import BaseTool, StructuredTool, Tool, tool
import requests, os

# Path: examples/main.py
tools = [DiscordWebhookTool()]

llm = ChatOpenAI(temperature=0)

os.environ["WEBHOOK_URL"] = "https://discord.com/api/webhooks/1111194690939785296/azQ6OqeHyh17_XjIsv-sdnMpYePD5_lyHIKV_MRYOpWc_Qlnul_8W7b2JNBFkZmdx9yd"
os.environ["WEBHOOK_USERNAME"] = "LangChain Agent"

agent = initialize_agent(tools, llm, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

agent.run("Send a webhook message with a short poem")