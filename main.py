#!/bin/env python3

import argparse
import sys

from pulp_connection import PulpConnection
from auth import Auth
from pulp import Pulp
from menu import Menu

parser = argparse.ArgumentParser()
parser.add_argument('--username', default=None)
parser.add_argument('--password', default=None)
parser.add_argument('--nosslverify', dest="nosslverify", action="store_true", default=False)
args = parser.parse_args()
auth = Auth(username=args.username, password=args.password)
auth.init()

if args.nosslverify:
    import requests.packages.urllib3 as urllib3
    urllib3.disable_warnings()
    pulp = Pulp(PulpConnection(auth=auth.get_tuple(), ca=False))
else:
    pulp = Pulp(PulpConnection(auth=auth.get_tuple()))

menu = Menu(pulp)
menu.mainmenu()
