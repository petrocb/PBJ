from fastapi import FastAPI
import requests
import uvicorn
app = FastAPI()
@app.get('/api')
async def api():
    return {'message': 'This is a mock API response.'}

@app.get("/api//v3/accounts/1/pricing?instruments=EUR_USD")
async def price():
    return {'message': 'This is a mock API response.'}



if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
