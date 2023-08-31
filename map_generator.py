	import sys
	import numpy as np
	import matplotlib.pyplot as plt
	from itertools import chain
	from mpl_toolkits.basemap import Basemap

	#Ustawienie wielkości generowanej mapy
	fig = plt.figure(figsize=(8, 6), edgecolor='w')

	#Ustawienie odpowiedniej projekcji mapy
	m = Basemap(projection='cyl',resolution=None,
				llcrnrlat=-90, urcrnrlat=90,
				llcrnrlon=-180, urcrnrlon=180, )

	#Ustawienie wyświetlania wartości równoleżników i południków
	#w podanych przedziałach:
	lats = m.drawparallels(np.linspace(-90, 90, 13),
							labels=[False,True,True,False])
	lons = m.drawmeridians(np.linspace(-180, 180, 13),
							labels=[True,False,False,True])

	#Ustawienie rysowania linii równoleżników i południków
	lat_lines = chain(*(tup[1][0] for tup in lats.items()))
	lon_lines = chain(*(tup[1][0] for tup in lons.items()))
	all_lines = chain(lat_lines, lon_lines)
	   
	for line in all_lines:
		line.set(linestyle='-', alpha=0.3, color='w')

	#Wybór sposobu wyświetlania mapy:
	m.bluemarble()

	#Wyświetlanie mapy:
	plt.show()

	#Zapis do pliku:
	plt.savefig('map.png')

