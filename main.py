from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - novostack-crm-coll-63ed80bf3d4541e6b4e4948aff203e34',debug=False,docs_url='/busy-rekha-d6a478fa9c2e11ef9b7f0242c0a8b00326/docs',openapi_url='/busy-rekha-d6a478fa9c2e11ef9b7f0242c0a8b00326/openapi.json')

app.include_router(router, prefix='/busy-rekha-d6a478fa9c2e11ef9b7f0242c0a8b00326/api', tags=['APIs v1'])

def run_h11():
    uvicorn.run('main:app', host='0.0.0.0', port=8008, reload=True)

if __name__ == '__main__':
    run_h11()