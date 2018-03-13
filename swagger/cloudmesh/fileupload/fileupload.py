#import connexion
#import six

#from swagger_server.models.add import ADD  # noqa: E501
#from swagger_server import util

from flask import Flask, render_template, request
from werkzeug import secure_filename


def fileupload(filename):

      f = request.files['file_name']
      f.save(secure_filename(f.filename))
      return 'File received.'


