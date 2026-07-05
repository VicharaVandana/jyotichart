import os
import jyotichart as chart

def generate_images():
    outdir = os.path.join(os.path.dirname(__file__), "docs", "images")
    os.makedirs(outdir, exist_ok=True)

    # 1. Full North & South Natal Charts
    north = chart.NorthChart("D1 Natal", "John Doe")
    north.set_ascendantsign("Aries")
    north.add_planet(chart.SUN, "Su", 1)
    north.add_planet(chart.MOON, "Mo", 2)
    north.add_planet(chart.MARS, "Ma", 3)
    north.add_planet(chart.MERCURY, "Me", 4)
    north.add_planet(chart.JUPITER, "Ju", 5, retrograde=True)
    north.add_planet(chart.VENUS, "Ve", 6)
    north.add_planet(chart.SATURN, "Sa", 7)
    north.add_planet(chart.RAHU, "Ra", 8)
    north.add_planet(chart.KETU, "Ke", 2)
    north.draw(outdir, "north_natal", "svg")

    south = chart.SouthChart("D1 Natal", "John Doe")
    south.set_birth_details("08 October 1991", "14:47", "New York")
    south.set_ascendantsign("Aries")
    south.add_planet(chart.SUN, "Su", 1)
    south.add_planet(chart.MOON, "Mo", 2)
    south.add_planet(chart.MARS, "Ma", 3)
    south.add_planet(chart.MERCURY, "Me", 4)
    south.add_planet(chart.JUPITER, "Ju", 5, retrograde=True)
    south.add_planet(chart.VENUS, "Ve", 6)
    south.add_planet(chart.SATURN, "Sa", 7)
    south.add_planet(chart.RAHU, "Ra", 8)
    south.add_planet(chart.KETU, "Ke", 2)
    south.draw(outdir, "south_natal", "svg")

    # 2. Partial North & South Natal Charts
    n_partial = chart.NorthChart("Partial", "Alice", IsFullChart=False)
    n_partial.set_ascendantsign("Leo")
    n_partial.add_planet(chart.SUN, "Su", 1)
    n_partial.add_planet(chart.JUPITER, "Ju", 9)
    n_partial.draw(outdir, "north_partial", "svg")

    s_partial = chart.SouthChart("Partial", "Alice", IsFullChart=False)
    s_partial.set_ascendantsign("Leo")
    s_partial.add_planet(chart.SUN, "Su", 1)
    s_partial.add_planet(chart.JUPITER, "Ju", 9)
    s_partial.draw(outdir, "south_partial", "svg")

    # 3. Custom Colored Charts
    n_custom = chart.NorthChart("Colored", "Custom User")
    n_custom.set_ascendantsign("Gemini")
    n_custom.add_planet(chart.SUN, "Su", 1)
    n_custom.add_planet(chart.MOON, "Mo", 2)
    n_custom.add_planet(chart.MARS, "Ma", 3)
    n_custom.add_planet(chart.MERCURY, "Me", 4)
    n_custom.add_planet(chart.VENUS, "Ve", 5, colour="cyan")
    n_custom.add_planet(chart.JUPITER, "Ju", 6)
    n_custom.add_planet(chart.SATURN, "Sa", 7)
    n_custom.add_planet(chart.RAHU, "Ra", 8)
    n_custom.add_planet(chart.KETU, "Ke", 2)
    housecolours = ['black'] * 12
    housecolours[0] = '#2b2b2b'
    housecolours[4] = '#3d1212'
    n_custom.updatechartcfg(aspect=False, clr_background='#1a1a1a', clr_line='orange', clr_sign='yellow', clr_houses=housecolours)
    n_custom.draw(outdir, "north_custom", "svg")

    s_custom = chart.SouthChart("Colored", "Custom User")
    s_custom.set_ascendantsign("Gemini")
    s_custom.add_planet(chart.SUN, "Su", 1)
    s_custom.add_planet(chart.MOON, "Mo", 2)
    s_custom.add_planet(chart.MARS, "Ma", 3)
    s_custom.add_planet(chart.MERCURY, "Me", 4)
    s_custom.add_planet(chart.VENUS, "Ve", 5, colour="cyan")
    s_custom.add_planet(chart.JUPITER, "Ju", 6)
    s_custom.add_planet(chart.SATURN, "Sa", 7)
    s_custom.add_planet(chart.RAHU, "Ra", 8)
    s_custom.add_planet(chart.KETU, "Ke", 2)
    housecolours_s = ['black'] * 12
    housecolours_s[0] = '#2b2b2b' # Aries
    housecolours_s[4] = '#3d1212' # Leo
    s_custom.updatechartcfg(aspect=False, clr_background='#1a1a1a', clr_line='orange', clr_Asc='yellow', clr_houses=housecolours_s)
    s_custom.draw(outdir, "south_custom", "svg")

    # 4. Numerical Charts
    n_num = chart.NorthNumericalChart("Ashtakavarga", "User")
    n_num.set_ascendantsign("Libra")
    north_values = [324, 156, 210, 489, 512, 123, 765, 890, 432, 234, 567, 876]
    for i in range(1, 13):
        n_num.set_house_value(i, north_values[i-1])
    n_num.draw(outdir, "north_numerical", "svg")

    s_num = chart.SouthNumericalChart("Ashtakavarga", "User")
    s_num.set_ascendantsign("Libra")
    south_values = [2, 5, 8, 3, 1, 9, 4, 7, 6, 2, 8, 5]
    for i in range(1, 13):
        s_num.set_house_value(i, south_values[i-1])
    s_num.draw(outdir, "south_numerical", "svg")

    # 5. Transit Charts (aspect=False)
    north.updatechartcfg(aspect=False)
    n_transit = chart.NorthTransitChart("Transit", "John Doe", north)
    n_transit.add_planet(chart.SUN, "Su", 10)
    n_transit.add_planet(chart.MOON, "Mo", 12)
    n_transit.add_planet(chart.MARS, "Ma", 1)
    n_transit.add_planet(chart.MERCURY, "Me", 2)
    n_transit.add_planet(chart.JUPITER, "Ju", 3)
    n_transit.add_planet(chart.VENUS, "Ve", 4)
    n_transit.add_planet(chart.SATURN, "Sa", 5)
    n_transit.add_planet(chart.RAHU, "Ra", 6)
    n_transit.add_planet(chart.KETU, "Ke", 12)
    n_transit.updatechartcfg(aspect=False)
    n_transit.draw(outdir, "north_transit", "svg")

    south.updatechartcfg(aspect=False)
    s_transit = chart.SouthTransitChart("Transit", "John Doe", south)
    s_transit.set_transit_details("12 Jan 2026", "10:00")
    s_transit.add_planet(chart.SUN, "Su", 10)
    s_transit.add_planet(chart.MOON, "Mo", 12)
    s_transit.add_planet(chart.MARS, "Ma", 1)
    s_transit.add_planet(chart.MERCURY, "Me", 2)
    s_transit.add_planet(chart.JUPITER, "Ju", 3)
    s_transit.add_planet(chart.VENUS, "Ve", 4)
    s_transit.add_planet(chart.SATURN, "Sa", 5)
    s_transit.add_planet(chart.RAHU, "Ra", 6)
    s_transit.add_planet(chart.KETU, "Ke", 12)
    s_transit.updatechartcfg(aspect=False)
    s_transit.draw(outdir, "south_transit", "svg")

    # 6. Hidden Aspects Chart
    h_aspects = chart.NorthChart("D1 Natal", "John Doe", IsFullChart=False)
    h_aspects.set_ascendantsign("Aries")
    h_aspects.add_planet(chart.JUPITER, "Ju", 1)
    h_aspects.updatechartcfg(aspect=False)
    h_aspects.draw(outdir, "hidden_aspects", "svg")

    print("Generated all README images successfully.")

if __name__ == '__main__':
    generate_images()
