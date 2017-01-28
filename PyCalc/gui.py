#!/usr/bin/python

from wxPython.wx import *
from calcu import *

class MyFrame(wxFrame):
	# Constructor
	def __init__(self, parent, id, title):
		# Inicializamos el constructor de la clase padre wxFrame
		wxFrame.__init__(self, parent, id, title,
			wxPoint(100, 100), wxSize(560, 100))
		# Adherimos un panel dentro del frame
		panel = wxPanel(self, -1)
		bsuma = wxButton(self,12,"Suma",wxPoint(10, 10),wxSize(100, 100))
		
	# Este metodo es llamado automaticamente cuando el evento de cierre es enviado
	def OnCloseWindow(self, event):
		# destruye la ventana
		self.Destroy()

	def OnSize(self, event):
		size = event.GetSize()
		# tell the event system to continue looking for an event handler,
		# so the default handler will get called.
		event.Skip()

	# Este metodo es llamado por el sistema cuando la ventana es movida
	def OnMove(self, event):
		pos = event.GetPosition()
		

# Todas las aplicaciones wxWidgets deben tener una clase derivada de wxApp
class MyApp(wxApp):
	# wxWidgets llama al metodo para inicializar la aplicacion
	def OnInit(self):
		# Crea una instancia de nuestra customizada clase Frame
		frame = MyFrame(NULL, -1, "PyCalc")
		frame.Show(true)
		# Retorna una bandera de exito
		return true

app = MyApp(0)     # Crea la instancia de la clase de la Aplicacion
app.MainLoop()     # Empieza a procesar eventos

