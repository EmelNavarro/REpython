import re
import sys
"""A123minusculas$%&([1-9]{3,3})([a-z]*)([]{3,3})s"""
class xpresionregular:
	def __init__ (self,expresion):
		self.expresion=expresion
	def ValidarExpresion(self):
		xpresionregular=re.compile(r'(([A-Z]{1,1})([1-9]{3,3})([a-z]*)(\W{3,3}))')
		if xpresionregular.match(self.expresion)is not None:
			print(self.expresion,"es una expresion valida")
		else:
			print(self.expresion,"no es una palabra correcta")
palabra = sys.argv[1] 
expresionRegular=xpresionregular(palabra)
expresionRegular.ValidarExpresion()


