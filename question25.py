# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:39:16 2017

@author: User
"""

import re

email=raw_input("Enter mail:")

format = "(\w+)@(\w+)\.(com)"

name = re.match(format,email)

print name.group(2)
