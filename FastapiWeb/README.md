# FASTAPI Web Resources

This repo utilized material from https://fastapi.tiangolo.com/tutorial

Personal notes are added along the way. If you find any inaccuracies. Please feel free to drop me a note. Thanks

- run uvicorn Routes.1_First_Step:app --reload
- localhost:8000 for json response
- localhost:8000/docs for swagger docs
- localhost:8000/redocs for ReDoc docs
- localhost:8000/openapi.json

---

## 1_First_Steps.py

- A "path" is also commonly called an "endpoint" or a "route".
- Path operaton
- Path operation decorator
- Path operation function

---

## 2_Path_Parameter.py

- Path parameter
- Type hinting 
- Order matter for path operation
- Predefined Values
- How to handle path parameters containing paths
    - /path/{file_path:path}

----

## 3_Query_Parameters.py

- Query parameter - Items that are not part of path parameters
- Shown in URL after ? and separated by & characters
- Understand difference between Path and Query parameter
- Optional Parameters and default value
- Multiple path and query parameters

---

## 4_Request_Body.py

- Sending data to API as request body
- Response Body is data from APIs
- Using pydantic in request body
- Creating data model for request body

---

## 5_Query_Param_Str_Validation.py

- Type hinting for validation
- Using Query validation (min_length, max_length)
- Using Regex validation (regex)
- Default and required parameters
- Multiple value for query parameter
- Adding metadata for parameter (title, description, alias, deprecated)
- Hide parameter on autodocs

---

## 6_Path_Param_Num_Validation.py

- Path parameter is always required if included
- Using Path Validation
- Num Validation (gt, ge, lt, le)

---

## 7_Body_Multiple_Parameters.py

- Putting it all together (Path, Query, Body Parameters)
- Multiple Body Parameters
- Declaring single parameter as a body parameter
- Embeding key into body parameter

---

## 8_Body_Fields.py

- Where is Field being used
- Using Field in Models/_8_Body_Fields.py

---

## 9_Body_Nested_Model.py

- Data type configure in Models/_9_Body_Nested_Model.py
- List, Set data type for body parameter
- Submodel data type for body parameter
- Using special type (HttpUrl)
- Using List & submodels
- Deep Nested Model

---

## 10_Declare_Request_Example_Data.py

- Where does the example show up
- Using Class config and schema_extra to declare example
- Using Field Object to declare example 
- Using Body object to declare example
- example applicable to Path, Query, Header, Cookie, Form, File object too
- Using Multiple examples in Body object

---

## 11_Extra_Data_types.py

- Data types like UUID, datetime(datetime, time, timedelta, date)
- Frozenset (request: list > set, responses: set > list)
- Bytes (request & response: str)
- Decimal (request & response: float)

---

## 12_Cookie_Parameters.py

- How to declare Cookie Parameters

---

## 13_Header_Parameters.py

- How to declare Header Parameters
- Auto conversion in Header Object (Header will convert underscore to hyphen to extract and document the header)
- Receiving duplicate headers

---

## 14_Response_Model.py

- Using different response model to control output
- Using response_model_exclude_unset to control output with no values set
- Using response_model_include, response_model_exclude to variate output 

---

## 15_Extra_Models.py

- Using multiple response model
- Using multiple response model of different type
- Using response model of List type
- Using arbitary dict for response model

---

## 16_Response_Status_Code.py

- Declaring HTTP status code for response

---

## 17_Form_Data.py

- How to add in Form Parameter and when to use it

---

## 18_Request_Files.py

- Difference between File Object and UploadFile Object
- UploadFile has following attributes (filename, content_type, file) and async methods (write, read, seek, close)
- Metadata for File object (description)
- Multiple file upload
- HTMLResponse for file upload from endpoint path

---

## 19_Request_Forms_Files.py

---

## 20_Handling_Errors.py

- How to raise error
- Customizing header for error handling
- Custom exception handling of error
- Overriding default exception handler
- Understand the internal working on validation error, RequestValidationError vs ValidationError (error shown in ur log due to pydantic, but shown as 500 to client. User should not have internal information)
- Using the RequestValidationError Body information
- Understand the internal workings on FastAPI HTTPException vs Starlette HTTPException (FastAPI HTTPException allow headers to be included to be used for OAuth2.0 and some security utilities)
- Reusing FastAPI error handlers

---

## 21_Path_Operation_Configuration.py

## 22_Json_Compatiable_Encoder.py

## 23_Body_Updates.py

## 24_Dependencies.py

## 25_Security.py

## 26_Middleware.py

## 27_CORS_Cross_Origin_Resource_Sharing.py

## 28_SQL_Relational_DB.py

## 29_Bigger_Application_Multiple_Files.py

## 30_Background_Tasks.py

## 31_Metadata_Docs_URLs.py

## 32_Static_files.py

## 33_Testing.py

## 34_Debugging.py