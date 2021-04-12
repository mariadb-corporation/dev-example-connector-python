import mariadb

config = {
    'host': '[host_address]',
    'port': 3306,
    'user': '[username]',
    'password': '***',
    'database': 'travel',
    'ssl': 1
}

conn = mariadb.connect(**config)

cur = conn.cursor()

cur.execute("SELECT COUNT(*) flights, year " \
            "FROM flights " \
            "WHERE year >= 2015 and year < 2021 " \
            "GROUP BY year " \
            "ORDER BY year DESC")

results = cur.fetchall()

print("------------------------------------")
print('Flights\t\tYear')
print("------------------------------------")
for (flights, year) in results:
    print(f"{year}\t\t{flights}")