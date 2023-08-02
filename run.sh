#!/bin/bash

if command -v python3 > /dev/null; then

    if command -v pip3 > /dev/null; then 
        pip3 install -r requirement.txt
        echo ">>> Packages Successfully Installed "
        source ./cron_setup.sh
    else
        echo ">>> pip3 not available"
        exit 1
   fi

else
    echo ">>> Error: Python is not installed"
    exit 1
fi
