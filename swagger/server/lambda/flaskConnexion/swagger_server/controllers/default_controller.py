import connexion
import six

from swagger_server.models.add import ADD  # noqa: E501
from swagger_server import util


def add_num():  # noqa: E501
    """add_num

    Returns addition result information of the hosting server # noqa: E501


    :rtype: ADD
    """
    #return 'do some magic!'
    f = lambda x,y : x + y
    add = f(1,3)
    return add

