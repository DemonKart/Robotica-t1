#!/usr/bin/env python
from math import sqrt

class Ponto(object):
  x = 0
  y = 0
  t = 0.0
  
  def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.t = t

text_file = open("in.txt", "r")
lines = text_file.read().split('\n')

pontos = []

for i in range(len(lines)):                                                                                                                                                                                   
  dados = lines[i].split(',')
  p = Ponto(dados[0], dados[1], dados[2])
  pontos.append(p)
  
for p in pontos:
  print "p = (" + p.x + "," + p.y + "), " + p.t
  


text_file.close()