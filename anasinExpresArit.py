import re
import sys
from program import *
aceitaveis = ["+","-","*","/","IDENTIFICADOR","NUMERAL","LITERAL","||","&&","==","!=","<",">",]
def erro(string):
	print string
	sys.exit
def Tlinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY):
	if(simbolos[i][0]=="*" or simbolos[i][0]=="/"):
		i = nextsimb(i)
		i,typeY = F(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		i,typeY = Tlinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		return i,typeY
	elif(simbolos[i][0]=="<" or simbolos[i][0]==">" or simbolos[i][0]=="<=" or simbolos[i][0]==">=" or simbolos[i][0]=="+" or simbolos[i][0]=="-"or simbolos[i][0]=="||" or simbolos[i][0]=="&&" or simbolos[i][0]=="==" or simbolos[i][0]=="!=" or simbolos[i][0]==")"or simbolos[i][0] not in aceitaveis):
		return i,typeY
	else:
		print i
		erro("Tlinha")
		return i,typeY

def Dlinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY):
	if(simbolos[i][0]=="+" or simbolos[i][0]=="-"):
		i = nextsimb(i)
		i,typeY = T(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		i,typeY = Dlinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		return i,typeY
	elif(simbolos[i][0]=="<" or simbolos[i][0]==">" or simbolos[i][0]=="<=" or simbolos[i][0]==">=" or simbolos[i][0]=="==" or simbolos[i][0]=="!=" or simbolos[i][0]==")" or simbolos[i][0]=="||" or simbolos[i][0]=="&&" or simbolos[i][0] not in aceitaveis):
		return i,typeY
	else:
		erro("Dlinha")
		return i,typeY


def Clinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY):
	if(simbolos[i][0]=="<" or simbolos[i][0]==">" or simbolos[i][0]=="<=" or simbolos[i][0]==">="):
		i = nextsimb(i)
		i,typeY = D(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		i,typeY = Clinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		return i,typeY
	elif(simbolos[i][0]=="==" or simbolos[i][0]=="!=" or simbolos[i][0]==")" or simbolos[i][0]=="||" or simbolos[i][0]=="&&" or simbolos[i][0] not in aceitaveis):
		return i,typeY
	else:
		erro("Clinha")
		return i,typeY

def Blinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY):
	if(simbolos[i][0]=="==" or simbolos[i][0]=="!="):
		i = nextsimb(i)
		i,typeY = C(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		i,typeY = Blinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		return i,typeY
	elif(simbolos[i][0]==")" or simbolos[i][0]=="||" or simbolos[i][0]=="&&" or simbolos[i][0] not in aceitaveis):
		return i,typeY
	else:
		erro("Blinha")
		return i,typeY

def Alinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY):
	if(simbolos[i][0]=="&&"):
		i = nextsimb(i)
		i,typeY = B(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		i,typeY = Alinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		return i,typeY
	elif(simbolos[i][0]==")" or simbolos[i][0]=="||"  or simbolos[i][0] not in aceitaveis):
		return i,typeY
	else:
		erro("Alinha")
		return i,typeY


def Elinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY):
	if(simbolos[i][0]=="||"):
		i = nextsimb(i)
		i,typeY = A(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		i,typeY = Elinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		return i,typeY
	elif(simbolos[i][0]==")"or simbolos[i][0] not in aceitaveis):
		return i,typeY
	else:
		erro("Elinha")
		return i,typeY

def F(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY):
	if (simbolos[i][0]=="("):
		i = nextsimb(i)
		i,typeY = E(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		i = nextsimb(i)
		return i,typeY
		if(simbolos[i]!=")"):
			erro("F")
			return i,typeY
	elif(simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL"):
		typei = checkDeclaracao(i,simbolos,listIds,listFloatId,listIntId,listCharId)
		if typeY == "":
			typeY = typei
		elif typeY == typei:
			pass
		else:
			erro("Declaracao errada no token "+simbolos[i][1]+" na linha "+simbolos[i][2])
		i = nextsimb(i)
		return i,typeY
	else:
		erro("F")
		return i,typeY

def T(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY):
	if(simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL" or simbolos[i][0]=="("):
		i,typeY = F(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		i,typeY = Tlinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		return i,typeY
	else:
		erro("T")
		return i,typeY

def D(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY):
	if(simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL" or simbolos[i][0]=="("):
		i,typeY = T(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		i,typeY = Dlinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		return i,typeY
	else:
		if simbolos[i][1] not in listIds and simbolos[i][0]=="IDENTIFICADOR":
			erro("Variavel "+simbolos[i][1]+" nao foi declarada. Erro na linha "+simbolos[i][2])
		erro("D")
		return i,typeY

def C(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY):
	if(simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL" or simbolos[i][0]=="("):
		i,typeY = D(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		i,typeY = Clinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		return i,typeY
	else:
		erro("C")
		return i,typeY

def B(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY):
	if(simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL" or simbolos[i][0]=="("):
		i,typeY = C(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		i,typeY = Blinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		return i,typeY
	else:
		erro("B")
		return i,typeY

def A(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY):
	if(simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL" or simbolos[i][0]=="("):
		i,typeY = B(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		i,typeY = Alinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		return i,typeY
	else:
		erro("A")
		return i,typeY

def E(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY):
	if (simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL" or simbolos[i][0]=="("):
		i,typeY = A(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		i,typeY = Elinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		return i,typeY
	else:
		print i
		erro("E")
		return i,typeY
def nextsimb(i):
	i = i+1
	return i
def checkDeclaracao(i,simbolos,listIds,listFloatId,listIntId,listCharId):
	if simbolos[i][1] not in listIds and simbolos[i][0]=="IDENTIFICADOR":
		erro("Variavel "+simbolos[i][1]+" nao foi declarada. Erro na linha "+simbolos[i][2])
	elif (simbolos[i][0]=="IDENTIFICADOR" and simbolos[i][1] in listFloatId):
		typei = "t"
		return typei
	elif(simbolos[i][0]=="IDENTIFICADOR" and simbolos[i][1] in listIntId):
		typei = "i"
		return typei
	elif(simbolos[i][0]=="IDENTIFICADOR" and simbolos[i][1] in listCharId):
		typei = "c"
		return typei
	elif(simbolos[i][0]=="LITERAL"):
		typei = "c"
		return typei
	elif simbolos[i][0]=="NUMERAL":
		typei = "i"
		return typei
