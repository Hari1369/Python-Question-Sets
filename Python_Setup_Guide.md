# Python Setup Guide for Running Scripts

# Method 1:
#   Step 1: Download Python :-
#       a)  Go to: https://www.python.org/downloads/
#       b)  Choose the version for your OS (Windows, Mac, Linux).
#       c)  Tip: For beginners, Python 3.x is recommended.
#   Step 2: Install Python :-
#       a)  Run the downloaded installer.
#       b)  Important: Check the box: Add Python to PATH.
#       c)  Click Install Now and follow the prompts.
#   Step 3: Verify Installation :-
#       a)  Open Command Prompt (Windows) or Terminal (Mac/Linux).
#       b)  Run:-
#               python --version or python3 --version
#       c)  You should see something like:
#               Python 3.x.x

# Method 2:
#   Step 1: Install Python :-
#       Follow Method 1 above if Python is not installed.
#   Step 2: Create a Project Folder
#       mkdir 'Question Sets' and cd 'Question Sets'
#           a) Run:-
#               python -m venv venv
#           or on Mac/Linux:
#               python3 -m venv venv
#   Step 4: Activate the Virtual Environment
#       a) Windows:
#           venv\Scripts\activate
#       b) Mac/Linux:
#           source venv/bin/activate
#   You’ll notice (venv) appears in your terminal prompt.
#   Step 6: Run Python Scripts
#       a)  Inside your project folder, create .py files (example: python_list.py).
#       b)  Run the script using:
#           python python_list.py or python3 python_list.py

#   Summary Comparison:-
#       a)  For simple learning scripts: Installing Python globally is fine.
#       b)  For organized project work: Using a virtual environment is better because it keeps dependencies isolated.


#   ====================================================================================================
#   | Method                   | Best For               | Requires Virtualenv? | Recommended?          |
#   | ------------------------ | ---------------------- | -------------------- | --------------------- |
#   | Official Python Download | Beginners, small tests | No                   | Good for quick start  |
#   | Virtual Environment      | Projects, Django apps  | Yes                  | Best for clean setups |
#   ====================================================================================================
