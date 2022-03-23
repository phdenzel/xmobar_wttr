# -*- coding: utf-8 -*-
"""
xmobar_wttr.utils

@author: phdenzel
"""
import os
from datetime import datetime
import xmobar_wttr


def get_parmap():
    """
    The parmap with only selected parameters

    Note:
        see xmobar_wttr.constants.default_parmap
    """
    defaults = xmobar_wttr.constants.default_parmap
    params = [p for p in defaults if p in xmobar_wttr.params]
    return {p: defaults[p] for p in params if p in defaults}

def update_parmap(data_fields: list, params: list=None):
    """
    The parmap with all parameters and its values
    """
    defaults = xmobar_wttr.constants.default_parmap
    if params is None:
        params = xmobar_wttr.params
    params_diff = [p for p in params if p not in defaults]
    params = [p for p in params if p not in params_diff]
    xmobar_wttr.parmap = {
        key: {**xmobar_wttr.parmap[key], **dict(val=data_fields[i])}
        for i, key in enumerate(params)}
    for key in params_diff:
        xmobar_wttr.parmap[key] = xmobar_wttr.constants.extra_parmap[key]
        xmobar_wttr.parmap[key]['val'] = \
            xmobar_wttr.constants.extra_parmap[key]['map']()

def get_parmap_val(key: str, parmap: dict=None):
    """
    Getter for the parmap key value
    """
    if parmap is None:
        parmap = xmobar_wttr.parmap
    if key in parmap and 'val' in parmap[key]:
        return parmap[key]['val']
    return None


def read_tail1(filename, sep=b"\n"):
    """
    Efficiently read last line of a file
    """
    with open(filename, "rb") as f:
        tail = f.readlines()[-1]
    return tail.decode('utf-8')[:-1]


def datetime_from_hms(hmsstr):
    """
    Datetime object from an hour:minute:seconds string
    """
    today = datetime.now().astimezone()
    if len(hmsstr) <= 8:
        dt = datetime.strptime(hmsstr, '%X').replace(
            today.year, today.month, today.day, tzinfo=today.tzinfo)
    elif len(hmsstr) <= 16:
        dt = datetime.strptime(hmsstr, '%X%z').replace(
            today.year, today.month, today.day)
    return dt

def default_season_d(key):
    """
    Default estimates for sunrise and sundown depending on the season
    """
    if key == 'spring':
        return (datetime.today().replace(hour=6, minute=30).astimezone(),
                datetime.today().replace(hour=20, minute=45).astimezone())
    elif key == 'summer':
        return (datetime.today().replace(hour=6, minute=15).astimezone(),
                datetime.today().replace(hour=21, minute=30).astimezone())
    elif key == 'fall':
        return (datetime.today().replace(hour=7, minute=15).astimezone(),
                datetime.today().replace(hour=17, minute=15).astimezone())
    elif key == 'winter':
        return (datetime.today().replace(hour=7, minute=50).astimezone(),
                datetime.today().replace(hour=17, minute=35).astimezone())
    else:
        raise ValueError(
            "Not a valid key, use 'spring', 'summer', 'fall', or 'winter'")

def default_seasonal_d(now: datetime=None):
    if now is None:
        doy = datetime.today().timetuple().tm_yday
    else:
        doy = now.timetuple().tm_yday
    spring = range(80, 172)
    summer = range(172, 264)
    fall = range(264, 355)
    if doy in spring:
        return default_season_d('spring')
    elif doy in summer:
        return default_season_d('summer')
    elif doy in fall:
        return default_season_d('fall')
    else:
        return default_season_d('winter')

def is_day():
    parmap = xmobar_wttr.parmap
    if "T" in parmap:
        now = parmap["T"]["val"]
    else:
        now = datetime.now().astimezone()
    if "S" in parmap and "s" in parmap:
        sunrise = parmap["S"]["val"]
        sunset = parmap["s"]["val"]
    else:
        sunrise, sunset = default_seasonal_d(now)
    return sunrise < now < sunset

def set_localtime(parmap: dict=None):
    if parmap is None:
        if "T" in xmobar_wttr.parmap and "val" in xmobar_wttr.parmap["T"]:
            lt = xmobar_wttr.parmap["T"]["val"]
        else:
            lt = datetime.now().astimezone()
    elif "T" in parmap and "val" in parmap["T"]:
        lt = parmap["T"]["val"]
    else:
        lt = datetime.now().astimezone()
    xmobar_wttr.localtime = lt


class WindVector(object):
    def __init__(self, vector_str):
        self.vector_str = vector_str
        if self.vector_str[0] not in xmobar_wttr.constants.wind_directions:
            self.vector_str = ' {}'.format(self.vector_str)

    @property
    def arrow(self):
        return self.vector_str[0]

    @property
    def direction(self):
        return xmobar_wttr.constants.wind_directions[self.vector_str[0]]

    @property
    def direction_icon(self):
        return xmobar_wttr.constants.wind_directions[self.direction]

    @property
    def mag(self):
        return self.vector_str[1:]

    def __str__(self):
        return '{}'.format(self.mag)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.direction)

    def __eq__(self, other):
        if isinstance(other, str):
            return self.direction == other
        return self.arrow == other.arrow


class IconMap(object):
    """ Mapping object for all parameter keys """
    @property
    def keys(self):
        return xmobar_wttr.constants.default_params \
            + xmobar_wttr.constants.extra_params
    @property
    def icons(self):
        return xmobar_wttr.constants.icons

    def __iter__(self):
        return iter(self.keys)

    def wrap_hook(self, icon, *hooks):
        for h in hooks:
            icon = h.format(icon)
        return icon

    def get_icon(self, par, val):
        icons = self.icons[par]
        if isinstance(icons, dict):
            icon = icons[val]
            if isinstance(icon, list):
                icon = icon[~is_day()]
        elif isinstance(icons, list):
            icon = icons[~is_day()]
        else:
            icon = icons
        return icon

    def __call__(self, key, parmap: dict=None, hooks: dict=None):
        if parmap is None:
            parmap = xmobar_wttr.parmap
        if hooks is None:
            hooks = xmobar_wttr.icon_map_hooks
        par = key[1:]
        val = get_parmap_val(par)
        icon = self.get_icon(par, val)
        par_hooks = [hooks[k] for k in [par, "*"] if k in hooks]
        icon = self.wrap_hook(icon, *par_hooks)
        return icon


if __name__ == "__main__":
    pass
