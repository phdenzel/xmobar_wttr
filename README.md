

# Prerequisites

This program mainly uses following python3 modules

-   requests
-   pyyaml


# Install

    pip install xmobar-wttr

For installing from source, clone the repository, and run

    cd xmobar_wttr
    python setup.py install

or create a virtual environment with

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


# Configuration

`xmobar_wttr` works with both command-line arguments as well as YAML
configuration files (the first takes precedence over the latter).  To
set your desired defaults edit the configuration file
`xmobar_wttr.yml` and place it in either 

-   `~/.config/xmobar_wttr/xmobar_wttr.yml`
-   `~/.config/xmobar/xmobar_wttr.yml`
-   `~/.xmobar_wttr/xmobar_wttr.yml`
-   `~/.xmobar_wttr.yml`


# Notation

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Notation</th>
<th scope="col" class="org-left">\*Description</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">%[par]</td>
<td class="org-left">parameter value</td>
</tr>


<tr>
<td class="org-left">%g[par]</td>
<td class="org-left">render parameter only as icon</td>
</tr>


<tr>
<td class="org-left">%G[par]</td>
<td class="org-left">prefix icon to parameter value</td>
</tr>


<tr>
<td class="org-left">.u</td>
<td class="org-left">append units of previous parameter</td>
</tr>
</tbody>
</table>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Format map</th>
<th scope="col" class="org-left">Result</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left"><2:&#x2026;></td>
<td class="org-left"><fn=2>&#x2026;</fn></td>
</tr>


<tr>
<td class="org-left">{#dedede:&#x2026;}</td>
<td class="org-left"><fc=#dedede>&#x2026;</fc></td>
</tr>


<tr>
<td class="org-left">\\&#x2026;</td>
<td class="org-left">\x&#x2026;</td>
</tr>


<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>
</table>

