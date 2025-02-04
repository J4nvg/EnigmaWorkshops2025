from fastapi import FastAPI, HTTPException
# from langgraph.graph import END
# from langgraph.graph import MessageGraph
import os
from dotenv import load_dotenv
from models import QueryRequest, QueryResponse, APIKeyModel
from nodes import simple_response, get_info
from utils import setup_api_key
import asyncio


# load API key;
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

# use override=True if you have the API key set up in your env variables
load_dotenv(dotenv_path=dotenv_path, override=True)

# check; has to be right as in .env
print(os.environ["OPENAI_API_KEY"])
print(os.environ["TAVILY_API_KEY"])

# this line instantiates an app
app = FastAPI()


# this function is a wrapped into an endpoint with HTTP post
@app.post("/query-llm", response_model=QueryResponse)
async def query_llm(payload: QueryRequest):
    response = await simple_response(payload.prompt)
    return {
        "response": response
    }


@app.post("/ask-question", response_model=QueryResponse)
async def ask_question(payload: QueryRequest):
    response = await get_info(payload.prompt)
    return {
        "response": response
    }


# send api keys over an endpoint
@app.post("/api-key-setup")
async def setup(payload: APIKeyModel):
    try:
        await setup_api_key(payload)
        return
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# to launch the server, enter this in terminal in the current directory of this project
# uvicorn main:app

# to launch FastAPI Swagger interface, go to:
# 127.0.0.1:8000/docs#

# you can also test the endpoint there or create a python code to send a request to the server with request library
