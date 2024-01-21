x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#result: Python is awesome


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#result: Python is fantastic
#result: Python is awesome