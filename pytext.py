#!/usr/bin/python

import sys
from random import randint
import optparse

string = ''
colornums = []
filters = {
    'retro': [1,2,3,6,33,36],
    'patriotic': [5,34,91],
    'wtf': [1,2,3,4,5,6,7,31,32,33,34,35,36,41,42,43,44,45,46,90,91,92,93,94,95,100,101,102,103,104,105,106],
}
colors = {
    'red': 91,
    'green': 92,
    'yellow': 93,
    'blue': 34,
    'purple': 95,
    'teal': 36,
    'invisible': 8,
}

# Get Options
parser = optparse.OptionParser()

parser.add_option('-b', '--bold',
                  dest="bold",
                  default=False,
                  action="store_true",
                  help='bold display',
                 )
parser.add_option('-i', '--italic',
                  dest="italic",
                  default=False,
                  action="store_true",
                  help='italic display',
                 )
parser.add_option('-u', '--underline',
                  dest="underline",
                  default=False,
                  action="store_true",
                  help='underline display',
                 )
parser.add_option('-s', '--strike',
                  dest="strike",
                  default=False,
                  action="store_true",
                  help='strikethrough display',
                 )
parser.add_option('-r', '--reverse',
                  dest="reverse",
                  default=False,
                  action="store_true",
                  help='flip background and foreground colors',
                 )
parser.add_option('-f', '--filter',
                  dest="filter",
                  default='none',
                  help='enter a text filter',
                 )
parser.add_option('-c', '--color',
                  dest="color",
                  default='none',
                  help='enter a static text color',
                 )
parser.set_usage("Usage: ./pytext.py [options] <text>\nUsage: ./pytext.py <text> [options]\nUsage: <command output> | ./pytext.py [options]\n\nValid filters: %s\nValid colors: %s" % (', '.join(filters.iterkeys()), ', '.join(colors.iterkeys())))
options, remainder = parser.parse_args()

bold = options.bold
italic = options.italic
underline = options.underline
strike = options.strike
reverse = options.reverse
filter = options.filter
color = options.color

# Figure out if there is stdin
if not sys.stdin.isatty():
    # Accept stdin, use piped input
    data = sys.stdin.readlines()
    string = ''.join(data).strip("\n")
elif len(remainder) > 0:
    # Use arguments
    string = remainder[0]
else:
    print "No input. Use -h or --help for help menu."
    sys.exit()

if color == 'none':
    statcolor = 0
elif color in colors:
    for color_name in colors:
	if color == color_name:
	    statcolor = colors[color_name]
	    break
else:
    print "Invalid color '%s'" % color
    print "Valid colors: %s" % ', '.join(colors.iterkeys())
    sys.exit()

if filter == 'none':
    colornums = []
elif filter in filters:
    for filter_name in filters:
	if filter == filter_name:
	    colornums = filters[filter_name]
	    break
else:
    print "Invalid filter name '%s'" % filter
    print "Valid filters: %s" % ', '.join(filters.iterkeys())
    sys.exit()

for char in string:
    str = ''
    # if color option
    if not statcolor == 0:
	if reverse:
	    if 30 <= statcolor <= 36 or 90 <= statcolor <= 96:
		str = '\033[%sm' % (statcolor + 10)
	    elif 40 <= statcolor <= 46 or 100 <= statcolor <= 106:
		str = '\033[%sm' % (statcolor - 10)
	else:
	    str = '\033[%sm' % statcolor
    # if filter option
    elif len(colornums) > 0:
	colornum = colornums[randint(0,len(colornums) - 1)]
        if reverse:
            if 30 <= colornum <= 36 or 90 <= colornum <= 96:
                str = '\033[%sm' % (colornum + 10)
            elif 40 <= colornum <= 46 or 100 <= colornum <= 106:
                str = '\033[%sm' % (colornum - 10)
        else:
            str = '\033[%sm' % colornum
    # other options
    if bold:
	str = '\033[1m%s' % str
    if italic:
        str = '\033[3m%s' % str
    if underline:
        str = '\033[4m%s' % str
    if strike:
        str = '\033[9m%s' % str
    sys.stdout.write('%s%s\033[0m' % (str, char))
print ''
