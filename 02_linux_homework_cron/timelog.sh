#! /bin/sh
DEFAULT_FILENAME='time.log'
FILE=$1
if [ ! $FILE ]; then
   FILE=$DEFAULT_FILENAME
fi

echo $(date '+%m/%d/%y - %T') >> $HOME/$FILE
