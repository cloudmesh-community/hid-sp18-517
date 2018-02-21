import connexion
import six

from swagger_server.models.add import ADD  # noqa: E501
from swagger_server import util


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


def upload_post(filename=None):  # noqa: E501
    """Upload a file

     # noqa: E501

    :param filename: File to be converted
    :type filename: werkzeug.datastructures.FileStorage

    :rtype: None
    """
    return 'do some magic!'


def xml2json(xmlStr):  # noqa: E501
    """xml2json

    Convert XML to JSON # noqa: E501

    :param xmlStr: XML String
    :type xmlStr: str

    :rtype: ADD
    """
# add the xml to json conversion login in a separate function/file and call it here
    return xmlStr
    #return 'do some magic!'
