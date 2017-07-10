# pytext
Simple python text filter


# Description

This script is basically just a simple proof of concept that uses ANSI escape characters to add color and style to text in a shell environment.

- Make shell output bold, italic, underlined and/or strikethrough
- Color shell output with basic colors like red, yellow, green, blue, etc.
- Apply filters to randomly stylize individual characters

=======

This is sort of just a fun little script with no real legitimate purpose other than to document a couple useful Python abilities.  Personally, I'm uploading this as somewhat of a cheatsheet for the following concepts/python use cases:

- Creating an easy/simple options menu (using the optparse module)
- Using ANSI escape characters to stylize shell output
- Dynamically accepting either traditional arguments as input or piped data/stdin as input


```
./pytext.py -h
Usage: ./pytext.py [options] <text>
Usage: ./pytext.py <text> [options]
Usage: <command output> | ./pytext.py [options]

Valid filters: patriotic, retro, wtf
Valid colors: blue, purple, yellow, green, teal, invisible, red

Options:
  -h, --help                  show this help message and exit
  -b, --bold                  bold display
  -i, --italic                italic display
  -u, --underline             underline display
  -s, --strike                strikethrough display
  -r, --reverse               flip background and foreground colors
  -f FILTER, --filter=FILTER  enter a text filter
  -c COLOR, --color=COLOR     enter a static text color
```
