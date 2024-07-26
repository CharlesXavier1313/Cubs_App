from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.openapi.utils import get_openapi
import subprocess
from sqlalchemy import create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from typing import List
from models import Base, Game, BettingOdds, ModelPredictions
from pydantic import BaseModel

# Database configuration
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@db/cubs_betting_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic model for Game
class GameSchema(BaseModel):
    id: int
    date: str
    home_team: str
    away_team: str
    score: str

    class Config:
        orm_mode = True

# Pydantic model for BettingOdds
class BettingOddsSchema(BaseModel):
    game_id: int
    bookmaker: str
    odds_type: str
    odds_value: float

    class Config:
        orm_mode = True

# Pydantic model for ModelPredictions
class ModelPredictionsSchema(BaseModel):
    game_id: int
    model_type: str
    prediction: str
    confidence: float

    class Config:
        orm_mode = True


# Pydantic model for WinLossData
class WinLossData(BaseModel):
    wins: int
    losses: int

# Pydantic model for BettingStats
class BettingStats(BaseModel):
    moneyline_win_rate: float
    over_under_win_rate: float
    run_line_win_rate: float

# Custom OpenAPI schema
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Cubs Betting Analytics API",
        version="1.0.0",
        description="API documentation for the Cubs Betting Analytics Web App",
        routes=app.routes,
    )
    # Add more detailed information about the API
    openapi_schema["info"]["x-logo"] = {
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/80/Chicago_Cubs_logo.svg"
    }
    openapi_schema["info"]["contact"] = {
        "name": "API Support",
        "email": "support@cubsbetting.com",
        "url": "https://www.cubsbetting.com/support",
    }
    openapi_schema["tags"] = [
        {"name": "control", "description": "Endpoints for controlling the application"},
        {"name": "data", "description": "Endpoints for retrieving betting data and statistics"},
    ]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

@app.post("/api/control/start", tags=["control"])
async def start_app():
    """
    Start the application by running the deploy_all.sh script.
    """
    try:
        subprocess.run(["./deploy_all.sh"], check=True)
        return {"message": "Application started successfully"}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Error starting application: {str(e)}")

@app.post("/api/control/stop", tags=["control"])
async def stop_app():
    """
    Stop the application by running docker-compose down.
    """
    try:
        subprocess.run(["docker-compose", "down"], check=True)
        return {"message": "Application stopped successfully"}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Error stopping application: {str(e)}")

@app.get("/api/health", tags=["control"])
async def health_check():
    """
    Perform a health check on the application.
    """
    return {"status": "healthy"}

@app.get("/api/test_db", tags=["control"])
def test_db_connection(db: Session = Depends(get_db)):
    """
    Test the database connection by executing a simple query.
    """
    try:
        db.execute("SELECT 1")
        return {"message": "Database connection successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")

@app.get("/api/games", response_model=List[GameSchema], tags=["data"])
def get_games(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(10, ge=1, le=100, description="Number of records to return"),
    db: Session = Depends(get_db)
):
    """
    Retrieve a list of games from the database.
    """
    try:
        games = db.query(Game).offset(skip).limit(limit).all()
        return games
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving games: {str(e)}")

@app.get("/api/odds/{game_id}", response_model=List[BettingOddsSchema], tags=["data"])
def get_odds(game_id: int, db: Session = Depends(get_db)):
    """
    Retrieve odds for a specific game.
    """
    try:
        odds = db.query(BettingOdds).filter(BettingOdds.game_id == game_id).all()
        if not odds:
            raise HTTPException(status_code=404, detail="Odds not found for this game")
        return odds
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving odds: {str(e)}")

@app.get("/api/predictions/{game_id}", response_model=List[ModelPredictionsSchema], tags=["data"])
def get_predictions(game_id: int, db: Session = Depends(get_db)):
    """
    Retrieve predictions for a specific game.
    """
    try:
        predictions = db.query(ModelPredictions).filter(ModelPredictions.game_id == game_id).all()
        if not predictions:
            raise HTTPException(status_code=404, detail="Predictions not found for this game")
        return predictions
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving predictions: {str(e)}")

@app.get("/api/win_loss_data", response_model=WinLossData, tags=["data"])
def get_win_loss_data(db: Session = Depends(get_db)):
    """
    Retrieve win-loss data for the Cubs.
    """
    try:
        wins = db.query(func.count(Game.id)).filter(Game.cubs_score > Game.opponent_score).scalar()
        losses = db.query(func.count(Game.id)).filter(Game.cubs_score < Game.opponent_score).scalar()
        return {"wins": wins, "losses": losses}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving win-loss data: {str(e)}")

@app.get("/api/betting_stats", response_model=BettingStats, tags=["data"])
def get_betting_stats(db: Session = Depends(get_db)):
    """
    Retrieve betting statistics for the Cubs.
    """
    try:
        total_games = db.query(func.count(Game.id)).scalar()
        
        moneyline_wins = db.query(func.count(Game.id)).filter(
            (Game.cubs_score > Game.opponent_score) & (Game.moneyline > 0)
        ).scalar()
        
        over_under_wins = db.query(func.count(Game.id)).filter(
            (Game.cubs_score + Game.opponent_score) > Game.over_under
        ).scalar()
        
        run_line_wins = db.query(func.count(Game.id)).filter(
            (Game.cubs_score - Game.opponent_score) > Game.run_line
        ).scalar()
        
        return BettingStats(
            moneyline_win_rate=moneyline_wins / total_games,
            over_under_win_rate=over_under_wins / total_games,
            run_line_win_rate=run_line_wins / total_games
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving betting stats: {str(e)}")

# TODO: Add more endpoints for advanced analytics and predictions