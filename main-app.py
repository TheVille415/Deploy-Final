import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import os

class Housing(BaseModel):
    id: int
    date: object
    price: float
    bedrooms: int
    bathrooms: float
    sqft_living: int
    sqft_lot: int  
    floors: float
    waterfront: int
    view: int
    condition: int  
    grade: int  
    sqft_above: int  
    sqft_basement: int  
    yr_built: int 
    yr_renovated: int  
    zipcode: int 
    lat: float
    long: float
    sqft_living15: int 
    sqft_lot15: int 
 
 
           
app = FastAPI()  
filename = '/Users/Jordan/dev/Make School Courses/DS in production/FINAL/housing.pkl'
with open(filename, "rb") as f:
    model = pickle.load(f)
    
@app.get('/')

def index():

    return {'message': "This is the home page of this API. Go to /apiv1/ or /apiv2/?name="}

@app.get('/apiv1/{name}')

def api1(name: str):

    return {'message': f'Hello! @{name}'}

@app.get('/apiv2/')

def api2(name: str):

    return {'message': f'Hello! @{name}'}

    
# @app.post('/apiv3/')
# def api3(data: Details):
#     return {'message': data}

@app.post('/prediction')
def get_housing_price(data: Housing):
    recived = data.dict()
    id = recived['id']
    date = recived['date']
    price = recived['price']
    bedrooms = recived['bedrooms']
    bathrooms = recived['bathrooms']
    sqft_living = recived['sqft_living']
    sqft_lot = recived['sqft_lot']
    floors = recived['floors']
    waterfront = recived['waterfront']
    view = recived['view']
    condition = recived['condition']
    grade = recived['grade']
    sqft_above = recived['sqft_above']
    sqft_basement = recived['sqft_basement']
    yr_built = recived['yr_built']
    yr_renovated = recived['yr_renovated']
    zipcode = recived['zipcode']
    lat = recived['lat']
    long = recived['long']
    sqft_living15 = recived['sqft_living15']
    sqft_lot15 = recived['sqft_lot15']
    
    pred_input = model.predict([[id, date, price, bedrooms, bathrooms, 
                                 sqft_living, sqft_lot, floors, waterfront, 
                                 view, condition, grade, sqft_above, sqft_basement, 
                                 yr_built, yr_renovated, zipcode, lat, long, 
                                 sqft_living15, sqft_lot15]]).tolist()[0]
    return {'prediction': pred_input}

if __name__ == '__main__':

    uvicorn.run(app, host='127.0.0.1', port=4000, debug=True)