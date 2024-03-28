import psycopg2
import csv

def insert_values(dbname: str, csv_path: str):
    try:
        db = "dbname=" + dbname
        conn = psycopg2.connect(db)
        curs = conn.cursor()
        with open(csv_path) as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                curs.execute("INSERT INTO krisha (id, owner_type, contact, price, appartment_description, urls, rooms, apartment_size, floors, rent, districts, addresses) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", row)
        conn.commit()
        curs.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

def main():
    insert_values("postgres", "./krisha.csv")

if __name__ == "__main__":
    main()