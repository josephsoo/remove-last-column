import csv
import os
import glob

kept_columns = ['x [nm]', 'y [nm]', 'z [nm]']
keyword = "filtered"

# gets the parent directory path from bash
def main():
    parent_directory = 'G:\\Cav568\\'
    if not os.path.isdir(parent_directory):
        print(f"Error: Parent directory '{parent_directory}' does not exist.")
        exit(1)
    remove_columns(parent_directory)


def remove_columns(parent_directory):

    for item in glob.glob(os.path.join(parent_directory, "*")):


        if os.path.isfile(item):    
            if (item.endswith('.csv')) and keyword in item:
                print(item)
                
                with open(item, 'r') as file:
                    reader = csv.reader(file)
                    rows = list(reader)

                    remove_columns_indexs = []

                    # Get the indexes of the columns to keep
                    for header in rows[0]:
                        if not (header in kept_columns):
                            remove_columns_indexs.append(rows[0].index(header))

                    for i in reversed(remove_columns_indexs):
                        for row in rows:
                            del row[i]
                # Write the modified data back to the CSV file
                with open(item, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)

        else:
            remove_columns(item)

# Provide the input CSV file and the desired output file name

if __name__=="__main__":
     main()
