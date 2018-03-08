import connexion
import six

from swagger_server.models.add import ADD  # noqa: E501
from swagger_server import util

from flask import Flask, render_template, request
from werkzeug import secure_filename



def add_num(number1, number2):  # noqa: E501
    """add_num

    Returns addition result from the hosting server # noqa: E501

    :param number1: Number 1
    :type number1: int
    :param number2: Number 2
    :type number2: int

    :rtype: ADD
    """
    sum = number1 + number2
    return sum
    #return 'do some magic!'


     # noqa: E501

#@app.route('/uploader', methods = ['GET', 'POST'])

def upload_file():
   #iFile = request.files.getlist('file')[0]
   if request.method == 'POST':
      f = request.files['file_name']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

   """
      :param filename: File to be converted
      :type filename: werkzeug.datastructures.FileStorage

      :rtype: None
    """
    #test = storage.read(filename)
    #print filename
    #return 'do some magic!'
    #return test

def xml2json(xmlStr):  # noqa: E501
    """xml2json

    Convert XML to JSON # noqa: E501

    :param xmlStr: XML String
    :type xmlStr: str

    :rtype: ADD
    """
    #return 'do some magic!'
    return xmlStr
