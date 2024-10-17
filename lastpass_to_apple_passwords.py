#!/usr/bin/env python3

import csv
import os

# Function to transform LastPass CSV to Apple Passwords format
def transform_lastpass_to_apple(lastpass_file, apple_file):
    # Check if input file exists
    if not os.path.isfile(lastpass_file):
        print(f"Error: The file {lastpass_file} does not exist.")
        return
    
    try:
        with open(lastpass_file, 'rb') as infile:
            # Read the binary file and replace null bytes
            content = infile.read().replace(b'\x00', b'')
            
            with open(apple_file, 'w', newline='', encoding='utf-8') as outfile:
                csv_reader = csv.DictReader(content.decode('utf-8').splitlines())
                
                # Apple Passwords expected headers
                fieldnames = ['Title', 'URL', 'Username', 'Password', 'Notes', 'OTPAuth']
                csv_writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                
                # Write the header
                csv_writer.writeheader()
                
                for row in csv_reader:
                    transformed_row = {
                        'Title': row.get('name', ''),        # 'name' in LastPass becomes 'Title'
                        'URL': row.get('url', ''),           # 'url' stays 'URL'
                        'Username': row.get('username', ''), # 'username' stays 'Username'
                        'Password': row.get('password', ''), # 'password' stays 'Password'
                        'Notes': row.get('extra', ''),       # 'extra' becomes 'Notes'
                        'OTPAuth': ''                        # No direct mapping, leave empty for now
                    }
                    csv_writer.writerow(transformed_row)

        print(f"Transformed CSV saved as {apple_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to handle user input for file paths
def main():
    lastpass_csv = input("Enter the path to the LastPass CSV export file (or press Enter to use 'lastpass_export.csv'): ") or 'lastpass_export.csv'
    apple_passwords_csv = input("Enter the path to save the Apple Passwords import CSV (or press Enter to use 'apple_passwords_import.csv'): ") or 'apple_passwords_import.csv'
    
    transform_lastpass_to_apple(lastpass_csv, apple_passwords_csv)

if __name__ == "__main__":
    main()
