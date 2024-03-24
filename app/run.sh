#!/bin/bash

# Check if running as root
if [ "$(id -u)" != "0" ]; then
    echo "This script must be run as root. Use sudo." 1>&2
    exit 1
fi

echo "Running with sudo permission..."

echo "Checking if PostgreSQL is installed..."
if command -v psql >/dev/null 2>&1; then
    echo "PostgreSQL is already installed."
else
    echo "PostgreSQL is not installed."
    echo "Do you want to install PostgreSQL? (y/n)"
    read answer
    if [ "$answer" != "${answer#[Yy]}" ]; then
        echo "Installing PostgreSQL..."
        sudo apt update
        sudo apt install postgresql
    else
        echo "PostgreSQL is required to run the application."
        exit 1
    fi
fi

# New user and password
NEW_USER="coorlab"
NEW_PASS="coorlab"

echo "Creating a new user for PostgreSQL and adding permission to create new DBs..."
# Create a new user
sudo -u postgres psql -c "CREATE USER $NEW_USER PASSWORD '$NEW_PASS';"
# Allow the new user to create databases
sudo -u postgres psql -c "ALTER ROLE $NEW_USER CREATEDB;"

cd backend
echo "Creating a virtual environment"
# Create a virtual environment
python3 -m venv venv
echo "Activating the virtual environment..."
# Activate the virtual environment
source venv/bin/activate
echo "Installing the required packages..."
# Install the required packages
pip install -r requirements.txt

cd ..

if command -v dbus-launch >/dev/null 2>&1; then
    echo "dbus-launch is already installed."
else
    echo "Installing dbus-launch..."
    sudo apt install dbus-x11
fi

echo "Starting the backend..."
# Starting backend
gnome-terminal -- bash -c "cd backend; source venv/bin/activate; cd ..; python3 backend/app.py"

echo "Checking if Node and NPM are installed..."
# Check node and npm installation
if command -v node >/dev/null 2>&1; then
    echo "Node is already installed."
else
    echo "Installing Node..."
    sudo apt update
    sudo apt install nodejs
fi

if command -v npm >/dev/null 2>&1; then
    echo "NPM is already installed."
else
    echo "Installing NPM..."
    sudo apt update
    sudo apt install npm
fi

cd frontend

echo "Checking if Vue CLI is installed..."
if command -v vue >/dev/null 2>&1; then
    echo "Vue CLI is already installed."
else
    echo "Installing Vue CLI..."
    npm install -g @vue/cli
fi

# Install the required packages
if [ -d "/node_modules" ]; then
    echo "node_modules directory exists"
else
    echo "node_modules directory does not exist"
    echo "Installing the required packages in frontend..."
    sudo npm install
fi

echo "Starting the frontend..."
# Starting frontend
gnome-terminal -- bash -c "cd frontend; npm run serve; xdg-open http://localhost:8080"