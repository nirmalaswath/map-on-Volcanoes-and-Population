import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
LAT = list(data.LAT)
LON = list(data.LON)
elev = list(data.ELEV)

def change_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[-50,-120] ,zoom_start = 1 ,tiles = "Stamen Terrain" )

fgv = folium.FeatureGroup(name="Volcanoes")

for lat,lon,el in zip(LAT,LON, elev):
    fgv.add_child(folium.CircleMarker(location=[lat,lon] , tooltip = str(el)+"m",radius = 5, fill_color=change_color(el),color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r' , encoding = 'utf-8-sig').read() , style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'yellow' if 10000000 <= x['properties']['POP2005'] <20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
