############################################################################
# languages.py - Multi-language translation support for JyotiChart
#
# Supported languages: "english" (default), "kannada", "hindi"
############################################################################

# Supported language codes
SUPPORTED_LANGUAGES = ["english", "kannada", "hindi"]

############################################################################
# Planet Abbreviations
# Keys match the planet name constants in jyotichart.py
############################################################################
planet_symbols = {
    "english": {
        "Sun"     : "Su",
        "Moon"    : "Mo",
        "Mars"    : "Ma",
        "Mercury" : "Me",
        "Jupiter" : "Ju",
        "Venus"   : "Ve",
        "Saturn"  : "Sa",
        "Rahu"    : "Ra",
        "Ketu"    : "Ke"
    },
    "kannada": {
        "Sun"     : "ಸೂ",
        "Moon"    : "ಚಂ",
        "Mars"    : "ಮಂ",
        "Mercury" : "ಬು",
        "Jupiter" : "ಗು",
        "Venus"   : "ಶು",
        "Saturn"  : "ಶ",
        "Rahu"    : "ರಾ",
        "Ketu"    : "ಕೇ"
    },
    "hindi": {
        "Sun"     : "सू",
        "Moon"    : "चं",
        "Mars"    : "मं",
        "Mercury" : "बु",
        "Jupiter" : "गु",
        "Venus"   : "शु",
        "Saturn"  : "श",
        "Rahu"    : "रा",
        "Ketu"    : "के"
    }
}

############################################################################
# Sign Names
############################################################################
sign_names = {
    "english": {
        "Aries"       : "Aries",
        "Taurus"      : "Taurus",
        "Gemini"      : "Gemini",
        "Cancer"      : "Cancer",
        "Leo"         : "Leo",
        "Virgo"       : "Virgo",
        "Libra"       : "Libra",
        "Scorpio"     : "Scorpio",
        "Saggitarius" : "Saggitarius",
        "Capricorn"   : "Capricorn",
        "Aquarius"    : "Aquarius",
        "Pisces"      : "Pisces"
    },
    "kannada": {
        "Aries"       : "ಮೇಷ",
        "Taurus"      : "ವೃಷಭ",
        "Gemini"      : "ಮಿಥುನ",
        "Cancer"      : "ಕರ್ಕ",
        "Leo"         : "ಸಿಂಹ",
        "Virgo"       : "ಕನ್ಯಾ",
        "Libra"       : "ತುಲಾ",
        "Scorpio"     : "ವೃಶ್ಚಿಕ",
        "Saggitarius" : "ಧನು",
        "Capricorn"   : "ಮಕರ",
        "Aquarius"    : "ಕುಂಭ",
        "Pisces"      : "ಮೀನ"
    },
    "hindi": {
        "Aries"       : "मेष",
        "Taurus"      : "वृषभ",
        "Gemini"      : "मिथुन",
        "Cancer"      : "कर्क",
        "Leo"         : "सिंह",
        "Virgo"       : "कन्या",
        "Libra"       : "तुला",
        "Scorpio"     : "वृश्चिक",
        "Saggitarius" : "धनु",
        "Capricorn"   : "मकर",
        "Aquarius"    : "कुम्भ",
        "Pisces"      : "मीन"
    }
}

############################################################################
# UI Labels used in chart center text and Asc marker
############################################################################
ui_labels = {
    "english": {
        "asc"         : "Asc",
        "birth"       : "Birth",
        "birthplace"  : "BirthPlace",
        "chart"       : "Chart",
        "inner"       : "Inner",
        "outer"       : "Outer",
        "transit"     : "Transit",
        "outerbirth"  : "Outer Birth",
        "outerbirthplace": "Outer BirthPlace"
    },
    "kannada": {
        "asc"         : "ಲಗ್ನ",
        "birth"       : "ಜನನ",
        "birthplace"  : "ಜನ್ಮಸ್ಥಳ",
        "chart"       : "ಕುಂಡಲಿ",
        "inner"       : "ಒಳ",
        "outer"       : "ಹೊರ",
        "transit"     : "ಗೋಚಾರ",
        "outerbirth"  : "ಹೊರ ಜನನ",
        "outerbirthplace": "ಹೊರ ಜನ್ಮಸ್ಥಳ"
    },
    "hindi": {
        "asc"         : "लग्न",
        "birth"       : "जन्म",
        "birthplace"  : "जन्मस्थान",
        "chart"       : "कुंडली",
        "inner"       : "आंतर",
        "outer"       : "बाहर",
        "transit"     : "गोचर",
        "outerbirth"  : "बाहर जन्म",
        "outerbirthplace": "बाहर जन्मस्थान"
    }
}


############################################################################
# Helper Functions
############################################################################

def get_planet_symbol(planet, language="english"):
    """Return the planet abbreviation/symbol in the requested language.

    Parameters:
        planet   (str): Planet name. Must be one of: "Sun", "Moon", "Mars",
                        "Mercury", "Jupiter", "Venus", "Saturn", "Rahu", "Ketu".
        language (str): Language code. One of "english" (default), "kannada", "hindi".

    Returns:
        str: The abbreviation string for the planet in the given language.
             Falls back to English if the language or planet is not found.
    """
    lang = language.lower() if language else "english"
    if lang not in SUPPORTED_LANGUAGES:
        print(f"Warning: Language '{language}' is not supported. Falling back to English.")
        lang = "english"
    symbols = planet_symbols.get(lang, planet_symbols["english"])
    return symbols.get(planet, planet_symbols["english"].get(planet, planet))


def get_sign_name(sign, language="english"):
    """Return the zodiac sign name in the requested language.

    Parameters:
        sign     (str): English sign name e.g. "Aries", "Taurus", etc.
        language (str): Language code. One of "english" (default), "kannada", "hindi".

    Returns:
        str: The sign name string in the given language.
             Falls back to English if the language is not found.
    """
    lang = language.lower() if language else "english"
    if lang not in SUPPORTED_LANGUAGES:
        print(f"Warning: Language '{language}' is not supported. Falling back to English.")
        lang = "english"
    names = sign_names.get(lang, sign_names["english"])
    return names.get(sign, sign)


def get_ui_label(label_key, language="english"):
    """Return a UI label string (e.g. 'Asc', 'Birth') in the requested language.

    Parameters:
        label_key (str): Key from ui_labels dict e.g. "asc", "birth", "birthplace".
        language  (str): Language code. One of "english" (default), "kannada", "hindi".

    Returns:
        str: The label in the requested language. Falls back to English if not found.
    """
    lang = language.lower() if language else "english"
    if lang not in SUPPORTED_LANGUAGES:
        lang = "english"
    labels = ui_labels.get(lang, ui_labels["english"])
    return labels.get(label_key, ui_labels["english"].get(label_key, label_key))
