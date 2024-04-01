import argparse
import pandas as pd
import psycopg2

def export_to_csv(dbname, user, password, host, port):
    # Connect to the database
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

    # SQL query to select all columns from the staging.hacker_data_model table
    sql_query = "SELECT * FROM staging.hacker_data_model;"

    # Read data into a DataFrame
    df = pd.read_sql(sql_query, conn)

    # Close the database connection
    conn.close()

    # Define the file path for the CSV file
    csv_file_path = r'C:\Users\harishreddy.kaki\dbt_core\dbt_demo\seeds\hacker_data.csv'

    # Write DataFrame to CSV file
    df.to_csv(csv_file_path, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Export data from PostgreSQL to CSV file.')
    parser.add_argument('--dbname', required=True, help='Database name')
    parser.add_argument('--user', required=True, help='Database user')
    parser.add_argument('--password', required=True, help='Database password')
    parser.add_argument('--host', required=True, help='Database host')
    parser.add_argument('--port', required=True, help='Database port')

    args = parser.parse_args()

    # Call export_to_csv function with provided arguments
    export_to_csv(args.dbname, args.user, args.password, args.host, args.port)
