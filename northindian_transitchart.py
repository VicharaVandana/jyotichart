import support.constants as c
import support.general as gen
import os


natalPlanetPosition_northSquareClassic = [
    # Tan Bhav Planets positions
    [
        {"y": "240", "x": "285"},
        {"y": "200", "x": "295"},
        {"y": "238", "x": "325"},
        {"y": "200", "x": "335"},
        {"y": "160", "x": "305"},
        {"y": "185", "x": "265"},
        {"y": "230", "x": "245"},
        {"y": "222", "x": "363"}
    ],
    # Dhan Bhav Planets positions
    [
        {"x": "196", "y": "156"},
        {"y": "135", "x": "230"},
        {"y": "132", "x": "170"},
        {"y": "170", "x": "223"},
        {"y": "170", "x": "173"},
        {"y": "133", "x": "140"},
        {"y": "133", "x": "260"},
        {"y": "136", "x": "205"}
    ],
    # Anuj Bhav Planets positions
    [
        {"x": "140", "y": "210"},
        {"x": "115", "y": "245"},
        {"x": "112", "y": "185"},
        {"x": "145", "y": "235"},
        {"x": "150", "y": "190"},
        {"x": "113", "y": "155"},
        {"x": "113", "y": "275"},
        {"x": "116", "y": "220"}
    ],
    # Maata Bhav Planets positions
    [
        {"x": "220", "y": "300"},
        {"x": "180", "y": "310"},
        {"x": "218", "y": "340"},
        {"x": "180", "y": "350"},
        {"x": "140", "y": "320"},
        {"x": "165", "y": "280"},
        {"x": "210", "y": "260"},
        {"x": "202", "y": "378"}
    ],
    # Santan Bhav Planets positions
    [
        {"x": "140", "y": "410"},
        {"x": "115", "y": "445"},
        {"x": "112", "y": "385"},
        {"x": "150", "y": "438"},
        {"x": "150", "y": "388"},
        {"x": "113", "y": "355"},
        {"x": "113", "y": "475"},
        {"x": "116", "y": "420"}
    ],
    # Rog Bhav Planets positions
    [
        {"x": "197", "y": "460"},
        {"x": "160", "y": "475"},
        {"x": "228", "y": "498"},
        {"x": "200", "y": "485"},
        {"x": "180", "y": "503"},
        {"x": "140", "y": "500"},
        {"x": "262", "y": "502"},
        {"x": "230", "y": "470"}
    ],
    # Dampathya Bhav Planets positions
    [
        {"y": "375", "x": "282"},
        {"y": "425", "x": "295"},
        {"y": "385", "x": "325"},
        {"y": "425", "x": "335"},
        {"y": "465", "x": "305"},
        {"y": "440", "x": "265"},
        {"y": "395", "x": "245"},
        {"y": "405", "x": "360"}
    ],
    # Aayu Bhav Planets positions
    [
        {"x": "400", "y": "460"},
        {"x": "360", "y": "475"},
        {"x": "428", "y": "498"},
        {"x": "400", "y": "485"},
        {"x": "380", "y": "503"},
        {"x": "340", "y": "500"},
        {"x": "462", "y": "502"},
        {"x": "430", "y": "470"}
    ],
    # Bhagya Bhav Planets positions
    [
        {"x": "460", "y": "410"},
        {"x": "450", "y": "440"},
        {"x": "450", "y": "385"},
        {"x": "480", "y": "373"},
        {"x": "480", "y": "435"},
        {"x": "469", "y": "460"},
        {"x": "483", "y": "350"},
        {"x": "485", "y": "482"}
    ],
    # Karma Bhav Planets positions
    [
        {"x": "370", "y": "300"},
        {"x": "420", "y": "310"},
        {"x": "382", "y": "340"},
        {"x": "420", "y": "350"},
        {"x": "460", "y": "320"},
        {"x": "435", "y": "280"},
        {"x": "390", "y": "260"},
        {"x": "398", "y": "378"}
    ],
    # Laab Bhav Planets positions
    [
        {"x": "460", "y": "210"},
        {"x": "450", "y": "240"},
        {"x": "450", "y": "185"},
        {"x": "480", "y": "173"},
        {"x": "480", "y": "235"},
        {"x": "469", "y": "260"},
        {"x": "483", "y": "150"},
        {"x": "485", "y": "282"}
    ],
    # Karch Bhav Planets positions
    [
        {"x": "396", "y": "156"},
        {"y": "135", "x": "430"},
        {"y": "132", "x": "370"},
        {"y": "170", "x": "423"},
        {"y": "170", "x": "373"},
        {"y": "133", "x": "340"},
        {"y": "133", "x": "460"},
        {"y": "136", "x": "405"}
    ]
]


transitPlanetPosition_northSquareClassic = [
    # Tan Bhav Transit Planets Positions
    [{"x": "282", "y": "50"}, {"x": "325", "y": "70"}, {"x": "230", "y": "35"}, {"x": "250", "y": "80"},
     {"x": "332", "y": "30"}, {"x": "300", "y": "95"}, {"x": "350", "y": "100"}, {"x": "365", "y": "70"}],

    # Dhan Bhav Transit Planets Positions
    [{"x": "125", "y": "45"}, {"x": "160", "y": "70"}, {"x": "72", "y": "32"}, {"x": "120", "y": "95"},
     {"x": "175", "y": "32"}, {"x": "85", "y": "65"}, {"x": "178", "y": "95"}, {"x": "32", "y": "28"}],

    # Anuj Bhav Transit Planets Positions
    [{"x": "25", "y": "145"}, {"x": "50", "y": "180"}, {"x": "12", "y": "92"}, {"x": "75", "y": "140"},
     {"x": "15", "y": "210"}, {"x": "50", "y": "105"}, {"x": "75", "y": "222"}, {"x": "8", "y": "52"}],

    # Maata Bhav Transit Planets Positions
    [{"x": "37", "y": "295"}, {"x": "52", "y": "330"}, {"x": "30", "y": "360"}, {"x": "15", "y": "260"},
     {"x": "13", "y": "320"}, {"x": "75", "y": "370"}, {"x": "70", "y": "260"}, {"x": "80", "y": "300"}],

    # Santaan Bhav Transit Planets Positions
    [{"x": "25", "y": "485"}, {"x": "50", "y": "450"}, {"x": "12", "y": "538"}, {"x": "75", "y": "490"},
     {"x": "15", "y": "420"}, {"x": "50", "y": "525"}, {"x": "75", "y": "412"}, {"x": "8", "y": "578"}],

    # Rog Bhav Transit Planets Positions
    [{"x": "125", "y": "585"}, {"x": "160", "y": "560"}, {"x": "72", "y": "598"}, {"x": "120", "y": "535"},
     {"x": "175", "y": "598"}, {"x": "85", "y": "565"}, {"x": "178", "y": "535"}, {"x": "32", "y": "602"}],

    # Dhampathya Bhav Transit Planets Positions
    [{"x": "282", "y": "580"}, {"x": "325", "y": "560"}, {"x": "230", "y": "595"}, {"x": "250", "y": "550"},
     {"x": "332", "y": "600"}, {"x": "300", "y": "535"}, {"x": "350", "y": "530"}, {"x": "365", "y": "560"}],

    # Aayu Bhav Transit Planets Positions
    [{"x": "465", "y": "587"}, {"x": "440", "y": "562"}, {"x": "518", "y": "600"}, {"x": "470", "y": "537"},
     {"x": "415", "y": "600"}, {"x": "505", "y": "567"}, {"x": "412", "y": "537"}, {"x": "558", "y": "604"}],

    # Bhagya Bhav Transit Planets Positions
    [{"x": "568", "y": "485"}, {"x": "543", "y": "450"}, {"x": "581", "y": "538"}, {"x": "518", "y": "490"},
     {"x": "578", "y": "425"}, {"x": "543", "y": "525"}, {"x": "518", "y": "414"}, {"x": "585", "y": "578"}],

    # Karma Bhav Transit Planets Positions
    [{"x": "563", "y": "295"}, {"x": "548", "y": "330"}, {"x": "570", "y": "365"}, {"x": "580", "y": "260"},
     {"x": "583", "y": "323"}, {"x": "525", "y": "370"}, {"x": "530", "y": "260"}, {"x": "520", "y": "300"}],

    # Laab Bhav Transit Planets Positions
    [{"x": "568", "y": "145"}, {"x": "543", "y": "180"}, {"x": "581", "y": "92"}, {"x": "518", "y": "140"},
     {"x": "578", "y": "210"}, {"x": "543", "y": "105"}, {"x": "518", "y": "222"}, {"x": "585", "y": "52"}],

    # Karch Bhav Transit Planets Positions
    [{"x": "465", "y": "45"}, {"x": "440", "y": "70"}, {"x": "518", "y": "32"}, {"x": "470", "y": "95"},
     {"x": "415", "y": "32"}, {"x": "505", "y": "65"}, {"x": "412", "y": "95"}, {"x": "558", "y": "28"}]
]


############################################################################
################# Global Functions #########################################
############################################################################

# Function to get svg coordinates with house and planet number in that house for natal part in transit chart
def get_natalcoordniates(housenum, planetidx):
    # housenum is the house number : 1 for tan bhav, 4 for matrubhav, 6 for rog bhav etc
    # planetidx is index of the planet in that house. If its first planet in that house then its 1 and if its 3rd planet then its 3.
    #return value is a tuple (x,y) containing 2 elements. x-coordinate and y-coordinate
    if (planetidx in range(1,9)):
        x_coordinate = int(natalPlanetPosition_northSquareClassic[housenum-1][planetidx-1]["x"])
        y_coordinate = int(natalPlanetPosition_northSquareClassic[housenum-1][planetidx-1]["y"])
        return((x_coordinate,y_coordinate))
    else: 
        print(f"INPUTERROR: planetidx must be in the range 1 to 8 but given value is {planetidx}.")
        return((0,0))
    
# Function to get svg coordinates with house and planet number in that house for transit part in transit chart
def get_transitcoordniates(housenum, planetidx):
    # housenum is the house number : 1 for tan bhav, 4 for matrubhav, 6 for rog bhav etc
    # planetidx is index of the planet in that house. If its first planet in that house then its 1 and if its 3rd planet then its 3.
    #return value is a tuple (x,y) containing 2 elements. x-coordinate and y-coordinate
    if (planetidx in range(1,9)):
        x_coordinate = int(transitPlanetPosition_northSquareClassic[housenum-1][planetidx-1]["x"])
        y_coordinate = int(transitPlanetPosition_northSquareClassic[housenum-1][planetidx-1]["y"])
        return((x_coordinate,y_coordinate))
    else: 
        print(f"INPUTERROR: planetidx must be in the range 1 to 8 but given value is {planetidx}.")
        return((0,0))

def reset_chartcfg():
    chartcfg = {
                    "background-colour" : "black",
                    "outerbox-colour" : "red",
                    "line-colour" : "yellow",
                    "sign-colour" : "pink",
                    "house-colour" : {
                                        "tanbhav"      : "black",
                                        "dhanbhav"     : "black",
                                        "anujbhav"     : "black",
                                        "maatabhav"    : "black",
                                        "santanbhav"   : "black",
                                        "rogbhav"      : "black",
                                        "dampathyabhav": "black",
                                        "aayubhav"     : "black",
                                        "bhagyabhav"   : "black",
                                        "karmabhav"    : "black",
                                        "laabbhav"     : "black",
                                        "karchbhav"    : "black"
                                    },
                    "aspect-visibility"  : True
                }
    return(chartcfg)

def draw_classicNorthTransitChartSkeleton(chartSVG, chartCfg):
    # Chart drawing section - Skeleton part for template - north-square-classic for Transit chart
    chartSVG.write(f'''  <rect width="610" height="610" x="5" y="5" style="fill:{chartCfg["background-colour"]};stroke-width:2;stroke:{chartCfg["outerbox-colour"]}" />\n''')

    chartSVG.write(f'''  <polygon id ="tanbhav" points="310,110 210,210 310,310 410,210" style="fill:{chartCfg["house-colour"]["tanbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="dhanbhav" points="110,110 310,110 210,210" style="fill:{chartCfg["house-colour"]["dhanbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="anujbhav" points="110,110 110,310 210,210" style="fill:{chartCfg["house-colour"]["anujbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="maatabhav" points="210,210 110,310 210,410 310,310" style="fill:{chartCfg["house-colour"]["maatabhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="santanbhav" points="110,310 210,410 110,510" style="fill:{chartCfg["house-colour"]["santanbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="rogbhav" points="310,510 210,410 110,510" style="fill:{chartCfg["house-colour"]["rogbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="dampathyabhav" points="310,510 210,410 310,310 410,410" style="fill:{chartCfg["house-colour"]["dampathyabhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="aayubhav" points="310,510 410,410 510,510" style="fill:{chartCfg["house-colour"]["aayubhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="bhagyabhav" points="410,410 510,510 510,310" style="fill:{chartCfg["house-colour"]["bhagyabhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="karmabhav" points="410,410 510,310 410,210 310,310" style="fill:{chartCfg["house-colour"]["karmabhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="laabbhav" points="510,310 410,210 510,110" style="fill:{chartCfg["house-colour"]["laabbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="karchbhav" points="410,210 510,110 310,110" style="fill:{chartCfg["house-colour"]["karchbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')

    # Outer Transit Chart Section (Lines)
    chartSVG.write(f'''  <line x1="220" y1="5" x2="220" y2="108" style="stroke:{chartCfg["line-colour"]};stroke-width:2"/>\n''')
    chartSVG.write(f'''  <line x1="400" y1="5" x2="400" y2="108" style="stroke:{chartCfg["line-colour"]};stroke-width:2"/>\n''')
    chartSVG.write(f'''  <line x1="220" y1="510" x2="220" y2="613" style="stroke:{chartCfg["line-colour"]};stroke-width:2"/>\n''')
    chartSVG.write(f'''  <line x1="400" y1="510" x2="400" y2="613" style="stroke:{chartCfg["line-colour"]};stroke-width:2"/>\n''')
    chartSVG.write(f'''  <line x1="5" y1="230" x2="108" y2="230" style="stroke:{chartCfg["line-colour"]};stroke-width:2"/>\n''')
    chartSVG.write(f'''  <line x1="5" y1="390" x2="108" y2="390" style="stroke:{chartCfg["line-colour"]};stroke-width:2"/>\n''')
    chartSVG.write(f'''  <line x1="510" y1="230" x2="613" y2="230" style="stroke:{chartCfg["line-colour"]};stroke-width:2"/>\n''')
    chartSVG.write(f'''  <line x1="510" y1="390" x2="613" y2="390" style="stroke:{chartCfg["line-colour"]};stroke-width:2"/>\n''')
    chartSVG.write(f'''  <line x1="8" y1="8" x2="108" y2="108" style="stroke:{chartCfg["line-colour"]};stroke-width:2"/>\n''')
    chartSVG.write(f'''  <line x1="8" y1="613" x2="108" y2="512" style="stroke:{chartCfg["line-colour"]};stroke-width:2"/>\n''')
    chartSVG.write(f'''  <line x1="512" y1="512" x2="615" y2="615" style="stroke:{chartCfg["line-colour"]};stroke-width:2"/>\n''')
    chartSVG.write(f'''  <line x1="510" y1="108" x2="615" y2="8" style="stroke:{chartCfg["line-colour"]};stroke-width:2"/>\n''')

    return


def write_signnumOnChart_ntsc(chartSVG, signclr, signnumlist):
    chartSVG.write('\n  <!-- ********** Sign Numbers ********** -->\n')
    chartSVG.write(f'''  <text id ="tan" x="293" y="295" fill="{signclr}" class="sign-num">{signnumlist[0]:02}</text>\n''')
    chartSVG.write(f'''  <text id ="dhan" x="197" y="195" fill="{signclr}" class="sign-num">{signnumlist[1]:02}</text>\n''')
    chartSVG.write(f'''  <text id ="anuj" x="170" y="218" fill="{signclr}" class="sign-num">{signnumlist[2]:02}</text>\n''')
    chartSVG.write(f'''  <text id ="maata" x="270" y="318" fill="{signclr}" class="sign-num">{signnumlist[3]:02}</text>\n''')
    chartSVG.write(f'''  <text id ="santaan" x="175" y="416" fill="{signclr}" class="sign-num">{signnumlist[4]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="rog" x="197" y="435" fill="{signclr}" class="sign-num">{signnumlist[5]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="dampathya" x="295" y="340" fill="{signclr}" class="sign-num">{signnumlist[6]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="aayu" x="396" y="437" fill="{signclr}" class="sign-num">{signnumlist[7]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="bhagya" x="420" y="418" fill="{signclr}" class="sign-num">{signnumlist[8]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="karma" x="320" y="318" fill="{signclr}" class="sign-num">{signnumlist[9]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="laab" x="418" y="218" fill="{signclr}" class="sign-num">{signnumlist[10]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="karch" x="398" y="198" fill="{signclr}" class="sign-num">{signnumlist[11]:02}</text>\n''')
    return

def write_natalplanetsOnChart_ntsc(chartSVG, planets):
    chartSVG.write('\n  <!-- ********** Natal Planets ********** -->\n')
    
    for planetname in planets:
        chartSVG.write(f'\n  <!-- ********** {planetname} ********** -->\n')
        symbol = planets[planetname]["symbol"]
        retro = planets[planetname]["retro"]
        planetcolour = planets[planetname]["colour"]
        #Get planet position co-ordinates x and y on chart svg
        px = planets[planetname]["pos"]["x"] + 100
        py = planets[planetname]["pos"]["y"] + 100

        #Since all needed properties are computed, Now create the svg entry string for planet
        if(retro == True):
            Planet_SVGstring = f'''  <text y="{py}" x="{px}" fill="{planetcolour}" text-decoration="underline" class="natal-planet" id="natal-{planetname}">({symbol})</text>\n'''
        else:
            Planet_SVGstring = f'''  <text y="{py}" x="{px}" fill="{planetcolour}" class="natal-planet" id="natal-{planetname}">{symbol}</text>\n'''
        #write the planet to SVG chart
        chartSVG.write(Planet_SVGstring)
    return

def write_transitplanetsOnChart_ntsc(chartSVG, planets):
    chartSVG.write('\n  <!-- ********** Transit Planets ********** -->\n')
    
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
            Planet_SVGstring = f'''  <text y="{py}" x="{px}" fill="{planetcolour}" text-decoration="underline" class="transit-planet" id="transit-{planetname}">({symbol})</text>\n'''
        else:
            Planet_SVGstring = f'''  <text y="{py}" x="{px}" fill="{planetcolour}" class="transit-planet" id="transit-{planetname}">{symbol}</text>\n'''
        #write the planet to SVG chart
        chartSVG.write(Planet_SVGstring)
    return

def write_natalplanetsAspectsOnChart_ntsc(chartSVG, planets):
    chartSVG.write('\n  <!-- ********** Natal Planets Aspects ********** -->\n')
    
    for planetname in planets:
        chartSVG.write(f'\n  <!-- ********** {planetname} Aspect ********** -->\n')
        symbol = planets[planetname]["aspect_symbol"]
        planetcolour = planets[planetname]["colour"]
        for aspectpositions in planets[planetname]["aspectpos"]:
            #Get planet position co-ordinates x and y on chart svg
            px = aspectpositions["x"] + 100
            py = aspectpositions["y"] + 100

            #Since all needed properties are computed, Now create the svg entry string for planet
            Planet_SVGstring = f'''  <text y="{py}" x="{px}" fill="{planetcolour}" class="natal-aspect" id="natal-{planetname}-aspect">{symbol}</text>\n'''
            #write the planet to SVG chart
            chartSVG.write(Planet_SVGstring)
    return

def write_transitplanetsAspectsOnChart_ntsc(chartSVG, planets):
    chartSVG.write('\n  <!-- ********** Transit Planets Aspects ********** -->\n')
    
    for planetname in planets:
        chartSVG.write(f'\n  <!-- ********** {planetname} Aspect ********** -->\n')
        symbol = planets[planetname]["aspect_symbol"]
        planetcolour = planets[planetname]["colour"]
        for aspectpositions in planets[planetname]["aspectpos"]:
            #Get planet position co-ordinates x and y on chart svg
            px = aspectpositions["x"]
            py = aspectpositions["y"]

            #Since all needed properties are computed, Now create the svg entry string for planet
            Planet_SVGstring = f'''  <text y="{py}" x="{px}" fill="{planetcolour}" class="transit-aspect" id="transit-{planetname}-aspect">{symbol}</text>\n'''
            #write the planet to SVG chart
            chartSVG.write(Planet_SVGstring)
    return

def create_chartSVG(chartObj,location,chartSVGfilename, parentChartObj):
    ''' Creates SVG image of astrology chart as per the chart draw configuration
        with data in division. The divisional chart is mentioned by division and 
        hence named accordingly'''
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
    chartSVG.write(f'''<svg id="{chartObj.chartname}_chart_{chartObj.personname}" height="610" width="610" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 616 616" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" charset="utf-16">\n''')
    chartSVG.write('  <style>\n')
    chartSVG.write('    .sign-num { font: bold 22px sans-serif; }\n')
    chartSVG.write('    .planet { font: bold 20px sans-serif; }\n')
    chartSVG.write('    .aspect { font: bold 22px sans-serif; }\n')
    chartSVG.write('  </style>\n')
    chartSVG.write('  <!-- ********** Chart Diagram ********** -->\n')

    #create chart North indian style
    draw_classicNorthTransitChartSkeleton(chartSVG, chartObj.chartcfg)    #Create skeleton
    write_signnumOnChart_ntsc(chartSVG, chartObj.chartcfg["sign-colour"],chartObj.housesigns)    #Update the sign numbers on chart skeleton
    
    write_natalplanetsOnChart_ntsc(chartSVG, parentChartObj.planets)    #Update the planets on chart for every house on natal section
    if(parentChartObj.chartcfg["aspect-visibility"] == True):
        write_natalplanetsAspectsOnChart_ntsc(chartSVG, parentChartObj.planets)
    

    write_transitplanetsOnChart_ntsc(chartSVG, chartObj.planets)    #Update the planets on chart for every house on transit section
    if(chartObj.chartcfg["aspect-visibility"] == True):
        write_transitplanetsAspectsOnChart_ntsc(chartSVG, chartObj.planets)
    
    #SVG chart End section
    chartSVG.write('\n  Sorry, your browser does not support inline SVG.\n')
    chartSVG.write('</svg>\n')

    #close the file
    chartSVG.close()

    return "Success"

if __name__ == '__main__':
    pos = get_natalcoordniates(c.KARCH, 8)
    print(pos)







