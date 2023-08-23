import support.constants as c
import support.general as gen
import os


x = "x"
y = "y"
planetPosition_northSquareClassic = [
                                      #Tan Bhav Planets positions
                                      [
                                            {y:"140", x:"185"}, #first planet
                                            {y:"100", x:"195"}, #second planet
                                            {y:"138", x:"225"}, #third planet
                                            {y:"100", x:"235"}, #fourth planet
                                            {y:"60", x:"205"},  #fifth planet
                                            {y:"85", x:"165"},  #sixth planet
                                            {y:"130", x:"145"}, #seventh planet
                                            {y:"122", x:"263"}  #eighth planet
                                      ],
                                      #Dhan Bhav Planets positions
                                      [
                                            {x:"96", y:"56"},
                                            {y:"35", x:"130"},
                                            {y:"32", x:"70"},
                                            {y:"70", x:"123"},  
                                            {y:"70", x:"73"},  
                                            {y:"33", x:"40"},  
                                            {y:"33", x:"160"},  
                                            {y:"36", x:"105"}
                                      ],
                                      #Anuj Bhav Planets positions
                                      [
                                            {x:"40", y:"110"},
                                            {x:"15", y:"145"},
                                            {x:"12", y:"85"},
                                            {x:"45", y:"135"},
                                            {x:"50", y:"90"},
                                            {x:"13", y:"55"},
                                            {x:"13", y:"175"},
                                            {x:"16", y:"120"}
                                      ],
                                      #Maata Bhav Planets positions
                                      [
                                            {x:"120", y:"200"},
                                            {x:"80", y:"210"},
                                            {x:"118", y:"240"},
                                            {x:"80", y:"250"},
                                            {x:"40", y:"220"},
                                            {x:"65", y:"180"},
                                            {x:"110", y:"160"},
                                            {x:"102", y:"278"}
                                      ],
                                      #Santan Bhav Planets positions
                                      [
                                            {x:"40", y:"310"},
                                            {x:"15", y:"345"},
                                            {x:"12", y:"285"},
                                            {x:"50", y:"338"},  
                                            {x:"50", y:"288"},  
                                            {x:"13", y:"255"},  
                                            {x:"13", y:"375"},  
                                            {x:"16", y:"320"}
                                      ],
                                      #Rog Bhav Planets positions
                                      [
                                            {x:"97", y:"360"},                                            
                                            {x:"60", y:"375"},                                            
                                            {x:"128", y:"398"},                                            
                                            {x:"100", y:"385"},                                            
                                            {x:"80", y:"403"},                                            
                                            {x:"40", y:"400"},                                            
                                            {x:"162", y:"402"},
                                            {x:"130", y:"370"}
                                      ],
                                      #Dampathya Bhav Planets positions
                                      [
                                            {y:"275", x:"182"},
                                            {y:"325", x:"195"},
                                            {y:"285", x:"225"},
                                            {y:"325", x:"235"},
                                            {y:"365", x:"205"},
                                            {y:"340", x:"165"},
                                            {y:"295", x:"145"},
                                            {y:"305", x:"260"}
                                      ],
                                      #Aayu Bhav Planets positions
                                      [
                                            {x:"300", y:"360"},                                            
                                            {x:"260", y:"375"},                                            
                                            {x:"328", y:"398"},                                            
                                            {x:"300", y:"385"},                                            
                                            {x:"280", y:"403"},                                            
                                            {x:"240", y:"400"},                                            
                                            {x:"362", y:"402"},
                                            {x:"330", y:"370"}
                                      ],
                                      #Bhagya Bhav Planets positions
                                      [
                                            {x:"360", y:"310"}, 
                                            {x:"350", y:"340"},
                                            {x:"350", y:"285"},
                                            {x:"380", y:"273"},
                                            {x:"380", y:"335"},
                                            {x:"369", y:"360"},
                                            {x:"383", y:"250"},
                                            {x:"385", y:"382"}
                                      ],
                                      #Karma Bhav Planets positions
                                      [
                                            {x:"270", y:"200"},
                                            {x:"320", y:"210"},
                                            {x:"282", y:"240"},
                                            {x:"320", y:"250"},
                                            {x:"360", y:"220"},
                                            {x:"335", y:"180"},
                                            {x:"290", y:"160"},
                                            {x:"298", y:"278"}
                                      ],
                                      #Laab Bhav Planets positions
                                      [
                                            {x:"360", y:"110"}, 
                                            {x:"350", y:"140"},
                                            {x:"350", y:"85"},
                                            {x:"380", y:"73"},
                                            {x:"380", y:"135"},
                                            {x:"369", y:"160"},
                                            {x:"383", y:"50"},
                                            {x:"385", y:"182"}
                                      ],
                                      #Karch Bhav Planets positions
                                      [
                                            {x:"296", y:"56"},
                                            {y:"35", x:"330"},
                                            {y:"32", x:"270"},
                                            {y:"70", x:"323"},                                            
                                            {y:"70", x:"273"},                                            
                                            {y:"33", x:"240"},                                            
                                            {y:"33", x:"360"},                                            
                                            {y:"36", x:"305"}
                                      ]

                                    ]

############################################################################
################# Global Functions #########################################
############################################################################

# Function to get svg coordinates with house and planet number in that house
def get_coordniates(housenum, planetidx):
    # housenum is the house number : 1 for tan bhav, 4 for matrubhav, 6 for rog bhav etc
    # planetidx is index of the planet in that house. If its first planet in that house then its 1 and if its 3rd planet then its 3.
    #return value is a tuple (x,y) containing 2 elements. x-coordinate and y-coordinate
    if (planetidx in range(1,9)):
        x_coordinate = int(planetPosition_northSquareClassic[housenum-1][planetidx-1]["x"])
        y_coordinate = int(planetPosition_northSquareClassic[housenum-1][planetidx-1]["y"])
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

def draw_classicNorthChartSkeleton(chartSVG, chartCfg):
    # Chart drawing section - Skeleton part for template - north-square-classic
    chartSVG.write(f'''  <rect width="410" height="410" x="5" y="5" style="fill:{chartCfg["background-colour"]};stroke-width:3;stroke:{chartCfg["outerbox-colour"]}" />\n''')
    chartSVG.write(f'''  <polygon id ="tanbhav" points="210,10 110,110 210,210 310,110" style="fill:{chartCfg["house-colour"]["tanbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="dhanbhav" points="10,10 210,10 110,110" style="fill:{chartCfg["house-colour"]["dhanbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="anujbhav" points="10,10 10,210 110,110" style="fill:{chartCfg["house-colour"]["anujbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="maatabhav" points="110,110 10,210 110,310 210,210" style="fill:{chartCfg["house-colour"]["maatabhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="santanbhav" points="10,210 110,310 10,410" style="fill:{chartCfg["house-colour"]["santanbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="rogbhav" points="210,410 110,310 10,410" style="fill:{chartCfg["house-colour"]["rogbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="dampathyabhav" points="210,410 110,310 210,210 310,310" style="fill:{chartCfg["house-colour"]["dampathyabhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="aayubhav" points="210,410 310,310 410,410" style="fill:{chartCfg["house-colour"]["aayubhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="bhagyabhav" points="310,310 410,410 410,210" style="fill:{chartCfg["house-colour"]["bhagyabhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="karmabhav" points="310,310 410,210 310,110 210,210" style="fill:{chartCfg["house-colour"]["karmabhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="laabbhav" points="410,210 310,110 410,10" style="fill:{chartCfg["house-colour"]["laabbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    chartSVG.write(f'''  <polygon id ="karchbhav" points="310,110 410,10 210,10" style="fill:{chartCfg["house-colour"]["karchbhav"]};stroke:{chartCfg["line-colour"]};stroke-width:2" />\n''')
    return

def write_signnumOnChart_nsc(chartSVG, signclr, signnumlist):
    chartSVG.write('\n  <!-- ********** Sign Numbers ********** -->\n')
    chartSVG.write(f'''  <text id ="tan" x="193" y="195" fill="{signclr}" class="sign-num">{signnumlist[0]:02}</text>\n''')
    chartSVG.write(f'''  <text id ="dhan" x="97" y="95" fill="{signclr}" class="sign-num">{signnumlist[1]:02}</text>\n''')
    chartSVG.write(f'''  <text id ="anuj" x="70" y="118" fill="{signclr}" class="sign-num">{signnumlist[2]:02}</text>\n''')
    chartSVG.write(f'''  <text id ="maata" x="170" y="218" fill="{signclr}" class="sign-num">{signnumlist[3]:02}</text>\n''')
    chartSVG.write(f'''  <text id ="santaan" x="75" y="316" fill="{signclr}" class="sign-num">{signnumlist[4]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="rog" x="97" y="335" fill="{signclr}" class="sign-num">{signnumlist[5]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="dampathya" x="195" y="240" fill="{signclr}" class="sign-num">{signnumlist[6]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="aayu" x="296" y="337" fill="{signclr}" class="sign-num">{signnumlist[7]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="bhagya" x="320" y="318" fill="{signclr}" class="sign-num">{signnumlist[8]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="karma" x="220" y="218" fill="{signclr}" class="sign-num">{signnumlist[9]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="laab" x="318" y="118" fill="{signclr}" class="sign-num">{signnumlist[10]:02}</text>\n''')  
    chartSVG.write(f'''  <text id ="karch" x="298" y="98" fill="{signclr}" class="sign-num">{signnumlist[11]:02}</text>\n''')
    return

def write_planetsOnChart_nsc(chartSVG, planets):
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

def write_planetsAspectsOnChart_nsc(chartSVG, planets):
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
    chartSVG.write(f'''<svg id="{chartObj.chartname}_chart_{chartObj.personname}" height="500" width="500" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 420 420" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" charset="utf-16">\n''')
    chartSVG.write('  <style>\n')
    chartSVG.write('    .sign-num { font: bold 22px sans-serif; }\n')
    chartSVG.write('    .planet { font: bold 20px sans-serif; }\n')
    chartSVG.write('    .aspect { font: bold 22px sans-serif; }\n')
    chartSVG.write('  </style>\n')
    chartSVG.write('  <!-- ********** Chart Diagram ********** -->\n')

    #create chart North indian style
    draw_classicNorthChartSkeleton(chartSVG, chartObj.chartcfg)    #Create skeleton
    write_signnumOnChart_nsc(chartSVG, chartObj.chartcfg["sign-colour"],chartObj.housesigns)    #Update the sign numbers on chart skeleton
    write_planetsOnChart_nsc(chartSVG, chartObj.planets)    #Update the planets on chart for every house
    if(chartObj.chartcfg["aspect-visibility"] == True):
        write_planetsAspectsOnChart_nsc(chartSVG, chartObj.planets)
    
    #SVG chart End section
    chartSVG.write('\n  Sorry, your browser does not support inline SVG.\n')
    chartSVG.write('</svg>\n')

    #close the file
    chartSVG.close()

    return "Success"

if __name__ == '__main__':
    pos = get_coordniates(c.KARCH, 8)
    print(pos)





