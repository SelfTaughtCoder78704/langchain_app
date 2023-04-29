

from langchain.agents import initialize_agent
from langchain.agents import load_tools
import os
from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()


OPENAI_KEY = os.getenv("OPENAI_API_KEY")


os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")
llm = OpenAI(temperature=0)

# Next, let's load some tools to use. Note that the `llm-math` tool uses an LLM, so we need to pass that in.
tools = load_tools(["serpapi", "llm-math"], llm=llm)


# Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.
agent = initialize_agent(
    tools, llm, agent="zero-shot-react-description", verbose=True)


agent.run(
    "I set up a blog at https://www.surviving-ourselves.com. It was directed by myself, and written by AI. I want to know if the keywords I used are good enough to get me to the top of Google."
)
