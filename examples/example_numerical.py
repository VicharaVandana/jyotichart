import sys
import os

# Add jyotichart package path so the script can find it
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'jyotichart'))

import jyotichart as chart

# Output directory (must exist or be created)
outdir = os.path.join(os.path.dirname(__file__), 'jyotichart', 'astrocharts')
os.makedirs(outdir, exist_ok=True)

##############################################################################
# NORTH NUMERICAL CHART EXAMPLE
# Simulates a BhavaBala chart - showing one numerical score per house
##############################################################################
north_num = chart.NorthNumericalChart("BhavaBala", "Shyam Bhat")
north_num.set_ascendantsign("Capricorn")

# Sample bhavabala scores for each house (house 1 to house 12)
bhavabala_scores = [520, 340, 410, 290, 375, 460, 315, 480, 390, 425, 355, 280]

for house, score in enumerate(bhavabala_scores, start=1):
    north_num.set_house_value(house, score, colour='lime')

# Optional: customise look
north_num.updatechartcfg(clr_background='black', clr_line='yellow', clr_sign='pink')

result = north_num.draw(outdir, "BhavaBala_North")
print(f"North Numerical Chart: {result}")

##############################################################################
# SOUTH NUMERICAL CHART EXAMPLE (using house numbers via set_house_value)
# Simulates an AshtakaVarga chart for Jupiter
##############################################################################
south_num = chart.SouthNumericalChart("AshtakaVarga_Jupiter", "Shyam Bhat")
south_num.set_ascendantsign("Capricorn")

# AshtakaVarga points per house (house 1 to 12) - sample data
ashtaka_points = [4, 3, 5, 2, 6, 4, 3, 5, 4, 3, 6, 2]

for house, pts in enumerate(ashtaka_points, start=1):
    south_num.set_house_value(house, pts, colour='skyblue')

result = south_num.draw(outdir, "AshtakaVarga_Jupiter_South")
print(f"South Numerical Chart: {result}")

print(f"\nCharts saved to: {outdir}")
