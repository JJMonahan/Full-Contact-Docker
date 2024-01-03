#!/bin/bash

# Define your app name and version
#APP_NAME="FullContact"
#DJANGO_APP_NAME="fc"
#APP_VERSION="0.5"

# Define the paths for your app
# Get the directory where the currently running script resides
script_dir="$(dirname "$(readlink -f "$0")")"
VENV_DIR="$script_dir/../venv"

echo "Script Director is $script_dir"
echo "venv directory is $VENV_DIR"

# Update system packages and install required packages
sudo apt update
sudo apt install -y python3-venv python3-pip

# Create a Python virtual environment
python3 -m venv $VENV_DIR

# Activate the virtual environment
source $VENV_DIR/bin/activate

#create an acivation script - this wont work - you should install an alias instead
#echo "source $VENV_DIR/bin/activate" > $script_dir/activate.sh
#chmod +x $script_dir/activate.sh

pip install -r $script_dir/../fc/requirements.txt


# Deactivate the virtual environment
deactivate

