import southindianchart as sc
import northindianchart as nc
import northindian_transitchart as ntc
import northindian_numericalchart as nnc
import southindian_numericalchart as snc
import southindian_transitchart as stc
import support.general as gen
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


################################### NORTH CHART ###################################
class NorthChart:
    def __init__(self, chartname, personname, IsFullChart = True):
        self.chartname = chartname
        self.personname = personname
        self.chartcfg = nc.reset_chartcfg()
        self.ascendantsign = "NotSet"
        self.fullchart = IsFullChart
        self.planets = {
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
        self.planetindex = [1,1,1,1,1,1,1,1,1,1,1,1]
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
        if sign not in gen.signs:
            return(f'''Input Error: The given input sign {sign} is not a valid astrological sign.''')
        self.ascendantsign = sign
        ascendantsignnum = gen.signnum(sign)
        self.housesigns = []
        for hno in range(1,13):
            self.housesigns.append(gen.compute_nthsignnum(ascendantsignnum,hno)) 
        return("Success")
     
    
    
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
        pos = nc.get_coordniates(housenum,self.planetindex[housenum-1])
        if(pos == (0,0)):
            return(f'''Overflow Error: The given planet overflows the house. no position available in house diagram for planet {planet}.''')
        self.planetindex[housenum-1] = self.planetindex[housenum-1] + 1
        self.planets[planet]["pos"]["x"] = pos[0]
        self.planets[planet]["pos"]["y"] = pos[1]
        if(aspectsymbol != "Default"):
            self.planets[planet]["aspect_symbol"] = aspectsymbol
        #Adding aspects of the planet
        for aspect in planet_aspects[planet]:
            aspecthousenum = gen.compute_nthsignnum(housenum,aspect)
            asp_pos = nc.get_coordniates(aspecthousenum,self.planetindex[aspecthousenum-1])
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
            aspecthousenum = gen.compute_nthsignnum(housenum,aspect)
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

        svgstatus = nc.create_chartSVG(self,location,filename)

        return(svgstatus)
    
################################### NORTH TRANSIT CHART ###################################
class NorthTransitChart:
    def __init__(self, chartname, personname, parentNorthChart, IsFullChart = True):
        self.chartname = chartname
        self.personname = personname
        self.chartcfg = nc.reset_chartcfg()
        self.ascendantsign = "NotSet"
        self.fullchart = IsFullChart
        self.parentNorthChart = parentNorthChart
        self.set_ascendantsign(self.parentNorthChart.ascendantsign)
        self.planets = {
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
        self.planetindex = [1,1,1,1,1,1,1,1,1,1,1,1]
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
        if sign not in gen.signs:
            return(f'''Input Error: The given input sign {sign} is not a valid astrological sign.''')
        self.ascendantsign = sign
        ascendantsignnum = gen.signnum(sign)
        self.housesigns = []
        for hno in range(1,13):
            self.housesigns.append(gen.compute_nthsignnum(ascendantsignnum,hno)) 
        return("Success")
     
    
    
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
        pos = ntc.get_transitcoordniates(housenum,self.planetindex[housenum-1])
        if(pos == (0,0)):
            return(f'''Overflow Error: The given planet overflows the house. no position available in house diagram for planet {planet}.''')
        self.planetindex[housenum-1] = self.planetindex[housenum-1] + 1
        self.planets[planet]["pos"]["x"] = pos[0]
        self.planets[planet]["pos"]["y"] = pos[1]
        if(aspectsymbol != "Default"):
            self.planets[planet]["aspect_symbol"] = aspectsymbol
        #Adding aspects of the planet
        for aspect in planet_aspects[planet]:
            aspecthousenum = gen.compute_nthsignnum(housenum,aspect)
            asp_pos = ntc.get_transitcoordniates(aspecthousenum,self.planetindex[aspecthousenum-1])
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
            aspecthousenum = gen.compute_nthsignnum(housenum,aspect)
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

        svgstatus = ntc.create_transitchartSVG(self,location,filename,self.parentNorthChart)

        return(svgstatus)

################################### SOUTH CHART ###################################
class SouthChart:
    def __init__(self, chartname, personname, IsFullChart = True):
        self.chartname = chartname
        self.personname = personname
        self.chartcfg = sc.reset_chartcfg()
        self.ascendantsign = "NotSet"
        self.fullchart = IsFullChart
        self.dob = ""
        self.tob = ""
        self.pob = ""
        self.planets = {
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
        self.planetindex = [1,1,1,1,1,1,1,1,1,1,1,1]
        return
    
    def __str__(self):
        return f"{self.chartname} chart object of {self.personname}."

    def set_birth_details(self, dob, tob, pob):
        self.dob = dob
        self.tob = tob
        self.pob = pob
        return "Success"

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
        if sign not in gen.signs:
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
        sign = gen.get_signofsign(housenum, self.ascendantsign)
        pos = sc.get_coordniates(sign,self.planetindex[housenum-1])
        if(pos == (0,0)):
            return(f'''Overflow Error: The given planet overflows the house. no position available in house diagram for planet {planet}.''')
        self.planetindex[housenum-1] = self.planetindex[housenum-1] + 1
        self.planets[planet]["pos"]["x"] = pos[0]
        self.planets[planet]["pos"]["y"] = pos[1]
        if(aspectsymbol != "Default"):
            self.planets[planet]["aspect_symbol"] = aspectsymbol
        #Adding aspects of the planet
        for aspect in planet_aspects[planet]:
            aspecthousenum = gen.compute_nthsignnum(housenum,aspect)
            aspectsign = gen.get_signofsign(aspecthousenum, self.ascendantsign)
            asp_pos = sc.get_coordniates(aspectsign,self.planetindex[aspecthousenum-1])
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
            aspecthousenum = gen.compute_nthsignnum(housenum,aspect)
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

        svgstatus = sc.create_chartSVG(self,location,filename)

        return(svgstatus)


################################### SOUTH TRANSIT CHART ###################################
class SouthTransitChart:
    def __init__(self, chartname, personname, parentSouthChart, IsFullChart = True):
        self.chartname = chartname
        self.personname = personname
        self.chartcfg = stc.reset_chartcfg()
        self.ascendantsign = "NotSet"
        self.fullchart = IsFullChart
        self.parentSouthChart = parentSouthChart
        self.set_ascendantsign(self.parentSouthChart.ascendantsign)
        self.planetindex = [1,1,1,1,1,1,1,1,1,1,1,1]
        self.transit_date = ""
        self.transit_time = ""
        self.outer_dob = ""
        self.outer_tob = ""
        self.outer_pob = ""
        self.planets = {
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
        self.planetindex = [1,1,1,1,1,1,1,1,1,1,1,1]
        return
    
    def __str__(self):
        return f"{self.chartname} chart object of {self.personname}."

    def set_transit_details(self, date, time):
        self.transit_date = date
        self.transit_time = time
        return "Success"
        
    def set_outer_birth_details(self, dob, tob, pob):
        self.outer_dob = dob
        self.outer_tob = tob
        self.outer_pob = pob
        return "Success"
    
    def updatechartcfg(self, aspect=True, clr_background = 'black', clr_outbox = 'cyan', clr_line = 'yellow', clr_sign = 'pink', 
    clr_houses = ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black']):
        self.chartcfg['aspect-visibility'] = aspect
        self.chartcfg['background-colour'] = clr_background
        self.chartcfg['outerbox-colour'] = clr_outbox
        self.chartcfg['line-colour'] = clr_line
        self.chartcfg['sign-colour'] = clr_sign
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
        if sign not in gen.signs:
            return(f'''Input Error: The given input sign {sign} is not a valid astrological sign.''')
        self.ascendantsign = sign
        return("Success")
     
    
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

        self.planets[planet]["isUpdated"] = False
        self.planets[planet]["symbol"] = symbol
        self.planets[planet]["house_num"] = housenum
        self.planets[planet]["colour"] = colour
        self.planets[planet]["retro"] = retrograde
        sign = gen.get_signofsign(housenum, self.ascendantsign)
        pos = stc.get_transitcoordniates(sign,self.planetindex[housenum-1])
        if(pos == (0,0)):
            return(f'''Overflow Error: The given planet overflows the house. no position available in house diagram for planet {planet}.''')
        self.planetindex[housenum-1] = self.planetindex[housenum-1] + 1
        self.planets[planet]["pos"]["x"] = pos[0]
        self.planets[planet]["pos"]["y"] = pos[1]
        if(aspectsymbol != "Default"):
            self.planets[planet]["aspect_symbol"] = aspectsymbol
        #Adding aspects of the planet
        for aspect in planet_aspects[planet]:
            aspecthousenum = gen.compute_nthsignnum(housenum,aspect)
            aspectsign = gen.get_signofsign(aspecthousenum, self.ascendantsign)
            asp_pos = stc.get_transitcoordniates(aspectsign,self.planetindex[aspecthousenum-1])
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
            aspecthousenum = gen.compute_nthsignnum(housenum,aspect)
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

        svgstatus = stc.create_transitchartSVG(self,location,filename,self.parentSouthChart)

        return(svgstatus)



################################### NORTH NUMERICAL CHART ###################################
class NorthNumericalChart:
    '''Chart for displaying one numerical value per house in North Indian style.
    Useful for BhavaBala, BhavaBala Rank, AshtakaVarga points, etc.
    The ascendant sign is required so that sign numbers are shown in each house.
    '''
    def __init__(self, chartname, personname):
        self.chartname = chartname
        self.personname = personname
        self.chartcfg = nc.reset_chartcfg()
        self.ascendantsign = "NotSet"
        # housevalues: list of 12 dicts, one per house (house1 at index 0)
        self.housevalues = [{"value": "", "colour": "lime"} for _ in range(12)]
        return

    def __str__(self):
        return f"{self.chartname} numerical chart object of {self.personname}."

    def updatechartcfg(self, aspect=True, clr_background='black', clr_outbox='red', clr_line='yellow', clr_sign='pink',
    clr_houses=['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black']):
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

    def set_ascendantsign(self, sign):
        if sign not in gen.signs:
            return(f'''Input Error: The given input sign {sign} is not a valid astrological sign.''')
        self.ascendantsign = sign
        ascendantsignnum = gen.signnum(sign)
        self.housesigns = []
        for hno in range(1, 13):
            self.housesigns.append(gen.compute_nthsignnum(ascendantsignnum, hno))
        return("Success")

    def set_house_value(self, housenum, value, colour='lime'):
        '''Set the numerical value to display at the centre of a house.

        Parameters:
            housenum (int)   : House number 1-12.
            value    (int/str): The number or string to display in the house.
            colour   (str)   : Colour of the displayed value. Default is lime.

        Returns "Success" on valid input, or an error string.
        '''
        if housenum not in range(1, 13):
            return(f'''Input Error: housenum {housenum} is not valid. Must be 1-12.''')
        self.housevalues[housenum - 1]["value"] = value
        self.housevalues[housenum - 1]["colour"] = colour
        return("Success")

    def __isObjectDrawReady(self):
        if self.ascendantsign == "NotSet":
            print("Error: Ascendant sign is not set yet.")
            return False
        for idx in range(12):
            if self.housevalues[idx]["value"] == "":
                print(f"Error: Value for house {idx + 1} is not set yet.")
                return False
        return True

    def draw(self, location, filename, format="svg"):
        if(os.path.isdir(location) == False):
            return(f'''Input Error: The given location {location} is not a valid location on this machine.''')
        if(isinstance(filename, str) == False):
            return(f'''Input Error: The given filename {filename} is not a string.''')
        if(format not in ["svg"]):
            return(f'''Input Error: The given format {format} is not supported. Please choose from {["svg"]}.''')
        if(self.__isObjectDrawReady() == False):
            return(f'''The chart is not ready to be drawn yet as all the needed inputs are not provided!!!''')

        return nnc.create_numericalchartSVG(self, location, filename)


################################### SOUTH NUMERICAL CHART ###################################
class SouthNumericalChart:
    '''Chart for displaying one numerical value per sign in South Indian style.
    Useful for BhavaBala, BhavaBala Rank, AshtakaVarga points, etc.
    The ascendant sign is required so that the Asc marker is shown.
    Values are provided per sign (fixed positions), not per house.
    '''
    # All 12 zodiac signs in order (matches south_sign_order in southindian_numericalchart.py)
    _sign_order = [
        "Aries", "Taurus", "Gemini", "Cancer",
        "Leo", "Virgo", "Libra", "Scorpio",
        "Saggitarius", "Capricorn", "Aquarius", "Pisces"
    ]

    def __init__(self, chartname, personname):
        self.chartname = chartname
        self.personname = personname
        self.chartcfg = snc.reset_chartcfg()
        self.ascendantsign = "NotSet"
        # signvalues: dict keyed by lowercase sign name
        self.signvalues = {s.lower(): {"value": "", "colour": "lime"} for s in self._sign_order}
        # Fix the Saggitarius key to match southindian_numericalchart.py's 'sagittarius' key
        self.signvalues["sagittarius"] = self.signvalues.pop("saggitarius", {"value": "", "colour": "lime"})
        return

    def __str__(self):
        return f"{self.chartname} numerical chart object of {self.personname}."

    def updatechartcfg(self, aspect=True, clr_background='black', clr_outbox='red', clr_inbox='red', clr_line='yellow', clr_Asc='pink',
    clr_houses=['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black']):
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

    def set_ascendantsign(self, sign):
        if sign not in gen.signs:
            return(f'''Input Error: The given input sign {sign} is not a valid astrological sign.''')
        self.ascendantsign = sign
        return("Success")

    def set_sign_value(self, sign, value, colour='lime'):
        '''Set the numerical value to display at the centre of a sign box.

        Parameters:
            sign   (str)     : Zodiac sign name e.g. "Aries", "Taurus" etc.
            value  (int/str) : The number or string to display in the sign box.
            colour (str)     : Colour of the displayed value. Default is lime.

        Returns "Success" on valid input, or an error string.
        '''
        if sign not in gen.signs:
            return(f'''Input Error: {sign} is not a valid astrological sign.''')
        key = "sagittarius" if sign == "Saggitarius" else sign.lower()
        self.signvalues[key]["value"] = value
        self.signvalues[key]["colour"] = colour
        return("Success")

    def set_house_value(self, housenum, value, ascendantsign=None, colour='lime'):
        '''Convenience method: set value by house number instead of sign name.
        Requires ascendantsign to be already set via set_ascendantsign(), or
        pass it explicitly as the optional ascendantsign parameter.

        Parameters:
            housenum      (int)     : House number 1-12.
            value         (int/str) : The number or string to display.
            ascendantsign (str)     : Override ascendant; uses the already-set one if None.
            colour        (str)     : Colour of the displayed value.

        Returns "Success" on valid input, or an error string.
        '''
        asc = ascendantsign if ascendantsign else self.ascendantsign
        if asc == "NotSet":
            return("Input Error: Ascendant sign is not set. Call set_ascendantsign() first or pass ascendantsign parameter.")
        if housenum not in range(1, 13):
            return(f'''Input Error: housenum {housenum} is not valid. Must be 1-12.''')
        sign = gen.get_signofsign(housenum, asc)
        return self.set_sign_value(sign, value, colour)

    def __isObjectDrawReady(self):
        if self.ascendantsign == "NotSet":
            print("Error: Ascendant sign is not set yet.")
            return False
        for sign, entry in self.signvalues.items():
            if entry["value"] == "":
                print(f"Error: Value for sign {sign} is not set yet.")
                return False
        return True

    def draw(self, location, filename, format="svg"):
        if(os.path.isdir(location) == False):
            return(f'''Input Error: The given location {location} is not a valid location on this machine.''')
        if(isinstance(filename, str) == False):
            return(f'''Input Error: The given filename {filename} is not a string.''')
        if(format not in ["svg"]):
            return(f'''Input Error: The given format {format} is not supported. Please choose from {["svg"]}.''')
        if(self.__isObjectDrawReady() == False):
            return(f'''The chart is not ready to be drawn yet as all the needed inputs are not provided!!!''')

        return snc.create_numericalchartSVG(self, location, filename)


if __name__ == '__main__':
    mychart = NorthChart("Lagna", "Shyam Bhat")
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
    mychart.updatechartcfg(aspect=False)
    
    print(mychart.draw("./astrocharts", "LagnaChart", "svg"))
    #print(mychart)

    mytransitchart = NorthTransitChart("Lagna", "Shyam Bhat", mychart)
    mytransitchart.add_planet(SUN,"Su", 1)
    mytransitchart.add_planet(MOON,"Mo", 1)
    mytransitchart.add_planet(MARS,"Ma", 1)
    mytransitchart.add_planet(MERCURY,"Me", 1)
    mytransitchart.add_planet(JUPITER,"Ju", 2)
    mytransitchart.add_planet(VENUS,"Ve", 1)
    mytransitchart.add_planet(SATURN,"Sa", 1,colour="lime")
    mytransitchart.add_planet(RAHU,"Ra", 2)
    mytransitchart.add_planet(KETU,"Ke", 8)
    #mytransitchart.updatechartcfg(aspect=False)
    
    print(mytransitchart.draw("./astrocharts", "LagnaChart", "svg"))
    print(mytransitchart)