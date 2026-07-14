import sqlite3


def create_database():

    conn = sqlite3.connect("company.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees(

        id INTEGER PRIMARY KEY,

        name TEXT,

        department TEXT,

        salary INTEGER

    )
    """)

    cursor.execute("DELETE FROM employees")

    employees = [

        (1, "John", "HR", 40000),

        (2, "Sarah", "IT", 65000),

        (3, "David", "Finance", 55000),

        (4, "Emma", "IT", 72000),

        (5, "Mike", "Sales", 45000)

    ]

    cursor.executemany(
        "INSERT INTO employees VALUES (?,?,?,?)",
        employees
    )

    conn.commit()

    conn.close()


def run_query(query):

    conn = sqlite3.connect("company.db")

    cursor = conn.cursor()

    cursor.execute(query)

    rows = cursor.fetchall()

    columns = []

    if cursor.description:
        columns = [col[0] for col in cursor.description]

    conn.close()

    return columns, rows