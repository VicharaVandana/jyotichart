import jyotichart as chart


mychart = chart.NorthChart("Lagna", "Shyam Bhat")
mychart.set_ascendantsign("Capricorn")
mychart.add_planet(chart.SUN,"Su", 9)
mychart.add_planet(chart.MOON,"Mo", 9)
mychart.add_planet(chart.MARS,"Ma", 10)
mychart.add_planet(chart.MERCURY,"Me", 9, colour='yellow')
mychart.add_planet(chart.JUPITER,"Jup", 8,colour="lime", aspectsymbol="ju", retrograde=True)
mychart.add_planet(chart.VENUS,"Ve", 8)
mychart.add_planet(chart.SATURN,"Sa", 1)
mychart.add_planet(chart.RAHU,"Ra", 12)
mychart.add_planet(chart.KETU,"Ke", 6)

mychart.draw("J:\Serials\\New folder", "LagnaChart", "svg")