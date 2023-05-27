# Discord Langchain

Discord Langchain is a tool for Langchain to use Discord in agents.
It is currently in development and bugs may encounter.
If you find any bugs, please report it to the [issues](https://github.com/0w9/langchain-discord/issues).
Thanks for all your support!

## Installation (and example)

1. Install the package from PyPI.
```bash
$ python3 -m pip install langchain-discord
```

2. Import the package
```python
from langchain_discord import DiscordWebhookTool
```

... and all other required packages for the example
```python
from langchain import OpenAI
from langchain.agents import initialize_agent, AgentType
import os
```

1. Initialize and environment variables
```python
tools = [
    DiscordWebhookTool()
]

llm = OpenAI(temperature=0)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

os.environ["WEBHOOK_URL"] = "https://discord.com/api/webhooks/<use the webhook url from your discord server>"
os.environ["WEBHOOK_USERNAME"] = "LangChain Agent"
```

2. Run the agent
```python
agent.run("Post a joke to the webhook!")
```

## Notice

This package is in development, more info above.
Currently the package was only tested on the `ZERO_SHOT_REACT_DESCRIPTION` agent.
I'm currently working to add a custom output parser, so it can be used on other agents.

## Support this project

You can support this project by giving a star to this repository, or by reporting all bugs.
I am the only developer of this project, so it may take a while to fix bugs.
You can find more info on my [Twitter](https://twitter.com/lennardeth), or on my [website](https://beachcode.de). 
Donations are also welcome, you can donate to my [BuyMeACoffee](https://www.buymeacoffee.com/lennardships).

## License
I don't know a lot about licenses, so I just used the MIT license.
In general it's free to use (both private and for enterprise), but you can't claim it as your own. 
