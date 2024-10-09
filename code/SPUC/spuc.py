from typing import Union
from datetime import datetime
import argparse

import uvicorn
from fastapi import FastAPI

units = None
app = FastAPI()

@app.put("/unicorn_spotted/")
def unicorn_sighting(location: str, weight: float):

    # --------------------------------------------------------------------------
    # Write the sighting to a file and print to the console
    
    with open("unicorn_sightings.txt", "a") as unicorn_file:
        # Append the location to the file
        line = f"{datetime.now()}, {location}, {weight} {units}\n"
        unicorn_file.write(line)

        # Print the line to the console
        console_line = f":::: ({datetime.now()}) Unicorn spotted at {location}!! Weight: {weight} {units} ::::"
        print(console_line)
    
    return {"message": "Unicorn sighting recorded!"}


if __name__ == "__main__":

    # --------------------------------------------------------------------------
    # Parse the command line arguments
    
    parser = argparse.ArgumentParser(description="Run the unicorn sighting API")
    parser.add_argument("--units",
                        type=str,
                        default="imperial",
                        choices=["imperial", "metric"],
                        help="The units to use for the weight")
    args = parser.parse_args()

    # --------------------------------------------------------------------------
    # Set the units
    
    if args.units == "imperial":
        units = "space-lbs"
    else:
        units = "kg"

    # --------------------------------------------------------------------------
    # Run the API
    
    uvicorn.run(app, host="0.0.0.0", port=80)
