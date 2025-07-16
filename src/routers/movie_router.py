from fastapi import Path, Query, APIRouter #API Router allows us to modularize the project

from typing import List

#Importing models from movie_model
from src.models.movie_model import movieModel, movieupdateModel

#List of movies for the project
movies: List[movieModel] = []

#I create the router instance "movie_router", separating the movies endpoints
movie_router = APIRouter()

#GET METHOD, allows you to obtain data or information from the server
@movie_router.get('/', tags=['Movies']) 
def home():
	return movies

@movie_router.get('/{id}', tags=['Movies']) 
def get_movie_by_id(id : int = Path(gt=0))  -> movieModel | dict: 
	mv_sel = {}
	not_found = True
	i = 0
	while(i < len(movies) and not_found):
		if movies[i].id == id:
			mv_sel = movies[i]
			not_found = False
		i+=1
	return mv_sel

#Function with query parameters 
#(recognized because they are added only within the function, not in the endpoint)
@movie_router.get('/', tags=['Movies']) 
def get_movie_by_category(category : str = Query(min_length = 5, max_length = 10)) -> List[movieModel]: 
	mv_sel_list = []
	for movie in movies:
		if movie.category == category:
			mv_sel_list.append(movie.model_dump())
	return mv_sel_list


#POST METHOD, used to add elements (for example in a database, where it could be useful)
@movie_router.post('/', tags=['Movies'])
def add_movie(data : movieModel) -> List[movieModel]:
	movies.append(data)
	#Since we've modified movies to be a list of movieModel (class objects) 
	#I can convert them to a dictionary for each object to return it
	return [movie.model_dump() for movie in movies] 

#PUT METHOD, allows you to modify elements
@movie_router.put('/{id}', tags=['Movies'])
def update_movie_by_id(id : int, data : movieupdateModel) -> List[movieModel]:
	i = 0
	while(i < len(movies)):
		if movies[i].id == id:
			movies[i].title = data.title
			movies[i].overview = data.overview
			movies[i].year = data.year
			movies[i].rating = data.rating
			movies[i].category = data.category
		i+=1
	return movies	

#DELETE METHOD, allows you to delete items from the server, in this case by id
@movie_router.delete('/{id}', tags=['Movies'])
def delete_movie_by_id(id : int) -> List[movieModel]:
	i = 0
	while(i < len(movies)):
		if movies[i].id == id:
			movies.remove(movies[i])
		i+=1
	return movies