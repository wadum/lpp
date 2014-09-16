#!/usr/bin/bash

#Create files of random length
NUMFILES=5
COUNT=0
RND=0

# Create files
while [ "$COUNT" -lt $NUMFILES ]
do
	let "RND += `expr $RANDOM`"
	seq 1 $RND > "random$COUNT"
	let "COUNT += 1"
done

# Zip compress files
COUNT=0
while [ "$COUNT" -lt $NUMFILES ]
do
	gzip -kf "random$COUNT"
	let "COUNT += 1"
done

# Output file sizes to terminal
COUNT=0
echo "---   File  --- Original    --- Compressed"
while [ "$COUNT" -lt $NUMFILES ]
do
	ORIGFILESIZE=$(stat -c%s "random$COUNT")
	COMPFILESIZE=$(stat -c%s "random$COUNT.gz")
	echo "--- random$COUNT  |    $ORIGFILESIZE     |    $COMPFILESIZE"
	let "COUNT += 1"
done
echo "------------------------------------------"

# Clean up
COUNT=0
while [ "$COUNT" -lt $NUMFILES ]
do
	rm "random$COUNT" "random$COUNT.gz"
	let "COUNT += 1"
done