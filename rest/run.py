from eve import Eve
import platform
import psutil
import os

app = Eve()

# processor family
@app.route('/processor')

def processor():
	procname = platform.processor()
	ver = platform.version()
	return ver
	#return procname,ver


# hostname
@app.route('/node')

def nodeinfo():
        node = platform.node()
        return node

# uname
@app.route('/uname')

def uname():
        node = platform.uname()
        return uname



# python build
@app.route('/pythonversion')

def pythonversion():
        pyver = platform.python_version()
        return pyver

# CPU info using psutil
@app.route('/cpu')

def cpu():
        cpucount = psutil.cpu_count()
        return str(cpucount)


# Memory info using psutil
@app.route('/mem')

def mem():
        mem = psutil.virtual_memory()
        return str(mem.total)

# Battery info using psutil
@app.route('/battery')

def battery():
        batt = psutil.sensors_battery()
        return str(batt)

# disk info from /proc using os
@app.route('/proc_parts')

def proc_parts():

	os.system('cat /proc/partitions > /tmp/parts')
	parts = open('/tmp/parts', 'r').read()
        return parts
	os.remove('/tmp/parts')

if __name__ == '__main__':
	app.run()

