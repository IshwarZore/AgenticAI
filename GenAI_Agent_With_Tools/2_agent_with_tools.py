from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    description="You are a news reporter who reports news in a simple language in 3 lines along with date of news",
    tools=[DuckDuckGoTools()],
    # markdown=True
)

agent.print_response("Tell me the most latest breaking political news from the USA along with the web url of news")