# $`\textcolor{blue}{\text{Directory-Scan}}`$
A routine to scan a directory and list all subdirectories, recursively, as deep as necessary.
Richard Ay (August 2023, *updated September 2023*)

## $`\textcolor{blue}{\text{Table of Contents}}`$
* [Setup](#setup)
* [Environment](#environment)
* [Usage](#Usage)
* [References](#references)
* [File List](#file-list)
* [Technologies and Imports](#Technologies-and-Imports)
* [Sample Output](#sample-output)

## Setup

*(To use this program, copy both 'directory-scan.py' and 'dir_list.py' to a directory on a local drive.  Then invoke the program as indicated below.)* 

## Environment
To utilize this scripts, a virtual environment is created so that the installation of EasyGUI remains
local to this subdirectory, and does not affect the rest of the machine.

The virtual environment can be setup using the command: 
**'python -m venv "GUIenv" --upgrade-deps --prompt="GUIenv"'**

To start/stop the virtual environment, use the commands: **'GUIenv\scripts\activate'** or **'deactivate'**. Once
activated, the virtual environment will change the (terminal) prompt from (PS) to (GUIenv).

After starting the virtual environment, EasyGUI can be installed with the command:  
**'python -m pip install easygui'**.  Subsequently the installation can be verified with the command: 
**'python -m pip show easygui'**. 

The bundling utility 'PyInstaller' must also be installed to the virtual environment.  This is necessary to produce an EXE that can be run from Windows (without
starting VSCode and activating the virtual environment).
**'python -m pip install pyinstaller'**.  To bundle the required files into an EXE, issue the command **"pyinstaller --noconsole directory-scan.py"** from the 
active virtual environment.


## Usage
There are three ways to use this small programs: (1) the Python IDLE, (2) VS Code, or (3) Windows Explorer.  

1) From the IDLE, by selecting 'directory-scan.py' and pressing F5. For the Python IDLE, just start the IDLE (which opens a Python Shell), then select File/Open (which opens an Editor) and select the 'Directory_List.py" file.  From the Editor, F5 will run the file with the output written to a file, or diagnostics (trace-backs) appearing in the Shell.

2) From VSCode, by issuing the command 'python directory-scan.py' in the Terminal window. For VS Code it is important to change the Terminal from "Git Bash" to "Power Shell". Once in Power Shell, the command "python [filename].py" will run the file with the output going to the output file (user specified).  Note the suffix ".py" is required.

3) By double-clicking 'directory-scan.exe' from Windows Explorer.  Note this option requires that the Python script and associated libraries be bundled into an exe.  This is
accomplished by using 'pyinstaller', as discussed above.

The program prompts for two data items:
1) The name of the output (text) file.
2) The full pathname of the directory to scan.

Once this data is entered, the scan commences and the output file is generated. The output file (specified by the user) is written to the target directory that is scanned.


## References
1. Python for You and Me, Kushal Das, Feb 17, 2021  
2. Python Basics: A practical Introduction to Python 3, David Amos, Dan Bader, 2022  
3. Python Ultimate Guide (web download, source unknown) 
4. Automate The Boring Stuff with Python, Al Sweigart, 2020

## File List
**dir_list.py** - a small module with the 'worker' routines.  
**directory-scan.py** - the main program (invoke this file).   

## Technologies and Imports
The following modules are necessary imports (imported in the .py files):  
- os
- datetime
- dirlist
- pathlib
- easygui

## Sample Output
The image above shows a sample output:
![Sample Scan](https://github.com/CaptainRich/dir_list/blob/main/scan-output.png)

