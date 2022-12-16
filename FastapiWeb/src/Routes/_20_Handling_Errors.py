from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.encoders import jsonable_encoder
from Models._20_Handling_Errors import Item
from Exceptions._20_Handling_Errors import UnicornException


app = FastAPI()

items = {"foo": "The Foo Wrestlers"}

# General raising of HTTP erros
@app.get("/items/{item_id}", status_code=status.HTTP_200_OK)
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item Not Found")
    return {"item": items[item_id]}

# Using custom headers for some security
@app.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404, 
            detail="Item not found",
            headers={"X-Error": "There goes my error"}
        )
    return {"item": items[item_id]}

# custom exception for global handling, 
# 1. Create a class
# 2. Decorator with exception_handler
# 3. Raise Custom Error Class
@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f'Oops! {exc.name} did something'},
    )

@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}

# Overriding the default exception handlers
# Internall, FastAPI raise a RequestValidationError
# To override, decorator exception_handler raised
# Overriding the HTTP exception
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

# Overriding the validation error
# comment line 73 - 82 if running this exception_handler
# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc):
#     return PlainTextResponse(str(exc), status_code=400)

@app.get("/items2/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="No 3 allowed")
    return {"item_id": item_id}

# Using the RequestValidationError Body to return the information
# comment line 59-61 if running below
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )

@app.post("/items/")
async def create_item(item:Item):
    return item

# Reusing FastAPI Exception Handler
# from fastapi.exception_handlers import (
#     http_exception_handler,
#     request_validation_exception_handler,
# )

# Adding additonal print to http_exception
# @app.exception_handler(StarletteHTTPException)
# async def custom_http_exception_handler(request, exc):
#     print(f"OMG! An HTTP error!: {repr(exc)}")
#     return await http_exception_handler(request, exc)

# Adding additonal print to request_validation_exception
# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     print(f"OMG! The client sent invalid data!: {exc}")
#     return await request_validation_exception_handler(request, exc)


# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     if item_id == 3:
#         raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
#     return {"item_id": item_id}