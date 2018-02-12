import json
from eve import Eve
import platform
import psutil
import os
import pymongo
from pymongo import MongoClient
from flask import jsonify
from bson import json_util

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
        #return str(mem.total)
        mem_param = jsonify(mem)

        #return mem_param
       	client = MongoClient("mongodb://localhost:27017")

	try:
	    info = client.server_info() # check if connection is established
        except pymongo.errors.ServerSelectionTimeoutError:
    	    #print("Unable to connect to database!.")
	    return "Unable to connect to database!" 


	db = client["student_db"]
	#except pymongo.errors.ServerSelectionTimeoutError as e:
        #db = client["student_db"]

        collection = db["memData"]

	memDataDict = {}
	memDataDict["Total"] = mem.total
	memDataDict["Available"] = mem.available
	memDataDict["percent"] = mem.percent
	memDataDict["Used"] = mem.used
	memDataDict["Free"] = mem.free



        collection.insert(memDataDict)
	#return "Success"
	memStats = collection.find_one()
	return json.dumps(memStats,indent=2 , default=json_util.default)


	

# Battery info using psutil
@app.route('/battery')

def battery():
        util.virtual_memory()
        #return str(mem.total)
        mem_param = jsonify(mem)

        #return mem_param

        client = MongoClient("mongodb://localhost:27017")
        db = client["student_db"]
        collection = db["memData"]
	memData = {}
	memData["Total"] = mem.total
	memData["Available"] = mem.available
	memData["percent"] = mem.percent
	memData["Used"] = mem.used
	memData["Free"] = mem.free



        collection.insert(memData)

	return mem_param
        batt = psutil.sensors_battery()
        return str(batt)

# http://www.tldp.org/LDP/Linux-Filesystem-Hierarchy/html/proc.html
# disk info from /proc using os
@app.route('/proc_parts')

def proc_parts():
# https://stackoverflow.com/questions/4760215/
	os.system('cat /proc/partitions > /tmp/parts')
	parts = open('/tmp/parts', 'r').read()
        return parts
	os.remove('/tmp/parts')


if __name__ == '__main__':
	app.run()


# References:

#https://docs.python.org/2/library/platform.html
#https://pypi.python.org/pypi/psutil
#http://www.tldp.org/LDP/Linux-Filesystem-Hierarchy/html/proc.html
#https://stackoverflow.com/questions/4760215
#https://stackoverflow.com/questions/4404742/
