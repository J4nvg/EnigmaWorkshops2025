import openai
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from tavily import AsyncTavilyClient, TavilyClient
import asyncio
from dotenv import load_dotenv
import os
import json


# load API key;
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

# use override=True if you have the API key set up in your env variables
load_dotenv(dotenv_path=dotenv_path, override=True)
print(os.environ["OPENAI_API_KEY"])
print(os.environ["TAVILY_API_KEY"])


# Step 1. Setup (asynchronous) TavilyClient to query Tavily search engine
atavily_client = AsyncTavilyClient(api_key=os.environ["TAVILY_API_KEY"])
tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

# Step 2. Executing a simple search query
# q = "Who is Dimebag Darrell?"
# resp = asyncio.run(atavily_client.search(q))
# print(json.dumps(resp, indent=4, sort_keys=True))

# info = "\n".join([result["content"] for result in response["results"]])

# create llm model instance
llm = ChatOpenAI(model="gpt-4o-mini")


async def get_info(query: str):
    result = await atavily_client.search(query)
    info = "\n".join([r["content"] for r in result["results"]])
    response = await llm.ainvoke([SystemMessage(
        content="Combine the information from these sources and explain the information to the user.\n"
                "Provide a general overview of the subject of the information.\n" + info +
                "\nUser original prompt:" + query)])

    sources = "\n\nSources:\n\n" + "\n".join([f"{r['title']}\n{r['url']}" for r in result["results"]])

    return (
            response.content + sources)


async def simple_response(prompt: str, model: ChatOpenAI = llm):
    try:
        response = await model.ainvoke(prompt)
    except openai.AuthenticationError as e:
        print(f"yo the API key isnt right: \n{e}")
        return "wrong key provided"
    return response.content


if __name__ == "__main__":
    print("-"*50)
    print("-"*21 + "__main__" + "-"*21)
    print("-" * 50)

    # check the function
    output = asyncio.run(simple_response("hey wassup", model=llm))
    print(output)

    output = asyncio.run(get_info("dimebag darrell"))
    print(output)