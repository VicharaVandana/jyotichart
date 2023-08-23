import support.constants as c


SouthChart_offsets4mAries = {  "aries"  :   { "x": 0, "y": 0},
                        "taurus"        :   { "x": 120, "y": 0},
                        "gemini"        :   { "x": 240, "y": 0},
                        "cancer"        :   { "x": 240, "y": 80},
                        "leo"           :   { "x": 240, "y": 160},
                        "virgo"         :   { "x": 240, "y": 240},
                        "libra"         :   { "x": 120, "y": 240},
                        "scorpio"       :   { "x": 0, "y": 240},
                        "sagittarius"   :   { "x": -120, "y": 240},
                        "capricorn"     :   { "x": -120, "y": 160},
                        "aquarius"      :   { "x": -120, "y": 80},
                        "pisces"        :   { "x": -120, "y": 0}
                        }

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




if __name__ == '__main__':
    pos = get_coordniates("Virgo", 5)
    print(pos)




