import psycopg2
import csv

def delete_all_content(dbname: str):
    try:
        db = "dbname=" + dbname
        conn = psycopg2.connect(db)
        curs = conn.cursor()
        print("start")
        curs.execute("TRUNCATE krisha;\nDELETE FROM krisha;")
        conn.commit()
        curs.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

def main():
    delete_all_content("postgres")

if __name__ == "__main__":
    main()