"""
    FFM by @JusticeRage

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from model.driver.input_api import *
from model.plugin.command import Command
from commands.command_manager import register_plugin
import os


class RunPyScript(Command):
    def __init__(self, *args):
        if len(args) < 2:
            raise RuntimeError("Received %d argument(s), expected 2." % len(args))
        self.script = os.path.expanduser(args[1])
        if not os.path.exists(self.script):
            raise RuntimeError("%s not found!" % self.script)
        self.script_args = " ".join(args[2:]) if len(args) > 2 else None

    @staticmethod
    def regexp():
        return r"^\s*\!py($| )"

    @staticmethod
    def usage():
        write_str("Usage: !py [script on the local machine] [script arguments]\r\n", LogLevel.WARNING)

    @staticmethod
    def name():
        return "!py"

    @staticmethod
    def description():
        return "Runs a python script from the local machine in memory."

    def execute(self):
        with open(self.script, 'r') as f:
            contents = f.read()
            shell_exec("python - %s <<'__EOF__'\r\n%s\r\n__EOF__" % (self.script_args, contents), print_output=True)


register_plugin(RunPyScript)
