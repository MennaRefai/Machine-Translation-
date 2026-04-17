# # from fastapi import FastAPI
# # from pydantic import BaseModel
# # from transformers import MarianMTModel, MarianTokenizer

# # app = FastAPI()

# # # Load the model and tokenizer for translation
# # model_name = "Helsinki-NLP/opus-mt-en-ar"
# # model = MarianMTModel.from_pretrained(model_name)
# # tokenizer = MarianTokenizer.from_pretrained(model_name)

# # # Define a Pydantic model for the request body
# # class TranslationRequest(BaseModel):
# #     text: str

# # @app.post("/translate")
# # async def translate(request: TranslationRequest):
# #     # Tokenize the input text
# #     inputs = tokenizer(request.text, return_tensors="pt", padding=True)

# #     # Generate translation
# #     outputs = model.generate(**inputs)

# #     # Decode the output
# #     translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

# #     # Return the translated text
# #     return {"translated_text": translated_text}


# from fastapi import FastAPI
# from pydantic import BaseModel
# from transformers import MarianMTModel, MarianTokenizer

# # Initialize the FastAPI application
# app = FastAPI()

# # Load the MarianMT model and tokenizer for translation (English to Arabic in this case)
# model_name = "Helsinki-NLP/opus-mt-en-ar"  # Change this model for different language pairs
# model = MarianMTModel.from_pretrained(model_name)
# tokenizer = MarianTokenizer.from_pretrained(model_name)

# # Define a Pydantic model for the request body (input text to be translated)
# class TranslateRequest(BaseModel):
#     text: str

# # Define a Pydantic model for the response (translated text)
# class TranslateResponse(BaseModel):
#     translated_text: str

# # Define the translation function
# @app.post("/translate", response_model=TranslateResponse)
# async def translate(request: TranslateRequest):
#     # Translate the text using MarianMT
#     translated_text = translate_logic(request.text)
#     return {"translated_text": translated_text}

# # This is the translation function that uses the MarianMT model
# def translate_logic(input_text: str) -> str:
#     # Tokenize the input text
#     tokens = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
    
#     # Perform the translation
#     translation = model.generate(**tokens)
    
#     # Decode the translation
#     translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)
#     return translated_text

# # The home route (optional)
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Translation API!"}




# from fastapi import FastAPI
# from pydantic import BaseModel
# from transformers import MarianMTModel, MarianTokenizer

# # Initialize the FastAPI application
# app = FastAPI()

# # Load the MarianMT model and tokenizer for translation (English to Arabic in this case)
# model_name = "Helsinki-NLP/opus-mt-en-ar"  # You can change this model for different language pairs
# model = MarianMTModel.from_pretrained(model_name)
# tokenizer = MarianTokenizer.from_pretrained(model_name)

# # Define a Pydantic model for the request body (input text to be translated)
# class TranslateRequest(BaseModel):
#     text: str

# # Define a Pydantic model for the response (translated text)
# class TranslateResponse(BaseModel):
#     translated_text: str

# # Define the translation function
# @app.post("/translate", response_model=TranslateResponse)
# async def translate(request: TranslateRequest):
#     # Translate the text using MarianMT
#     translated_text = translate_logic(request.text)
#     return {"translated_text": translated_text}

# # This is the translation function that uses the MarianMT model
# def translate_logic(input_text: str) -> str:
#     # Tokenize the input text
#     tokens = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
    
#     # Perform the translation
#     translation = model.generate(**tokens)
    
#     # Decode the translation
#     translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)
#     return translated_text

# # The home route (optional)
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Translation API!"}

# # Run the server with host '0.0.0.0' to make it accessible on the local network




# from fastapi import FastAPI
# from pydantic import BaseModel
# from transformers import MarianMTModel, MarianTokenizer

# app = FastAPI()

# model_name = "Helsinki-NLP/opus-mt-en-ar"
# model = MarianMTModel.from_pretrained(model_name)
# tokenizer = MarianTokenizer.from_pretrained(model_name)

# class TranslateRequest(BaseModel):
#     text: str

# class TranslateResponse(BaseModel):
#     translated_text: str

# @app.post("/translate", response_model=TranslateResponse)
# async def translate(request: TranslateRequest):
#     translated_text = translate_logic(request.text)
#     return {"translated_text": translated_text}

# def translate_logic(input_text: str) -> str:
#     tokens = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
#     translation = model.generate(**tokens)
#     translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)
    
#     # Ensure the returned string is UTF-8 encoded
#     return translated_text.encode('utf-8').decode('utf-8')



# from fastapi import FastAPI
# from pydantic import BaseModel
# from transformers import MarianMTModel, MarianTokenizer
# from fastapi.middleware.cors import CORSMiddleware  # Import CORSMiddleware

# # Initialize the FastAPI application
# app = FastAPI()

# # Configure CORSMiddleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows requests from any origin (you can restrict this to specific IPs for better security)
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
#     allow_headers=["*"],  # Allows all headers
# )

# # Load the MarianMT model and tokenizer for translation (English to Arabic in this case)
# model_name = "Helsinki-NLP/opus-mt-en-ar"  # You can change this model for different language pairs
# model = MarianMTModel.from_pretrained(model_name)
# tokenizer = MarianTokenizer.from_pretrained(model_name)

# # Define a Pydantic model for the request body (input text to be translated)
# class TranslateRequest(BaseModel):
#     text: str

# # Define a Pydantic model for the response (translated text)
# class TranslateResponse(BaseModel):
#     translated_text: str

# # Define the translation function
# @app.post("/translate", response_model=TranslateResponse)
# async def translate(request: TranslateRequest):
#     translated_text = translate_logic(request.text)
#     return {"translated_text": translated_text}

# # This is the translation function that uses the MarianMT model
# def translate_logic(input_text: str) -> str:
#     tokens = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
#     translation = model.generate(**tokens)
#     translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)
    
#     # Ensure the returned string is UTF-8 encoded
#     return translated_text.encode('utf-8').decode('utf-8')

# # The home route (optional)
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Translation API!"}




#######2
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from transformers import MarianMTModel, MarianTokenizer
# from fastapi.middleware.cors import CORSMiddleware

# # Initialize the FastAPI application
# app = FastAPI()

# # Configure CORSMiddleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows requests from any origin (you can restrict this to specific IPs for better security)
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
#     allow_headers=["*"],  # Allows all headers
# )

# # Load the MarianMT model and tokenizer for translation (English to Arabic in this case)
# model_name = "Helsinki-NLP/opus-mt-en-ar"  # You can change this model for different language pairs
# model = MarianMTModel.from_pretrained(model_name)
# tokenizer = MarianTokenizer.from_pretrained(model_name)

# # Define a Pydantic model for the request body (input text to be translated)
# class TranslateRequest(BaseModel):
#     text: str

# # Define a Pydantic model for the response (translated text)
# class TranslateResponse(BaseModel):
#     translated_text: str

# # Define the translation function
# @app.post("/translate", response_model=TranslateResponse)
# async def translate(request: TranslateRequest):
#     if not request.text.strip():  # Check for empty or whitespace-only input
#         raise HTTPException(status_code=400, detail="Input text cannot be empty.")
    
#     translated_text = translate_logic(request.text)
#     return {"translated_text": translated_text}

# # This is the translation function that uses the MarianMT model
# def translate_logic(input_text: str) -> str:
#     tokens = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
#     translation = model.generate(**tokens)
#     translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)
#     return translated_text

# # Add a GET endpoint for testing
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Translation API! Use the /translate endpoint with POST requests to translate text."}

# # Optional GET route to clarify how to use the /translate endpoint
# @app.get("/translate")
# def translate_example():
#     return {"example": "Use POST to send text for translation."}

########3
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from transformers import MarianMTModel, MarianTokenizer
# from fastapi.middleware.cors import CORSMiddleware

# # Initialize the FastAPI application
# app = FastAPI()

# # Configure CORSMiddleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows requests from any origin (you can restrict this to specific IPs for better security)
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
#     allow_headers=["*"],  # Allows all headers
# )

# # Load the MarianMT model and tokenizer for translation (English to Arabic in this case)
# model_name = "Helsinki-NLP/opus-mt-en-ar"  # You can change this model for different language pairs
# model = MarianMTModel.from_pretrained(model_name)
# tokenizer = MarianTokenizer.from_pretrained(model_name)

# # Define a Pydantic model for the request body (input text to be translated)
# class TranslateRequest(BaseModel):
#     text: str

# # Define a Pydantic model for the response (translated text)
# class TranslateResponse(BaseModel):
#     translated_text: str

# # Define the translation function
# @app.post("/translate", response_model=TranslateResponse)
# async def translate(request: TranslateRequest):
#     if not request.text.strip():  # Check for empty or whitespace-only input
#         raise HTTPException(status_code=400, detail="Input text cannot be empty.")
    
#     translated_text = translate_logic(request.text)
#     # Explicitly encode and decode to ensure UTF-8 handling
#     translated_text_utf8 = translated_text
#     return {"translated_text": translated_text_utf8}

# # This is the translation function that uses the MarianMT model
# def translate_logic(input_text: str) -> str:
#     tokens = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
#     translation = model.generate(**tokens)
#     translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)
#     return translated_text

# # Add a GET endpoint for testing
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Translation API! Use the /translate endpoint with POST requests to translate text."}

# # Optional GET route to clarify how to use the /translate endpoint
# @app.get("/translate")
# def translate_example():
#     return {"example": "Use POST to send text for translation."}





#4444
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from transformers import MarianMTModel, MarianTokenizer
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import JSONResponse

# # Initialize the FastAPI application
# app = FastAPI()

# # Configure CORSMiddleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows requests from any origin (you can restrict this to specific IPs for better security)
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
#     allow_headers=["*"],  # Allows all headers
# )

# # Load the MarianMT model and tokenizer for translation (English to Arabic in this case)
# model_name = "Helsinki-NLP/opus-mt-en-ar"  # You can change this model for different language pairs
# model = MarianMTModel.from_pretrained(model_name)
# tokenizer = MarianTokenizer.from_pretrained(model_name)

# # Define a Pydantic model for the request body (input text to be translated)
# class TranslateRequest(BaseModel):
#     text: str

# # Define a Pydantic model for the response (translated text)
# class TranslateResponse(BaseModel):
#     translated_text: str

# # Define the translation endpoint
# @app.post("/translate", response_model=TranslateResponse)
# async def translate(request: TranslateRequest):
#     if not request.text.strip():  # Check for empty or whitespace-only input
#         raise HTTPException(status_code=400, detail="Input text cannot be empty.")
    
#     translated_text = translate_logic(request.text)
#     # Explicitly set UTF-8 content type in the response
#     return JSONResponse(
#         content={"translated_text": translated_text},
#         media_type="application/json; charset=utf-8"
#     )

# # Define the translation logic
# def translate_logic(input_text: str) -> str:
#     tokens = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
#     translation = model.generate(**tokens)
#     translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)
#     return translated_text

# # Add a root GET endpoint for testing
# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Translation API! Use the /translate endpoint with POST requests to translate text."}

# # Optional GET route to clarify how to use the /translate endpoint
# @app.get("/translate")
# def translate_example():
#     return {"example": "Use POST to send text for translation."}



##Number 5 that work .

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from transformers import MarianMTModel, MarianTokenizer

# Initialize the FastAPI application
app = FastAPI()

# Configure CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from any origin (you can restrict this for better security)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Load the MarianMT model and tokenizer for translation (English to Arabic in this case)
model_name = "Helsinki-NLP/opus-mt-en-ar"  # You can change this model for different language pairs
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

# Define a Pydantic model for the request body (input text to be translated)
class TranslateRequest(BaseModel):
    text: str

# Define a Pydantic model for the response (translated text)
class TranslateResponse(BaseModel):
    translated_text: str

# Define the translation endpoint
@app.post("/translate", response_model=TranslateResponse)
async def translate(request: TranslateRequest):
    if not request.text.strip():  # Check for empty or whitespace-only input
        raise HTTPException(status_code=400, detail="Input text cannot be empty.")
    
    translated_text = translate_logic(request.text)
    
    # Return the translated text with explicit UTF-8 content type
    return JSONResponse(
        content={"translated_text": translated_text},
        media_type="application/json; charset=utf-8"
    )

# Translation logic function
def translate_logic(input_text: str) -> str:
    tokens = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)
    translation = model.generate(**tokens)
    translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)
    return translated_text

# Add a GET endpoint for testing
@app.get("/")
def read_root():
    return {"message": "Welcome to the Translation API! Use the /translate endpoint with POST requests to translate text."}

# Optional GET route to provide usage example
@app.get("/translate")
def translate_example():
    return {"example": "Use POST to send text for translation."}
