#!/bin/bash

if command -v psql >/dev/null 2>&1; then
    echo "PostgreSQL is already installed."
fi

# Install PostgreSQL
echo "Installing PostgreSQL..."
sudo apt update
sudo apt install postgresql

if [ $? -eq 0 ]; then
    echo "PostgreSQL installed successfully."
else
    echo "Failed to install PostgreSQL."
fi

# New user and password
NEW_USER="coorlab"
NEW_PASS="coorlab"

# Create a new user
sudo -u postgres psql -c "CREATE USER $NEW_USER PASSWORD '$NEW_PASS';"
# Allow the new user to create databases
sudo -u postgres psql -c "ALTER ROLE $NEW_USER CREATEDB;"

cd backend
# Create a virtual environment
python3 -m venv venv
# Activate the virtual environment
source venv/bin/activate
# Install the required packages
pip install -r requirements.txt

cd ..

# Starting backend
gnome-terminal -- bash -c "cd backend; source venv/bin/activate; cd ..; python3 backend/app.py"

# Check node and npm installation
if command -v node >/dev/null 2>&1; then
    echo "Node is already installed."
    continue
else
    echo "Installing Node..."
    sudo apt update
    sudo apt install nodejs
fi

if command -v npm >/dev/null 2>&1; then
    echo "NPM is already installed."
    continue
else
    echo "Installing NPM..."
    sudo apt update
    sudo apt install npm
fi

cd frontend

# Install the required packages
npm run install

# Starting frontend
gnome-terminal -- bash -c "cd frontend; npm run serve; xdg-open http://localhost:8080"