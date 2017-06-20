import re
aceitaveis = ["+","-","*","/","IDENTIFICADOR","NUMERAL","LITERAL"]
def erro():
	print "EROU"
def Tlinha(i,simbolos):
	if(simbolos[i][0]=="*" or simbolos[i][0]=="/"):
		i = nextsimb(i)
		i = F(i,simbolos)
		i = Tlinha(i,simbolos)
		return i
	elif(simbolos[i][0]=="+" or simbolos[i][0]=="-" or simbolos[i][0]==")"or simbolos[i][0] not in aceitaveis):
		return i
	else:
		print i
		erro()
		return i

def Elinha(i,simbolos):
	if(simbolos[i][0]=="+" or simbolos[i][0]=="-"):
		i = nextsimb(i)
		i = T(i,simbolos)
		i = Elinha(i,simbolos)
		return i
	elif(simbolos[i][0]==")"or simbolos[i][0] not in aceitaveis):
		return i
	else:
		erro()
		return i

def F(i,simbolos):
	if (simbolos[i][0]=="("):
		i = nextsimb(i)
		i = E(i,simbolos)
		i = nextsimb(i)
		return i
		if(simbolos[i]!=")"):
			erro()
			return i
	elif(simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL"):
		i = nextsimb(i)
		return i
	else:
		erro()
		return i

def T(i,simbolos):
	if(simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL" or simbolos[i][0]=="("):
		i = F(i,simbolos)
		i = Tlinha(i,simbolos)
		return i
	else:
		erro()
		return i

def E(i,simbolos):
	if (simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL" or simbolos[i][0]=="("):
		i = T(i,simbolos)
		i = Elinha(i,simbolos)
		return i
	else:
		print i
		erro()
		return i

def nextsimb(i):
	i = i+1
	return i
