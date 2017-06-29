from anasinExpresArit import *
import re
import sys
aux = 0
aux2 = 0
aux3 = 0
aceitaveis = ["+","-","*","/","IDENTIFICADOR","NUMERAL","LITERAL","||","&&","==","!=","<",">",]
listInt = []
listFloat = []
listChar = []
listIds = []
listFloatId = []
listCharId = []
listIntId = []
def initPrograma(i,simbolos):
	global aux2
	if (simbolos[i][1]=="int" and simbolos[i+1][1]=="main " and simbolos[i+2][0]=="("and simbolos[i+3][0]==")"and simbolos[i+4][0]=="{"):

		if i+1 < len(simbolos):
			i=nextsimb(i)
			i=nextsimb(i)
			i=nextsimb(i)
			i=nextsimb(i)
			i=nextsimb(i)
			i = programa(i,simbolos)
			if  simbolos[i][0]=="}":
				i = nextsimb(i)
				return i
			else:
				erro(str(simbolos[i]))
				return i
	elif simbolos[i][0]=="{":
		i=nextsimb(i)
		i = programa(i,simbolos)
		if  simbolos[i][0]=="}":
			aux2 = aux2 -1
			print "label"+str(aux2)+":"
			i = nextsimb(i)
			return i
		else:
			erro(str(simbolos[i]))
			return i
	else:
		erro(str(simbolos[i]))
		return i
def programa2(i,simbolos):
	if simbolos[i][0]==";" and i+1 < len(simbolos):
		i=nextsimb(i)
		i = programa(i,simbolos)
	elif simbolos[i-1][0]=="}"and i+1 < len(simbolos):
		#i=nextsimb(i)
		i = programa(i,simbolos)
	elif simbolos[i][0]=="}"and i+1 == len(simbolos):
		return i
	else:
		erro(str(simbolos[i]))
	return i
def programa(i,simbolos):
	global aux
	global aux2
	global aux3
	if(simbolos[i][0]=="IDENTIFICADOR"):
		i = atribui(i,simbolos)
		i = programa2(i,simbolos)
		return i
	elif(simbolos[i][1]=="int" or simbolos[i][1]=="float" or simbolos[i][1]=="char"):
		i = declara(i,simbolos)
		i = programa2(i,simbolos)
		return i
	elif simbolos[i][1] == "while":
		#i = repeti(i,simbolos)

		i = nextsimb(i)
		typeY = ""
		print "label"+str(aux2)+":"
		i,typeY = E(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		aux = 0
		print "BNE 0,$t0,saida"+str(aux3)
		aux2 =aux2+1
		aux3 =aux3+1
		if(simbolos[i][0]=="{"):
			i = initPrograma(i,simbolos)
		else:
			erro("repeticao" + str(simbolos[i]))

		print "j label"+str(aux2)
		aux3 = aux3-1
		print "saida"+str(aux3)+":"
		i = programa2(i,simbolos)
		return i
	elif simbolos[i][1] == "if":
		i = nextsimb(i)
		typeY = ""
		i,typeY = E(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		print "BEQ 0,$t0,label"+str(aux2)
		aux2 =aux2+1
		aux = 0
		if(simbolos[i][0]=="{"):

			i = initPrograma(i,simbolos)
		else:
			erro("condicao" + str(simbolos[i]))
		i = programa2(i,simbolos)
		return i
	else:
		if simbolos[i][0] == "}":
			return i
		erro(+str(simbolos[i])+" - "+str(i))
		return i
def nextsimb(i):
	i = i+1
	return i
def declara(i,simbolos):
	tipo = simbolos[i][1]
	i = nextsimb(i)
	if(simbolos[i][0]=="IDENTIFICADOR"):
		addTabelaVarTipo(i,simbolos,tipo)
		if simbolos[i+1][0]=="=":
			i = atribui(i,simbolos)
		else:
			i = nextsimb(i)
		i = declara2(i,simbolos,tipo)
		if(simbolos[i][0]==";"):
			return i
		else:
			erro(str(simbolos[i]))
			return i
	else:
		erro(str(simbolos[i]))
		return i
def declara2(i,simbolos,tipo):
	if (simbolos[i][0]=="comma"):
		i= nextsimb(i)
		if(simbolos[i][0]=="IDENTIFICADOR"):
			addTabelaVarTipo(i,simbolos,tipo)
			if simbolos[i+1][0]=="=":
				i = atribui(i,simbolos)
			else:
				i = nextsimb(i)
		else:
			erro(str(simbolos[i]))
		i = declara2(i,simbolos,tipo)
		return i
	else:
		return i
def atribui(i,simbolos):
	global aux
	simb = ""
	if(simbolos[i][0]=="IDENTIFICADOR"):
		simb = simbolos[i][1]
		if simbolos[i][1] not in listIds and simbolos[i][0] == "IDENTIFICADOR":
			erro("Variavel "+simbolos[i][1]+" nao foi declarada. Erro na linha "+simbolos[i][2])
		i = nextsimb(i)
		if(simbolos[i][0]=="="):
			i = nextsimb(i)
			typeY = ""
			i,typeY = E(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
			print "STORE $t0,"+str(simb)
			aux = 0
			return i
		else:
			erro(str(simbolos[i]))
			return i
	else:
		erro(str(simbolos[i]))
		return i
def addTabelaVarTipo(i,simbolos,tipo):
	if tipo=="int":
		if simbolos[i][1] not in listIds:
			listInt.append("["+tipo+","+simbolos[i][1]+","+simbolos[i][2]+"]")
			listIntId.append(simbolos[i][1])
			listIds.append(simbolos[i][1])
		else:
			print "O identificador "+simbolos[i][1]+" ja foi declarado. Declaracao dupla na linha "+simbolos[i][2]
			erro("Dupla declaracao "+str(i))
	elif tipo=="float":
		if simbolos[i][1] not in listIds:
			listFloat.append("["+tipo+","+simbolos[i][1]+","+simbolos[i][2]+"]")
			listFloatId.append(simbolos[i][1])
			listIds.append(simbolos[i][1])
		else:
			print "O identificador "+simbolos[i][1]+" ja foi declarado. Declaracao dupla na linha "+simbolos[i][2]
			erro("Dupla declaracao "+str(i))
	elif tipo=="char":
		if simbolos[i][1] not in listIds:
			listChar.append("["+tipo+","+simbolos[i][1]+","+simbolos[i][2]+"]")
			listCharId.append(simbolos[i][1])
			listIds.append(simbolos[i][1])
		else:
			print "O identificador "+simbolos[i][1]+" ja foi declarado. Declaracao dupla na linha "+simbolos[i][2]
			erro("Dupla declaracao")


def erro(string):
	print string
	sys.exit
def Tlinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY):
	if(simbolos[i][0]=="*"):
		i = nextsimb(i)
		i,typeY = F(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		i,typeY = Tlinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		gerarSimbolos("MUL",simbolos,i)
		return i,typeY
	elif (simbolos[i][0]=="/"):
		i = nextsimb(i)
		i,typeY = F(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		i,typeY = Tlinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		gerarSimbolos("DIV",simbolos,i)
		return i,typeY
	elif(simbolos[i][0]=="<" or simbolos[i][0]==">" or simbolos[i][0]=="<=" or simbolos[i][0]==">=" or simbolos[i][0]=="+" or simbolos[i][0]=="-"or simbolos[i][0]=="||" or simbolos[i][0]=="&&" or simbolos[i][0]=="==" or simbolos[i][0]=="!=" or simbolos[i][0]==")"or simbolos[i][0] not in aceitaveis):
		return i,typeY
	else:
		print i
		erro("Tlinha")
		return i,typeY

def Dlinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY):
	global aux
	if(simbolos[i][0]=="+"):
		i = nextsimb(i)
		i,typeY = T(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		i,typeY = Dlinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		gerarSimbolos("ADD",simbolos,i)
		return i,typeY
	elif(simbolos[i][0]=="-"):
		i = nextsimb(i)
		i,typeY = T(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		i,typeY = Dlinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		gerarSimbolos("SUB",simbolos,i)
		return i,typeY
	elif(simbolos[i][0]=="<" or simbolos[i][0]==">" or simbolos[i][0]=="<=" or simbolos[i][0]==">=" or simbolos[i][0]=="==" or simbolos[i][0]=="!=" or simbolos[i][0]==")" or simbolos[i][0]=="||" or simbolos[i][0]=="&&" or simbolos[i][0] not in aceitaveis):
		return i,typeY
	else:
		erro("Dlinha")
		return i,typeY


def Clinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY):
	if(simbolos[i][0]=="<"):
		i = nextsimb(i)
		i,typeY = D(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		i,typeY = Clinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		gerarSimbolos("MEN",simbolos,i)
		return i,typeY
	elif simbolos[i][0]==">":
		i = nextsimb(i)
		i,typeY = D(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		i,typeY = Clinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		gerarSimbolos("MAI",simbolos,i)
		return i,typeY
	elif simbolos[i][0]=="<=":
		i = nextsimb(i)
		i,typeY = D(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		i,typeY = Clinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		gerarSimbolos("MENI",simbolos,i)
		return i,typeY
	elif simbolos[i][0]==">=":
		i = nextsimb(i)
		i,typeY = D(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		i,typeY = Clinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		gerarSimbolos("MAII",simbolos,i)
		return i,typeY
	elif(simbolos[i][0]=="==" or simbolos[i][0]=="!=" or simbolos[i][0]==")" or simbolos[i][0]=="||" or simbolos[i][0]=="&&" or simbolos[i][0] not in aceitaveis):
		return i,typeY
	else:
		erro("Clinha")
		return i,typeY

def Blinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY):
	if(simbolos[i][0]=="=="):
		i = nextsimb(i)
		i,typeY = C(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		i,typeY = Blinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		gerarSimbolos("EQUAL",simbolos,i)
		return i,typeY
	elif simbolos[i][0]=="!=":
		i = nextsimb(i)
		i,typeY = C(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		i,typeY = Blinha(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY)
		gerarSimbolos("NEQUAL",simbolos,i)
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
		gerarSimbolos("AND",simbolos,i)
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
		gerarSimbolos("OR",simbolos,i)
		return i,typeY
	elif(simbolos[i][0]==")"or simbolos[i][0] not in aceitaveis):
		return i,typeY
	else:
		erro("Elinha")
		return i,typeY

def F(i,simbolos,listIds,listFloatId,listIntId,listCharId,typeY):
	global aux
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
			gerarSimbolos("LOAD",simbolos,i)
		elif typeY == typei:
			gerarSimbolos("LOAD",simbolos,i)
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

def gerarSimbolos(instrucao,simbolos,i):
	global aux
	if(instrucao=="LOAD"):
		print "LOAD $t"+str(aux)+","+simbolos[i][1]
		aux = aux +1
	else:
		print instrucao+" $t"+str(aux-2)+",$t"+str(aux-2)+",$t"+str(aux-1)
		aux = aux -1
