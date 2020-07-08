# Google CLI

A simple and minimalist command line interface for executing everyday google searches.

# Installation
Download the goog file via curl and output it into a directory in your PATH (in my case ~/bin)
[see here](https://linuxize.com/post/how-to-add-directory-to-path-in-linux/)

`curl "https://raw.githubusercontent.com/joeysnclr/google-cli/master/goog" --output ~/bin/goog`

Use chmod to make the goog file executable

`chmod +x ~/bin/goog`

# Usage
Simply type `goog` then anything you would like to search for.

Example:

`goog how to reverse a linked list`

# Uninstall
To uninstall goog all you have to do is remove the file from your path directory

`rm ~/bin/goog`
