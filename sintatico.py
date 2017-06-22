from program import *
from anasinExpresArit import *
def leituraTokens():
	arq = open("Tokens.txt", 'r')
	arquivos = arq.read()
	tokens = arquivos.split('\n')
	return tokens

def tratToken(token):
	if (token[1]==','):
		token=token.split(',')
		token[0]="[,"
		token.remove("")
	else:
		token=token.split(',')
	return token

tokens = leituraTokens()
#separa os tokens
for i in range(len(tokens)-1):
	tokens[i]=tratToken(tokens[i])
#retira tokens com espaco
i=0
while i!=len(tokens)-1:
	tokens[i][0] = tokens[i][0].replace("[","")
	tokens[i][3] = tokens[i][3].replace("]","")
	if(tokens[i][0]==' '):
		del tokens[i]
		i=i-1
	if i!=len(tokens)-1:
		i=i+1
#for i in range(len(tokens)-1):
	#print tokens[i]
#	print len(tokens[i])
tokens.remove("")
i=0
#COMEcA AQUI A leituraTokens
initPrograma(i,tokens)
#i = E(i,tokens)
