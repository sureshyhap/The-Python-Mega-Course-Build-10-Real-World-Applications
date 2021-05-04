import folium, pandas

data = pandas.read_csv("Volcanoes.txt")
lat = []
lon = []
name = []
color = []
for i in range(data.shape[0]):
    lat.append(data["LAT"][i])
    lon.append(data["LON"][i])
    name.append(data["NAME"][i])
    if data["ELEV"][i] < 2000:
        color.append("green")
    elif data["ELEV"][i] < 3000:
        color.append("orange")
    else:
        color.append("red")

map = folium.Map(location=[45, -36], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="Volcanoes")
for lt, ln, n, c in zip(lat, lon, name, color):
    fg.add_child(folium.Marker(location=[lt, ln], popup=n, icon=folium.Icon(color=c)))
f_obj = open ("world.json", "r", encoding="utf-8-sig")
contents = f_obj.read()

def pop(x):
    if x["properties"]["POP2005"] < 10e6:
        return {"fillColor" : "green"}
    elif 10e6 <= x["properties"]["POP2005"] < 20e6:
        return {"fillColor" : "orange"}
    else:
        return {"fillColor" : "red"}

fg2 = folium.FeatureGroup(name="Population")    
fg2.add_child(folium.GeoJson(data=contents, style_function=lambda x: pop(x)))
map.add_child(fg)
map.add_child(fg2)
map.add_child(folium.LayerControl())
map.save("Map1.html")

