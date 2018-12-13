import importlib.util
import os.path
import sys
sys.path.insert(0, '../img-generator')
sys.path.insert(0, '../convNet')
import generate_dataset
import convNet
import dataFeeder


generate_dataset.generate_dataset("../DataSet")


print()