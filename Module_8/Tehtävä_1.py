import mysql.connector

icao = input("Enter the ICAO code of an airport: ").upper()

try:

    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        database="flight_game",
        user="root",
        password="mariadbroot5",
        autocommit=True
    )

    cursor = connection.cursor()


    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor.execute(sql, (icao,))

    result = cursor.fetchone()
    if result:
        name, municipality = result
        print(f"Airport name: {name}")
        print(f"Location: {municipality}")
    else:
        print(f"No airport found with ICAO code {icao}")


    cursor.close()
    connection.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")