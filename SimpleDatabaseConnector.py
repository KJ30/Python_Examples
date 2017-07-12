import pyodbc

# Header parameters 

title = 'Database Connector'
width = len(title) * 3
middle = int(width / 3)


def main():
    print_header()
    sql_table()


# Print Header

def print_header():
    print("=" * width)
    print(" " * middle, title.upper())
    print("=" * width)
    print()


# SQL Connection Details

def sql_table():
    connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                "Server= ServerName ;"  # Insert your SQL server instance
                                "Database= DatabaseName ;"  # SQL Database to use
                                "Trusted_Connection=yes;")
    try:
        cursor = connection.cursor()
        cursor.execute(
            " Your SQL Query"  # Insert Query here
        )

        # Print Column Names
        headers = [i[0] for i in cursor.description]
        h1 = headers
        print(h1)
        # Print Row Info
        for record in cursor:
            r2 = record

            print(r2)

    finally:
        cursor.close()


if __name__ == '__main__':
    main()
