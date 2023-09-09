import jyotichart as chart


mychart = chart.NorthChart("Lagna", "Shyam Bhat", IsFullChart = False)
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
housecolours[0] = 'green'   #FIRST HOUSE
housecolours[4] = 'green'   #FIFTH HOUSE
housecolours[8] = 'green'   #NINTH HOUSE
housecolours[5] = 'red'   #SIXTH HOUSE
housecolours[7] = 'red'   #EIGHTH HOUSE
housecolours[11] = 'red'   #TWELFTH HOUSE

mychart.updatechartcfg(aspect=False, clr_background='yellow', clr_line='white', clr_sign='lime', clr_houses=housecolours)

mychart.draw("C:\\Users\hp\Downloads\\astrocharts", "LagnaChart", "svg")
