

# Prerequisites

This program mainly uses following python3 modules

-   requests
-   pyyaml


# Install

For now, this program runs only from source. To install, clone the
repository, and create a virtual environment with

    pipenv install
    pipenv install -e .

To activate the virtual environment run

    pipenv shell

or start every command with `pipenv run`.


# Usage

    usage: xmobar_wttr [-h] [-c <path>] [-l <loc>] [-f <format>] [-o <path>] [-s <section>] [-p <par-list> [<par-list> ...]] [-v]
    
    optional arguments:
      -h, --help            show this help message and exit
      -c <path>, --config <path>
    			Path to the config file
      -l <loc>, --location <loc>
    			Location for which to pull information.
      -f <format>, --format <format>
    			Format template for xmobarrc
      -o <path>, --output <path>
    			Path to the output file
      -s <section>, --section <section>
    			Section in the yaml file to be parsed
      -p <par-list> [<par-list> ...], --pars <par-list> [<par-list> ...]
    			Select parameters to be fetched from wttr.in
    			excluded parameters are not available in xmobar template format
      -v, --verbose         Run program in verbose mode


# Notation

  `%[par]`       -> parameter value
  `%g[par]`      -> render parameter only as icon
  `%G[par]`      -> prefix icon to parameter value
  `.u`           -> append units of previous parameter
Format map:
  `<2...>`       -> `<fn=2>...</fn>`
  `{#dedede...}` -> `<fc=#dedede>...</fc>`
  `\...`         -> `\x...`
