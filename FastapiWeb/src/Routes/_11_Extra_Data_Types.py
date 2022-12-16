from doctest import Example
from this import d
from fastapi import FastAPI, Path, Body
from datetime import datetime, time, timedelta
from uuid import UUID
from typing import Union

app = FastAPI()

@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID = Path(default=..., example="ea9fc3c2-580c-11ed-9b6a-0242ac120002"),
    start_datetime: Union[datetime, None] = Body(default="2022-10-30T10:30:00"),
    end_datetime: Union[datetime, None] = Body(default="2022-10-30T12:30:00"),
    repeat_at: Union[time, None] = Body(default="12:00:00"),
    process_after: Union[timedelta, None] = Body(default=3600), # timedelta in seconds
):
    start_process = start_datetime + process_after # start after 1 hr
    # duration = 3600 seconds as start process is delay by 1 hr reducing total
    # duration from 2 hr to 1 hr 
    duration = end_datetime - start_process 
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }