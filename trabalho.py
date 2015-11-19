#!/usr/bin/env python
from math import atan2, sqrt, pi

class Ponto(object):
  x = 0.0
  y = 0.0
  t = 0.0
  v = 0.0
  a = 0.0
  
  def __init__(self, x, y, t, v, a):
        self.x = x
        self.y = y
        self.t = t
        self.v = 0.0
        self.a = 0.0

def velocidade(p1, p2):
  deltaX = p2.x-p1.x
  deltaY = p2.y-p1.y
  deltaT = p2.t-p1.t
  
  deltaS = sqrt(abs((deltaY^2)-(deltaX^2))) # Calculo de velocidade media
  return (deltaS/deltaT)

def angulo(p1, p2):
  deltaX = p2.x-p1.x
  deltaY = p2.y-p1.y

  if deltaX == 0: # Se nao se deslocou no eixo X, divisao por zero!
    if deltaY > 0: # Se deslocou em Y para cima
      return 90.0
    if deltaY < 0: # Se deslocou em Y para baixo
      return -90.0
    return p1.a # Nao se deslocou nem em X nem em Y

  a = atan2(deltaY, deltaX) * 180 / pi # Calcula o angulo
    
  return a # Se deslocou em X e Y
  
  
text_file = open("in.txt", "r")
lines = text_file.read().split('\n')

pontos = []

for i in range(len(lines)):                                                                                                                                                                                   
  dados = lines[i].split(',')
  p = Ponto(int(dados[0]), int(dados[1]), float(dados[2]),0.0,0.0)
  if i > 0: # Se estiver a partir do segundo ponto
    p.v = velocidade(pontos[i-1], p)
    p.a = angulo(pontos[i-1], p)
    
  pontos.append(p)
  
for i in range(len(lines)):
  p = pontos[i]
  print "P" + str(i) + "= (" + str(p.x) + "," + str(p.y) + ") \t| Tempo " + str(p.t) + "\t | Angulo " + str("%0.4f" % p.a) + "\t | Velocidade=> Total: " + str("%0.4f" % p.v) + " \t Cada roda: " + str("%0.4f" % ((p.v)/2))

text_file.close()