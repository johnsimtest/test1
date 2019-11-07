
#192.168.223.5
import threading

def run(n):
	print(n)
	if n == 0:
		return
	n -= 1
	t=threading.Timer(1,run,(n,))
	t.start()

if __name__ == '__main__':
	n = 180
	run(n)
