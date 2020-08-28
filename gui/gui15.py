from tkinter import filedialog
file = filedialog.askopenfilename()
print("File Path is ",file)
print(type(file))
s=file.index('.')
print(file[s:])
print(file[0:s])

