#!/usr/bin/python

import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
from calcu import *

class Ventana(Gtk.Window):
	def __init__(self,c):
		# Constructor de la clase Gtk.Window
		Gtk.Window.__init__(self,title="PyCalc",resizable=False)
		self.set_size_request(270,170)
		self.calculadora = c
		# Construyendo el area dentro de la ventana
		self.area = Gtk.Fixed()
		# Construyo elementos de la ventana
		self.creditos = Gtk.Label("Calculadora by reGNU")
		self.creditos.set_size_request(270,15)
		self.resultado = Gtk.Label("Resultado: "+ str(self.calculadora.last()))
		self.resultado.set_size_request(270,15)
		self.a = Gtk.Label("a:")
		self.b = Gtk.Label("b:")
		self.caja_entrada_a = Gtk.Entry()
		self.caja_entrada_a.set_size_request(200,20)
		self.caja_entrada_b = Gtk.Entry()
		self.caja_entrada_b.set_size_request(200,20)
		self.btnsuma = Gtk.Button(label="+")
		self.btnsuma.connect("clicked",self.btnsuma_clicked)
		self.btnsuma.set_size_request(50,50)
		self.btnres = Gtk.Button(label="-")
		self.btnres.connect("clicked",self.btnres_clicked)
		self.btnres.set_size_request(50,50)
		self.btnmul = Gtk.Button(label="*")
		self.btnmul.connect("clicked",self.btnmul_clicked)
		self.btnmul.set_size_request(50,50)
		self.btndiv = Gtk.Button(label="/")
		self.btndiv.connect("clicked",self.btndiv_clicked)
		self.btndiv.set_size_request(50,50)
		self.area.put(self.caja_entrada_a,50,10)
		self.area.put(self.caja_entrada_b,50,40)
		self.area.put(self.btnsuma,20,70)
		self.area.put(self.btnres,80,70)
		self.area.put(self.btnmul,140,70)
		self.area.put(self.btndiv,200,70)
		self.area.put(self.creditos,0,150)
		self.area.put(self.resultado,0,130)
		self.area.put(self.a,20,10)
		self.area.put(self.b,20,40)
		self.add(self.area)
		self.connect("delete-event",Gtk.main_quit)
		
	def btnsuma_clicked(self,widget):
		try:
			a = float(self.caja_entrada_a.get_text())
			b = float(self.caja_entrada_b.get_text())
			self.resultado.set_text("Resultado: " + str(self.calculadora.suma(a,b)))
		except:
			self.resultado.set_text("Syntax Error!")
		self.caja_entrada_a.set_text(self.calculadora.last())
		self.caja_entrada_b.set_text("")
		
	def btnres_clicked(self,widget):
		try:
			a = float(self.caja_entrada_a.get_text())
			b = float(self.caja_entrada_b.get_text())
			self.resultado.set_text("Resultado: " + str(self.calculadora.resta(a,b)))
		except:
			self.resultado.set_text("Syntax Error!")
		self.caja_entrada_a.set_text(self.calculadora.last())
		self.caja_entrada_b.set_text("")
	def btndiv_clicked(self,widget):
		try:
			a = float(self.caja_entrada_a.get_text())
			b = float(self.caja_entrada_b.get_text())
			if b == 0:
				self.resultado.set_text("Math error!")
			else:
				self.resultado.set_text("Resultado: " + str(self.calculadora.div(a,b)))
		except:
			self.resultado.set_text("Syntax Error!")
		self.caja_entrada_a.set_text(self.calculadora.last())
		self.caja_entrada_b.set_text("")
	def btnmul_clicked(self,widget):
		try:
			a = float(self.caja_entrada_a.get_text())
			b = float(self.caja_entrada_b.get_text())
			self.resultado.set_text("Resultado: " + str(self.calculadora.multip(a,b)))
		except:
			self.resultado.set_text("Syntax Error!")
		self.caja_entrada_a.set_text(self.calculadora.last())
		self.caja_entrada_b.set_text("")

c = Calculadora()
v = Ventana(c)
v.show_all()
Gtk.main()
