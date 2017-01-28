#!/usr/bin/python

class Calculadora():
	def __init__(self):
		self.resultado = 0.0
	def suma(self,a,b):
		self.resultado = float(a+b)
		return self.resultado
	def resta(self,a,b):
		self.resultado = float(a-b)
		return self.resultado
	def multip(self,a,b):
		self.resultado = float(a*b)
		return self.resultado
	def div(self,a,b):
		self.resultado = float(a/b)
		return self.resultado
	def last(self):
		return str(self.resultado)

