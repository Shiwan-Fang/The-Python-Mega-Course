import pandas
import folium

data = pandas.read_csv("volcanoes.txt")  # 读取这个文件
lat = list(data["LAT"])  # 建立纬度列表
lon = list(data["LON"])  # 经度
elev = list(data["ELEV"])  # 海拔


def color_producer(elevation):  # 海拔不同，颜色不一样
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[-38.58, 99.09],
                 zoom_start=6, tiles="Stamen Terrain")

# 这一行不可以放到for loop里面，不然fg里面数量不会变，循环结束的时候fg等于文件volcanoes里面最后一行
fgv = folium.FeatureGroup(name="volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(
        location=[lt, ln],
        radius=6,
        popup=str(el)+" m",
        fill_color=color_producer(el),  # 中间的颜色填充不进去是什么原因？？？？
        color='grey',
        fill=True,
        fill_opacity=0.07))


fgp = folium.FeatureGroup(name="population")

fgp.add_child(folium.GeoJson(
    data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x:
    {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
     else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())  # 图层，要放在前两行内容的后面

map.save("Map1.html")
