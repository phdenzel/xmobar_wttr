"""
xmobar_wttr.fetch

@author: phdenzel
"""
from datetime import datetime
import requests
import xmobar_wttr
import xmobar_wttr.parsing as xwp

class LocationError(ValueError):
    pass

class ServiceError(ValueError):
    pass


def fetch_wttr_data(wttr_url: str='https://wttr.in/', location: str=None,
                    fetch_params: list=None, sep_char: str="|",
                    verbose=False) -> str:
    if location is None:
        location = xmobar_wttr.location
    if fetch_params is None:
        fetch_params = [p.replace('!', '') for p in xmobar_wttr.params
                        if p in xmobar_wttr.constants.default_params]
    loc_uri = requests.utils.requote_uri(location)
    params = sep_char.join([f"%{p}" for p in fetch_params])
    param_uri = '?format="{}"'.format(params)
    url = "".join([wttr_url, loc_uri, param_uri])
    if verbose:
        print(url)
    resp = requests.get(url)
    if resp.status_code == 200:
        return url, resp.text[1:-1]
    elif resp.status_code == 404:  # page not found
        raise LocationError("Location not found (404)! "
                            "Try excluding parameters T, S, and s.\n"
                            "Response: {}".format(resp.text))
    elif resp.status_code == 503:  # service unavailable
        raise ServiceError("Service currently unavailable (503)! "
                           "Response: {}".format(resp.text))


def strip_units(data_fields: list, parmap: dict=None):
    if parmap is None:
        parmap = xmobar_wttr.utils.get_parmap()
    for i, p in enumerate(parmap.keys()):
        if isinstance(parmap[p], dict) and 'units' in parmap[p]:
            units = parmap[p]['units']
        else:
            units = parmap[p]
        data_fields[i] = data_fields[i].replace(units, '')
    return data_fields


def filter_fields(data_fields: list, parmap: dict=None):
    if parmap is None:
        parmap = xmobar_wttr.utils.get_parmap()
    for i, p in enumerate(parmap.keys()):
        if isinstance(parmap[p], dict) and 'map' in parmap[p]:
            filter_map = parmap[p]['map']
        else:
            filter_map = parmap[p]
        if isinstance(filter_map, dict):
            data_fields[i] = filter_map[data_fields[i]]
        elif callable(filter_map):
            data_fields[i] = filter_map(data_fields[i])
    return data_fields


def type_fields(data_fields: list, parmap: dict=None):
    if parmap is None:
        parmap = xmobar_wttr.utils.get_parmap()
    for i, p in enumerate(parmap.keys()):
        df = data_fields[i]
        if isinstance(df, str):
            try:
                data_fields[i] = float(df) if '.' in df else int(df)
            except Exception:
                pass
    return data_fields


def render_fields(data_fields: list,
                  _format: str=None,
                  format_map: dict=None):
    if _format is None:
        _format = xmobar_wttr.xmobar_format
    if format_map is None:
        format_map = xmobar_wttr.format_map
    field_string = xwp.parse_fields(data_fields, _format=_format)
    field_string = xwp.parse_format(field_string, format_map=format_map)
    return field_string


if __name__ == "__main__":
    url, data = fetch_wttr_data(sep_char='|')
    dta_fields = data.split('|')
    dta_fields = strip_units(dta_fields)
    dta_fields = filter_fields(dta_fields)
    dta_fields = convert_fields(dta_fields)
    parmap = xmobar_wttr.utils.update_parmap()
    field_string = render_fields(dta_fields,
                                 _format=xmobar_wttr.xmobar_format,
                                 format_map=xmobar_wttr.format_map)
    print(dta_fields, field_string)
