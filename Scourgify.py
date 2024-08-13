import csv
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if not sys.argv[1].endswith(".csv"):
            sys.exit("Invalid input file format")
        else:
            clean_data(sys.argv[1], sys.argv[2])

def clean_data(input_file, output_file):
    try:
        with open(input_file) as in_file:
            reader = csv.DictReader(in_file)
            with open(output_file, "w") as out_file:
                columns = ["first", "last", "house"]
                writer = csv.DictWriter(out_file, fieldnames=columns)
                writer.writeheader()
                for student in reader:
                    last_name, first_name = student["name"].split(", ")
                    house = student["house"]
                    writer.writerow({"first": first_name, "last": last_name, "house": house})
    except FileNotFoundError:
        sys.exit(f"Error: Could not read {input_file}")

if __name__ == "__main__":
    main()
