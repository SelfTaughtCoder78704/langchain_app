

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
    "I want to have a pool of ten friends who each put 5 dollars into a jar. I want 5 of them to split the money in the jar one week. Next week, follow the same pattern, but the other 5 friends split the money. How would this play out?"
)


