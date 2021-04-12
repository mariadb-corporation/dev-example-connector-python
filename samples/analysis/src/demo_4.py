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

cur.execute("SELECT COUNT(*) flights, a.airport airport, a.latitude latitude, a.longitude longitude " \
            "FROM airports a INNER JOIN flights f ON a.iata_code = f.dest " \
            "WHERE year = 2019 " \
            "GROUP BY a.airport, a.latitude, a.longitude")

results = cur.fetchall()
        
df = DataFrame(results, columns = ['flights','airport','latitude','longitude'])

fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", hover_name="airport", 
                        hover_data=["flights"], color_continuous_scale=px.colors.cyclical.IceFire, 
                        color="flights", size="flights", zoom=3, height=300)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()