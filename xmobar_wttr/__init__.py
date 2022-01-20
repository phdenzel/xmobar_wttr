"""
xmobar_wttr.__init__

@author: phdenzel
"""
from types import ModuleType
import xmobar_wttr
import xmobar_wttr.constants
import xmobar_wttr.parsing
import xmobar_wttr.utils
import xmobar_wttr.fetch


config_path = 'xmobar_wttr.yml'
config_section = 'Defaults'
location = None
output_file = '/tmp/xmobar_wttr'
params = xmobar_wttr.constants.default_params
parmap = xmobar_wttr.constants.default_parmap
xmobar_format = xmobar_wttr.constants.default_xmobar_format
format_map = xmobar_wttr.constants.default_format_map
icon_map_hook = xmobar_wttr.constants.default_icon_map_hook
haskell_color_lib = ""
color_lib = {}

parser, args = xmobar_wttr.parsing.read_args()
xmobar_wttr.parsing.read_configs()
xmobar_wttr.parsing.load_configs(args.config_section)
xmobar_wttr.parsing.load_args()


def env():
    """
    All variables from xmobar_wttr module as dictionary
    """
    env_d = {}
    for vstr in dir(xmobar_wttr):
        if vstr in ('configs', 'args', 'parser'):
            continue
        v = getattr(globals()['xmobar_wttr'], vstr)
        if not vstr.startswith("__") and not isinstance(v, (type, ModuleType)) and not callable(v):
            env_d[vstr] = v
    return env_d
