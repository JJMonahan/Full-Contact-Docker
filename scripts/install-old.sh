#!/bin/bash

# Define your app name and version
APP_NAME="FullContact"
DJANGO_APP_NAME="fc"
APP_VERSION="0.5"

# Define the paths for your app
BASE_DIR="/opt/$APP_NAME"
VENV_DIR="$BASE_DIR/venv"
INSTALL_DIR="$BASE_DIR/$APP_NAME-$APP_VERSION"

# Define the "fullcontact" user and group names
APP_USER="fullcontact"
APP_GROUP="fullcontact"

# Get the directory where the currently running script resides
script_dir=$(dirname "$0")

# Create the "fullcontact" group (if it doesn't exist)
sudo groupadd "$APP_GROUP"

# Create the "fullcontact" user, set the home directory, and add to the group
sudo useradd -m -d "/home/$APP_USER" -g "$APP_GROUP" "$APP_USER"

# Set a password for the "fullcontact" user (optional)
# sudo passwd "$APP_USER"

# Create the base directory if it doesn't exist
mkdir -p $BASE_DIR

# Update system packages and install required packages
apt update
apt install -y python3-venv python3-pip

# Create a Python virtual environment
python3 -m venv $VENV_DIR

# Activate the virtual environment
source $VENV_DIR/bin/activate

# Install python dependencies in the virtual environment
pip install -r $script_dir/../requirements.txt

# Deactivate the virtual environment
deactivate

# Copy your app code to the installation directory
echo "Copying code to $INSTALL_DIR"
cp -r $script_dir/../$DJANGO_APP_NAME $INSTALL_DIR

# Change ownership to the "fullcontact" user and group
sudo chown -R "$APP_USER:$APP_GROUP" $INSTALL_DIR

# Check if the alias already exists in .bashrc
if ! grep -q  "alias ${DJANGO_APP_NAME}venv=\"$VENV_DIR/bin/activate\"" /home/$APP_USER/.bashrc; then
    # Create an alias in the user's .bashrc for activating the venv
    echo "alias ${DJANGO_APP_NAME}venv=\"$VENV_DIR/bin/activate\"" >> /home/$APP_USER/.bashrc
    echo "Added alias ${DJANGO_APP_NAME}venv for starting the fc venv to .bashrc"
fi

# Create a systemd service file to run your app (optpwd
ional)
# This step depends on your specific application and how you want to run it.

# Enable and start the service (if applicable)
# sudo systemctl enable your_app.service
# sudo systemctl start your_app.service
