# pylint: disable=C0111,R0902,R0904,R0912,R0913,R0915,E1101
# Smartsheet Python SDK.
#
# Copyright 2016 Smartsheet.com, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"): you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from __future__ import absolute_import

from ..util import prep
from .object_value import ObjectValue
import json
import six

class Contact(object):

    """Smartsheet Contact data model."""

    def __init__(self, props=None, base_obj=None):
        """Initialize the Contact model."""
        if isinstance(super(Contact, self), ObjectValue):
            super(Contact, self).__init__(props, base_obj)
        self._base = None
        if base_obj is not None:
            self._base = base_obj

        self._email = None
        self.__id = None
        self._name = None

        if props:
            # account for alternate variable names from raw API response
            if 'email' in props:
                self.email = props['email']
            if 'id' in props:
                self._id = props['id']
            if '_id' in props:
                self._id = props['_id']
            if 'name' in props:
                self.name = props['name']
        # requests package Response object
        self.request_response = None
        self.__initialized = True

    def __getattr__(self, key):
        if key == 'id':
            return self._id
        else:
            raise AttributeError(key)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if isinstance(value, six.string_types):
            self._email = value

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        if isinstance(value, six.string_types):
            self.__id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, six.string_types):
            self._name = value

    def to_dict(self, op_id=None, method=None):
        parent_obj = {}
        if isinstance(super(Contact, self), ObjectValue):
            parent_obj = super(Contact, self).to_dict(op_id, method)
        obj = {
            'email': prep(self._email),
            'id': prep(self.__id),
            'name': prep(self._name)}
        combo = parent_obj.copy()
        combo.update(obj)
        return combo

    def to_json(self):
        return json.dumps(self.to_dict(), indent=2)

    def __str__(self):
        return json.dumps(self.to_dict())
