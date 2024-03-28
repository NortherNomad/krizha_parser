# Data Scraping Project from Krisha.kz

This project involves a script for scraping data from the Krisha.kz website. With this script, you can gather information about rental properties in the city of Almaty and store it in a PostgreSQL database.

This project is not done yet, and will be updated.


# Files
- drop.py file is for dropping all content of the table
- insert_values.py for inserting values in the table from csv
- scrap.ipynb parses data from the website, gathers it into the sqlite and csv formats

## Dependencies

This project uses the following dependencies:
- `selenium`: for parsing data
- `beautifulsoup4`: for parsing HTML pages
- `requests`: for making HTTP requests to the website
- `psycopg2`: for working with the PostgreSQL database
