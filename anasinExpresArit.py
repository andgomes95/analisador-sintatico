import re
name = "a+(a-a)-(a/a)$"
def erro():
	print "EROU"
def Tlinha(i,simbolos):
	if(simbolos[i]=="*" or simbolos[i]=="/"):
		i = nextsimb(i)
		i = F(i,simbolos)
		i = Tlinha(i,simbolos)
		return i
	elif(simbolos[i]=="+" or simbolos[i]=="-" or simbolos[i]==")"or simbolos[i]=="$"):
		return i
	else:
		print i
		erro()
		return i

def Elinha(i,simbolos):
	if(simbolos[i]=="+" or simbolos[i]=="-"):
		i = nextsimb(i)
		i = T(i,simbolos)
		i = Elinha(i,simbolos)
		return i
	elif(simbolos[i]==")"or simbolos[i]=="$"):
		return i
	else:
		erro()
		return i

def F(i,simbolos):
	if (simbolos[i]=="("):
		i = nextsimb(i)
		i = E(i,simbolos)
		i = nextsimb(i)
		return i
		if(simbolos[i]!=")"):
			erro()
			return i
	elif(simbolos[i]=="a"):
		#re.match(simbolos[i][0],"IDENTIFICADOR") or re.match(simbolos[i][0],"LITERAL") or re.match(simbolos[i][0],"NUMERAL")
		i = nextsimb(i)
		return i
	else:
		erro()
		return i

def T(i,simbolos):
	if( simbolos[i]=="a" or simbolos[i]=="("):
		#simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL"
		i = F(i,simbolos)
		i = Tlinha(i,simbolos)
		return i
	else:
		erro()
		return i

def E(i,simbolos):
	if (simbolos[i]=="a" or simbolos[i][0]=="("):
		#simbolos[i][0]=="IDENTIFICADOR" or simbolos[i][0]=="LITERAL" or simbolos[i][0]=="NUMERAL"
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


E(0,name)
