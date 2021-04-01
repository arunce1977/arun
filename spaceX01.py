#!/usr/bin/env python3
"""SpaceX data"""

# imports always go at the top of your code
import requests
import pyexcel


def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get("https://api.spacexdata.com/v3/launches")

    # display the methods available to our new object
    #print( dir(r))

    mylist =[]

    for spacex in r.json():
        d ={"space_attempt":spacex.get("flight_number"),"rocket_name":spacex.get("rocket_name")}
        mylist.append(d)
    filename = input("\nWhat is the name of the *.xls file?");
    pyexcel.save_as(records=mylist, dest_file_name=f'{filename}.xls')


main()

