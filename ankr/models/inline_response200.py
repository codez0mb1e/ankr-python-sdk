# coding: utf-8

"""
    Ankr Advanced API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse200(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'error': 'object',
        'id': 'int',
        'jsonrpc': 'str',
        'result': 'object'
    }

    attribute_map = {
        'error': 'error',
        'id': 'id',
        'jsonrpc': 'jsonrpc',
        'result': 'result'
    }

    def __init__(self, error=None, id=None, jsonrpc=None, result=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501
        self._error = None
        self._id = None
        self._jsonrpc = None
        self._result = None
        self.discriminator = None
        if error is not None:
            self.error = error
        if id is not None:
            self.id = id
        self.jsonrpc = jsonrpc
        if result is not None:
            self.result = result

    @property
    def error(self):
        """Gets the error of this InlineResponse200.  # noqa: E501


        :return: The error of this InlineResponse200.  # noqa: E501
        :rtype: object
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this InlineResponse200.


        :param error: The error of this InlineResponse200.  # noqa: E501
        :type: object
        """

        self._error = error

    @property
    def id(self):
        """Gets the id of this InlineResponse200.  # noqa: E501


        :return: The id of this InlineResponse200.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse200.


        :param id: The id of this InlineResponse200.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def jsonrpc(self):
        """Gets the jsonrpc of this InlineResponse200.  # noqa: E501


        :return: The jsonrpc of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._jsonrpc

    @jsonrpc.setter
    def jsonrpc(self, jsonrpc):
        """Sets the jsonrpc of this InlineResponse200.


        :param jsonrpc: The jsonrpc of this InlineResponse200.  # noqa: E501
        :type: str
        """
        if jsonrpc is None:
            raise ValueError("Invalid value for `jsonrpc`, must not be `None`")  # noqa: E501
        allowed_values = ["2.0"]  # noqa: E501
        if jsonrpc not in allowed_values:
            raise ValueError(
                "Invalid value for `jsonrpc` ({0}), must be one of {1}"  # noqa: E501
                .format(jsonrpc, allowed_values)
            )

        self._jsonrpc = jsonrpc

    @property
    def result(self):
        """Gets the result of this InlineResponse200.  # noqa: E501

        Result of the query.  # noqa: E501

        :return: The result of this InlineResponse200.  # noqa: E501
        :rtype: object
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this InlineResponse200.

        Result of the query.  # noqa: E501

        :param result: The result of this InlineResponse200.  # noqa: E501
        :type: object
        """

        self._result = result

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InlineResponse200, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
