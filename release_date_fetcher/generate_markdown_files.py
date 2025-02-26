from typing import List

import numpy as np
import pandas as pd
import requests
from packaging.version import Version

# curl -s "https://data.services.jetbrains.com/products?release.type=release"  | jq -r '.[] | "\"\(.code)\",  # \(.name)"' | sort
IDES = [
    "AC",  # AppCode
    "CL",  # CLion
    "GO",  # GoLand
    "IIU",  # IntelliJ IDEA Ultimate
    "PCP",  # PyCharm Professional Edition
    "PS",  # PhpStorm
    "RC",  # ReSharper C++
    "RD",  # Rider
    "RM",  # RubyMine
    "RS",  # ReSharper
    "WS",  # WebStorm

    # We leave the below IDEs commented out, because...
    #   "IIC",  # IntelliJ IDEA Community Edition - ...the release dates are identical to IIU (as of 2021-01-01)
    #   "PCC",  # PyCharm Community Edition       - ...longer release history in PCP; otherwise nearly identical dates.
]


def get_data(ides: List[str]):
    ide_str = "%2C".join(ides)
    url = f'https://data.services.jetbrains.com/products?code={ide_str}&release.type=release'
    return requests.get(url=url).json()


for ide in get_data(IDES):
    code = ide['code']
    name = ide['name']

    # Create a DataFrame to store the dates
    df = pd.DataFrame()

    print(f'Processing releases for {code} -> {name}')
    for release in ide['releases']:
        # Extract the version information for this particular release.
        # We want the `major` version, and `minor.patch`, as that is how the table is formatted.
        version = Version(release['version'])
        major = str(version.major)
        minor_patch = f'{version.minor}.{version.micro}'

        # Set the date for the given `major` & `minor.patch` cell in the DataFrame.
        # The `minor.patch` will be the rows, and the `major` will be the columns.
        df.at[minor_patch, major] = release['date']

    # Change the column names to ints before sorting
    df.columns = [int(x) for x in df.columns]
    
    # Ensure the index is treated as numeric for sorting purposes.
    # This will ensure that the ordering is `1.3 -> 2.0 -> ... -> 10.0 -> 11.0`
    # (as opposed to `1.3 -> 10.0 -> 11.0 -> ... -> 2.0`)
    df.index = pd.to_numeric(df.index, errors='coerce')

    # Sort the rows and columns
    df = df.reindex(sorted(df.columns), axis=1).sort_index()

    # Replace all the `nan` cell values with empty string - frankly, it looks nicer IMO.
    df = df.replace(np.nan, '', regex=True)

    # Get the DataFrame as Markdown, formatting the first column with 1 decimal place.
    # The formatting is because for the minor version `X`, we want to see `X.0` instead
    # of just `X` in the output.
    markdown_table = df.to_markdown(floatfmt=('.1f',))

    # Write out to a file
    with open(file=f'../ides/{name.replace(" ", "_")}_Release_Dates.md', mode='w') as f:
        f.write(f'# {name} Release Dates\n')
        f.write(f'Below you will find a table of the JetBrains {name} Release Dates.\n')
        f.write("\n")
        f.write(markdown_table)
