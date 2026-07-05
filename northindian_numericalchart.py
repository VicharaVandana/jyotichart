import northindianchart as nc
import support.general as gen
import os


############################################################################
############## Centre positions for numerical values per house #############
############################################################################
# These are the (x, y) coordinates for placing a large number at the
# visual centre of each house in the North Indian diamond chart.

north_numerical_centre = [
    {"x": "185", "y": "120"},   # House 1  - Tan Bhav (top diamond)
    {"x": "90",  "y": "55"},    # House 2  - Dhan Bhav (top-left triangle)
    {"x": "25",  "y": "118"},   # House 3  - Anuj Bhav (left triangle)           [left+up]
    {"x": "75",  "y": "210"},   # House 4  - Maata Bhav (left diamond)
    {"x": "18",  "y": "315"},   # House 5  - Santan Bhav (bottom-left triangle)
    {"x": "90",  "y": "375"},   # House 6  - Rog Bhav (bottom-left corner)
    {"x": "185", "y": "335"},   # House 7  - Dampathya Bhav (bottom diamond)
    {"x": "285", "y": "375"},   # House 8  - Aayu Bhav (bottom-right corner)
    {"x": "362", "y": "318"},   # House 9  - Bhagya Bhav (bottom-right triangle) [up, aligned to sign-num y]
    {"x": "300", "y": "210"},   # House 10 - Karma Bhav (right diamond)
    {"x": "362", "y": "118"},   # House 11 - Laab Bhav (right triangle)           [up, aligned to sign-num y]
    {"x": "282", "y": "55"},    # House 12 - Karch Bhav (top-right triangle)
]


############################################################################
################# Global Functions #########################################
############################################################################

def reset_chartcfg():
    return nc.reset_chartcfg()


def write_numericalValuesOnChart_nsc(chartSVG, housevalues):
    ''' Writes the numerical values at the centre of each house.
        housevalues is a list of 12 elements [house1_val, ..., house12_val].
        Each element is a dict: {"value": <number or string>, "colour": <colour string>} '''
    chartSVG.write('\n  <!-- ********** Numerical Values ********** -->\n')
    for idx in range(0, 12):
        val   = housevalues[idx]["value"]
        clr   = housevalues[idx]["colour"]
        px    = north_numerical_centre[idx]["x"]
        py    = north_numerical_centre[idx]["y"]
        chartSVG.write(
            f'  <text x="{px}" y="{py}" fill="{clr}" class="num-value">{val}</text>\n'
        )
    return


def create_numericalchartSVG(chartObj, location, chartSVGfilename):
    ''' Creates an SVG of a North Indian numerical chart.
        Draws the skeleton + sign numbers + one large number per house. '''
    # Build the full file path
    if((location[-1] == '\\') or (location[-1] == '/')):
        chartSVGFullname = f'{location}{chartSVGfilename}.svg'
    elif('/' in location):
        chartSVGFullname = f'{location}/{chartSVGfilename}.svg'
    else:
        chartSVGFullname = f'{location}\\{chartSVGfilename}.svg'

    chartSVG = open(chartSVGFullname, 'w', encoding='utf-16')

    # SVG open tag
    chartSVG.write(
        f'<svg id="{chartObj.chartname}_chart_{chartObj.personname}" '
        f'height="500" width="500" '
        f'xmlns="http://www.w3.org/2000/svg" '
        f'xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'viewBox="0 0 420 420" shape-rendering="geometricPrecision" '
        f'text-rendering="geometricPrecision" charset="utf-16">\n'
    )
    chartSVG.write('  <style>\n')
    chartSVG.write('    .sign-num  { font: bold 22px sans-serif; }\n')
    chartSVG.write('    .num-value { font: bold 24px sans-serif; }\n')
    chartSVG.write('  </style>\n')
    chartSVG.write('  <!-- ********** Chart Diagram ********** -->\n')

    # Draw skeleton, sign numbers, and numerical values
    nc.draw_classicNorthChartSkeleton(chartSVG, chartObj.chartcfg)
    nc.write_signnumOnChart_nsc(chartSVG, chartObj.chartcfg["sign-colour"], chartObj.housesigns)
    write_numericalValuesOnChart_nsc(chartSVG, chartObj.housevalues)

    # SVG close
    chartSVG.write('\n  Sorry, your browser does not support inline SVG.\n')
    chartSVG.write('</svg>\n')
    chartSVG.close()

    return "Success"
