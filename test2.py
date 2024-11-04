#!/usr/bin/env python3
import pandas as pd

def filter_excel(input_file, output_file, filter_column, filter_value):
    # Read Excel file into a pandas DataFrame
    df = pd.read_excel(input_file)
    
    # Filter DataFrame based on criteria
    filtered_df = df[df[filter_column].str.contains(filter_value, na=False)]
    
    # Write filtered DataFrame to new Excel file
    filtered_df.to_excel(output_file, index=False)
    
    print(f"Filtered data saved to {output_file}")

if __name__ == "__main__":
    # Example usage:
    input_file = "Test.xlsx"  # Replace with your input Excel file
    output_file = "output.xlsx"  # Replace with desired output Excel file
    filter_column = "First"  # Replace with the column name to filter
    filter_value = "Hi"  # Replace with the value to filter for

    # Call the function to filter Excel
    filter_excel(input_file, output_file, filter_column, filter_value)