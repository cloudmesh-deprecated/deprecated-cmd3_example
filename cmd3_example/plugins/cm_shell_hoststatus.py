from __future__ import print_function
import os
from cloudmesh_common.tables import print_format_dict, two_column_table

from cmd3.console import Console
from cmd3.shell import command
import json
from cloudmesh.user.cm_user import cm_user
from cloudmesh.config.cm_config import cm_config
from pprint import pprint

from cmd3_example.HostStatus import HostStatus

class cm_shell_hoststatus:

    def activate_cm_shell_hoststatus(self):
        self.register_command_topic('mycommands', 'hoststatus')

    @command
    def do_hoststatus(self, args, arguments):
        """
        ::

          Usage:
              hoststatus NAME 

          tests via pingif the host ith the give NAME is reacahble

          Arguments:

            NAME      Name of the machine to test

          Options:

             -v       verbose mode

        """
        # pprint(arguments)

        if arguments["NAME"] is None:
            Console.error("Please specify a host name")
        else:
            host = arguments["NAME"]
            Console.info("trying to reach {0}".format(host))
            status = HostStatus.status(host)
            if status:
                Console.info("machine " + host + " has been found. ok.")
            else:
                Console.error("machine " + host + " not reachable. error.")
            
            
        # shell_command_open_ssh(arguments)
        pass

if __name__ == '__main__':
    command = cm_shell_hoststatus()
    command.do_hoststatus("iu.edu")
    command.do_hoststatus("iu.edu-wrong")