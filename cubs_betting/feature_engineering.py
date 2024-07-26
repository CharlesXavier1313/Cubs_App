import pandas as pd
import numpy as np

def calculate_rolling_averages(data, window_sizes=[7, 14, 30]):
    """
    Calculate rolling averages for specified window sizes.
    
    Parameters:
    data (pd.DataFrame): DataFrame containing the data.
    window_sizes (list): List of window sizes for rolling averages.
    
    Returns:
    pd.DataFrame: DataFrame with rolling averages.
    """
    for window in window_sizes:
        data[f'rolling_avg_{window}'] = data['value'].rolling(window=window).mean()
    return data

def generate_matchup_statistics(batter_stats, pitcher_stats):
    """
    Generate matchup statistics between batters and pitchers.
    
    Parameters:
    batter_stats (pd.DataFrame): DataFrame containing batter statistics.
    pitcher_stats (pd.DataFrame): DataFrame containing pitcher statistics.
    
    Returns:
    pd.DataFrame: DataFrame with matchup statistics.
    """
    matchup_stats = pd.merge(batter_stats, pitcher_stats, on='game_id')
    matchup_stats['matchup_score'] = matchup_stats['batter_avg'] - matchup_stats['pitcher_avg']
    return matchup_stats

def encode_weather_conditions(weather_data):
    """
    Encode weather conditions into numerical values.
    
    Parameters:
    weather_data (pd.DataFrame): DataFrame containing weather data.
    
    Returns:
    pd.DataFrame: DataFrame with encoded weather conditions.
    """
    weather_data['weather_encoded'] = weather_data['weather'].astype('category').cat.codes
    return weather_data

def calculate_player_fatigue(player_stats):
    """
    Calculate player fatigue index based on recent game frequency.
    
    Parameters:
    player_stats (pd.DataFrame): DataFrame containing player statistics.
    
    Returns:
    pd.DataFrame: DataFrame with player fatigue index.
    """
    player_stats['game_date'] = pd.to_datetime(player_stats['game_date'])
    player_stats = player_stats.sort_values(by=['player_id', 'game_date'])
    player_stats['days_since_last_game'] = player_stats.groupby('player_id')['game_date'].diff().dt.days
    player_stats['fatigue_index'] = player_stats['days_since_last_game'].apply(lambda x: 1 if x < 3 else 0)
    return player_stats

def calculate_team_momentum(game_stats):
    """
    Calculate team momentum score using weighted recent performance.
    
    Parameters:
    game_stats (pd.DataFrame): DataFrame containing game statistics.
    
    Returns:
    pd.DataFrame: DataFrame with team momentum score.
    """
    game_stats['game_date'] = pd.to_datetime(game_stats['game_date'])
    game_stats = game_stats.sort_values(by=['team', 'game_date'])
    game_stats['recent_performance'] = game_stats.groupby('team')['score'].rolling(window=5).mean().reset_index(0, drop=True)
    game_stats['momentum_score'] = game_stats['recent_performance'] * 0.5 + game_stats['score'] * 0.5
    return game_stats

def calculate_pitching_impact(pitcher_stats):
    """
    Calculate pitching rotation impact factor.
    
    Parameters:
    pitcher_stats (pd.DataFrame): DataFrame containing pitcher statistics.
    
    Returns:
    pd.DataFrame: DataFrame with pitching rotation impact factor.
    """
    pitcher_stats['game_date'] = pd.to_datetime(pitcher_stats['game_date'])
    pitcher_stats = pitcher_stats.sort_values(by=['pitcher_id', 'game_date'])
    pitcher_stats['days_since_last_pitch'] = pitcher_stats.groupby('pitcher_id')['game_date'].diff().dt.days
    pitcher_stats['impact_factor'] = pitcher_stats['days_since_last_pitch'].apply(lambda x: 1 if x > 5 else 0.5)
    return pitcher_stats
