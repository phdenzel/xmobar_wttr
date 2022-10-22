"""
xmobar_wttr.__main__

@author: phdenzel
"""
import os
import requests
import xmobar_wttr
import xmobar_wttr.fetch as xwf


def fallback():
    tmpf = xmobar_wttr.output_file
    if os.path.exists(tmpf) and os.stat(tmpf).st_size != 0:
        xmobar_line = xmobar_wttr.utils.read_tail1(tmpf)
    else:
        xmobar_line = ""
    return xmobar_line


def main(verobse=False):
    sep_char = '|'
    verbose = xmobar_wttr.args.verbose
    if verbose:
        print("Config file:\t", xmobar_wttr.config_path)
        print("Output file:\t", xmobar_wttr.output_file)
    # fetch data
    try:
        url, data = xwf.fetch_wttr_data(sep_char=sep_char)
    except (xwf.LocationError, xwf.ServiceError,
            requests.exceptions.ConnectionError) as e:
        xmobar_line = fallback()
        print(xmobar_line)
        return
    if verbose:
        print("URL:        \t", url)
        print("Response:   \t", data)
    if 'nknown location' in data or 'please try' in data:
        xmobar_line = fallback()
        print(xmobar_line)
        return
    # transmute data fields
        
    dta_fields = data.split(sep_char)
    if verbose:
        print("Data fields:\t", dta_fields)
    dta_fields = xwf.strip_units(dta_fields)
    dta_fields = xwf.filter_fields(dta_fields)
    dta_fields = xwf.type_fields(dta_fields)
    # update module variables
    xmobar_wttr.utils.update_parmap(dta_fields, xmobar_wttr.params)
    xmobar_wttr.utils.set_localtime(xmobar_wttr.parmap)
    xmobar_wttr.parsing.import_haskell_color_lib(xmobar_wttr.haskell_color_lib)
    # construct xmobar line
    xmobar_line = xwf.render_fields(dta_fields,
                                    _format=xmobar_wttr.xmobar_format,
                                    format_map=xmobar_wttr.format_map)
    with open(xmobar_wttr.output_file, 'a') as f:
        f.write(xmobar_line)
        f.write('\n')
    xmobar_line = xmobar_wttr.utils.read_tail1(xmobar_wttr.output_file)
    print(xmobar_line)


if __name__ == "__main__":
    main()
