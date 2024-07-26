from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    position = Column(String(50))
    team = Column(String(50))

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    home_team = Column(String(50))
    away_team = Column(String(50))
    score = Column(String(20))

class PlayerStats(Base):
    __tablename__ = "player_stats"

    game_id = Column(Integer, ForeignKey('games.id'), primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'), primary_key=True)
    at_bats = Column(Integer)
    hits = Column(Integer)
    runs = Column(Integer)

class BettingOdds(Base):
    __tablename__ = "betting_odds"

    game_id = Column(Integer, ForeignKey('games.id'), primary_key=True)
    bookmaker = Column(String(50), primary_key=True)
    odds_type = Column(String(50), primary_key=True)
    odds_value = Column(Float)

class ModelPredictions(Base):
    __tablename__ = "model_predictions"

    game_id = Column(Integer, ForeignKey('games.id'), primary_key=True)
    model_type = Column(String(50), primary_key=True)
    prediction = Column(String(50))
    confidence = Column(Float)