# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.become import BecomeBase


class BecomeModule(BecomeBase):

    name = 'podman_unshare'

    def build_become_command(self, cmd, shell):
        super(BecomeModule, self).build_become_command(cmd, shell)

        if not cmd:
            return cmd

        exe = self.get_option('become_exe') or 'podman'
        flags = self.get_option('become_flags') or ''

        return '%s unshare %s %s' % (exe, flags, self._build_success_command(cmd, shell))
