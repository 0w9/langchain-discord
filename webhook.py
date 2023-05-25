from langchain import LLMMathChain, SerpAPIWrapper
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from typing import Optional, Type
from dhooks import Webhook

from langchain.callbacks.manager import AsyncCallbackManagerForToolRun, CallbackManagerForToolRun
from langchain.tools import BaseTool, StructuredTool, Tool, tool
import requests, os

class DiscordWebhookTool(BaseTool):
    name = "discord_webhook"
    description = "useful for when you need to send a webhook message"

    def _run(self, webhook_message: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        if(os.environ.get("WEBHOOK_URL") is None): raise ValueError("WEBHOOK_URL environment variable not set")
        if(os.environ.get("WEBHOOK_URL") is None): raise ValueError("WEBHOOK_URL environment variable not set")
        
        WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
        WEBHOOK_USERNAME = os.environ.get("WEBHOOK_USERNAME", "LangChain Agent")

        answer = requests.post(WEBHOOK_URL, 
                      json={
                            "content": webhook_message, 
                            "username": WEBHOOK_USERNAME
                        }, 
                      headers={"Content-Type": "application/json"}
        )

        if(answer.status_code != 204 or answer.status_code != 200):
            raise Exception("Webhook message could not be sent! Please check your webhook URL and message and try again.")
        else:
            return "Webhook message sent successfully!"

    
    def _arun(self, webhook_message: str, webhook_url: str, webhook_username: str): raise NotImplementedError("This tool does not support async")

tools = [DiscordWebhookTool()]

llm = ChatOpenAI(temperature=0)

os.environ["WEBHOOK_URL"] = "https://discord.com/api/webhooks/<...>"
os.environ["WEBHOOK_USERNAME"] = "LangChain Agent"

agent = initialize_agent(tools, llm, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

agent.run("Send a webhook message with a short poem")