import random
import time

from fastapi import FastAPI
from pydantic import BaseSettings
import threading


class Settings(BaseSettings):
    app_name = float


    @classmethod
    def set_cls_id(cls, a, b):
        while True:
            cls.app_name = random.randint(a, b)
            time.sleep(1)
            print(cls.app_name)
        return cls.app_name

class Settings2(BaseSettings):
    app_name2 = float

    @classmethod
    def set_cls_id2(cls, a, b):
        while True:
            cls.app_name2 = random.randint(a, b)
            time.sleep(1)
            print(cls.app_name2)
        return cls.app_name2

settings = Settings()
settings2 = Settings2()
app = FastAPI()


@app.get("/info")
async def info():
    return [{
        "app_name": settings.app_name
    }]

@app.get("/info2")
async def info():
    return [{
        "app_name2": settings2.app_name2
    }]


temp_obj1 = Settings()
t = threading.Thread(target=temp_obj1.set_cls_id, args=(100,300), daemon=True)
t.start()
temp_obj1 = Settings2()
t = threading.Thread(target=temp_obj1.set_cls_id2, args=(10,30), daemon=True)
t.start()
