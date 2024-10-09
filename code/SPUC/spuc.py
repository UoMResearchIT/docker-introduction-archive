import os
import sys
from typing import Union
from datetime import datetime

import argparse
import print_format as pf

import uvicorn
from fastapi import FastAPI
from starlette.responses import FileResponse

units = None
app = FastAPI()

if os.environ.get('EXPORT') == 'True':
    @app.get("/sightings/")
    def chart():
        return FileResponse("unicorn_sightings.txt")

@app.put("/unicorn_spotted/")
def unicorn_sighting(location: str, brightness: float):

    # --------------------------------------------------------------------------
    # Write the sighting to a file and print to the console
    with open("unicorn_sightings.txt", "a") as unicorn_file:
        # Append the location to the file
        line = pf.get_str(location, brightness, units)
        unicorn_file.write(line)

        # Print the line to the console
        console_line = f":::: ({datetime.now()}) Unicorn spotted at {location}!! Brightness: {brightness} {units} ::::"
        print(console_line)
        sys.stdout.flush()

    return {"message": "Unicorn sighting recorded!"}


if __name__ == "__main__":
    # --------------------------------------------------------------------------
    # Parse the command line arguments
    parser = argparse.ArgumentParser(description="Run the unicorn sighting API")
    parser.add_argument(
        "--units",
        type=str,
        default="iuhc",
        choices=["iuhc", "iulu"],
        help="The units to use for the unicorn brightness",
    )
    args = parser.parse_args()

    # --------------------------------------------------------------------------
    # Set the units
    units = args.units
    if units == "iuhc":
        unit_long_name = "Imperial Unicorn Hoove Candles"
    elif units == "iulu":
        unit_long_name = "Intergalactic Unicorn Luminiocity Units"

    # --------------------------------------------------------------------------
    # Print the initialization message
    logo = r"""
            \\
             \\
              \\
               \\
                >\/7
            _.-(6'  \
           (=___._/` \            ____  ____  _    _  ____
                )  \ |           / ___||  _ \| |  | |/ ___|
               /   / |           \___ \| |_) | |  | | |
              /    > /            ___) |  __/| |__| | |___
             j    < _\           |____/|_|    \____/ \____|
         _.-' :      ``.
         \ r=._\        `.       Space Purple Unicorn Counter
        <`\\_  \         .`-.
         \ r-7  `-. ._  ' .  `\
          \`,      `-.`7  7)   )
           \/         \|  \'  / `-._
                      ||    .'
                       \\  (
                        >\  >
                    ,.-' >.'
                   <.'_.''
                     <'
    """
    print(logo)
    print(f"Initializing SPUC...")
    print(f"Units set to {unit_long_name} [{units}].")
    sys.stdout.flush()

    # --------------------------------------------------------------------------
    # Run the API
    uvicorn.run(app, host="0.0.0.0", port=80, log_level="warning")
