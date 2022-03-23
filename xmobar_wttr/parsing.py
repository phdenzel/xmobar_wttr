"""
xmobar_wttr.parsing

@author: phdenzel

Everything for configs and command-line arguments.
Hierarchy:
    1) command-line arguments
    2) configs
    3) defaults
"""
import os
from argparse import ArgumentParser, RawTextHelpFormatter
from collections import deque
import yaml
import xmobar_wttr


def default_config_file(basename='xmobar_wttr.yml'):
    paths = xmobar_wttr.constants.default_config_paths
    for p in paths:
        p = os.path.expanduser(p)
        if not p.endswith("."):
            filename = os.path.join(p, basename)
        else:
            bn = '.' + basename
            p = os.path.dirname(p)
            filename = os.path.join(p, bn)
        if os.path.exists(filename):
            return filename
    return basename


def import_haskell_color_lib(path=None):
    """
    Parse a Haskell file and import all variables
    """
    color_lib = {}
    if path is None:
        path = xmobar_wttr.haskell_color_lib
    filepath = os.path.expanduser(path)
    if not os.path.exists(filepath):
        return color_lib
    with open(filepath, 'r') as f:
        lib_text = f.readlines()
    for line in lib_text:
        if '=' in line:
            v, c = line.split('=')
            color_lib[v.strip()] = c.strip().replace('"', "")
    xmobar_wttr.color_lib = color_lib
    return color_lib


def read_args():
    """
    Parse command-line arguments
    """
    from argparse import ArgumentParser, RawTextHelpFormatter
    p = ArgumentParser(prog='xmobar_wttr', formatter_class=RawTextHelpFormatter)
    
    p.add_argument("-c", "--config", dest="config_path", metavar="<path>",
                   type=str, default=default_config_file(),
                   help="Path to the config file")
    p.add_argument("-l", "--location", dest="location", metavar="<loc>",
                   type=str,
                   help="Location for which to pull information.")
    p.add_argument("-f", "--format", dest="xmobar_format", metavar="<format>",
                   type=str,
                   help="Format template for xmobarrc")
    p.add_argument("-o", "--output", dest="output_file", metavar="<path>",
                   type=str, default="/tmp/xmobar_wttr",
                   help="Path to the output file")
    p.add_argument("-s", "--section", dest="config_section", metavar="<section>",
                   type=str, default="Defaults",
                   help="Section in the yaml file to be parsed")
    p.add_argument("-p", "--pars", dest="params", metavar="<par-list>",
                   nargs="+", required=False,
                   help="Select parameters to be fetched from wttr.in " \
                   "\nexcluded parameters are not available in xmobar " \
                   "template format")
    p.add_argument("-v", "--verbose", dest="verbose", action="store_true",
                   help="Run program in verbose mode")
    args = p.parse_args()
    xmobar_wttr.parser = p
    xmobar_wttr.args = args
    return p, args


def load_args(args=None):
    """
    Load command-line arguments into main module

    Kwargs:
        args <Namespace>
    """
    if args is None:
        args = xmobar_wttr.args
    for a in vars(args):
        val = getattr(args, a)
        if val is not None:
            setattr(xmobar_wttr, a, val)


def read_configs(config_path=None):
    """
    Parse the configuration file

    Kwargs:
        config_path <str>
    """
    if config_path is None:
        config_path = xmobar_wttr.args.config_path
    with open(config_path, 'r') as c:
        configs = yaml.safe_load(c)
    xmobar_wttr.configs = configs


def load_configs(config_section='Defaults'):
    """
    Load section from parsed configuration file into main module
    """
    confs = xmobar_wttr.configs[config_section]
    for k in confs:
        if confs[k] is not None:
            setattr(xmobar_wttr, k, confs[k])


def parse_fields(data_fields,
                 _format: str=None,
                 parmap: dict=None,
                 icon_map: dict=None):
    """
    Parse format string and insert fetched values or icons
    """
    if _format is None:
        _format = xmobar_wttr.xmobar_format
    if parmap is None:
        parmap = xmobar_wttr.parmap
    if icon_map is None:
        icon_map = xmobar_wttr.utils.IconMap()
    string_fields = []
    fields = _format.split("%")
    for f in fields:
        string = []
        pointer = lookahead = 0
        cache = {}
        for pointer, f_p in enumerate(f):
            # replace from cache
            if pointer in cache:
                string.append(cache[pointer])
                continue
            # graphical replacement
            if f_p in ['G', 'g']:
                lookahead = pointer + 1
                while f[lookahead] != "!":
                    lookahead += 1
                if lookahead > len(f)-1:
                    break
                f_p = icon_map(f[pointer]+f[lookahead]+f[lookahead+1])
                # lowercase g skips the value
                if f[pointer] == 'g':
                    cache[lookahead] = ''
                    cache[lookahead+1] = ''
            # value replacement
            elif f_p == "!":
                if pointer >= len(f):
                    continue
                f_p = str(parmap[f[pointer]+f[pointer+1]]['val'])
                cache[pointer+1] = ''
                lookahead = pointer
                # units replacement
                while lookahead < len(f):
                    if f[lookahead:min(lookahead+2,len(f))] == '.u':
                        cache[lookahead] = parmap[f[pointer]+f[pointer+1]]['units']
                        cache[min(lookahead+1,len(f)-1)] = ''
                        break
                    lookahead += 1
            string.append(f_p)
            pointer += 1
        string_fields.append("".join(string))
    field_string = "".join(string_fields)
    return field_string


def findall(pattern, string):
    """
    Find all indices of occurrences of a pattern substring
    """
    i = string.find(pattern)
    while i != -1:
        yield i
        i = string.find(pattern, i+1)


def parse_format(field_string, format_map: dict=None):
    """
    Parse format string and format data
    """
    if format_map is None:
        format_map = xmobar_wttr.format_map
    for key in format_map:
        if key not in xmobar_wttr.constants.format_sign_pairs:
            # simply replace all occurences
            field_string = field_string.replace(key, format_map[key])
            continue
        string_cache = []
        pattern = format_map[key][1:format_map[key].index("=")]
        # closing key and format
        akey = xmobar_wttr.constants.format_sign_pairs[key]
        afmt = f"</{pattern}>"
        # all occurrences
        key_idcs = findall(key, field_string)
        akey_idcs = findall(akey, field_string)
        # end of previous replacement
        endian = 0
        for kidx, akidx in zip(key_idcs, akey_idcs):
            # everything inbetween
            content = field_string[kidx+1:akidx]
            arg, content = content.split(":")
            if arg in xmobar_wttr.color_lib:
                arg = xmobar_wttr.color_lib[arg]
            # opening format
            fmt = format_map[key].format(arg)
            # first partition at occurrence
            partition = field_string[:kidx]
            # move relevant partitions to cache
            string_cache.append(partition[endian:])
            string_cache.append("".join([fmt, content, afmt]))
            # update endian
            endian = akidx+1
        string_cache.append(field_string[endian:])
        field_string = "".join(string_cache)
    return field_string


if __name__ == "__main__":
    import_haskell_color_lib()
