import mariadb
import plotly.express as px
from pandas import DataFrame

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

df = DataFrame(results, columns = ['flights','year'])
fig = px.bar(df, x="year", y="flights", title="Flights per Year")
fig.show()
    