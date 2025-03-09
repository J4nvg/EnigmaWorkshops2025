from pydantic import BaseModel

# create a Pydantic model for the data; any data that you use this model to send or receive data has to adhere to this
# structure
# this is a part of FastAPI data validation. it ensures the payload matches the structure


class QueryRequest(BaseModel):
    # only one parameter in the request model; possible to add more; possible to use typing lib to use other datatypes
    prompt: str


class QueryResponse(BaseModel):
    # same here; only one parameter
    response: str


class APIKeyModel(BaseModel):
    name: str
    key: str

