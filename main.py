from fastapi import FastAPI, HTTPException
import os
import asyncio
import json
from google import genai
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Configuration Error: GEMINI_API_KEY not found in .env file.")
    exit()

client = genai.Client(api_key=api_key)

app=FastAPI()

@app.get("/")
def root():
    return {"hello": "world"}

class Query(BaseModel):
    prompt: str

class GenerateResponse(BaseModel):
    status: str
    response: str


# generate response dictates how the response should look like
# here '/generate' is the endpoint
@app.post("/generate", response_model=GenerateResponse)
async def generate(query: Query):
    try:
        # implementing a manual timeout of 30 seconds
        # we will use client.aio for asynchronous calls so it doesn't block the server
        # async connects await, and asyncio connects aio
        llm_response = await asyncio.wait_for( 
            client.aio.models.generate_content(
                model='gemini-2.5-flash',
                # we extract the 'prompt' from the 'query' class
                contents=query.prompt, 
            ),
            timeout=30.0
        )

        # returning a structured json object
        return GenerateResponse(status="success", response=llm_response.text)
    
    except asyncio.TimeoutError:
        # return a 504 Gateway Timeout if the the request times out
        # here, HTTPExecution indentifies the error based on the status code assigned to each error, hence flagging and resolving them
        raise HTTPException(
            status_code=504,
            detail="Gateway Timeout: The AI provider took too long to respond."
        )
    
    except Exception as e:
        # return a 503 service unavailable for other LLM/Server errors
        raise HTTPException(
            status_code=503,
            detail=f"Service Unavailable: {str(e)}"
        )

