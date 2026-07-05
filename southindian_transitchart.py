import support.constants as c
import support.languages as lang_module

p_rel = [
    (32, 30),  # P1
    (62, 38),  # P2
    (47, 60),  # P3
    (12, 48),  # P4
    (92, 50),  # P5
    (22, 73),  # P6
    (87, 25),  # P7
    (7,  22),  # P8
    (57, 20),  # P9
]

# Top-left positions of each sign's box in the natal chart (shifted by X+120, Y+80)
natal_box = {
    "aries"       : (243, 90),
    "taurus"      : (363, 90),
    "gemini"      : (483, 90),
    "cancer"      : (483, 170),
    "leo"         : (483, 250),
    "virgo"       : (483, 330),
    "libra"       : (363, 330),
    "scorpio"     : (243, 330),
    "saggitarius" : (123, 330),
    "capricorn"   : (123, 250),
    "aquarius"    : (123, 170),
    "pisces"      : (123, 90)
}

# Top-left positions of each sign's box in the transit ring (outer boxes)
transit_box = {
    "aries"       : (243, 10),
    "taurus"      : (363, 10),
    "gemini"      : (483, 10),
    "cancer"      : (603, 170),
    "leo"         : (603, 250),
    "virgo"       : (483, 410),
    "libra"       : (363, 410),
    "scorpio"     : (243, 410),
    "saggitarius" : (123, 410),
    "capricorn"   : (3,   250),
    "aquarius"    : (3,   170),
    "pisces"      : (123, 10)
}

SouthChart_AscendantPositionAries = {"x": 202, "y": 83}

############################################################################
################# Global Functions #########################################
############################################################################

def reset_chartcfg():
    chartcfg = {
                    "background-colour" : "black",
                    "outerbox-colour" : "cyan",
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
                                        "saggitarius"   : "black",
                                        "capricorn"     : "black",
                                        "aquarius"      : "black",
                                        "pisces"        : "black"
                                    },
                    "aspect-visibility"  : True
                }
    return(chartcfg)

# Function to get svg coordinates for natal chart
def get_natalcoordniates(sign, planetidx):
    if (planetidx in range(1,10)):
        sign_key = "saggitarius" if sign == "Saggitarius" else sign.lower()
        bx, by = natal_box[sign_key]
        rx, ry = p_rel[planetidx-1]
        return ((bx + rx, by + ry))
    else: 
        print(f"INPUTERROR: planetidx must be in the range 1 to 9 but given value is {planetidx}.")
        return ((0,0))

# Function to get svg coordinates for transit chart
def get_transitcoordniates(sign, planetidx):
    if (planetidx in range(1,10)):
        sign_key = "saggitarius" if sign == "Saggitarius" else sign.lower()
        bx, by = transit_box[sign_key]
        rx, ry = p_rel[planetidx-1]
        return ((bx + rx, by + ry))
    else: 
        print(f"INPUTERROR: planetidx must be in the range 1 to 9 but given value is {planetidx}.")
        return ((0,0))

def draw_classicSouthTransitChartSkeleton(chartSVG, chartCfg):
    chartSVG.write(f'''  <!-- ********** Chart Diagram ********** -->\n''')
    
    # Outer Octagonal boundary
    OCT_PTS = "123,10 603,10 723,170 723,330 603,490 123,490 3,330 3,170"
    chartSVG.write(f'''  <polygon points="{OCT_PTS}" style="fill:{chartCfg["background-colour"]};stroke-width:3;stroke:{chartCfg["outerbox-colour"]}" />\n''')

    # Transit boxes (cyan)
    for sign, (tx, ty) in transit_box.items():
        chartSVG.write(f'''  <rect id ="transit_{sign}" width="120" height="80" x="{tx}" y="{ty}" style="fill:{chartCfg["house-colour"][sign]};stroke:cyan;stroke-width:2" />\n''')

    # Inner Natal boxes (yellow dashes)
    # Inner Natal outer border
    chartSVG.write(f'''  <rect id = "border" width="486" height="327" x="120" y="87" style="fill:none;stroke-width:3;stroke:{chartCfg["innerbox-colour"]}" />\n''')
    # Center hollow box
    chartSVG.write(f'''  <rect id = "center" width="235" height="156" x="246" y="172" style="fill:{chartCfg["background-colour"]};stroke-width:3;stroke:{chartCfg["innerbox-colour"]}" />\n''')
    
    for sign, (nx, ny) in natal_box.items():
        chartSVG.write(f'''  <rect id ="natal_{sign}" width="120" height="80" x="{nx}" y="{ny}" style="fill:{chartCfg["house-colour"][sign]};stroke:{chartCfg["line-colour"]};stroke-width:2;stroke-dasharray:4 2" />\n''')

    # Connector lines
    chartSVG.write(f'''  <line x1="123" y1="90" x2="123" y2="410" style="stroke:cyan;stroke-width:1.5;stroke-dasharray:6 3"/>\n''')
    chartSVG.write(f'''  <line x1="603" y1="90" x2="603" y2="410" style="stroke:cyan;stroke-width:1.5;stroke-dasharray:6 3"/>\n''')
    chartSVG.write(f'''  <line x1="123" y1="90" x2="603" y2="90" style="stroke:cyan;stroke-width:1.5;stroke-dasharray:6 3"/>\n''')
    chartSVG.write(f'''  <line x1="123" y1="410" x2="603" y2="410" style="stroke:cyan;stroke-width:1.5;stroke-dasharray:6 3"/>\n''')
    
    return

def write_signnumOnChart_stsc(chartSVG, signclr, ascendantsign, language="english"):
    chartSVG.write('\n  <!-- ********** Ascendant Sign ********** -->\n')
    # Ascendant is in the natal chart, shift by 120, 80
    pxAsc = SouthChart_AscendantPositionAries["x"] + 120
    pyAsc = SouthChart_AscendantPositionAries["y"] + 80
    
    # Needs to add sign offset 
    sign_key = "saggitarius" if ascendantsign == "Saggitarius" else ascendantsign.lower()
    bx, by = natal_box[sign_key]
    # Aries base is 243, 90. So offset is bx - 243, by - 90
    pxAsc = pxAsc + (bx - 243)
    pyAsc = pyAsc + (by - 90)
    asc_label = lang_module.get_ui_label("asc", language)
    chartSVG.write(f'''  <text id ="{ascendantsign}Asc" x="{pxAsc}" y="{pyAsc}" fill="{signclr}" class="sign-num">{asc_label}</text>\n''')
    return

def write_natalplanetsOnChart_stsc(chartSVG, planets):
    chartSVG.write('\n  <!-- ********** Natal Planets ********** -->\n')
    
    for planetname in planets:
        chartSVG.write(f'\n  <!-- ********** {planetname} ********** -->\n')
        symbol = planets[planetname]["symbol"]
        retro = planets[planetname]["retro"]
        planetcolour = planets[planetname]["colour"]
        
        px = planets[planetname]["pos"]["x"] + 120
        py = planets[planetname]["pos"]["y"] + 80

        if(retro == True):
            Planet_SVGstring = f'''  <text y="{py}" x="{px}" fill="{planetcolour}" text-decoration="underline" class="natal-planet" id="natal-{planetname}">{symbol}</text>\n'''
        else:
            Planet_SVGstring = f'''  <text y="{py}" x="{px}" fill="{planetcolour}" class="natal-planet" id="natal-{planetname}">{symbol}</text>\n'''
        chartSVG.write(Planet_SVGstring)
    return

def write_transitplanetsOnChart_stsc(chartSVG, planets):
    chartSVG.write('\n  <!-- ********** Transit Planets ********** -->\n')
    
    for planetname in planets:
        chartSVG.write(f'\n  <!-- ********** {planetname} ********** -->\n')
        symbol = planets[planetname]["symbol"]
        retro = planets[planetname]["retro"]
        planetcolour = planets[planetname]["colour"]
        
        px = planets[planetname]["pos"]["x"]
        py = planets[planetname]["pos"]["y"]

        if(retro == True):
            Planet_SVGstring = f'''  <text y="{py}" x="{px}" fill="{planetcolour}" text-decoration="underline" class="transit-planet" id="transit-{planetname}">{symbol}</text>\n'''
        else:
            Planet_SVGstring = f'''  <text y="{py}" x="{px}" fill="{planetcolour}" class="transit-planet" id="transit-{planetname}">{symbol}</text>\n'''
        chartSVG.write(Planet_SVGstring)
    return

def write_natalplanetsAspectsOnChart_stsc(chartSVG, planets):
    chartSVG.write('\n  <!-- ********** Natal Planets Aspects ********** -->\n')
    
    for planetname in planets:
        chartSVG.write(f'\n  <!-- ********** {planetname} Aspect ********** -->\n')
        symbol = planets[planetname]["aspect_symbol"]
        planetcolour = planets[planetname]["colour"]
        for aspectpositions in planets[planetname]["aspectpos"]:
            px = aspectpositions["x"] + 120
            py = aspectpositions["y"] + 80

            Planet_SVGstring = f'''  <text y="{py}" x="{px}" fill="{planetcolour}" class="natal-aspect" id="natal-{planetname}-aspect">{symbol}</text>\n'''
            chartSVG.write(Planet_SVGstring)
    return

def write_transitplanetsAspectsOnChart_stsc(chartSVG, planets):
    chartSVG.write('\n  <!-- ********** Transit Planets Aspects ********** -->\n')
    
    for planetname in planets:
        chartSVG.write(f'\n  <!-- ********** {planetname} Aspect ********** -->\n')
        symbol = planets[planetname]["aspect_symbol"]
        planetcolour = planets[planetname]["colour"]
        for aspectpositions in planets[planetname]["aspectpos"]:
            px = aspectpositions["x"]
            py = aspectpositions["y"]

            Planet_SVGstring = f'''  <text y="{py}" x="{px}" fill="{planetcolour}" class="transit-aspect" id="transit-{planetname}-aspect">{symbol}</text>\n'''
            chartSVG.write(Planet_SVGstring)
    return

def write_chartdetailsOnChart_stsc(chartSVG, chartObj, parentChartObj, language="english"):
    chartSVG.write('\n  <!-- ********** Chart Details ********** -->\n')
    cx = 363.5
    cy = 200
    line_height = 16

    lbl_birth        = lang_module.get_ui_label("birth", language)
    lbl_birthplace   = lang_module.get_ui_label("birthplace", language)
    lbl_inner        = lang_module.get_ui_label("inner", language)
    lbl_outer        = lang_module.get_ui_label("outer", language)
    lbl_transit      = lang_module.get_ui_label("transit", language)
    lbl_outerbirth   = lang_module.get_ui_label("outerbirth", language)
    lbl_outerbirthpl = lang_module.get_ui_label("outerbirthplace", language)

    details = []
    if chartObj.personname:
        details.append(chartObj.personname)
        
    if hasattr(parentChartObj, 'dob') and parentChartObj.dob:
        dob_tob = f"{lbl_birth} : {parentChartObj.dob}"
        if hasattr(parentChartObj, 'tob') and parentChartObj.tob:
            dob_tob += f" | {parentChartObj.tob}"
        details.append(dob_tob)
        
    if hasattr(parentChartObj, 'pob') and parentChartObj.pob:
        details.append(f"{lbl_birthplace} : {parentChartObj.pob}")
        
    if parentChartObj.chartname:
        details.append(f"{lbl_inner} : {parentChartObj.chartname}")
        
    if chartObj.chartname:
        details.append(f"{lbl_outer} : {chartObj.chartname}")
        
    if hasattr(chartObj, 'outer_dob') and chartObj.outer_dob:
        outer_dob_tob = f"{lbl_outerbirth} : {chartObj.outer_dob}"
        if hasattr(chartObj, 'outer_tob') and chartObj.outer_tob:
            outer_dob_tob += f" | {chartObj.outer_tob}"
        details.append(outer_dob_tob)
        if hasattr(chartObj, 'outer_pob') and chartObj.outer_pob:
            details.append(f"{lbl_outerbirthpl} : {chartObj.outer_pob}")
    elif chartObj.transit_date:
        transit_dt = f"{lbl_transit} : {chartObj.transit_date}"
        if chartObj.transit_time:
            transit_dt += f" | {chartObj.transit_time}"
        details.append(transit_dt)
        
    for i, detail in enumerate(details):
        y_pos = cy + (i * line_height)
        chartSVG.write(f'''  <text x="{cx}" y="{y_pos}" fill="white" class="chart-details" text-anchor="middle">{detail}</text>\n''')
    return

def create_transitchartSVG(chartObj,location,chartSVGfilename, parentChartObj, language="english"):
    if((location[-1] == '\\') or (location[-1] == '/')):
        chartSVGFullname = f'{location}{chartSVGfilename}.svg'
    elif('/' in location):
        chartSVGFullname = f'{location}/{chartSVGfilename}.svg'
    else:
        chartSVGFullname = f'{location}\{chartSVGfilename}.svg'
    
    chartSVG = open(chartSVGFullname, 'w',  encoding='utf-16')
    
    # SVG chart open section
    chartSVG.write(f'''<svg id="{chartObj.chartname}_chart_{chartObj.personname}" height="500" width="730" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="-10 -10 740 510" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" charset="utf-16">\n''')
    chartSVG.write('  <style>\n')
    chartSVG.write('    .sign-num { font: bold 20px sans-serif; }\n')
    chartSVG.write('    .natal-planet { font: bold 14px sans-serif; }\n')
    chartSVG.write('    .transit-planet { font: bold 14px sans-serif; }\n')
    chartSVG.write('    .natal-aspect { font: bold 16px sans-serif; }\n')
    chartSVG.write('    .transit-aspect { font: bold 16px sans-serif; }\n')
    chartSVG.write('    .chart-details { font: bold 12px sans-serif; }\n')
    chartSVG.write('  </style>\n')
    
    draw_classicSouthTransitChartSkeleton(chartSVG, chartObj.chartcfg)
    write_signnumOnChart_stsc(chartSVG, chartObj.chartcfg["sign-colour"], chartObj.ascendantsign, language)
    
    write_natalplanetsOnChart_stsc(chartSVG, parentChartObj.planets)
    if(parentChartObj.chartcfg["aspect-visibility"] == True):
        write_natalplanetsAspectsOnChart_stsc(chartSVG, parentChartObj.planets)
    
    write_transitplanetsOnChart_stsc(chartSVG, chartObj.planets)
    if(chartObj.chartcfg["aspect-visibility"] == True):
        write_transitplanetsAspectsOnChart_stsc(chartSVG, chartObj.planets)

    write_chartdetailsOnChart_stsc(chartSVG, chartObj, parentChartObj, language)
    
    chartSVG.write('\n  Sorry, your browser does not support inline SVG.\n')
    chartSVG.write('</svg>\n')
    chartSVG.close()

    return "Success"
