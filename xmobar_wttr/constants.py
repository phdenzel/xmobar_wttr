# -*- coding: utf-8 -*-
"""
xmobar_wttr.constants

@author: phdenzel
"""
import xmobar_wttr
from xmobar_wttr.utils import WindVector
from xmobar_wttr.utils import datetime_from_hms, is_day


weather_symbol_plain = {
    "?":   "Unknown",
    "mm":  "Cloudy",
    "=":   "Fog",
    "///": "HeavyRain",
    "//":  "HeavyShowers",
    "**":  "HeavySnow",
    "*/*": "HeavySnowShowers",
    "/":   "LightRain",
    ".":   "LightShowers",
    "x":   "LightSleet",
    "x/":  "LightSleetShowers",
    "*":   "LightSnow",
    "*/":  "LightSnowShowers",
    "m":   "PartlyCloudy",
    "o":   "Sunny",
    "/!/": "ThunderyHeavyRain",
    "!/":  "ThunderyShowers",
    "*!*": "ThunderySnowShowers",
    "mmm": "VeryCloudy",
}


# wind_arrows = ["↓", "↙", "←", "↖", "↑", "↗", "→", "↘"]
wind_directions = {
    "↓" : "S",
    "S" : "",
    "↙" : "SW",
    "SW": "",
    "←" : "W",
    "W" : "",
    "↖" : "NW",
    "NW": "",
    "↑" : "N",
    "N" : "",
    "↗" : "NE",
    "NE": "",
    "→" : "E",
    "E" : "",
    "↘" : "SE",
    "SE": "",
    "0" : "",
    ""  : "",
    " " : "",
}

wind_direction_codes = {
    "↓" : "S",
    "S" : "\\f044",
    "↙" : "SW",
    "SW": "\\f043",
    "←" : "W",
    "W" : "\\f048",
    "↖" : "NW",
    "NW": "\\f087",
    "↑" : "N",
    "N" : "\\f058",
    "↗" : "NE",
    "NE": "\\f057",
    "→" : "E",
    "E" : "\\f04d",
    "↘" : "SE",
    "SE": "\\f088",
    "0" : "",
    ""  : "",
    " " : "",
}

weather_symbols = {
    "Unknown":             ["", ""],
    "Cloudy":              ["", ""],
    "Fog":                 ["", ""],
    "HeavyRain":           ["", ""],
    "HeavyShowers":        ["", ""],
    "HeavySnow":           ["", ""],
    "HeavySnowShowers":    ["", ""],
    "LightRain":           ["", ""],
    "LightShowers":        ["", ""],
    "LightSleet":          ["", ""],
    "LightSleetShowers":   ["", ""],
    "LightSnow":           ["", ""],
    "LightSnowShowers":    ["", ""],
    "PartlyCloudy":        ["", ""],
    "Sunny":               ["", ""],
    "ThunderyHeavyRain":   ["", ""],
    "ThunderyShowers":     ["", ""],
    "ThunderySnowShowers": ["", ""],
    "VeryCloudy":          ["", ""],
}

weather_symbol_codes = { # [     day,  night]
    "Unknown":             ["\\f00d", "\\f02e"],
    "Cloudy":              ["\\f002", "\\f086"],
    "Fog":                 ["\\f003", "\\f04a"],
    "HeavyRain":           ["\\f019", "\\f019"],
    "HeavyShowers":        ["\\f01a", "\\f01a"],
    "HeavySnow":           ["\\f064", "\\f064"],
    "HeavySnowShowers":    ["\\f01b", "\\f01b"],
    "LightRain":           ["\\f008", "\\f036"],
    "LightShowers":        ["\\f009", "\\f037"],
    "LightSleet":          ["\\f0b2", "\\f0b3"],
    "LightSleetShowers":   ["\\f006", "\\f034"],
    "LightSnow":           ["\\f065", "\\f066"],
    "LightSnowShowers":    ["\\f00a", "\\f038"],
    "PartlyCloudy":        ["\\f00c", "\\f083"],
    "Sunny":               ["\\f00d", "\\f077"],
    "ThunderyHeavyRain":   ["\\f010", "\\f03b"],
    "ThunderyShowers":     ["\\f00e", "\\f02c"],
    "ThunderySnowShowers": ["\\f06b", "\\f06c"],
    "VeryCloudy":          ["\\f013", "\\f013"],
}

moon_phase_symbols = {
    0: "",  1: "",  2: "",  3: "",  4: "",  5: "",  6: "",  7: "",
    8: "",  9: "", 10: "",  11: "", 12: "", 13: "", 14: "", 15: "",
    16: "", 17: "", 18: "", 19: "", 20: "", 21: "", 22: "", 23: "",
    24: "", 25: "", 26: "", 27: "", 28: "", 29: ""}

moon_phase_symbol_codes = {
    0: "\\f095", 1: "\\f096", 2: "\\f097", 3: "\\f098", 4: "\\f099", 5: "\\f09a",
    6: "\\f09b", 7: "\\f09c", 8: "\\f09d", 9: "\\f09e", 10:"\\f09f", 11:"\\f0a0",
    12:"\\f0a1", 13:"\\f0a2", 14:"\\f0a3", 15:"\\f0a4", 16:"\\f0a5", 17:"\\f0a6",
    18:"\\f0a7", 19:"\\f0a8", 20:"\\f0a9", 21:"\\f0aa", 22:"\\f0ab", 23:"\\f0ac",
    24:"\\f0ad", 25:"\\f0ae", 26:"\\f0af", 27:"\\f0a0", 28:"\\f0eb", 29:"\\f0d0"
}

icons = {
    "!t": "",  # "\\f055",
    "!f": "",  # "\\f053",
    "!x": weather_symbols,
    "!h": "",  # "\\f07a",
    "!p": "",  # "\\f084",
    "!o": "",  # "\\f03e",
    "!P": "",  # "\\f079",
    "!w": wind_directions,
    "!W": "",  # "\\f050",
    "!M": moon_phase_symbols,
    "!T": "",  # "\\f08d",
    "!S": "",  # "\\f051",
    "!s": "",  # "\\f052",
}

icon_codes = {
    "!t": "\\f055",
    "!f": "\\f053",
    "!x": weather_symbol_codes,
    "!h": "\\f07a",
    "!p": "\\f084",
    "!o": "\\f03e",
    "!P": "\\f079",
    "!w": wind_direction_codes,
    "!W": "\\f050",
    "!M": moon_phase_symbol_codes,
    "!T": "\\f08d",
    "!S": "\\f051",
    "!s": "\\f052",
}

default_parmap = {
    "!t": {'hdr': "temp",
           'units': "°C",
           'map': None},
    "!f": {'hdr': "temp_feel",
           'units': "°C",
           'map': None},
    "!x": {'hdr': "weather",
           'units': "",
           'map': weather_symbol_plain},
    "!h": {'hdr': "humidity",
           'units': "%",
           'map': None},
    "!p": {'hdr': "precip",
           'units': "mm",
           'map': None},
    "!o": {'hdr': "chance_precip",
           'units': "%",
           'map': None},
    "!P": {'hdr': "pressure",
           'units': "hPa",
           'map': None},
    "!w": {'hdr': "wind",
           'units': "km/h",
           'map': WindVector},
    "!M": {'hdr': "moon_day",
           'units': "d",
           'map': None},
    "!T": {'hdr': "localtime",
           'units': "",
           'map': datetime_from_hms},
    "!S": {'hdr': "sunrise",
           'units': "",
           'map': datetime_from_hms},
    "!s": {'hdr': "sunset",
           'units': "",
           'map': datetime_from_hms}
}

default_params = list(default_parmap.keys())

extra_parmap = {
    "!d": {'hdr': "daytime",
           'units': "",
           'map': is_day},
    "!W": {'hdr': "Wind",
           'units': "",
           'map': None}
}
extra_params = list(extra_parmap.keys())

default_xmobar_format = '%g!x %!t(%!f)<1: >.u %G<1: >!h %g!W<1: >%G<1: >!w<1: >.u %G<1: >!P<1: >.u'

default_format_map = {
    '<': '<fn={}>',
    '{': '<fc={}>',
    '\\': "\\x"
}

default_icon_map_hook = {
    '*': '<2:{}>'
}

format_sign_pairs = {
    '{': '}',
    '[': ']',
    '(': ')',
    '<': '>',
    '!': 'i',
}

default_config_paths = [
    "~/.config/xmobar_wttr",
    "~/.config/xmobar",
    "~/.xmobar_wttr",
    "~/.xmobar",
    "~/."
]
