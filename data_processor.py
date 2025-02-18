import csv
import os

DATA_DIRECTORY = "./data"
OUTPUT_FILE_PATH = "./formatted_data.csv"

# Open output file
with open(OUTPUT_FILE_PATH, "w") as output_file:
    writer = csv.writer(output_file)

    # Add csv header
    header = ["sales", "date", "region"]
    writer.writerow(header)

    # Iterate through all files in data directory
    for file_name in os.listdir(DATA_DIRECTORY):
        # Open csv file (read)
        with open(f"{DATA_DIRECTORY}/{file_name}", "r") as input_file:
            reader = csv.reader(input_file)
            # Iterate through rows in csv file
            row_i = 0
            for input_row in reader:
                # Skip row header
                if row_i > 0:
                    # Collect data from row
                    product = input_row[0]
                    raw_price = input_row[1]
                    quantity = input_row[2]
                    transaction_date = input_row[3]
                    region = input_row[4]

                    # If pink morsel transaction then process it
                    if product == "pink morsel":
                        # Finish data formatting
                        price = float(raw_price[1:])
                        sale = price * int(quantity)

                        # Write row to output file
                        output_row = [sale, transaction_date, region]
                        writer.writerow(output_row)
                row_i += 1
