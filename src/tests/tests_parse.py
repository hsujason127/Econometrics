import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from parse import *

p = GetData('./raw_data.csv')
result = p.GetIndex("s&p500")
for res in result:
    print(res.name_, res.date_, res.price_)