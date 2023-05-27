from typing import Optional
from langchain.callbacks.manager import CallbackManagerForToolRun
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Optional, Type
import requests, os
from typing import Any, Dict
from pydantic import BaseModel, Field, root_validator
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

#class DiscordWebhookInput(BaseModel):
#    webhook_message: str = Field(description="The message you want to send to the webhook")
#
#    @root_validator
#    def validate_query(cls, values: Dict[str, Any]) -> Dict:
#
#        if "webhook_message" not in values:
#            raise ValueError("webhook_message is required")
#        if not isinstance(values["webhook_message"], str):
#            raise ValueError("webhook_message must be a string")
#
#        return values
        

class DiscordWebhookTool(BaseTool):
    name = "discord_webhook"
    description = "useful for when you need to send a webhook message"
    #args_schema: Type[DiscordWebhookInput] = DiscordWebhookInput

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
            print(answer)
            raise Exception("Webhook message could not be sent! Please check your webhook URL and message and try again.")
        else:
            return "Webhook message sent successfully!"

    
    def _arun(self, webhook_message: str, webhook_url: str, webhook_username: str): raise NotImplementedError("This tool does not support async")

