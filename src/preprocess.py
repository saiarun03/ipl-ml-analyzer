from load_data import load_data

def preprocess():
    matches, deliveries = load_data()
    matches.to_parquet("data/processed/matches.parquet", index=False)
    deliveries.to_parquet("data/processed/deliveries.parquet", index=False)
    print("Preprocessed data saved.")

if __name__ == "__main__":
    preprocess()
