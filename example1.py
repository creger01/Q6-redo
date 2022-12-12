import os
cwd = os.getcwd()
print(cwd)

absolute = os.path.abspath("my_story.txt")
print(absolute)

os.chdir(r"C:\Users\creger01\Desktop\new folder for os practice")
cwd = os.getcwd()
print(cwd)

new = os.listdir()
print(new)
