import mysql.connector


def get_airports_by_country(country_code):
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

        sql = '''
              SELECT type, COUNT(*)
              FROM airport
              WHERE iso_country = %s
              GROUP BY type
              ORDER BY type DESC\
              '''

        cursor.execute(sql, (country_code,))
        result = cursor.fetchall()

        cursor.close()
        connection.close()

        return result

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return None


def run_country_program():
    country_code = input("Enter the country code (e.g., FI for Finland):").upper()

    airports = get_airports_by_country(country_code)

    if not airports:
        print(f" No airports found for country code '{country_code}'.")
    else:
        print(f"\n\nAirports in {country_code}:")
        for airport_type, count in airports:
            print(f"{count} {airport_type} airports")


run_country_program()