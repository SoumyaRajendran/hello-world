#The code will run for 2 minutes

from time import time,sleep

end = time() + 120
while time() < end:
  print "TEST-A"    
  sleep(60)  
