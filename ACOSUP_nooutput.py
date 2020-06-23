#importing packages
import os
import shutil
print("Welcome to the Automated Code-Out Submission Using Python (ACOSUP) developed by Aaditya Rengarajan for automation of writing code for submission of assignments.\nWARNING:You are using the no_output version of this program which will not include the output!!!")


#knowing the required directory
reqdir=input("\n\nEnter the absolute path of the folder containing the files (please use forward slash ('/') as separator for directories) :")

#creating the output file
outf=open('finaloutput.txt','w')

#iterating
i=0

for filename in os.listdir(reqdir):
    if filename.endswith('.py'):
        #preparing the dos command
        i+=1
        
        #writing the code into the file
        f=open(str(reqdir+'/'+filename)).read()
        outf.write(f)

        #report status to user
        if i<=1:
                print("Completed writing",i," file")
        else:
                print("Completed writing",i," files")

#deleting the temporary file
if i>0:
        deltemp=str(reqdir)+'/output.txt'
        os.remove(deltemp)
#close-screen
outf.close()
todir=input("\n\nThank you for using the ACOSUP application. Please enter the directory to save the output file :")
while 1:
        try:
                shutil.move('finaloutput.txt', todir)
                break
        except:
                while 1:
                        choice=input("\nThere seems to be an error. Perhaps there is already a file with the same filename. Overwrite (O) or change directory (C)?\n Please type (O/C) :")
                        if choice in "oO":
                                     torem=str(todir)+'/finaloutput.txt'
                                     os.remove(torem)
                                     break
                        elif choice in "Cc":
                                     todir=input("Please enter the directory to save the output file :")

print("Your file has been saved as 'finaloutput.txt' in the directory you had entered.\nThe program will now terminate.")
input()
