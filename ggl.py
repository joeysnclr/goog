#!/usr/bin/env python
import sys

if len(sys.argv) == 1:
    print("Please enter a search string")
    quit()
searchString = ""
for arg in sys.argv[1:]:
    searchString += arg + " "
print(searchString)
