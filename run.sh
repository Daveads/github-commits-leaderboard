#!/bin/bash

RUN="To run this code  ./main.py "

if command -v python > /dev/null; then

    if [ -d "env" ]; then
        source env/bin/activate
        pip install -r requirement.txt > /dev/null
        echo ">>> Packages Successfully Installed "
        chmod +x main.py
        echo ">>> $RUN"

        # Run the main.py script and print its output
        echo ">>> Output of ./main.py:"
        ./main.py
    else
        python -m venv env
        pip install --upgrade pip
        source env/bin/activate
        pip install -r requirement.txt
        echo ">>> Packages Successfully Installed "
        chmod +x main.py
        echo ">>> $RUN"

        # Run the main.py script and print its output
        echo ">>> Output of ./main.py:"
        ./main.py
    fi

else
    echo ">>> Error: Python is not installed"
    exit 1
fi
