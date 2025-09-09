import pandas as pd

def load_data():
    matches = pd.read_csv("data/raw/matches.csv", parse_dates=['date'])
    deliveries = pd.read_csv("data/raw/deliveries.csv")
    return matches, deliveries
