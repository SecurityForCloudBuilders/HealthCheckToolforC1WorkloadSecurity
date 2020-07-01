# coding: utf-8

"""
    Trend Micro Deep Security API

    Copyright 2018 - 2020 Trend Micro Incorporated.<br/>Get protected, stay secured, and keep informed with Trend Micro Deep Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Deep Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 20.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RegistryScannerSessionInfo(object):
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
        'token': 'str',
        'expires': 'int',
        'url': 'str',
        'session_id': 'str'
    }

    attribute_map = {
        'token': 'token',
        'expires': 'expires',
        'url': 'url',
        'session_id': 'sessionID'
    }

    def __init__(self, token=None, expires=None, url=None, session_id=None):  # noqa: E501
        """RegistryScannerSessionInfo - a model defined in Swagger"""  # noqa: E501

        self._token = None
        self._expires = None
        self._url = None
        self._session_id = None
        self.discriminator = None

        if token is not None:
            self.token = token
        if expires is not None:
            self.expires = expires
        if url is not None:
            self.url = url
        if session_id is not None:
            self.session_id = session_id

    @property
    def token(self):
        """Gets the token of this RegistryScannerSessionInfo.  # noqa: E501

        Session token of the registry scanner.  # noqa: E501

        :return: The token of this RegistryScannerSessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this RegistryScannerSessionInfo.

        Session token of the registry scanner.  # noqa: E501

        :param token: The token of this RegistryScannerSessionInfo.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def expires(self):
        """Gets the expires of this RegistryScannerSessionInfo.  # noqa: E501

        Timestamp of the expiration date of the session token, in numbers of milliseconds since epoch.  # noqa: E501

        :return: The expires of this RegistryScannerSessionInfo.  # noqa: E501
        :rtype: int
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this RegistryScannerSessionInfo.

        Timestamp of the expiration date of the session token, in numbers of milliseconds since epoch.  # noqa: E501

        :param expires: The expires of this RegistryScannerSessionInfo.  # noqa: E501
        :type: int
        """

        self._expires = expires

    @property
    def url(self):
        """Gets the url of this RegistryScannerSessionInfo.  # noqa: E501

        URL of the registry scanner.  # noqa: E501

        :return: The url of this RegistryScannerSessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RegistryScannerSessionInfo.

        URL of the registry scanner.  # noqa: E501

        :param url: The url of this RegistryScannerSessionInfo.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def session_id(self):
        """Gets the session_id of this RegistryScannerSessionInfo.  # noqa: E501

        ID of the registry scanner session.  # noqa: E501

        :return: The session_id of this RegistryScannerSessionInfo.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this RegistryScannerSessionInfo.

        ID of the registry scanner session.  # noqa: E501

        :param session_id: The session_id of this RegistryScannerSessionInfo.  # noqa: E501
        :type: str
        """

        self._session_id = session_id

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
        if issubclass(RegistryScannerSessionInfo, dict):
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
        if not isinstance(other, RegistryScannerSessionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
