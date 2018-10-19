# Warning
This is not a complete project, it contains several bugs and lack features. I'm not responsible for your lost, please be careful.
Tool only works if MySQL database enabled binary log
Contributed by Anson Tan

# MAT - MySQL Analysis Tool

MAT is a simple tool that used to analyze MySQL database. It is able to create image file for entire MySQL directory and analyze the log files. This tool provides fastest and easiest way to analyze MySQL database to find out which data had been modified, inserted or deleted. 

# Installation
- Download MAT zip file from GitHub and extract on Linux
- On command terminal, cd into the extracted directory and run ". installer.sh"
- To launch MAT, simply run "mat" on command terminal

# MAT tutorial
Type 'man' in the tool will show all commands and descriptions. Suggest to read all commands and description before using it. MAT zip file contains sample MySQL database for testing the tool.

Create MySQL User
- mysql -uroot -p
- create user 'rea'@'localhost' identified by 'reatest';
- grant all privileges on * . * to 'rea'@'localhost';
- mysql -urea -preatest

Enable Binary Log
- /etc/mysql/my.cnf
- Remove "#" for log-bin = /path/to/log

# Updated
- Release v1.4.1, Mar 08
- Added installer for user to install all needed files
- Added sample MySQL Database for testing MAT
- Bugs fixed

- Release v1.4, Feb 28
- Added 'show tables' command for showing tables in MySQL database
- Added 'show databases' command for showing database name and number of tables in MySQL database
- Bugs fixed and improved performance

- Release v1.3, Feb 27
- Added 'save output' command for saving previous output into a file
- Added 'num state' command for counting number of changes including insert, delete and update statement
- Bugs fixed and improved performance

- Release v1.2, Jan 16
- Added function for calculate hash value after creating image file and before mount image, MD5
- Added some shortcut commands for most of commands, such as “an bin” for “analyze binary“, “s log” for “show logs”, “m  mysql.iso” for “mount mysql.iso” 
- Added shortcut commands in “man” command list
- Colour print output for “analyze binary” command

- Released v1.1, Jan 10
- Added ‘man’ command which show command list and description for each command
- Added ‘version’ command which show tool’s version
- Added ‘clear’ command which clear terminal screen and return to main menu
