#!/usr/bin/env python3

class Enum():
   def __init__(self, *args):
      for i in range(len(args)):
         setattr(self, args[i], i)


states = Enum("DEFAULT", "STRING", "EQUATION", "VARIABLE", "NAMING", "VARSTRING", "VAREQUATION")
"""
0 : DEFAULT     : NORMAL
1 : STRING      : INSIDE A LITERAL STATEMENT
2 : EQUATION    : INSIDE A MATHEMATICAL STATEMENT
3 : VARIABLE    : VARIABLE INSTANTIATION
"""
