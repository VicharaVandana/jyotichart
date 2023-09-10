import jyotichart as chart


mychart = chart.SouthChart("Lagna", "Shyam Bhat", IsFullChart = False)
mychart.set_ascendantsign("Capricorn")
mychart.add_planet(chart.SUN,"Su", 9)
mychart.add_planet(chart.MOON,"Mo", 9)
mychart.add_planet(chart.MARS,"Ma", 10, aspectsymbol="m")
mychart.add_planet(chart.MERCURY,"Me", 9, colour='yellow')
mychart.add_planet(chart.JUPITER,"Ju", 8,colour="lime", retrograde=True)
mychart.add_planet(chart.VENUS,"Ve", 8)
mychart.add_planet(chart.SATURN,"Sa", 1)
mychart.add_planet(chart.RAHU,"Ra", 12)
mychart.add_planet(chart.KETU,"Ke", 6)

housecolours = ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black']
housecolours[0] = 'green'   #Aries
housecolours[4] = 'green'   #Leo
housecolours[8] = 'green'   #Sagittarius
housecolours[5] = 'red'   #Virgo
housecolours[7] = 'red'   #Scorpio
housecolours[11] = 'red'   #Pisces

mychart.updatechartcfg(aspect=False, clr_background='yellow', clr_line='white', clr_Asc='lime', clr_houses=housecolours)

mychart.draw("C:/Users/hp/Downloads/astrocharts", "updatechartcfgsamplesouth")
