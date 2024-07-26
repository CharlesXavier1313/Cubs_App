import pandas as pd

def calculate_expected_value(odds, win_probability):
    """
    Calculate the expected value of a bet.
    
    Parameters:
    odds (float): The odds of the bet.
    win_probability (float): The probability of winning the bet.
    
    Returns:
    float: The expected value of the bet.
    """
    return (odds * win_probability) - (1 - win_probability)

def compute_historical_accuracy(predictions, outcomes):
    """
    Compute the historical accuracy of model predictions.
    
    Parameters:
    predictions (pd.Series): Series of model predictions.
    outcomes (pd.Series): Series of actual outcomes.
    
    Returns:
    float: The historical accuracy of the model.
    """
    return (predictions == outcomes).mean()

def generate_betting_score(expected_value, historical_accuracy, model_confidence):
    """
    Generate a betting score based on expected value, historical accuracy, and model confidence.
    
    Parameters:
    expected_value (float): The expected value of the bet.
    historical_accuracy (float): The historical accuracy of the model.
    model_confidence (float): The confidence of the model in its prediction.
    
    Returns:
    float: The betting score.
    """
    return (expected_value * 0.4) + (historical_accuracy * 0.3) + (model_confidence * 0.3)

def classify_good_bet(betting_score, threshold=70):
    """
    Classify whether a bet is a "good bet" based on the betting score.
    
    Parameters:
    betting_score (float): The betting score.
    threshold (float): The threshold for classifying a good bet.
    
    Returns:
    bool: True if the bet is classified as a good bet, False otherwise.
    """
    return betting_score >= threshold

def normalize_betting_score(betting_score, min_score=0, max_score=100):
    """
    Normalize the betting score on a scale of 0-100.
    
    Parameters:
    betting_score (float): The betting score.
    min_score (float): The minimum score for normalization.
    max_score (float): The maximum score for normalization.
    
    Returns:
    float: The normalized betting score.
    """
    return (betting_score - min_score) / (max_score - min_score) * 100

def classify_good_bet_dynamic(betting_score, risk_preference='medium'):
    """
    Classify whether a bet is a "good bet" based on the betting score and user risk preference.
    
    Parameters:
    betting_score (float): The betting score.
    risk_preference (str): The user's risk preference ('low', 'medium', 'high').
    
    Returns:
    bool: True if the bet is classified as a good bet, False otherwise.
    """
    thresholds = {
        'low': 80,
        'medium': 70,
        'high': 60
    }
    threshold = thresholds.get(risk_preference, 70)
    return betting_score >= threshold
