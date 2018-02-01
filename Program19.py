# Program 19 (62-74)
#     get file creation and modification date/times
#     sort files by date
#     get a directory listing, sorted by date

# Solution:1
import os,glob,time

FilePath= os.path.join('D:\Github','Python Tutorial','LearnPython')
os.chdir(FilePath)

for f in glob.glob('*.*'):
        print("creation time of the file {0} is {1}".format(f,time.ctime(os.stat(f).st_ctime)))
        print(" and modification time is {0}".format(time.ctime(os.stat(f).st_mtime))) 
        

 # Solution: 2
files=glob.glob('*.*')
files.sort(key=os.path.getmtime,reverse=True)
files

# Solution: 3

# TempPath=os.path.join('D:\Github')
Path_Dict=dict()
for(Root,Directories,Files) in os.walk(FilePath):
    if Directories==[]:
        Path_Dict[os.path.split(Root)[1]]=time.ctime(os.path.getmtime(Root))
        for filename in Files:
            Path_Dict[os.path.split(os.path.join(Root,filename))[1]]=time.ctime(os.path.getmtime(os.path.join(Root,filename)))    
    else:
        Path_Dict[os.path.split(Root)[1]]=time.ctime(os.path.getmtime(Root))
        for Dir in Directories:
            Path_Dict[os.path.split(os.path.join(Root,Dir))[1]]=time.ctime(os.path.getmtime(os.path.join(Root,Dir)))
        for filename in Files:
            Path_Dict[os.path.split(os.path.join(Root,filename))[1]]=time.ctime(os.path.getmtime(os.path.join(Root,filename)))    

for Key in sorted(Path_Dict,key=Path_Dict.get):
    print("%s,%s"%(Key,Path_Dict[Key]))     
    


