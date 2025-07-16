#Import the framework into main
from fastapi import FastAPI

#Movie Routes Module
from src.routers.movie_router import movie_router 

#This indicates that the application is a FastAPI model:
app = FastAPI()

#endpoint with the tag indicating that it belongs to Home
@app.get('/', tags=['Home']) 
def home():
	return "Hello World"

#Include routers in the application
app.include_router(prefix='/movies' , router=movie_router) 



	
