from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from RedisDataTypes.load_data_to_postgres import get_postgres_data
from RedisDataTypes.load_data_to_redis import get_data
import time

app = FastAPI()

template = Jinja2Templates(directory="templates")


def get_all_data():
    start = time.perf_counter()
    courses = get_data()
    if not courses:
        data_source = "POSTGRESQL"
        courses = get_postgres_data()
    else:
        data_source = "REDIS"
    duration = time.perf_counter() - start

    return data_source,duration,courses




@app.get('/',response_class=HTMLResponse,tags=['index'])
def get_index(request: Request):
    data_source, duration, courses = get_all_data()
    return template.TemplateResponse('index.html',context={
        "request":request,
        "data_source": data_source,
        "duration": duration,
        "courses": courses
    })


app.mount("/templates/static",StaticFiles(directory="templates/static"),'static')