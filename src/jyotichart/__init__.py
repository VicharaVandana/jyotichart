import os

####################################################################
################### Constants ######################################
####################################################################
SUN = "Sun"
MOON = "Moon"
MARS = "Mars"
MERCURY = "Mercury"
JUPITER = "Jupiter"
VENUS = "Venus"
SATURN = "Saturn"
RAHU = "Rahu"
KETU = "Ketu"

#Housenumber related constants
TAN = 1
DHAN = 2
ANUJ = 3
MAATA = 4
SANTAAN = 5
ROG = 6
YUVATI = 7
AAYU = 8
BHAGYA = 9
KARMA = 10
LAABA = 11
KARCH = 12

signs = [ "Aries",       "Taurus",    "Gemini",   "Cancer",
          "Leo",         "Virgo",     "Libra",    "Scorpio",
          "Saggitarius", "Capricorn", "Aquarius", "Pisces"
        ]

signnum = lambda signstr: signs.index(signstr) + 1

planet_aspects = {
    "Sun":[7],
    "Moon":[7],
    "Mars":[4,7,8],
    "Mercury":[7],
    "Jupiter":[5,7,9],
    "Venus":[7],
    "Saturn":[3,7,10],
    "Rahu":[5,7,9],
    "Ketu":[5,7,9]
}

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
                        

base_coordinates_sc = [{"x":155, "y":40},   #planet 1
                    {"x":185, "y":48},   #planet 2
                    {"x":170, "y":70},   #planet 3
                    {"x":135, "y":58},   #planet 4
                    {"x":215, "y":60},   #planet 5
                    {"x":145, "y":83},   #planet 6
                    {"x":210, "y":35},   #planet 7
                    {"x":130, "y":32},   #planet 8
                    {"x":180, "y":30}    #planet 9
                    ]

################################### NORTH CHART ###################################
class NorthChart:
    def __init__(self, chartname, personname, IsFullChart = True):
        self.chartname = chartname
        self.personname = personname
        self.chartcfg = reset_chartcfg_nc()
        self.ascendantsign = "NotSet"
        self.fullchart = IsFullChart
        return
    
    def __str__(self):
        return f"{self.chartname} chart object of {self.personname}."
    
    def updatechartcfg(self, aspect=True, clr_background = 'black', clr_outbox = 'red', clr_line = 'yellow', clr_sign = 'pink', 
    clr_houses = ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black']):
        self.chartcfg['aspect-visibility'] = aspect
        self.chartcfg['background-colour'] = clr_background
        self.chartcfg['outerbox-colour'] = clr_outbox
        self.chartcfg['line-colour'] = clr_line
        self.chartcfg['sign-colour'] = clr_sign
        self.chartcfg['house-colour']['tanbhav'] = clr_houses[0]
        self.chartcfg['house-colour']['dhanbhav'] = clr_houses[1]
        self.chartcfg['house-colour']['anujbhav'] = clr_houses[2]
        self.chartcfg['house-colour']['maatabhav'] = clr_houses[3]
        self.chartcfg['house-colour']['santanbhav'] = clr_houses[4]
        self.chartcfg['house-colour']['rogbhav'] = clr_houses[5]
        self.chartcfg['house-colour']['dampathyabhav'] = clr_houses[6]
        self.chartcfg['house-colour']['aayubhav'] = clr_houses[7]
        self.chartcfg['house-colour']['bhagyabhav'] = clr_houses[8]
        self.chartcfg['house-colour']['karmabhav'] = clr_houses[9]
        self.chartcfg['house-colour']['laabbhav'] = clr_houses[10]
        self.chartcfg['house-colour']['karchbhav'] = clr_houses[11]
        return

    def set_ascendantsign(self,sign):
        if sign not in signs:
            return(f'''Input Error: The given input sign {sign} is not a valid astrological sign.''')
        self.ascendantsign = sign
        ascendantsignnum = signnum(sign)
        self.housesigns = []
        for hno in range(1,13):
            self.housesigns.append(compute_nthsignnum(ascendantsignnum,hno)) 
        return("Success")
     
    planets = {
        SUN:{"symbol":"", "aspect_symbol":"☉", "retro":False, "house_num":0, "colour":"black", "pos": {"x":0, "y":0},"aspectpos":[],"isUpdated":False},
        MOON:{"symbol":"", "aspect_symbol":"☾", "retro":False, "house_num":0, "colour":"black", "pos": {"x":0, "y":0},"aspectpos":[],"isUpdated":False},
        MARS:{"symbol":"", "aspect_symbol":"♂", "retro":False, "house_num":0, "colour":"black", "pos": {"x":0, "y":0},"aspectpos":[],"isUpdated":False},
        MERCURY:{"symbol":"", "aspect_symbol":"☿", "retro":False, "house_num":0, "colour":"black", "pos": {"x":0, "y":0},"aspectpos":[],"isUpdated":False},
        JUPITER:{"symbol":"", "aspect_symbol":"♃", "retro":False, "house_num":0, "colour":"black", "pos": {"x":0, "y":0},"aspectpos":[],"isUpdated":False},
        VENUS:{"symbol":"", "aspect_symbol":"♀", "retro":False, "house_num":0, "colour":"black", "pos": {"x":0, "y":0},"aspectpos":[],"isUpdated":False},
        SATURN:{"symbol":"", "aspect_symbol":"♄", "retro":False, "house_num":0, "colour":"black", "pos": {"x":0, "y":0},"aspectpos":[],"isUpdated":False},
        RAHU:{"symbol":"", "aspect_symbol":"☊", "retro":True, "house_num":0, "colour":"black", "pos": {"x":0, "y":0},"aspectpos":[],"isUpdated":False},
        KETU:{"symbol":"", "aspect_symbol":"☋", "retro":True, "house_num":0, "colour":"black", "pos": {"x":0, "y":0},"aspectpos":[],"isUpdated":False}
    }
    
    
    planetindex = [1,1,1,1,1,1,1,1,1,1,1,1]
    def add_planet(self,planet,symbol,housenum,retrograde = False,aspectsymbol="Default",colour='white'):
        #Validating input parameters
        if planet not in self.planets:
            return(f'''Input Error: The given planet {planet} is invalid.''')
        if (isinstance(symbol, str) == False):
            return(f'''Input Error: The given symbol {symbol} is not a string.''')
        if (isinstance(aspectsymbol, str) == False):
            return(f'''Input Error: The given aspectsymbol {aspectsymbol} is not a string.''')
        if (housenum not in range(1,13)):
            return(f'''Input Error: The given housenum {housenum} is not valid. it must be a integer value from 1 to 12.''')
        if(self.planets[planet]["isUpdated"] == True):
            return(f'''The planet {planet} is already added. you can delete planet and then add again.''')

        if((planet == RAHU) or (planet == KETU)):
            retrograde = True
        elif((planet == SUN) or (planet == MOON)):
            retrograde = False
        else:
            pass

        #initially make updation status as false. then update and then make it true.
        self.planets[planet]["isUpdated"] = False
        self.planets[planet]["symbol"] = symbol
        self.planets[planet]["house_num"] = housenum
        self.planets[planet]["colour"] = colour
        self.planets[planet]["retro"] = retrograde
        pos = get_coordniates_nc(housenum,self.planetindex[housenum-1])
        if(pos == (0,0)):
            return(f'''Overflow Error: The given planet overflows the house. no position available in house diagram for planet {planet}.''')
        self.planetindex[housenum-1] = self.planetindex[housenum-1] + 1
        self.planets[planet]["pos"]["x"] = pos[0]
        self.planets[planet]["pos"]["y"] = pos[1]
        if(aspectsymbol != "Default"):
            self.planets[planet]["aspect_symbol"] = aspectsymbol
        #Adding aspects of the planet
        for aspect in planet_aspects[planet]:
            aspecthousenum = compute_nthsignnum(housenum,aspect)
            asp_pos = get_coordniates_nc(aspecthousenum,self.planetindex[aspecthousenum-1])
            if(asp_pos == (0,0)):
                return(f'''Overflow Error: The given planet aspect {planet} - {aspect} overflows the house. no position available in house diagram for planet.''')
            self.planetindex[aspecthousenum-1] = self.planetindex[aspecthousenum-1] + 1
            aspectpos = {"x":0, "y":0}
            aspectpos["x"] = asp_pos[0]
            aspectpos["y"] = asp_pos[1]
            self.planets[planet]["aspectpos"].append(aspectpos)
            
        self.planets[planet]["isUpdated"] = True

        return("Success")

    def delete_planet(self,planet):
        #Validating input parameters
        if planet not in self.planets:
            return(f'''Input Error: The given planet {planet} is invalid.''')
        if(self.planets[planet]["isUpdated"] == False):
            return(f'''The planet {planet} is not added to be deleted.''')
        housenum = self.planets[planet]["house_num"]
        self.planetindex[housenum-1] = self.planetindex[housenum-1] - 1

        #removing aspects of the planet
        for aspect in planet_aspects[planet]:
            aspecthousenum = compute_nthsignnum(housenum,aspect)
            self.planetindex[aspecthousenum-1] = self.planetindex[aspecthousenum-1] - 1
        self.planets[planet]["aspectpos"] = []

        #Update the aspect symbol back to default
        if (planet == SUN):
            self.planets[SUN]["aspect_symbol"] = "☉"
        elif (planet == MOON):
            self.planets[MOON]["aspect_symbol"] = "☾"
        elif (planet == MARS):
            self.planets[MARS]["aspect_symbol"] = "♂"
        elif (planet == MERCURY):
            self.planets[MERCURY]["aspect_symbol"] = "☿"
        elif (planet == JUPITER):
            self.planets[JUPITER]["aspect_symbol"] = "♃"
        elif (planet == VENUS):
            self.planets[VENUS]["aspect_symbol"] = "♀"
        elif (planet == SATURN):
            self.planets[SATURN]["aspect_symbol"] = "♄"
        elif (planet == RAHU):
            self.planets[RAHU]["aspect_symbol"] = "☊"
        elif (planet == KETU):
            self.planets[KETU]["aspect_symbol"] = "☋"
        else:
            pass

        self.planets[planet]["isUpdated"] = False
        return("Success")
    
    def __isObjectDrawReady(self):
        #check if ascendant sign updated
        if (self.ascendantsign == "NotSet"):
            print("Error : Chart is not ready to be drawn as ascendant sign is not set yet")
            return False
        if (self.fullchart == True):
            for planet in self.planets:
                if(self.planets[planet]["isUpdated"] == False):
                    print(f"Error : Chart is not ready to be drawn as planet {planet} is not added yet")
                    return False
        return True
    
    def draw(self,location,filename,format="svg"):
        #Validating input parameters
        if(os.path.isdir(location) == False):
            return(f'''Input Error: The given location {location} is not valid location on this machine.''')
        if (isinstance(filename, str) == False):
            return(f'''Input Error: The given filename {filename} is not a string.''')
        if (format not in ["svg"]):
            return(f'''Input Error: The given format {format} is not supported. please choose from{["svg"]}.''')
        #check if the chart is ready to be drawn
        if(self.__isObjectDrawReady() == False):
            return(f'''The chart is not ready to be drawn yet as all the needed inputs are not provided!!!''')

        svgstatus = create_chartSVG_nc(self,location,filename)

        return(svgstatus)

################################### SOUTH CHART ###################################
class SouthChart:
    def __init__(self, chartname, personname, IsFullChart = True):
        self.chartname = chartname
        self.personname = personname
        self.chartcfg = reset_chartcfg_sc()
        self.ascendantsign = "NotSet"
        self.fullchart = IsFullChart
        return
    
    def __str__(self):
        return f"{self.chartname} chart object of {self.personname}."

    def updatechartcfg(self, aspect=True, clr_background = 'black', clr_outbox = 'red', clr_inbox = 'red', clr_line = 'yellow', clr_Asc = 'pink', 
    clr_houses = ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black']):
        self.chartcfg['aspect-visibility'] = aspect
        self.chartcfg['background-colour'] = clr_background
        self.chartcfg['outerbox-colour'] = clr_outbox
        self.chartcfg['innerbox-colour'] = clr_inbox
        self.chartcfg['line-colour'] = clr_line
        self.chartcfg['sign-colour'] = clr_Asc
        self.chartcfg['house-colour']['aries'] = clr_houses[0]
        self.chartcfg['house-colour']['taurus'] = clr_houses[1]
        self.chartcfg['house-colour']['gemini'] = clr_houses[2]
        self.chartcfg['house-colour']['cancer'] = clr_houses[3]
        self.chartcfg['house-colour']['leo'] = clr_houses[4]
        self.chartcfg['house-colour']['virgo'] = clr_houses[5]
        self.chartcfg['house-colour']['libra'] = clr_houses[6]
        self.chartcfg['house-colour']['scorpio'] = clr_houses[7]
        self.chartcfg['house-colour']['sagittarius'] = clr_houses[8]
        self.chartcfg['house-colour']['capricorn'] = clr_houses[9]
        self.chartcfg['house-colour']['aquarius'] = clr_houses[10]
        self.chartcfg['house-colour']['pisces'] = clr_houses[11]
        return

    def set_ascendantsign(self,sign):
        if sign not in signs:
            return(f'''Input Error: The given input sign {sign} is not a valid astrological sign.''')
        self.ascendantsign = sign 
        return("Success")

    planets = {
        SUN:{"symbol":"", "aspect_symbol":"☉", "retro":False, "house_num":0, "colour":"black", "pos": {"x":0, "y":0},"aspectpos":[],"isUpdated":False},
        MOON:{"symbol":"", "aspect_symbol":"☾", "retro":False, "house_num":0, "colour":"black", "pos": {"x":0, "y":0},"aspectpos":[],"isUpdated":False},
        MARS:{"symbol":"", "aspect_symbol":"♂", "retro":False, "house_num":0, "colour":"black", "pos": {"x":0, "y":0},"aspectpos":[],"isUpdated":False},
        MERCURY:{"symbol":"", "aspect_symbol":"☿", "retro":False, "house_num":0, "colour":"black", "pos": {"x":0, "y":0},"aspectpos":[],"isUpdated":False},
        JUPITER:{"symbol":"", "aspect_symbol":"♃", "retro":False, "house_num":0, "colour":"black", "pos": {"x":0, "y":0},"aspectpos":[],"isUpdated":False},
        VENUS:{"symbol":"", "aspect_symbol":"♀", "retro":False, "house_num":0, "colour":"black", "pos": {"x":0, "y":0},"aspectpos":[],"isUpdated":False},
        SATURN:{"symbol":"", "aspect_symbol":"♄", "retro":False, "house_num":0, "colour":"black", "pos": {"x":0, "y":0},"aspectpos":[],"isUpdated":False},
        RAHU:{"symbol":"", "aspect_symbol":"☊", "retro":True, "house_num":0, "colour":"black", "pos": {"x":0, "y":0},"aspectpos":[],"isUpdated":False},
        KETU:{"symbol":"", "aspect_symbol":"☋", "retro":True, "house_num":0, "colour":"black", "pos": {"x":0, "y":0},"aspectpos":[],"isUpdated":False}
    }    
    
    planetindex = [1,1,1,1,1,1,1,1,1,1,1,1]
    def add_planet(self,planet,symbol,housenum,retrograde = False,aspectsymbol="Default",colour='white'):
        if (self.ascendantsign == "NotSet"):
            return(f'''Invocation Order Error: The plannet cannot be added before setting the ascendant sign.''')
        #Validating input parameters
        if planet not in self.planets:
            return(f'''Input Error: The given planet {planet} is invalid.''')
        if (isinstance(symbol, str) == False):
            return(f'''Input Error: The given symbol {symbol} is not a string.''')
        if (isinstance(aspectsymbol, str) == False):
            return(f'''Input Error: The given aspectsymbol {aspectsymbol} is not a string.''')
        if (housenum not in range(1,13)):
            return(f'''Input Error: The given housenum {housenum} is not valid. it must be a integer value from 1 to 12.''')
        if(self.planets[planet]["isUpdated"] == True):
            return(f'''The planet {planet} is already added. you can delete planet and then add again.''')

        if((planet == RAHU) or (planet == KETU)):
            retrograde = True
        elif((planet == SUN) or (planet == MOON)):
            retrograde = False
        else:
            pass

        #initially make updation status as false. then update and then make it true.
        self.planets[planet]["isUpdated"] = False
        self.planets[planet]["symbol"] = symbol
        self.planets[planet]["house_num"] = housenum
        self.planets[planet]["colour"] = colour
        self.planets[planet]["retro"] = retrograde
        sign = get_signofsign(housenum, self.ascendantsign)
        pos = get_coordniates_sc(sign,self.planetindex[housenum-1])
        if(pos == (0,0)):
            return(f'''Overflow Error: The given planet overflows the house. no position available in house diagram for planet {planet}.''')
        self.planetindex[housenum-1] = self.planetindex[housenum-1] + 1
        self.planets[planet]["pos"]["x"] = pos[0]
        self.planets[planet]["pos"]["y"] = pos[1]
        if(aspectsymbol != "Default"):
            self.planets[planet]["aspect_symbol"] = aspectsymbol
        #Adding aspects of the planet
        for aspect in planet_aspects[planet]:
            aspecthousenum = compute_nthsignnum(housenum,aspect)
            aspectsign = get_signofsign(aspecthousenum, self.ascendantsign)
            asp_pos = get_coordniates_sc(aspectsign,self.planetindex[aspecthousenum-1])
            if(asp_pos == (0,0)):
                return(f'''Overflow Error: The given planet aspect {planet} - {aspect} overflows the house. no position available in house diagram for planet.''')
            self.planetindex[aspecthousenum-1] = self.planetindex[aspecthousenum-1] + 1
            aspectpos = {"x":0, "y":0}
            aspectpos["x"] = asp_pos[0]
            aspectpos["y"] = asp_pos[1]
            self.planets[planet]["aspectpos"].append(aspectpos)
            
        self.planets[planet]["isUpdated"] = True

        return("Success")
    
    def delete_planet(self,planet):
        #Validating input parameters
        if planet not in self.planets:
            return(f'''Input Error: The given planet {planet} is invalid.''')
        if(self.planets[planet]["isUpdated"] == False):
            return(f'''The planet {planet} is not added to be deleted.''')
        housenum = self.planets[planet]["house_num"]
        self.planetindex[housenum-1] = self.planetindex[housenum-1] - 1

        #removing aspects of the planet
        for aspect in planet_aspects[planet]:
            aspecthousenum = compute_nthsignnum(housenum,aspect)
            self.planetindex[aspecthousenum-1] = self.planetindex[aspecthousenum-1] - 1
        self.planets[planet]["aspectpos"] = []

        #Update the aspect symbol back to default
        if (planet == SUN):
            self.planets[SUN]["aspect_symbol"] = "☉"
        elif (planet == MOON):
            self.planets[MOON]["aspect_symbol"] = "☾"
        elif (planet == MARS):
            self.planets[MARS]["aspect_symbol"] = "♂"
        elif (planet == MERCURY):
            self.planets[MERCURY]["aspect_symbol"] = "☿"
        elif (planet == JUPITER):
            self.planets[JUPITER]["aspect_symbol"] = "♃"
        elif (planet == VENUS):
            self.planets[VENUS]["aspect_symbol"] = "♀"
        elif (planet == SATURN):
            self.planets[SATURN]["aspect_symbol"] = "♄"
        elif (planet == RAHU):
            self.planets[RAHU]["aspect_symbol"] = "☊"
        elif (planet == KETU):
            self.planets[KETU]["aspect_symbol"] = "☋"
        else:
            pass

        self.planets[planet]["isUpdated"] = False
        return("Success")
    
    def __isObjectDrawReady(self):
        #check if ascendant sign updated
        if (self.ascendantsign == "NotSet"):
            print("Error : Chart is not ready to be drawn as ascendant sign is not set yet")
            return False
        if (self.fullchart == True):
            for planet in self.planets:
                if(self.planets[planet]["isUpdated"] == False):
                    print(f"Error : Chart is not ready to be drawn as planet {planet} is not added yet")
                    return False
        return True
    
    def draw(self,location,filename,format = 'svg'):
        #Validating input parameters
        if(os.path.isdir(location) == False):
            return(f'''Input Error: The given location {location} is not valid location on this machine.''')
        if (isinstance(filename, str) == False):
            return(f'''Input Error: The given filename {filename} is not a string.''')
        if (format not in ["svg"]):
            return(f'''Input Error: The given format {format} is not supported. please choose from{["svg"]}.''')
        #check if the chart is ready to be drawn
        if(self.__isObjectDrawReady() == False):
            return(f'''The chart is not ready to be drawn yet as all the needed inputs are not provided!!!''')

        svgstatus = create_chartSVG_sc(self,location,filename)

        return(svgstatus)


########### GENERIC FUNCTIONS #################
def compute_nthsignnum(fromsignnum, n):
    s = (fromsignnum + n - 1) % 12
    if (s == 0):
        s = 12
    return (s)

def compute_nthsignnum_backwards(fromsignnum, n):
    s =  (12 + fromsignnum - n + 1) % 12
    if (s == 0):
        s = 12
    return (s)

def housediff(fromsign, tosign):
  ''' Computes how many houses is difference between from fromsign to tosign
      This function is used to compute housenumber for planets too '''
  if(tosign > fromsign):
    house = tosign - fromsign + 1
  elif(tosign < fromsign):
    house = 12 + tosign - fromsign + 1
  else: #same signs
    house = 1 #first house
  return house

def get_housenumofsign(sign,ascendantsign):
    ascendant_signnum = signnum(ascendantsign)
    focus_signnum = signnum(sign)
    housenum = housediff(ascendant_signnum,focus_signnum)
    return(housenum)

def get_signofsign(housenum, ascendantsign):
  ascendant_signnum = signnum(ascendantsign)
  focus_signnum = compute_nthsignnum(ascendant_signnum,housenum)
  return(signs[focus_signnum-1])


############################################################################
################# Global Functions for SouthIndian Chart ###################
############################################################################

def reset_chartcfg_sc():
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
def get_coordniates_sc(sign, planetidx):
    # sign is the sign in which planet is placed like "Aries", "Taurus" etc
    # planetidx is index of the planet in that house. If its first planet in that house then its 1 and if its 3rd planet then its 3.
    #return value is a tuple (x,y) containing 2 elements. x-coordinate and y-coordinate
    if (planetidx in range(1,10)):
        offset = SouthChart_offsets4mAries[sign.lower()]
        x_coordinate = base_coordinates_sc[planetidx-1]["x"] + offset["x"]
        y_coordinate = base_coordinates_sc[planetidx-1]["y"] + offset["y"]
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

def create_chartSVG_sc(chartObj,location,chartSVGfilename):
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

############################################################################
################# Global Functions for North Indian Chart###################
############################################################################

# Function to get svg coordinates with house and planet number in that house
def get_coordniates_nc(housenum, planetidx):
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

def reset_chartcfg_nc():
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

def create_chartSVG_nc(chartObj,location,chartSVGfilename):
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
    mychart = SouthChart("Lagna", "Shyam Bhat")
    mychart.set_ascendantsign("Capricorn")
    #print(mychart.housesigns)
    mychart.add_planet(SUN,"Su", 9)
    mychart.add_planet(MOON,"Mo", 9)
    mychart.add_planet(MARS,"Ma", 10)
    mychart.add_planet(MERCURY,"Me", 9)
    mychart.add_planet(JUPITER,"Ju", 8)
    mychart.add_planet(VENUS,"Ve", 8)
    mychart.add_planet(SATURN,"Sa", 1,colour="yellow")
    mychart.add_planet(RAHU,"Ra", 12)
    mychart.add_planet(KETU,"Ke", 6)
    mychart.updatechartcfg(aspect=False, clr_Asc='lime')
    
    print(mychart.draw("C:\\Users\hp\Downloads\\astrocharts", "LagnaChart", "svg"))
    print(mychart)