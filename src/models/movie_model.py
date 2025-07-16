from pydantic import BaseModel, Field
import datetime

#Standard model for most endpoints
class movieModel(BaseModel):
	id : int = Field(ge = 1, default = 1)
	title : str = Field(min_length = 5, max_length = 30, default = "My Movie")
	overview : str = Field(min_length = 15, max_length = 100, default = "Esta película trata de ...")
	year : int = Field(le = datetime.date.today().year, ge=1900, default = 2025)
	rating : float = Field(ge = 0, le = 10, default = 5.0)
	category : str = Field(min_length = 5, max_length = 10, default = "Acción")

#This other model is used to update a movie (filtered by id)
class movieupdateModel(BaseModel):
	title : str = Field(min_length = 5, max_length = 30, default = "My Movie")
	overview : str = Field(min_length = 15, max_length = 100, default = "Esta película trata de ...")
	year : int = Field(le = datetime.date.today().year, ge=1900, default = 2025)
	rating : float = Field(ge = 0, le = 10, default = 5.0)
	category : str = Field(min_length = 5, max_length = 10, default = "Acción")