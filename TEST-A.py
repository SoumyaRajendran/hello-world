from time import time

end = time() + 120
while time() < end:
  time.sleep(50)
  print "Hello World"    
  

