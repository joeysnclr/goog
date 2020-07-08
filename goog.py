#!/usr/bin/env python
import sys
import webbrowser

if len(sys.argv) == 1:
    print("Please enter a search string")
    quit()
searchString = ""
for arg in sys.argv[1:]:
    searchString += arg + " "
searchURL = "https://www.google.com/search?q={}".format(searchString)
print("Opening a Google search for: {}".format(searchString))
webbrowser.open(searchURL)
