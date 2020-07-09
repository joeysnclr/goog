# Srch-CLI

A simple and minimalist command line interface for executing everyday web searches.

# Installation

Download the `srch` file via curl and output it into a directory in your PATH (in my case ~/bin)
[see here](https://linuxize.com/post/how-to-add-directory-to-path-in-linux/)

`curl "https://raw.githubusercontent.com/joeysnclr/srch-cli/master/srch" --output ~/bin/srch`

Use chmod to make the `srch` file executable

`chmod +x ~/bin/srch`

# Usage

Simply type `srch` then anything you would like to search for.

Example:

`srch how to reverse a linked list`

# Config

**Change Search Engine**

The `SRCH_ENGINE` environment variable controls the search engine used.
To change the default search engine to something other than google, add `export SRCH_ENGINE=<engine>`
to your `.bashrc`, `.zshrc`, etc. file where <engine> is replaced with one of the following values.

Other search engines:
 - duckduckgo


# Uninstall
To uninstall srch-cli all you have to do is remove the file from your PATH directory

`rm ~/bin/srch`
