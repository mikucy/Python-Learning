import os

# This function find all the files in a directory including its subfolders according to a keyword.

def find_files(dir='/home/cp612sh', keyword='Python'):
  for i in os.walk(dir):
    for j in i[2]:
      if keyword in j:
        print(os.path.join(i[0], j))
        
find_files('/home/cp612sh/github', 'pb')
