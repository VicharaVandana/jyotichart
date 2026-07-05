import jyotichart as jy
import support.constants as c
import os

if __name__ == '__main__':
    # 1. Create the base Natal South Chart
    mychart = jy.SouthChart("D1", "Shyam Bhat")
    mychart.set_birth_details("12-10-1990", "10:30 AM", "Bangalore")
    mychart.set_ascendantsign("Capricorn")
    mychart.add_planet(jy.SUN,"Su", 9)
    mychart.add_planet(jy.MOON,"Mo", 9)
    mychart.add_planet(jy.MARS,"Ma", 10)
    mychart.add_planet(jy.MERCURY,"Me", 9)
    mychart.add_planet(jy.JUPITER,"Ju", 8)
    mychart.add_planet(jy.VENUS,"Ve", 8)
    mychart.add_planet(jy.SATURN,"Sa", 1,colour="yellow")
    mychart.add_planet(jy.RAHU,"Ra", 12)
    mychart.add_planet(jy.KETU,"Ke", 6)
    
    # Optional: draw it just to have it
    outdir = os.path.join(os.path.dirname(__file__), "astrocharts")
    os.makedirs(outdir, exist_ok=True)
    mytransitchart = jy.SouthTransitChart("Transit", "Shyam Bhat", mychart)
    mytransitchart.set_transit_details("05-07-2026", "15:30")
    mytransitchart.add_planet(jy.SUN,"Su", 1)
    mytransitchart.add_planet(jy.MOON,"Mo", 1)
    mytransitchart.add_planet(jy.MARS,"Ma", 1)
    mytransitchart.add_planet(jy.MERCURY,"Me", 1)
    mytransitchart.add_planet(jy.JUPITER,"Ju", 2)
    mytransitchart.add_planet(jy.VENUS,"Ve", 1)
    mytransitchart.add_planet(jy.SATURN,"Sa", 1,colour="lime")
    mytransitchart.add_planet(jy.RAHU,"Ra", 2)
    mytransitchart.add_planet(jy.KETU,"Ke", 8)
    
    status = mytransitchart.draw(outdir, "TransitChart_South", "svg")
    print(f"Chart generation status: {status}")
    print(f"File saved to {outdir}/TransitChart_South.svg")
