# TimeTracker
A small tool to track time for different projects from the terminal

### List of commands:
- start: start tracking from this moment or from a given time
- end: end tracking at this moment or at a given time
- set: set tracked time to the amount given as param
- check: checks how much time you tracked in the active day
- change: change the project that you are working in (you can track 
multiple projects)
- date: change the date that you are tracking (you can see older days)

### How to:
There are 2 directories that need to be defined: 
1. source code of this project (track.py, variable source_code_directory)
2. directory where the user files will be stored (it will be 
created automatically in .TimeTracker under you home directory, can be
changed in file ProjectService.py, variable user_data_directory)
    - this directory will have the following structure:
        - file 'data' (first line is the project that is currently 
        tracked, second line the date tracked - or today it this line 
        is missing)
        - directory 'user-data' - here you have multiple directories for 
        each project that you tracked

You can create a symbolic link to track.py file and use it 
anywhere you want