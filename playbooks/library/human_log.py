# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Inspired from: https://gist.github.com/cliffano/9868180
# Improved and made compatible with Ansible v2

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.callback import CallbackBase
try:
    import simplejson as json
except ImportError:
    import json

import os
import datetime
import re
from json2html import *

# Fields to reformat output for
FIELDS = ['cmd', 'command', 'start', 'end', 'delta', 'msg', 'stdout',
          'stderr', 'results']

HTML_HEADER = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Ansible playbook logs</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">

  <style>
      td {
          white-space: pre;
      }
  </style>
</head>
<body>
  <h1 class="text-center">Ansible playbook logs</h1>
  <h2 class="text-center">%s @ %s</h2>
""".encode('ascii', 'replace')


class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'aggregate'
    CALLBACK_NAME = 'human_log'
    CALLBACK_NEEDS_WHITELIST = False

    def __init__(self):
        super(CallbackModule, self).__init__()
        self.printed_playbook = False
        self.log_filename = None
        self.log_path = None
        self.play = None
        self.playbook = None

    def human_log(self, data):
        if type(data) == dict:
            for field in FIELDS:
                if field in data.keys() and data[field]:
                    output = self._format_output(data[field])
                    print("\n{0}: {1}".format(field,
                                              output.replace("\\n","\n")))
            self._write_to_log(data.encode('ascii', 'replace'))

    def _format_output(self, output):
        # Strip unicode
        if type(output) == unicode:
            output = output.encode('ascii', 'replace')

        # If output is a dict
        if type(output) == dict:
            return json.dumps(output, indent=2)

        # If output is a list of dicts
        if type(output) == list and type(output[0]) == dict:
            # This gets a little complicated because it potentially means
            # nested results, usually because of with_items.
            real_output = list()
            for index, item in enumerate(output):
                copy = item
                if type(item) == dict:
                    for field in FIELDS:
                        if field in item.keys():
                            copy[field] = self._format_output(item[field])
                real_output.append(copy)
            return json.dumps(output, indent=2)

        # If output is a list of strings
        if type(output) == list and type(output[0]) != dict:
            # Strip newline characters
            real_output = list()
            for item in output:
                if "\n" in item:
                    for string in item.split("\n"):
                        real_output.append(string)
                else:
                    real_output.append(item)

            # Reformat lists with line breaks only if the total length is
            # >75 chars
            if len("".join(real_output)) > 75:
                return "\n" + "\n".join(real_output)
            else:
                return " ".join(real_output)

        # Otherwise it's a string, just return it
        return output

    def _write_to_log(self, message):
        with open(self.log_path, 'a+') as f:
            f.write(json2html.convert(json=json.dumps(message),
                                      table_attributes='class="table '
                                                       'table-bordered '
                                                       'table-hover '
                                                       'table-condensed"'))
            f.write('<hr>')
        f.close()

    def runner_on_failed(self, host, res, ignore_errors=False):
        self.human_log(res)

    def runner_on_ok(self, host, res):
        self.human_log(res)

    def runner_on_unreachable(self, host, res):
        self.human_log(res)

    def runner_on_async_poll(self, host, res, jid, clock):
        self.human_log(res)

    def runner_on_async_ok(self, host, res, jid):
        self.human_log(res)

    def runner_on_async_failed(self, host, res, jid):
        self.human_log(res)

    def v2_playbook_on_start(self, playbook):
        self.playbook = playbook

    def v2_playbook_on_play_start(self, play):
        self.play = play

        if not self.printed_playbook:
            playbook_path = self.playbook._basedir
            log_dir = os.path.join(playbook_path, 'logs')
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)

            playbook_file = self.playbook._file_name
            playbook_file = os.path.basename(playbook_file)
            playbook_name = re.sub(r"\.(yml|yaml)", '', playbook_file)
            now = datetime.datetime.now().strftime('%m-%d_%H:%M:%S')
            friendly_now = datetime.datetime.now().strftime('%c%Z')

            log_filename = "{0}_log_{1}.html".format(playbook_name, now)
            self.log_path = os.path.join(log_dir, log_filename)
            if not os.path.exists(self.log_path):
                with open(self.log_path, 'a+') as f:
                    header = HTML_HEADER % (playbook_file, friendly_now)
                    f.write(header)
                f.close()

            self.printed_playbook = True
