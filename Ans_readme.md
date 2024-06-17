# Development Environment Documentation

# 1. Homebrew Installation
To manage installations, I have used Homebrew, a popular package manager for macOS.

Installation Command:/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Installed Packages
Here are the primary packages installed via Homebrew:

Git: Version control system: brew install git
Python 3.12: Programming language and interpreter:brew install python@3.12
MySQL: Database management system:brew install mysql
Dart: Programming language optimized for building mobile, desktop, server, and web applications:brew install dart

CocoaPods: Dependency manager for Swift and Objective-C Cocoa projects:brew install cocoapods


# 3. Installed Applications
Here are the applications installed via Homebrew Cask:

Visual Studio Code: Source-code editor developed by Microsoft: brew install --cask visual-studio-code
brew install --cask visual-studio-code: brew install --cask flutter


# 4. Visual Studio Code Extensions
Here are the extensions installed in Visual Studio Code:

Python: I understand this provides IntelliSense, linting, and debugging for Python.
Dart: Provides support for Dart programming language.
Prettier - Code formatter: An opinionated code formatter.
Blackbox: AI-powered code generation and autocompletion.
SQLite Viewer: View and edit SQLite databases.
GitLens (for Git classroom): Supercharges the Git capabilities built into Visual Studio Code.


# 5. Configuration and Setup
Git Configuration:
Set up my Git configuration with your user details and preferred settings:
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

Python Configuration:
I ensured Python 3.12 is the default version used in your environment: 
echo 'export PATH="/usr/local/opt/python@3.12/bin:$PATH"' >> ~/.bash_profile
source ~/.bash_profile

MySQL Setup:
I Initialized and started the MySQL service to confirm it worked:
brew services start mysql
mysql_secure_installation

Dart and Flutter Setup:
I ensured Dart and Flutter are in my system’s PATH:
echo 'export PATH="$PATH":"$(brew --prefix)/opt/dart/libexec/bin"' >> ~/.bash_profile
echo 'export PATH="$PATH":"$(brew --prefix)/opt/flutter/bin"' >> ~/.bash_profile
source ~/.bash_profile

CocoaPods Setup:
I made an update to CocoaPods and installed dependencies for your Xcode project:
pod setup
pod install


# 6. Django Project Setup
To set up a Django project,I first created a virtual environment, then installed Django and any other necessary packages.

I Create Virtual Environment:
I Created and activated a virtual environment using Python’s venv module:
python3 -m venv myenv
source myenv/bin/activate

I installed django: python3 -m pip install django

I started a Django Project: django-admin startproject myproject

I checked if django project could start by running the server:
cd myproject
python3 manage.py runserver
I Create a new Django app: python3 manage.py startapp myapp

I Made migrations and applied them: python manage.py makemigrations myapp

# 9. Challenges Encountered
Challenge: I encountered issues adding Dart to the PATH.
Resolution: Verified the installation path and ensured it was correctly added to .bash_profile. Running source ~/.bash_profile was necessary to apply the changes.


challange: Setting up a path for my template.
Resolution: I created a new directory for templates and updated the settings.py file to include the new path.







