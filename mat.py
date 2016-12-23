'''
Digital Forensic Tool for Database
Name Anson Tan Wui Kang
ID   056 654 114
'''
import os
import sys
import fileinput

#function for analyze binary file
def analyze():

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
	#Display menu options
	log()

#function for detect, backup and load image for Raspberry Pi
def raspberry():
	print '\n1. Detect Mysql'
	print '2. Create Mysql ISO'
	print '3. Mount Mysql ISO'
	print '4. Unmount ISO'
	print '5. Back'
	option = input("\nPlease select option : ")
			
	#Detect Raspberry Pi
	if option == 1:
		os.system('ls -l /var/log/mysql')
		print '\n'
		forensic()

	#Backup Raspberry Pi mysql
	elif option == 2:
		con = raw_input("May takes a while to backup, type 'Yes' to proceed or 'R' to return : ")
		if con == 'Yes':
			os.system('sudo mkisofs -o ~/Downloads/mysql.iso /var/log/mysql')
			print '\n'

		elif con == 'R':
			raspberry()
		else:
			print 'Invalid option'
			raspberry()

	#mount Mysql image file
	elif option == 3:
		os.system('sudo mkdir ~/Downloads/mysql-iso')
		os.system('sudo mount -o loop mysql.iso ~/Downloads/mysql-iso')
		forensic()

	elif option == 4:	
		os.system('sudo umount mysql-iso')
		forensic()
	
	elif option == 5:
		forensic()

	#return to raspberry function after accepted invalid input
	else:
		print 'Invalid option'
		raspberry()
		
#Log feature
def log():
	print '\n1. Binary Log'
	print '2. General Query Log'
	print '3. Error Log'
	print '4. Logs file'
	print '5. Mysql_history'
	print '6. Back'
	option = input("\nPlease select option : ")
	
	#Binary Log
	if option == 1:
		print '\n1. Read Binary log'
		print '2. Analyze Binary log'
		print '3. Back'
		option = input("\nPlease select option : ")
					
		#Read specific Binary log			
		if option == 1:
			#Accept binary file name from user input
			binaryfile = raw_input('\nEnter binary file name: ')
			#Read binary file
			os.system('mysqlbinlog ~/Downloads/mysql-iso/' + binaryfile)
			######ask user whether want to save file
			forensic()
				
		#Summaries specific Binary log
		elif option == 2:
			analyze()
		
		elif option == 3:
			log()
		
		#return to log function after accepted invalid input
		else:
			print 'Invalid option'
			log()
	
	#General Query Log			
	elif option == 2:
		#download query, make it more easier to read
		print '\nGeneral Query Log\n'
		os.system('cat ~/Downloads/mysql-iso/mysql.log')
		log()
	
	#Error Log		
	elif option == 3:
		print '\nError Log\n'
		os.system('cat ~/Downloads/mysql-iso/error.log')
		log()

	#Show binary log file in /var/log/mysql			
	elif option == 4:
		os.system('ls -la ~/Downloads/mysql-iso/')
		log()

	#show mysql_history
	elif option == 5:
		os.system('cat /home/wk/.mysql_history')
		log()

	elif option == 6:
		forensic()
	
	#return to log function after accepted invalid input
	else:
		print 'Invalid opton'
		log()

#show menu
def forensic():

	option = 0

	#Menu options
	print '\n*********************\n'
	print 'MYSQL Analytics Tool'
	print '\n*********************\n'

	while option != 4:
		print '1. List Partition Table'
		print '2. Mysql'
		print '3. Log File'
		print '4. Exit\n'
		option = input("Please select option : ")
		
		#List partition table
		if option == 1:
#			os.system('lsblk')
			os.system("sudo fdisk -l")
#			os.system('mmls ~/Downloads/raspberry.img')
			print '\n'
			
		
		#Raspberry Pi
		elif option == 2:
			#call raspberry function
			raspberry()

		#Log File
		elif option == 3:
			#call log function
			log()

		#Exit program
		elif option == 4:
			###################save into a file?
			sys.exit(1)

		#return to forensic function after accepted invalid input
		else:
			print 'Invalid option'
			forensic()
		

#Display menu options
forensic()
