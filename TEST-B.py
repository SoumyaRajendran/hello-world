#The code will run for 3 minutes

from time import time,sleep

end = time() + 180
while time() < end:
  print "TEST-B"    
  sleep(60)

