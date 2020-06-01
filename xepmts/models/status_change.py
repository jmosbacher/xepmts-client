# coding: utf-8

"""
    PMT API

    API for the XenonnT PMT database  # noqa: E501

    OpenAPI spec version: 0.1
    Contact: joe.mosbacher@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class StatusChange(object):
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
        'timestamp': 'int',
        'detector': 'str',
        'experiment': 'str',
        'new_status': 'str',
        'event': 'str',
        'operator': 'str',
        'comments': 'str',
        '_date': 'str',
        'id': 'str'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'detector': 'detector',
        'experiment': 'experiment',
        'new_status': 'new_status',
        'event': 'event',
        'operator': 'operator',
        'comments': 'comments',
        '_date': 'date',
        'id': '_id'
    }

    def __init__(self, timestamp=None, detector=None, experiment=None, new_status=None, event=None, operator=None, comments=None, _date=None, id=None):  # noqa: E501
        """StatusChange - a model defined in Swagger"""  # noqa: E501
        self._timestamp = None
        self._detector = None
        self._experiment = None
        self._new_status = None
        self._event = None
        self._operator = None
        self._comments = None
        self.__date = None
        self._id = None
        self.discriminator = None
        if timestamp is not None:
            self.timestamp = timestamp
        if detector is not None:
            self.detector = detector
        if experiment is not None:
            self.experiment = experiment
        if new_status is not None:
            self.new_status = new_status
        if event is not None:
            self.event = event
        if operator is not None:
            self.operator = operator
        if comments is not None:
            self.comments = comments
        if _date is not None:
            self._date = _date
        if id is not None:
            self.id = id

    @property
    def timestamp(self):
        """Gets the timestamp of this StatusChange.  # noqa: E501


        :return: The timestamp of this StatusChange.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this StatusChange.


        :param timestamp: The timestamp of this StatusChange.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def detector(self):
        """Gets the detector of this StatusChange.  # noqa: E501


        :return: The detector of this StatusChange.  # noqa: E501
        :rtype: str
        """
        return self._detector

    @detector.setter
    def detector(self, detector):
        """Sets the detector of this StatusChange.


        :param detector: The detector of this StatusChange.  # noqa: E501
        :type: str
        """
        allowed_values = ["tpc", "nveto", "muveto", "unknown"]  # noqa: E501
        if detector not in allowed_values:
            raise ValueError(
                "Invalid value for `detector` ({0}), must be one of {1}"  # noqa: E501
                .format(detector, allowed_values)
            )

        self._detector = detector

    @property
    def experiment(self):
        """Gets the experiment of this StatusChange.  # noqa: E501


        :return: The experiment of this StatusChange.  # noqa: E501
        :rtype: str
        """
        return self._experiment

    @experiment.setter
    def experiment(self, experiment):
        """Sets the experiment of this StatusChange.


        :param experiment: The experiment of this StatusChange.  # noqa: E501
        :type: str
        """
        allowed_values = ["xenon1t", "xenonnt", "unknown"]  # noqa: E501
        if experiment not in allowed_values:
            raise ValueError(
                "Invalid value for `experiment` ({0}), must be one of {1}"  # noqa: E501
                .format(experiment, allowed_values)
            )

        self._experiment = experiment

    @property
    def new_status(self):
        """Gets the new_status of this StatusChange.  # noqa: E501


        :return: The new_status of this StatusChange.  # noqa: E501
        :rtype: str
        """
        return self._new_status

    @new_status.setter
    def new_status(self, new_status):
        """Sets the new_status of this StatusChange.


        :param new_status: The new_status of this StatusChange.  # noqa: E501
        :type: str
        """

        self._new_status = new_status

    @property
    def event(self):
        """Gets the event of this StatusChange.  # noqa: E501


        :return: The event of this StatusChange.  # noqa: E501
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this StatusChange.


        :param event: The event of this StatusChange.  # noqa: E501
        :type: str
        """

        self._event = event

    @property
    def operator(self):
        """Gets the operator of this StatusChange.  # noqa: E501


        :return: The operator of this StatusChange.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this StatusChange.


        :param operator: The operator of this StatusChange.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def comments(self):
        """Gets the comments of this StatusChange.  # noqa: E501


        :return: The comments of this StatusChange.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this StatusChange.


        :param comments: The comments of this StatusChange.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def _date(self):
        """Gets the _date of this StatusChange.  # noqa: E501


        :return: The _date of this StatusChange.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this StatusChange.


        :param _date: The _date of this StatusChange.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def id(self):
        """Gets the id of this StatusChange.  # noqa: E501


        :return: The id of this StatusChange.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StatusChange.


        :param id: The id of this StatusChange.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if issubclass(StatusChange, dict):
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
        if not isinstance(other, StatusChange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
