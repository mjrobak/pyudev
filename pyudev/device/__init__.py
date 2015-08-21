# -*- coding: utf-8 -*-
# Copyright (C) 2015 mulhern <amulhern@redhat.com>

# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation; either version 2.1 of the License, or (at your
# option) any later version.

# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
# for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this library; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA

"""
    pyudev.device
    =============

    Device class implementation of :mod:`pyudev`.

    .. moduleauthor::  Sebastian Wiesner  <lunaryorn@gmail.com>
"""

__all__ = [
  'Attributes',
  'Device',
  'DeviceNotFoundAtPathError',
  'DeviceNotFoundByNameError',
  'DeviceNotFoundByNumberError',
  'DeviceNotFoundError',
  'DeviceNotFoundInEnvironmentError',
  'Tags'
]

from ._device import Attributes
from ._device import Device
from ._device import Tags
from ._errors import DeviceNotFoundAtPathError
from ._errors import DeviceNotFoundByNameError
from ._errors import DeviceNotFoundByNumberError
from ._errors import DeviceNotFoundError
from ._errors import DeviceNotFoundInEnvironmentError
