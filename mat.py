#!/usr/bin/python2.7

'''
Mysql Analytic Tool

MAT is a simple tool that created by Python language which used to analyze Mysql directory files. It is able to create image file for entire Mysql directory and analyze the log files from the image. This tool provides fastest and easiest way to analyze Mysql database to find out which data had been modified, inserted or deleted after an attack.

This tool is a prototype, may contain several bugs and lack of features. 

Contributed by Anson Tan
'''

import os
import sys
import fileinput

def man():
	print '\nMysql Analytic tool command list and description\n'
	print '-----------------------------------------------------'
	print '        Command		|           Description'
	print '-----------------------------------------------------'
	print 'show binary		| show binary file'
	print 'show log		| show log files'
	print 'show history		| show mysql history'
	print 'show error		| show error log'
	print 'show query		| show general query file'
	print 'analyze binary		| analyze binary file, such as analyze binary mysql000.000'
	print 'create mysql		| create mysql image file'
	print 'mount mysql.iso		| mount an image file called mysql.iso'
	print 'unmount mysql.iso	| unmount an image file called mysql.iso'
	print 'save output		| save previous output'
	print 'version			| show tool version'
	print 'clear			| clear screen'
	forensic()
		
#command line
def forensic():
	#input command line
	option = raw_input("\nmat > ")

	#show binary file	
	if option == 'show binary':
		#Accept binary file name from user input
		binaryfile = raw_input('\nEnter binary file name: ')
		#Read binary file
		os.system('mysqlbinlog ~/Downloads/mysql-iso/' + binaryfile)
		######ask user whether want to save file
		forensic()

	#show log files
	elif option == 'show log':
		os.system("ls -la ~/Downloads/mysql-iso")
		forensic()

	#show mysql history
	elif option == 'show history':
		os.system('cat /home/wk/.mysql_history')
		forensic()

	#show error log
	elif option == 'show error':
		print '\nError Log\n'
		os.system('cat ~/Downloads/mysql-iso/error.log')
		forensic()

	#detect mysql directory
	elif option == 'detect mysql':
		os.system('ls -l /var/log/mysql')
		forensic()

	#show general query file
	elif option == 'show query':
		print '\nGeneral Query Log\n'
		os.system('cat ~/Downloads/mysql-iso/mysql.log')
		forensic()

	#create mysql image file
	elif option == 'create mysql':
		con = raw_input("May takes a while to backup, type 'Yes' to proceed or 'R' to return : ")
		if con == 'Yes':
			os.system('sudo mkisofs -o ~/Downloads/mysql.iso /var/log/mysql')
			print '\n'
		
		########### calculate Hash value after created image

		elif con == 'R':
			forensic()
		else:
			print 'Invalid option'
			forensic()

	#mount mysql image file
		######### Calculate hash value before mount image
	elif option == 'mount mysql.iso':
		os.system('sudo mkdir ~/Downloads/mysql-iso')
		os.system('sudo mount -o loop ~/Downloads/mysql.iso ~/Downloads/mysql-iso')
		forensic()

	#unmount mysql image flle
	elif option == 'unmount mysql.iso':
		os.system('sudo umount ~/Downloads/mysql-iso')
		#successed then print, 2>
		print 'ISO is successfully unmounted'
		forensic()

	elif option == 'analyze binary':
		#Accept binary file name
		filename = raw_input('Please input file name : ')
		#Open sum.sh but read only
		f1 = open('sum.sh', 'r')
		#Open analyze.sh but write only
		f2 = open('analyze.sh', 'w')
		for line in f1:
			#Copy all lines from sum.sh and replace user input into analyze.sh
			f2.write(line.replace('logfile', filename))
		f1.close()
		f2.close()
		#Execute analyze.sh
		os.system('. ~/Downloads/analyze.sh')
		print '\n'
		#Display menu options
		forensic()

	############ restore mysql file?

	#mat command list and description
	elif option == 'man':
		man()
	
	#clear screen
	elif option == 'clear':
		os.system('clear')
		forensic()

	elif option == 'version':
		print 'Mysql Analytic Tool v1.0, contributed by Anson Tan'
		forensic()

	#save output from previous command, need global name to keep previous command. Do you want to save output from previous command? Y/N if yes then input filename
	#elif option == 'save output':

	#exit program
	elif option == 'exit':
		sys.exit(1)

	#return to forensic function after accepted invalid input
	else:
		print 'Invalid option'
		forensic()
		

#Display menu options
#Menu options
print '***********************************'
print '*                MAT              *'
print '*     MYSQL Analytic Tool v1.0    *'
print '***********************************'
forensic()
