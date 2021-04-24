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
fg = folium.FeatureGroup(name="My Map")
for lt, ln, n, c in zip(lat, lon, name, color):
    fg.add_child(folium.Marker(location=[lt, ln], popup=n, icon=folium.Icon(color=c)))
map.add_child(fg);
map.save("Map1.html")

