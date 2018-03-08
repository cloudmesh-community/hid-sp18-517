from json import dumps
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring

def xml2json_conv(xmlStr):
	return dumps(bf.data(fromstring(xmlStr)))


# https://pypi.python.org/pypi/xmljson
