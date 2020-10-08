import time

end = time() + 120
while time() < end:
  print "Hello World"    
  time.sleep(60)

