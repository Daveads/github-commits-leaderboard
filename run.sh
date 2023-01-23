#!/bin/bash

RUN="To run this code  ./main.py "

if command -v python > /dev/null; then

	if [ -d "env" ]; then
			source env/bin/activate
			pip install -r requirement.txt > /dev/null
			echo ">>> Packages Successfully Installed "
			chmod +x main.py
		    echo ">>> $RUN"

   else
		   python -m venv env
		   pip install --upgrade pip
		   source env/bin/activate
		   pip install -r requirement.txt
		   echo ">>> Packages Successfully Installed "
		   chmod +x main.py
		   echo ">>> $RUN"
	fi

else
    echo ">>> Error: Python is not installed"
    exit 1
fi
