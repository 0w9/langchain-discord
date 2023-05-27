from typing import Optional
from langchain.callbacks.manager import CallbackManagerForToolRun
from langchain.tools import BaseTool
from pydantic import BaseModel, Field, Type
import requests, os

class DiscordWebhookInput(BaseModel):
    #webhook_url: str = Field()
    #webhook_username: str = Field()
    webhook_message: str = Field()

class DiscordWebhookTool(BaseTool):
    name = "discord_webhook"
    description = "useful for when you need to send a webhook message"
    args_schema: Type[DiscordWebhookInput] = DiscordWebhookInput

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
            print(answer.json())
            raise Exception("Webhook message could not be sent! Please check your webhook URL and message and try again.")
        else:
            return "Webhook message sent successfully!"

    
    def _arun(self, webhook_message: str, webhook_url: str, webhook_username: str): raise NotImplementedError("This tool does not support async")

