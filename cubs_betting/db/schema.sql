CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(50),
    team VARCHAR(50)
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    date DATE,
    home_team VARCHAR(50),
    away_team VARCHAR(50),
    score VARCHAR(20)
);

CREATE TABLE player_stats (
    game_id INT,
    player_id INT,
    at_bats INT,
    hits INT,
    runs INT,
    PRIMARY KEY (game_id, player_id),
    FOREIGN KEY (game_id) REFERENCES games(id),
    FOREIGN KEY (player_id) REFERENCES players(id)
);

CREATE TABLE betting_odds (
    game_id INT,
    bookmaker VARCHAR(50),
    odds_type VARCHAR(50),
    odds_value FLOAT,
    PRIMARY KEY (game_id, bookmaker, odds_type),
    FOREIGN KEY (game_id) REFERENCES games(id)
);

CREATE TABLE model_predictions (
    game_id INT,
    model_type VARCHAR(50),
    prediction VARCHAR(50),
    confidence FLOAT,
    PRIMARY KEY (game_id, model_type),
    FOREIGN KEY (game_id) REFERENCES games(id)
);
