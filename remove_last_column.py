import csv
import os
import glob

# gets the parent directory path from bash
def main():
    # parent_directory = '/Users/soojo/Documents/Cav_PTRF3_PTRF_aligned'
    parent_directory = os.environ['DATASET']

# Check if the parent directory exists
    if not os.path.isdir(parent_directory):
        print(f"Error: Parent directory '{parent_directory}' does not exist.")
        exit(1)

    for folder in glob.glob(os.path.join(parent_directory, "*")):


        if not os.path.isdir(folder):
            continue

        for textfile in glob.glob(os.path.join(folder, "*")):
            with open(textfile, 'r') as file:
                reader = csv.reader(file)
                rows = list(reader)

# Get the value of the upper right cell
            upper_right_cell = rows[0][-1]

# Check if it equals 'originalfile'
            if upper_right_cell == 'originalfile':
    # Remove the last column
                for row in rows:
                    del row[-1]

# Write the modified data back to the CSV file
            with open(textfile, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)

def remove_last_column(csv_file):
    output_file = csv_file
    with open(csv_file, 'r') as file:
        reader = csv.reader(file, delimiter= ",")
        rows = [row[:-1] for row in reader]

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print(f"The last column has been removed. Modified data saved to {output_file}.")

# Provide the input CSV file and the desired output file name

if __name__=="__main__":
     main()





