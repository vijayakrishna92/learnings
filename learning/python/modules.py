# modules
# modules are files that contain Python code. They can define functions, classes, and variables that can be reused in other Python programs.
# Modules are a way to organize code and make it more manageable. They can be imported into other Python files using the import statement.
import math # math is a built-in module in Python that provides mathematical functions and constants
print(math.pi)

from math import pi, sqrt, sin, cos, tan, radians, degrees
print(pi)

import math as m
m.cos(0)

from math import *
print(math.pi)

from packages import module_1 # This imports the module_1 module from the packages package
module_1.ant()
module_1.bee()

from packages.module_1 import ant, bee
ant()