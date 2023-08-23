import support.constants as c


SouthChart_offsets4mAries = {  "aries"  :   { "x": 0, "y": 0},
                        "taurus"        :   { "x": 120, "y": 0},
                        "gemini"        :   { "x": 240, "y": 0},
                        "cancer"        :   { "x": 240, "y": 80},
                        "leo"           :   { "x": 240, "y": 160},
                        "virgo"         :   { "x": 240, "y": 240},
                        "libra"         :   { "x": 120, "y": 240},
                        "scorpio"       :   { "x": 0, "y": 240},
                        "saggitarius"   :   { "x": -120, "y": 240},
                        "capricorn"     :   { "x": -120, "y": 160},
                        "aquarius"      :   { "x": -120, "y": 80},
                        "pisces"        :   { "x": -120, "y": 0}
                        }

SouthChart_AscendantPositionAries = {"x": 202, "y": 83}
                        

base_coordinates = [{"x":155, "y":40},   #planet 1
                    {"x":185, "y":48},   #planet 2
                    {"x":170, "y":70},   #planet 3
                    {"x":135, "y":58},   #planet 4
                    {"x":215, "y":60},   #planet 5
                    {"x":145, "y":83},   #planet 6
                    {"x":210, "y":35},   #planet 7
                    {"x":130, "y":32},   #planet 8
                    {"x":180, "y":30}    #planet 9
                    ]


############################################################################
################# Global Functions #########################################
############################################################################

def reset_chartcfg():
    chartcfg = {
                    "background-colour" : "black",
                    "outerbox-colour" : "red",
                    "innerbox-colour" : "red",
                    "line-colour" : "yellow",
                    "sign-colour" : "pink",
                    "house-colour" : {
                                        "aries"         : "black",
                                        "taurus"        : "black",
                                        "gemini"        : "black",
                                        "cancer"        : "black",
                                        "leo"           : "black",
                                        "virgo"         : "black",
                                        "libra"         : "black",
                                        "scorpio"       : "black",
                                        "sagittarius"   : "black",
                                        "capricorn"     : "black",
                                        "aquarius"      : "black",
                                        "pisces"        : "black"
                                    },
                    "aspect-visibility"  : True
                }
    return(chartcfg)

# Function to get svg coordinates with house and planet number in that house
def get_coordniates(sign, planetidx):
    # sign is the sign in which planet is placed like "Aries", "Taurus" etc
    # planetidx is index of the planet in that house. If its first planet in that house then its 1 and if its 3rd planet then its 3.
    #return value is a tuple (x,y) containing 2 elements. x-coordinate and y-coordinate
    if (planetidx in range(1,10)):
        offset = SouthChart_offsets4mAries[sign.lower()]
        x_coordinate = base_coordinates[planetidx-1]["x"] + offset["x"]
        y_coordinate = base_coordinates[planetidx-1]["y"] + offset["y"]
        return((x_coordinate,y_coordinate))
    else: 
        print(f"INPUTERROR: planetidx must be in the range 1 to 8 but given value is {planetidx}.")
        return((0,0))

def draw_classicSouthChartSkeleton(chartSVG, chartCfg):
    # Chart drawing section - Skeleton part for template - south-square-classic
    chartSVG.write(f'''  <!-- ********** Chart Diagram ********** -->\n''')
    chartSVG.write(f'''  <rect id = "border" width="486" height="327" x="0" y="7" style="fill:{chartCfg["background-colour"]};stroke-width:3;stroke:{chartCfg["outerbox-colour"]}" />\n''')
    chartSVG.write(f'''  <rect id = "center" width="235" height="156" x="126" y="92" style="fill:{chartCfg["background-colour"]};stroke-width:3;stroke:{chartCfg["innerbox-colour"]}" />\n''')
    chartSVG.write(f'''  <rect id ="aries" width="120" height="80" x="123" y="10" style="fill:{chartCfg["house-colour"]["aries"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <rect id ="taurus" width="120" height="80" x="243" y="10" style="fill:{chartCfg["house-colour"]["taurus"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <rect id ="gemini" width="120" height="80" x="363" y="10" style="fill:{chartCfg["house-colour"]["gemini"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <rect id ="cancer" width="120" height="80" x="363" y="90" style="fill:{chartCfg["house-colour"]["cancer"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <rect id ="leo" width="120" height="80" x="363" y="170" style="fill:{chartCfg["house-colour"]["leo"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <rect id ="virgo" width="120" height="80" x="363" y="250" style="fill:{chartCfg["house-colour"]["virgo"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <rect id ="libra" width="120" height="80" x="243" y="250" style="fill:{chartCfg["house-colour"]["libra"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <rect id ="scorpio" width="120" height="80" x="123" y="250" style="fill:{chartCfg["house-colour"]["scorpio"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <rect id ="sagittarius" width="120" height="80" x="3" y="250" style="fill:{chartCfg["house-colour"]["sagittarius"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <rect id ="capricorn" width="120" height="80" x="3" y="170" style="fill:{chartCfg["house-colour"]["capricorn"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <rect id ="aquarius" width="120" height="80" x="3" y="90" style="fill:{chartCfg["house-colour"]["aquarius"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <rect id ="pisces" width="120" height="80" x="3" y="10" style="fill:{chartCfg["house-colour"]["pisces"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    return

def write_signnumOnChart_ssc(chartSVG, signclr, ascendantsign):
    chartSVG.write('\n  <!-- ********** Ascendant Sign ********** -->\n')
    pxAsc = SouthChart_AscendantPositionAries["x"] + SouthChart_offsets4mAries[ascendantsign.lower()]["x"]
    pyAsc = SouthChart_AscendantPositionAries["y"] + SouthChart_offsets4mAries[ascendantsign.lower()]["y"]
    
    chartSVG.write(f'''  <text id ="{ascendantsign}Asc" x="{pxAsc}" y="{pyAsc}" fill="{signclr}" class="sign-num">Asc</text>\n''')
    return

def write_planetsOnChart_ssc(chartSVG, planets):
    chartSVG.write('\n  <!-- ********** Planets ********** -->\n')
    
    for planetname in planets:
        chartSVG.write(f'\n  <!-- ********** {planetname} ********** -->\n')
        symbol = planets[planetname]["symbol"]
        retro = planets[planetname]["retro"]
        planetcolour = planets[planetname]["colour"]
        #Get planet position co-ordinates x and y on chart svg
        px = planets[planetname]["pos"]["x"]
        py = planets[planetname]["pos"]["y"]

        #Since all needed properties are computed, Now create the svg entry string for planet
        if(retro == True):
            Planet_SVGstring = f'''  <text y="{py}" x="{px}" fill="{planetcolour}" text-decoration="underline" class="planet">({symbol})</text>\n'''
        else:
            Planet_SVGstring = f'''  <text y="{py}" x="{px}" fill="{planetcolour}" class="planet">{symbol}</text>\n'''
        #write the planet to SVG chart
        chartSVG.write(Planet_SVGstring)
    return

def write_planetsAspectsOnChart_ssc(chartSVG, planets):
    chartSVG.write('\n  <!-- ********** Planets Aspects ********** -->\n')
    
    for planetname in planets:
        chartSVG.write(f'\n  <!-- ********** {planetname} Aspect ********** -->\n')
        symbol = planets[planetname]["aspect_symbol"]
        planetcolour = planets[planetname]["colour"]
        for aspectpositions in planets[planetname]["aspectpos"]:
            #Get planet position co-ordinates x and y on chart svg
            px = aspectpositions["x"]
            py = aspectpositions["y"]

            #Since all needed properties are computed, Now create the svg entry string for planet
            Planet_SVGstring = f'''  <text y="{py}" x="{px}" fill="{planetcolour}" class="aspect">{symbol}</text>\n'''
            #write the planet to SVG chart
            chartSVG.write(Planet_SVGstring)
    return

def create_chartSVG(chartObj,location,chartSVGfilename):
    # open or create chart file 
    if((location[-1] == '\\') or (location[-1] == '/')):
        chartSVGFullname = f'{location}{chartSVGfilename}.svg'
    elif('/' in location):
        chartSVGFullname = f'{location}/{chartSVGfilename}.svg'
    else:
        chartSVGFullname = f'{location}\{chartSVGfilename}.svg'
    
    chartSVG = open(chartSVGFullname, 'w',  encoding='utf-16')
    

    #Write the content into the file
    #SVG chart open section
    chartSVG.write(f'''<svg id="{chartObj.chartname}_chart_{chartObj.personname}" height="330" width="490" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 490 340" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" charset="utf-16">\n''')
    chartSVG.write('  <style>\n')
    chartSVG.write('    .sign-num { font: bold 20px sans-serif; }\n')
    chartSVG.write('    .planet { font: bold 14px sans-serif; }\n')
    chartSVG.write('    .aspect { font: bold 16px sans-serif; }\n')
    chartSVG.write('  </style>\n')
    chartSVG.write('  <!-- ********** Chart Diagram ********** -->\n')

    #create chart South indian style
    draw_classicSouthChartSkeleton(chartSVG, chartObj.chartcfg)    #Create skeleton
    write_signnumOnChart_ssc(chartSVG, chartObj.chartcfg["sign-colour"],chartObj.ascendantsign)    #Update the sign numbers on chart skeleton
    write_planetsOnChart_ssc(chartSVG, chartObj.planets)    #Update the planets on chart for every house
    if(chartObj.chartcfg["aspect-visibility"] == True):
        write_planetsAspectsOnChart_ssc(chartSVG, chartObj.planets)
    
    #SVG chart End section
    chartSVG.write('\n  Sorry, your browser does not support inline SVG.\n')
    chartSVG.write('</svg>\n')

    #close the file
    chartSVG.close()

    return "Success"

if __name__ == '__main__':
    pos = get_coordniates("Virgo", 5)
    print(pos)




