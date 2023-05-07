#!/bin/bash

if [ $# -lt 3 ]
then
    echo "./ftp.sh [ip] [from] [to]"
    exit 1
fi

HOST=$1
PORT="21"
USER="root"
PASSWD="root"
FILE=$2
UFILE=$3

ftp -n $HOST $PORT << END_SCRIPT
quote USER $USER
quote PASS $PASSWD
bin
put $FILE $UFILE
quit
END_SCRIPT

exit 0
