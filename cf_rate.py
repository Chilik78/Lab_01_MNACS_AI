from statistics import mean

from fastapi import FastAPI, APIRouter
import requests

app = FastAPI(
    title = "cf_rate API", openapi_url="/openapi.json"
)

api_router = APIRouter()

@api_router.get("/cf_rate/{cf_id}", status_code=200)
def root(cf_id):
    """
    Root Get
    """
    
    rank = "0"
    try:
        req = requests.get('https://codeforces.com/api/user.rating?handle=' + cf_id)  
        if req.status_code == 200 and 'json' in req.headers['content-type']:
            print(req.json())
            ranks = []

            for contest in req.json()["result"]:
                ranks.append(contest['rank'])

            rank = str(mean(ranks))
    except:
        rank = "0"
        
    return rank

app.include_router(api_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    # Some nicks:
    # fefer_ivan
    # tourist
    # Petr
    # Um_nik
    # ecnerwala
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")