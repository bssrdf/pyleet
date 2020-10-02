'''
Design an in-memory file system to simulate the following functions:

ls: Given a path in string format. If it is a file path, return a list that 
only contains this file's name. If it is a directory path, return the list of 
file and directory names in this directory. Your output (file and directory 
names together) should in lexicographic order.

mkdir: Given a directory path that does not exist, you should make a new 
directory according to the path. If the middle directories in the path don't 
exist either, you should create them as well. This function has void return 
type.

addContentToFile: Given a file path and file content in string format. If the 
file doesn't exist, you need to create that file containing given content. If 
the file already exists, you need to append given content to original content. 
This function has void return type.

readContentFromFile: Given a file path, return its content in string format.

 

Example:

Input: 
["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]

Output:
[null,[],null,null,["a"],"hello"]


Note:

You can assume all file or directory paths are absolute paths which begin 
with / and do not end with / except that the path is just "/".
You can assume that all operations will be passed valid parameters and users 
will not attempt to retrieve file content or list a directory or file that does 
not exist.
You can assume that all directory names and file names only contain lower-case 
letters, and same names won't exist in the same directory.

'''


from collections import defaultdict

class Node(defaultdict):
    def __init__(self):
        super().__init__(Node)
        self.terminal = False
        self.content = ''


class FileSystem(object):
    def __init__(self):
        self.root = Node()

    def ls(self, path):
        if path.endswith('/'):
            return [k for k in sorted(self.root.keys())]
        else:
            dirs = path.split('/')[1:]
            cur = self.root
            for d in dirs:
                cur = cur[d]
            if cur.terminal:
                return [d]
            else:
                return [k for k in sorted(cur.keys())]

        
    
    def mkdir(self, path):
        dirs = path.split('/')[1:]
        cur = self.root
        for d in dirs:
            if d not in cur:
                cur = cur[d]
    
    def addContentToFile(self, path, content):
        dirs = path.split('/')[1:]
        cur = self.root
        for d in dirs[:-1]:
            cur = cur[d]        
        if dirs[-1] in cur:
            cur[dirs[-1]].content += content 
        else:
            cur = cur[dirs[-1]]
            cur.terminal = True
            cur.content += content 
        
    def readContentFromFile(self, path):
        dirs = path.split('/')[1:]
        cur = self.root
        for d in dirs:
            cur = cur[d]        
        return cur.content

if __name__ == "__main__":
    fs = FileSystem()
    print(fs.ls("/"))
    fs.mkdir("/a/b/c")
    fs.addContentToFile("/a/b/c/d", "hello")
    print(fs.ls("/"))
    print(fs.readContentFromFile("/a/b/c/d"))
    fs.addContentToFile("/a/b/c/d", " world!")
    print(fs.readContentFromFile("/a/b/c/d"))
    print(fs.ls("/a"))
    print(fs.ls("/a/b/c/d"))
    fs.addContentToFile("/a/b/c/e", "foo")
    print(fs.ls("/a/b/c"))


                
