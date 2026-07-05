import southindianchart as sc
import support.general as gen
import os


############################################################################
############## Centre positions for numerical values per sign ##############
############################################################################
# The South Indian chart has 12 fixed rectangular sign boxes arranged in a
# 4x4 grid with a hollow centre. Each sign's box top-left corner (x, y) is:
#
#   Pisces   (x=3,   y=10)   Aries    (x=123, y=10)   Taurus   (x=243, y=10)   Gemini  (x=363, y=10)
#   Aquarius (x=3,   y=90)                                                       Cancer  (x=363, y=90)
#   Capricorn(x=3,   y=170)                                                      Leo     (x=363, y=170)
#   Sagitt.  (x=3,   y=250)  Scorpio  (x=123,y=250)   Libra    (x=243, y=250)  Virgo   (x=363, y=250)
#
# Box size: 120 wide × 80 tall.  Centre offset from box top-left: (~60, ~50).

# Keyed by zodiac sign name (lowercase) → centre (x, y) for the large number.
south_numerical_centre = {
    "aries"       : {"x": "183", "y": "60"},
    "taurus"      : {"x": "303", "y": "60"},
    "gemini"      : {"x": "423", "y": "60"},
    "cancer"      : {"x": "423", "y": "140"},
    "leo"         : {"x": "423", "y": "220"},
    "virgo"       : {"x": "423", "y": "300"},
    "libra"       : {"x": "303", "y": "300"},
    "scorpio"     : {"x": "183", "y": "300"},
    "sagittarius" : {"x": "63",  "y": "300"},
    "capricorn"   : {"x": "63",  "y": "220"},
    "aquarius"    : {"x": "63",  "y": "140"},
    "pisces"      : {"x": "63",  "y": "60"},
}

# Sign order fixed in south indian chart (always Aries first)
south_sign_order = [
    "aries", "taurus", "gemini", "cancer",
    "leo", "virgo", "libra", "scorpio",
    "sagittarius", "capricorn", "aquarius", "pisces"
]


############################################################################
################# Global Functions #########################################
############################################################################

def reset_chartcfg():
    return sc.reset_chartcfg()


def write_numericalValuesOnChart_ssc(chartSVG, signvalues):
    ''' Writes the numerical values at the visual centre of each sign box.
        signvalues is a dict keyed by lowercase sign name:
            { "aries": {"value": 42, "colour": "lime"}, ... }
    '''
    chartSVG.write('\n  <!-- ********** Numerical Values ********** -->\n')
    for sign in south_sign_order:
        val = signvalues[sign]["value"]
        clr = signvalues[sign]["colour"]
        px  = south_numerical_centre[sign]["x"]
        py  = south_numerical_centre[sign]["y"]
        chartSVG.write(
            f'  <text x="{px}" y="{py}" fill="{clr}" class="num-value">{val}</text>\n'
        )
    return


def write_ascOnChart_ssc(chartSVG, signclr, ascendantsign):
    ''' Re-uses the south chart skeleton's Asc marker. '''
    sc.write_signnumOnChart_ssc(chartSVG, signclr, ascendantsign)
    return


def create_numericalchartSVG(chartObj, location, chartSVGfilename):
    ''' Creates an SVG of a South Indian numerical chart.
        Draws the skeleton + Asc marker + one large number per sign box. '''
    # Build the full file path
    if((location[-1] == '\\') or (location[-1] == '/')):
        chartSVGFullname = f'{location}{chartSVGfilename}.svg'
    elif('/' in location):
        chartSVGFullname = f'{location}/{chartSVGfilename}.svg'
    else:
        chartSVGFullname = f'{location}\\{chartSVGfilename}.svg'

    chartSVG = open(chartSVGFullname, 'w', encoding='utf-16')

    # SVG open tag (same viewport dimensions as the regular south chart)
    chartSVG.write(
        f'<svg id="{chartObj.chartname}_chart_{chartObj.personname}" '
        f'height="330" width="490" '
        f'xmlns="http://www.w3.org/2000/svg" '
        f'xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'viewBox="0 0 490 340" shape-rendering="geometricPrecision" '
        f'text-rendering="geometricPrecision" charset="utf-16">\n'
    )
    chartSVG.write('  <style>\n')
    chartSVG.write('    .sign-num  { font: bold 20px sans-serif; }\n')
    chartSVG.write('    .num-value { font: bold 30px sans-serif; }\n')
    chartSVG.write('  </style>\n')
    chartSVG.write('  <!-- ********** Chart Diagram ********** -->\n')

    # Draw skeleton, Asc marker, and numerical values
    sc.draw_classicSouthChartSkeleton(chartSVG, chartObj.chartcfg)
    write_ascOnChart_ssc(chartSVG, chartObj.chartcfg["sign-colour"], chartObj.ascendantsign)
    write_numericalValuesOnChart_ssc(chartSVG, chartObj.signvalues)

    # SVG close
    chartSVG.write('\n  Sorry, your browser does not support inline SVG.\n')
    chartSVG.write('</svg>\n')
    chartSVG.close()

    return "Success"
