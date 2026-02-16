from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from database import db
from data_fetcher import FPLDataFetcher

app = FastAPI(title="FPL Hub API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

fetcher = FPLDataFetcher()

@app.get("/")
def root():
    return {"message": "FPL Hub API is running!"}

@app.get("/api/players")
def get_players():
    conn, cursor = db.get_cursor()
    cursor.execute("""
        SELECT p.*, t.short_name as team_name 
        FROM players p 
        JOIN teams t ON p.team_id = t.id 
        ORDER BY p.total_points DESC 
        LIMIT 50
    """)
    players = cursor.fetchall()
    conn.close()
    return players

@app.get("/api/update-data")
def update_data():
    data = fetcher.fetch_bootstrap_data()
    if data:
        return {"message": "Data updated successfully"}
    return {"message": "Update failed"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)