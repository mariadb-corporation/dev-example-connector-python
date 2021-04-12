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

cur.execute("SELECT COUNT(*) flights, year, month " \
            "FROM flights " \
            "WHERE year >= 2015 and year < 2021 " \
            "GROUP BY year, month " \
            "ORDER BY year DESC, month ASC")

results = cur.fetchall()
        
df = DataFrame(results, columns = ['flights','year','month'])
fig = px.line(df, x="month", y="flights", color="year", title="Flights per Year")
fig.update_xaxes(type='category')
fig.show()