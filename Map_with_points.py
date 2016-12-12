import folium
map = folium.Map( location=[45.372, -121.697], zoom_start = 10, tiles="Stamen Terrain" )

#map.add_child( folium.ClickForMarker ( popup = 'Mt Hood Meadows' ), marker_color = 'red' )
map.simple_marker( location=[ 45.3288, -121.6625], popup="Mt Hood Meadows", marker_color = 'red')
map.simple_marker( location=[ 45.3311, -121.7311], popup="Timberlake Lodge", marker_color = 'green')
#map.add_child( folium.ClickForMarker ( popup = 'Timberlake Lodge' ), marker_color = 'green' )
map.save(outfile='Map2.html')# Depreciated code: map.create_map( path = 'map.html')