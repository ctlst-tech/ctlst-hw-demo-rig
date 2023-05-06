#!/bin/bash

if [ $# -eq 0 ]
then
    echo "Please enter target ip"
    echo "Example:"
    echo "./upload.sh 192.168.1.20"
    exit 1
fi

HOST=$1
BIN="${PWD}/build/firmware/catom-launcher"
UBIN="/fs/etfs/bin/catom-launcher"
SCRIPT="${PWD}/scripts/catpilot.sh"
USCRIPT="/fs/etfs/bin/catpilot"
SUBDIR="config"
CONF_TARGET="fs/etfs/catpilot"
ftp="${PWD}/scripts/ftp.sh"

HOST=$1
PORT="21"
USER="root"
PASSWD="root"
FILE=$2
UFILE=$3

ftp -n $HOST $PORT << END_SCRIPT
verbose
quote USER $USER
quote PASS $PASSWD
bin
mkdir $CONF_TARGET
quit
END_SCRIPT

sh ${ftp} ${HOST} ${BIN} ${UBIN}
sh ${ftp} ${HOST} ${SCRIPT} ${USCRIPT}

for FILE in ./${SUBDIR}/*
do
    name=`echo $FILE | cut -c 10-`
    FILE="${PWD}/${SUBDIR}/${name}"
    UFILE="${CONF_TARGET}/${name}"
    echo $FILE to $UFILE
    sh ${ftp} ${HOST} ${FILE} ${UFILE}
    echo
done

echo
echo "Firmware uploaded!"

exit 0
