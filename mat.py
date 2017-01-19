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
import hashlib

#command list
def man():
	print '\nMYSQL Analytic tool command list and description\n'
	print '-----------------------------------------------------'
	print '        Command		|         Description'
	print '-----------------------------------------------------'
	print 'detect mysql		| detect MYSQL directory in operating system'
	print 'show binary		| show binary file'
	print 'show log		| show log files'
	print 'show history		| show mysql history'
	print 'show error		| show error log'
	print 'show query		| show general query file'
	print 'analyze binary		| analyze binary file, such as analyze binary mysql000.000'
	print 'create mysql		| create mysql image file'
	print 'mount mysql.iso		| mount an image file called mysql.iso'
	print 'unmount mysql.iso	| unmount an image file called mysql.iso'
	print 'num state		| highest number of insert/delete/update statements'
	print 'save output		| save previous output'
	print 'hash mysql.iso		| calculate hash number for mysql.iso'
	print 'version			| show tool version'
	print 'clear			| clear screen'
	print '-----------------------------------------------------'
	print '        Command		|      shortcut command'
	print '-----------------------------------------------------'
	print 'detect mysql		| det mysql'
	print 'show binary		| s binary, s bin'
	print 'show log		| s log'
	print 'show history		| s history, s his'
	print 'show error		| s error, s err'
	print 'show query		| s query, s que'
	print 'analyze binary		| ana bin, an bin'
	print 'create mysql		| c mysql'
	print 'mount mysql.iso		| m mysql.iso'
	print 'unmount mysql.iso	| un mysql.iso'
	print 'save output		| save out'
	print 'hash mysql.iso		| h mysql.iso'
	forensic()
		
#command line
def forensic():

	output = ""
	#input command line
	option = raw_input("\nmat > ")

	#show binary file	
	if option == 'show binary' or option == 's binary' or option == 's bin':
		#Accept binary file name from user input
		binaryfile = raw_input('\nEnter binary file name: ')
		#Read binary file
		os.system('mysqlbinlog ~/Downloads/mysql-iso/' + binaryfile)
		option = raw_input("\nmat > ")

		#save output for binary file
		if option == 'save output' or option == 'save out':
			#input filename for binary file output
			filename = raw_input("Please enter filename for the output > ")
			os.system('mysqlbinlog ~/Downloads/mysql-iso/' + binaryfile + '>' + filename)
			print filename + ' is successfully saved'
			forensic()
		else:
			forensic()

	#show log files
	elif option == 'show log' or option == 's log':

		output = os.system("ls -la ~/Downloads/mysql-iso")
		output
		option = raw_input("\nmat > ")

		#save output for log files
		if option == 'save output' or option == 'save out':
			#input filename for log files output
			filename = raw_input("Please enter filename for the output > ")
			os.system('ls -la ~/Downloads/mysql-iso >' + filename)
			print filename + ' is successfully saved'
			forensic()
		else:
			forensic()

	#show mysql history
	elif option == 'show history' or option == 's history' or option == 's his':

		os.system('cat /home/wk/.mysql_history')
		option = raw_input("\nmat > ")

		#save output for history
		if option == 'save output' or option == 'save out':
			#input filename for history file output
			filename = raw_input("Please enter filename for the output > ")
			os.system('cat /home/wk/.mysql_history >' + filename)
			print filename + ' is successfully saved'
			forensic()
		else:
			forensic()

	#show error log
	elif option == 'show error' or option == 's error' or option == 's err':

		print '\nError Log\n'
		os.system('cat ~/Downloads/mysql-iso/error.log')
		option = raw_input("\nmat > ")

		#save output for error log
		if option == 'save output' or option == 'save out':
			#input filename for error log output
			filename = raw_input("Please enter filename for the output > ")
			os.system('cat ~/Downloads/mysql-iso/error.log >' + filename)
			print filename + ' is successfully saved'
			forensic()
		else:
			forensic()

	#detect mysql directory
	elif option == 'detect mysql' or option == 'det mysql':

		os.system('ls -l /var/log/mysql')
		option = raw_input("\nmat > ")

		#save output for mysql directory
		if option == 'save output' or option == 'save out':
			#input filename for mysql directory output
			filename = raw_input("Please enter filename for the output > ")
			os.system('ls -l /var/log/mysql >' + filename)
			print filename + ' is successfully saved'
			forensic()
		else:
			forensic()

	#show general query file
	elif option == 'show query' or option == 's query' or option == 's que':

		print '\nGeneral Query Log\n'
		os.system('cat ~/Downloads/mysql-iso/mysql.log')
		option = raw_input("\nmat > ")

		#save output for general query file
		if option == 'save output' or option == 'save out':
			#input filename for general query file output
			filename = raw_input("Please enter filename for the output > ")
			os.system('cat ~/Downloads/mysql-iso/mysql.log >' + filename)
			print filename + ' is successfully saved'
			forensic()
		else:
			forensic()

	#create mysql image file
	elif option == 'create mysql' or option == 'c mysql':

		con = raw_input("May takes a while to backup, type 'Y' to proceed or 'R' to return : ")
		if con == 'Y' or con == 'Yes':
			os.system('sudo mkisofs -o ~/Downloads/mysql.iso /var/log/mysql')
			print hashlib.md5(open('/home/wk/Downloads/mysql.iso', 'rb').read()).hexdigest()
			print '\n'
		
		########### calculate Hash value after created image

		elif con == 'R':
			forensic()
		else:
			print 'Invalid option'
			forensic()

	#mount mysql image file
		######### Calculate hash value before mount image
	elif option == 'mount mysql.iso' or option == 'm mysql.iso':

		os.system('sudo mkdir ~/Downloads/mysql-iso')
		os.system('sudo mount -o loop ~/Downloads/mysql.iso ~/Downloads/mysql-iso')
		print hashlib.md5(open('/home/wk/Downloads/mysql.iso', 'rb').read()).hexdigest()
		forensic()

	#calculate hash for Mysql image file using MD5
	elif option == 'hash mysql.iso' or option == 'h mysql.iso':

		print hashlib.md5(open('/home/wk/Downloads/mysql.iso', 'rb').read()).hexdigest()
		forensic()

	#unmount mysql image flle
	elif option == 'unmount mysql.iso' or option == 'un mysql.iso':

		os.system('sudo umount ~/Downloads/mysql-iso')
		#successed then print, 2>
		print 'ISO is successfully unmounted'
		forensic()

	#analyze binary file
	elif option == 'analyze binary' or option == 'ana bin' or option == 'an bin':

		#Accept binary file name
		filename = raw_input('Please input file name : ')
		#Open sum.sh but read only
		f1 = open('/usr/bin/sum.sh', 'r')
		#Open analyze.sh but write only
		f2 = open('/usr/bin/analyze.sh', 'w')
		for line in f1:
			#Copy all lines from sum.sh and replace user input into analyze.sh
			f2.write(line.replace('logfile', filename))
		f1.close()
		f2.close()
		#Execute analyze.sh
		os.system('. /usr/bin/analyze.sh')
		option = raw_input("\nmat > ")

		#save output for analyzed binary output
		if option == 'save output' or option == 'save out':
			#input filename for analyzed binary output
			filename = raw_input("Please enter filename for the output > ")
			os.system('. /usr/bin/analyze.sh >' + filename)
			print filename + ' is successfully saved'
			forensic()
		else:
			forensic()

	#highest number of insert/delete/update statements
	elif option == 'num state':

		#Accept binary file name
		filename = raw_input('Please input file name : ')
		#Open sum.sh but read only
		f1 = open('/usr/bin/sum.sh', 'r')
		#Open analyze.sh but write only
		f2 = open('/usr/bin/analyze.sh', 'w')
		for line in f1:
			#Copy all lines from sum.sh and replace user input into analyze.sh
			f2.write(line.replace('logfile', filename))
		f1.close()
		f2.close()
		#Execute analyze.sh
		os.system(". /usr/bin/analyze.sh | grep Table |cut -d':' -f5| cut -d' ' -f2 | sort | uniq -c | sort -nr")
	
	############ restore mysql file?

	#mat command list and description
	elif option == 'man':

		man()
	
	#clear screen
	elif option == 'clear' or option == 'cl':

		os.system('clear')
		forensic()

	elif option == 'version':

		print 'MYSQL Analytic Tool v1.2, contributed by Anson Tan'
		forensic()

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
print '*     MYSQL Analytic Tool v1.2    *'
print '***********************************'
forensic()
