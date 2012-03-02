# -*- coding: utf-8 -*-
# Copyright (C) 2012 Sebastian Wiesner <lunaryorn@googlemail.com>

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

from __future__ import (print_function, division, unicode_literals,
                        absolute_import)

import sys
import os
import socket


class FakeMonitor(object):
    """
    A dummy pyudev.Monitor class, which allows clients to trigger arbitrary
    events, emitting clearly defined device objects.
    """

    def __init__(self, device_to_emit):
        self.client, self.server = socket.socketpair(
            socket.AF_UNIX, socket.SOCK_DGRAM)
        if sys.version_info[0] >= 3:
            # in python 3 sockets returned by socketpair() lack the
            # ".makefile()" method, which is required by this class.  Work
            # around this limitation by wrapping these sockets in real
            # socket objects.
            def _wrap_socket(sock):
                wrapped = socket.socket(sock.family, sock.type,
                                        fileno=os.dup(sock.fileno()))
                sock.close()
                return wrapped
            self.client, self.server = (_wrap_socket(self.client),
                                        _wrap_socket(self.server))
        self.device_to_emit = device_to_emit

    def trigger_action(self, action):
        """
        Trigger the given ``action`` on clients of this monitor.
        """
        with self.server.makefile('w') as stream:
            stream.write(action)
            stream.write('\n')
            stream.flush()

    def fileno(self):
        return self.client.fileno()

    def enable_receiving(self):
        pass

    def filter_by(self, *args):
        pass

    start = enable_receiving

    def receive_device(self):
        with self.client.makefile('r') as stream:
            action = stream.readline().strip()
            return action, self.device_to_emit

    def close(self):
        """
        Close sockets acquired by this monitor.
        """
        try:
            self.client.close()
        finally:
            self.server.close()


def pytest_funcarg__fake_monitor(request):
    """
    Return a FakeMonitor, which emits the platform device as returned by
    the ``fake_monitor_device`` funcarg on all triggered actions.
    """
    return FakeMonitor(request.getfuncargvalue('fake_monitor_device'))
