import re
aceitaveis = ["+","-","*","/","IDENTIFICADOR","NUMERAL","LITERAL","||","&&","==","!=","<",">",]
def erro(string):
	print string
def Tlinha(i,simbolos):
	if(simbolos[i][0]=="*" or simbolos[i][0]=="/"):
		i = nextsimb(i)
		i = F(i,simbolos)
		i = Tlinha(i,simbolos)
		return i
	elif(simbolos[i][0]=="<" or simbolos[i][0]==">" or simbolos[i][0]=="<=" or simbolos[i][0]==">=" or simbolos[i][0]=="+" or simbolos[i][0]=="-"or simbolos[i][0]=="||" or simbolos[i][0]=="&&" or simbolos[i][0]=="==" or simbolos[i][0]=="!=" or simbolos[i][0]==")"or simbolos[i][0] not in aceitaveis):
		return i
	else:
		print i
		erro("Tlinha")
		return i

def Dlinha(i,simbolos):
	if(simbolos[i][0]=="+" or simbolos[i][0]=="-"):
		i = nextsimb(i)
		i = T(i,simbolos)
		i = Dlinha(i,simbolos)
		return i
	elif(simbolos[i][0]=="<" or simbolos[i][0]==">" or simbolos[i][0]=="<=" or simbolos[i][0]==">=" or simbolos[i][0]=="==" or simbolos[i][0]=="!=" or simbolos[i][0]==")" or simbolos[i][0]=="||" or simbolos[i][0]=="&&" or simbolos[i][0] not in aceitaveis):
		return i
	else:
		erro("Dlinha")
		return i


def Clinha(i,simbolos):
	if(simbolos[i][0]=="<" or simbolos[i][0]==">" or simbolos[i][0]=="<=" or simbolos[i][0]==">="):
		i = nextsimb(i)
		i = D(i,simbolos)
		i = Clinha(i,simbolos)
		return i
	elif(simbolos[i][0]=="==" or simbolos[i][0]=="!=" or simbolos[i][0]==")" or simbolos[i][0]=="||" or simbolos[i][0]=="&&" or simbolos[i][0] not in aceitaveis):
		return i
	else:
		erro("Clinha")
		return i

def Blinha(i,simbolos):
	if(simbolos[i][0]=="==" or simbolos[i][0]=="!="):
		i = nextsimb(i)
		i = C(i,simbolos)
		i = Blinha(i,simbolos)
		return i
	elif(simbolos[i][0]==")" or simbolos[i][0]=="||" or simbolos[i][0]=="&&" or simbolos[i][0] not in aceitaveis):
		return i
	else:
		erro("Blinha")
		return i

def Alinha(i,simbolos):
	if(simbolos[i][0]=="&&"):
		i = nextsimb(i)
		i = B(i,simbolos)
		i = Alinha(i,simbolos)
		return i
	elif(simbolos[i][0]==")" or simbolos[i][0]=="||"  or simbolos[i][0] not in aceitaveis):
		return i
	else:
		erro("Alinha")
		return i


def Elinha(i,simbolos):
	if(simbolos[i][0]=="||"):
		i = nextsimb(i)
		i = A(i,simbolos)
		i = Elinha(i,simbolos)
		return i
	elif(simbolos[i][0]==")"or simbolos[i][0] not in aceitaveis):
		return i
	else:
		erro("Elinha")
		return i

def F(i,simbolos):
	if (simbolos[i][0]=="("):
		i = nextsimb(i)
		i = E(i,simbolos)
		i = nextsimb(i)
		return i
		if(simbolos[i]!=")"):
			erro("F")
			return i
	elif(simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL"):
		i = nextsimb(i)
		return i
	else:
		erro("F")
		return i

def T(i,simbolos):
	if(simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL" or simbolos[i][0]=="("):
		i = F(i,simbolos)
		i = Tlinha(i,simbolos)
		return i
	else:
		erro("T")
		return i

def D(i,simbolos):
	if(simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL" or simbolos[i][0]=="("):
		i = T(i,simbolos)
		i = Dlinha(i,simbolos)
		return i
	else:
		erro("D")
		return i

def C(i,simbolos):
	if(simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL" or simbolos[i][0]=="("):
		i = D(i,simbolos)
		i = Clinha(i,simbolos)
		return i
	else:
		erro("C")
		return i

def B(i,simbolos):
	if(simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL" or simbolos[i][0]=="("):
		i = C(i,simbolos)
		i = Blinha(i,simbolos)
		return i
	else:
		erro("B")
		return i

def A(i,simbolos):
	if(simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL" or simbolos[i][0]=="("):
		i = B(i,simbolos)
		i = Alinha(i,simbolos)
		return i
	else:
		erro("A")
		return i

def E(i,simbolos):
	if (simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL" or simbolos[i][0]=="("):
		i = A(i,simbolos)
		i = Elinha(i,simbolos)
		return i
	else:
		print i
		erro("E")
		return i
def nextsimb(i):
	i = i+1
	return i
