# AI-Inference-Gateway

> A production-ready REST API wrapper for Google Gemini built with FastAPI. Features async I/O, Pydantic validation, and custom timeout handling for scalable LLM inference.

This project transforms a standard AI generation script into a scalable web service. By leveraging Python's asynchronous capabilities (`async`/`await`), the gateway ensures the server remains responsive to other requests while waiting for the LLM to process data. It includes strict payload validation, explicit API timeouts, and standardized error handling.

##  Features

* **Asynchronous Processing:** Utilizes `asyncio` and the `client.aio` SDK methods to handle I/O-bound LLM calls without blocking the main server thread.
* **Data Validation:** Uses **Pydantic** models to strictly define and validate expected Request and Response JSON schemas.
* **Resilience & Timeouts:** Implements a strict 30-second manual timeout (`asyncio.wait_for`) to prevent hanging requests.
* **Structured Error Handling:** Gracefully catches timeouts (504 Gateway Timeout) and server/provider errors (503 Service Unavailable) instead of crashing.
* **Interactive Documentation:** Automatically generates live Swagger UI documentation for easy testing and client integration.

##  Tech Stack

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **Server:** [Uvicorn](https://www.uvicorn.org/)
* **AI Provider:** Google Gemini (`google-genai`)
* **Validation:** Pydantic
* **Environment Management:** `python-dotenv`

##  Setup & Installation

**1. Clone the repository:**
```bash
git clone [https://github.com/yourusername/AI-Inference-Gateway.git](https://github.com/yourusername/AI-Inference-Gateway.git)
cd AI-Inference-Gateway
