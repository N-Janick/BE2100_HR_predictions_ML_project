# script to set up virtual environment for mac/Linux

#!/bin/bash

# if a 'venv' folder does not already exist creates one
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install the dependencies from requirements.txt
echo "Installing dependencies..."
python3 -m pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete! Virtual environment is ready."
