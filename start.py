import src

RAW_DATA_PATH = "data/raw/Tomato.csv"
ANALYZED_DATA_PATH = "data/interim/data_analyzed.csv"
FEATURED_DATA_PATH = "data/processed/data_featured.csv"

if __name__ == "__main__":
    src.analyze_data(RAW_DATA_PATH, ANALYZED_DATA_PATH)
    src.featured_data(ANALYZED_DATA_PATH, FEATURED_DATA_PATH)
