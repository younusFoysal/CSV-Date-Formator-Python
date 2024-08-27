import pandas as pd
from datetime import datetime

def convert_epoch_to_readable(epoch):
    return datetime.fromtimestamp(epoch).strftime('%Y-%m-%d %H:%M:%S')

# Read the CSV file
input_file = 'input.csv'
output_file = 'output.csv'

df = pd.read_csv(input_file)

# Print the columns to verify the column names
print("Columns in the CSV file:", df.columns)

# Remove leading/trailing spaces from column names
df.columns = df.columns.str.strip()

# Convert the 'creationdate' column
if 'creationdate' in df.columns:
    df['creationdate'] = df['creationdate'].apply(lambda x: convert_epoch_to_readable(int(x)))
else:
    print("Column 'creationdate' not found in the CSV file.")

# Save the updated DataFrame to a new CSV file
df.to_csv(output_file, index=False)

print(f"Converted file saved as {output_file}")

