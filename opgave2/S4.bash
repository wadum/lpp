#!/usr/bin/bash

# Initialize variables with the width and height of the rectangle
WIDTH=6
LENGTH=7

# Calculate the surface of the rectangle
AREA=`expr $WIDTH \* $LENGTH`

# Print the value of the surface
echo "The surface of a rectangle with width $WIDTH and length $LENGTH is $AREA"