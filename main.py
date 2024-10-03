# import the modules
from fastapi import FastAPI

# create a fastapi server
app = FastAPI()


# create routes
@app.get('/')
def hello_world():
    return "Hello World"


@app.get('/hi')
def hi():
    return "HI"
