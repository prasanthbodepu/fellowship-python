import sys
import os.path
from datetime import datetime


def printHelp():

	# Function to print Usage Section when asked for help or when no argur=ement is passed.
	taskhelp="""Usage :-
$ ./task add "task item"  # Add a new task
$ ./task ls               # Show remaining tasks
$ ./task del NUMBER       # Delete a task
$ ./task done NUMBER      # Complete a task
$ ./task help             # Show usage
$ ./task report           # Statistics"""
	sys.stdout.buffer.write(taskhelp.encode('utf8'))		# Print the Usage in UTF-8 Encoding as the default print() generates unexpected results.
	

def addToList(st):
	
	# Function to add a New task in the task.txt file.
	if os.path.isfile('task.txt'):					# If exists task.txt then appends the task in the first line.
	    with open("task.txt",'r') as taskFileOri:
	    	data=taskFileOri.read()
	    with open("task.txt",'w') as taskFileMod:
	    	taskFileMod.write(st+'\n'+data)
	else:											# If not then creates a new file and adds the task.
	    with open("task.txt",'w') as taskFile:
	    	taskFile.write(st+'\n')
	print('Added task: "{}"'.format(st))


def showList():

	# Function to List and print the available tasks' in the latest format order.
	if os.path.isfile('task.txt'):
	    with open("task.txt",'r') as taskFileOri:
	    	data=taskFileOri.readlines()
	    ct=len(data)
	    st=""
	    for line in data:
	    	st+='[{}] {}'.format(ct,line)
	    	ct-=1
	    sys.stdout.buffer.write(st.encode('utf8'))			# Print the Tasks in Reverse Order in UTF-8 Encoding as the default print() generates unexpected results.
	else:
	    print ("There are no pending tasks!") 


def delFromList(num):

	# Function to Delete the task from the List. (If available)
	if os.path.isfile('task.txt'):
	    with open("task.txt",'r') as taskFileOri:
	    	data=taskFileOri.readlines()
	    ct=len(data)
	    if num>ct or num<=0:
	    	print(f"Error: task #{num} does not exist. Nothing deleted.")
	    else:
	    	with open("task.txt",'w') as taskFileMod:
	    		for line in data:
	    			if ct!=num:
	    				taskFileMod.write(line)
	    			ct-=1
	    	print("Deleted task #{}".format(num))
	else:
	    print("Error: task #{} does not exist. Nothing deleted.".format(num))


def markDone(num):

	# Function to mark the given task as Done. (If available)
	if os.path.isfile('task.txt'):
	    with open("task.txt",'r') as taskFileOri:
	    	data=taskFileOri.readlines()
	    ct=len(data)
	    if num>ct or num<=0:
	    	print("Error: task #{} does not exist.".format(num))
	    else:
	    	with open("task.txt",'w') as taskFileMod:
	    		if os.path.isfile('done.txt'):						# Produces output according to the availability of done.txt file.
	    			with open("done.txt",'r') as doneFileOri:
				    	doneData=doneFileOri.read()
			    	with open("done.txt",'w') as doneFileMod:
			    		for line in data:
			    			if ct==num:
			    				doneFileMod.write("x "+datetime.today().strftime('%Y-%m-%d')+" "+line)
			    			else:
			    				taskFileMod.write(line)
			    			ct-=1
			    		doneFileMod.write(doneData)
		    	else:
		    		with open("done.txt",'w') as doneFileMod:
			    		for line in data:
			    			if ct==num:
			    				doneFileMod.write("x "+datetime.today().strftime('%Y-%m-%d')+" "+line)
			    			else:
			    				taskFileMod.write(line)
			    			ct-=1

	    	print("Marked task #{} as done.".format(num))
	else:
	    print("Error: task #{} does not exist.".format(num))


def generateReport():

	# Function to Generate the Report.
	counttask=0
	countDone=0
	if os.path.isfile('task.txt'):
	    with open("task.txt",'r') as taskFile:
	    	taskData=taskFile.readlines()
	    counttask=len(taskData)
	if os.path.isfile('done.txt'):
	    with open("done.txt",'r') as doneFile:
	    	doneData=doneFile.readlines()
	    countDone=len(doneData)
	st=datetime.today().strftime('%Y-%m-%d') + " Pending : {} Completed : {}".format(counttask,countDone)
	sys.stdout.buffer.write(st.encode('utf8'))


def main(): 

	# Main Function
	if len(sys.argv)==1:
		printHelp()
	elif sys.argv[1]=='help':
		printHelp()
	elif sys.argv[1]=='ls':
		showList()
	elif sys.argv[1]=='add':
		if len(sys.argv)>2:
			addToList(sys.argv[2])
		else:
			print("Error: Missing task string. Nothing added!")
	elif sys.argv[1]=='del':
		if len(sys.argv)>2:
			delFromList(int(sys.argv[2]))
		else:
			print("Error: Missing NUMBER for deleting task.")
	elif sys.argv[1]=='done':
		if len(sys.argv)>2:
			markDone(int(sys.argv[2]))
		else:
			print("Error: Missing NUMBER for marking task as done.")
	elif sys.argv[1]=='report':
		generateReport()
	else:
		print('Option Not Available. Please use "./task help" for Usage Information')

if __name__=="__main__": 
    main()
