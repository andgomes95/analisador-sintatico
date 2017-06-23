import re
import sys
from program import *
aceitaveis = ["+","-","*","/","IDENTIFICADOR","NUMERAL","LITERAL","||","&&","==","!=","<",">",]
def erro(string):
	print string
	sys.exit
def Tlinha(i,simbolos,listIds,listFloat,listInt,listChar):
	if(simbolos[i][0]=="*" or simbolos[i][0]=="/"):
		i = nextsimb(i)
		i = F(i,simbolos,listIds,listFloat,listInt,listChar)
		i = Tlinha(i,simbolos,listIds,listFloat,listInt,listChar)
		return i
	elif(simbolos[i][0]=="<" or simbolos[i][0]==">" or simbolos[i][0]=="<=" or simbolos[i][0]==">=" or simbolos[i][0]=="+" or simbolos[i][0]=="-"or simbolos[i][0]=="||" or simbolos[i][0]=="&&" or simbolos[i][0]=="==" or simbolos[i][0]=="!=" or simbolos[i][0]==")"or simbolos[i][0] not in aceitaveis):
		return i
	else:
		print i
		erro("Tlinha")
		return i

def Dlinha(i,simbolos,listIds,listFloat,listInt,listChar):
	if(simbolos[i][0]=="+" or simbolos[i][0]=="-"):
		i = nextsimb(i)
		i = T(i,simbolos,listIds,listFloat,listInt,listChar)
		i = Dlinha(i,simbolos,listIds,listFloat,listInt,listChar)
		return i
	elif(simbolos[i][0]=="<" or simbolos[i][0]==">" or simbolos[i][0]=="<=" or simbolos[i][0]==">=" or simbolos[i][0]=="==" or simbolos[i][0]=="!=" or simbolos[i][0]==")" or simbolos[i][0]=="||" or simbolos[i][0]=="&&" or simbolos[i][0] not in aceitaveis):
		return i
	else:
		erro("Dlinha")
		return i


def Clinha(i,simbolos,listIds,listFloat,listInt,listChar):
	if(simbolos[i][0]=="<" or simbolos[i][0]==">" or simbolos[i][0]=="<=" or simbolos[i][0]==">="):
		i = nextsimb(i)
		i = D(i,simbolos,listIds,listFloat,listInt,listChar)
		i = Clinha(i,simbolos,listIds,listFloat,listInt,listChar)
		return i
	elif(simbolos[i][0]=="==" or simbolos[i][0]=="!=" or simbolos[i][0]==")" or simbolos[i][0]=="||" or simbolos[i][0]=="&&" or simbolos[i][0] not in aceitaveis):
		return i
	else:
		erro("Clinha")
		return i

def Blinha(i,simbolos,listIds,listFloat,listInt,listChar):
	if(simbolos[i][0]=="==" or simbolos[i][0]=="!="):
		i = nextsimb(i)
		i = C(i,simbolos,listIds,listFloat,listInt,listChar)
		i = Blinha(i,simbolos,listIds,listFloat,listInt,listChar)
		return i
	elif(simbolos[i][0]==")" or simbolos[i][0]=="||" or simbolos[i][0]=="&&" or simbolos[i][0] not in aceitaveis):
		return i
	else:
		erro("Blinha")
		return i

def Alinha(i,simbolos,listIds,listFloat,listInt,listChar):
	if(simbolos[i][0]=="&&"):
		i = nextsimb(i)
		i = B(i,simbolos,listIds,listFloat,listInt,listChar)
		i = Alinha(i,simbolos,listIds,listFloat,listInt,listChar)
		return i
	elif(simbolos[i][0]==")" or simbolos[i][0]=="||"  or simbolos[i][0] not in aceitaveis):
		return i
	else:
		erro("Alinha")
		return i


def Elinha(i,simbolos,listIds,listFloat,listInt,listChar):
	if(simbolos[i][0]=="||"):
		i = nextsimb(i)
		i = A(i,simbolos,listIds,listFloat,listInt,listChar)
		i = Elinha(i,simbolos,listIds,listFloat,listInt,listChar)
		return i
	elif(simbolos[i][0]==")"or simbolos[i][0] not in aceitaveis):
		return i
	else:
		erro("Elinha")
		return i

def F(i,simbolos,listIds,listFloat,listInt,listChar):
	if (simbolos[i][0]=="("):
		i = nextsimb(i)
		i = E(i,simbolos,listIds,listFloat,listInt,listChar)
		i = nextsimb(i)
		return i
		if(simbolos[i]!=")"):
			erro("F")
			return i
	elif(simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL"):
		checkDeclaracao(i,simbolos,listIds,listFloat,listInt,listChar)

		i = nextsimb(i)
		return i
	else:
		erro("F")
		return i

def T(i,simbolos,listIds,listFloat,listInt,listChar):
	if(simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL" or simbolos[i][0]=="("):
		i = F(i,simbolos,listIds,listFloat,listInt,listChar)
		i = Tlinha(i,simbolos,listIds,listFloat,listInt,listChar)
		return i
	else:
		erro("T")
		return i

def D(i,simbolos,listIds,listFloat,listInt,listChar):
	if(simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL" or simbolos[i][0]=="("):
		i = T(i,simbolos,listIds,listFloat,listInt,listChar)
		i = Dlinha(i,simbolos,listIds,listFloat,listInt,listChar)
		return i
	else:
		if simbolos[i][1] not in listIds and simbolos[i][0]=="IDENTIFICADOR":
			erro("Variavel "+simbolos[i][1]+" nao foi declarada. Erro na linha "+simbolos[i][2])
		erro("D")
		return i

def C(i,simbolos,listIds,listFloat,listInt,listChar):
	if(simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL" or simbolos[i][0]=="("):
		i = D(i,simbolos,listIds,listFloat,listInt,listChar)
		i = Clinha(i,simbolos,listIds,listFloat,listInt,listChar)
		return i
	else:
		erro("C")
		return i

def B(i,simbolos,listIds,listFloat,listInt,listChar):
	if(simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL" or simbolos[i][0]=="("):
		i = C(i,simbolos,listIds,listFloat,listInt,listChar)
		i = Blinha(i,simbolos,listIds,listFloat,listInt,listChar)
		return i
	else:
		erro("B")
		return i

def A(i,simbolos,listIds,listFloat,listInt,listChar):
	if(simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL" or simbolos[i][0]=="("):
		i = B(i,simbolos,listIds,listFloat,listInt,listChar)
		i = Alinha(i,simbolos,listIds,listFloat,listInt,listChar)
		return i
	else:
		erro("A")
		return i

def E(i,simbolos,listIds,listFloat,listInt,listChar):
	if (simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL" or simbolos[i][0]=="("):
		i = A(i,simbolos,listIds,listFloat,listInt,listChar)
		i = Elinha(i,simbolos,listIds,listFloat,listInt,listChar)
		return i
	else:
		print i
		erro("E")
		return i
def nextsimb(i):
	i = i+1
	return i
def checkDeclaracao(i,simbolos,listIds,listFloat,listInt,listChar):
	if simbolos[i][1] not in listIds and simbolos[i][0]=="IDENTIFICADOR":
		erro("Variavel "+simbolos[i][1]+" nao foi declarada. Erro na linha "+simbolos[i][2])
		print listFloat
