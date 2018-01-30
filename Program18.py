# Program 18 (41-56) 
#     a File exists or not
#     Python shell in executing in 32 or 64 bits
#     Get OS Name, release information and platform
#     Locate Python site Package
#     Find out numbers of CPUs
#     List all files in a directory
#     Get the path and name of file currently executing
#     To get current username


import os,sys,math,site, getpass
import glob,platform,multiprocessing

FilePath= os.path.join('D:\Github','Python Tutorial','LearnPython')
os.chdir(FilePath)

# Answer for Q1

Name_of_File = raw_input("Please enter the filename to be checked: ")
FileName=os.path.join(FilePath,Name_of_File)
print("Answer for File Existence is: ", os.path.isfile(FileName))


# Answer for Q2
print("The Architecture of the System using maxint is %dbit"%math.log(sys.maxint,2))
print("The Architecture of the System using platform is ",platform.architecture())

# Answer for Q3
print("The name of the OS is {} with platform on {} and having released with {}".format(os.name,platform.system(),platform.release()))

# Answer for Q4
print("Current site for the python packages are: ",site.getsitepackages())

# Answer for Q5
print("Total # of running CPU are: ",multiprocessing.cpu_count())

# Answer for Q6
print(glob.glob('*.*'))

# Answer for Q7
print("The Current Path is: ",os.path.realpath(__file__))

# Answer for Q8
print("The Current User is: ",getpass.getuser)
