from src.file_reader import read_csv
from src.data_validator import validate_records
from src.data_transformer import transform_records
from src.database_loader import load_records

def main():

    records = read_csv("data/sample_customers.csv")

    valid, invalid = validate_records(records)

    transformed = transform_records(valid)

    load_records(transformed)

    print("Total records:", len(records))
    print("Valid records:", len(valid))
    print("Invalid records:", len(invalid))

    print("Processing completed successfully!")

if __name__ == "__main__":
    main()
