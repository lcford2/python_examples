from itertools import cycle
import time

# infinite spinner example
for c in cycle("/-\|"):
	print(f"[{c}]", end = "\r")
	time.sleep(0.2)


