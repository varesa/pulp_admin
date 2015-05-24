#!/bin/env python3

from pulp_connection import PulpConnection
from auth import Auth

from pulp import Pulp

from menu import Menu


auth = Auth()
auth.init()

pulp = Pulp(PulpConnection(auth=auth.get_tuple()))

menu = Menu(pulp)
menu.mainmenu()
