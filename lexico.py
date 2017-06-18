import re
# FALTA TABELA DE SIMBOLOS, PERGUNTAR A ALGUEM AMANHA
#Listas de Tokens
reservadas = ["char","int","float","if","else","for","while","return","continue","break","print","read"]
identificador = []
separador = [" ",";","\n",".","\t","#","[","]","(",")","{","}"]
operador = ["=","!","<",">","+","-","&","|","/","*","^"]
escrita = []
escritaTabela = []
#completa comentario tipo //
def catchComentarios(linha,coluna,codigo,i):
	lit = " "
	i = i+2
	while codigo[i]!="\n":
		lit = lit.replace(" ",codigo[i]+" ")
		i=i+1
	i = i+1
	#escrita.append("[comentario,"+lit+","+str(linha)+","+str(coluna)+"]\n")
	return i,0,linha+1

def catchComentarios2(linha,coluna,codigo,i):
	lit = "@"
	lin = linha
	col = coluna
	coluna = coluna+2
	i = i+2
	while codigo[i]!="*"and codigo[i+1]!="\\":
		if codigo[i] == "\n":
			lit = lit.replace("@",codigo[i]+"@")
			i = i+1
			linha = linha +1
			coluna = 0
		else:
			lit = lit.replace("@",codigo[i]+"@")
			coluna = coluna +1
			i=i+1
	lit = lit.replace("@","")
	i = i+2
	coluna = coluna+2
	#escrita.append("[comentario,"+lit+","+str(lin)+","+str(col)+"]\n")
	return i,coluna,linha

#completa literal tipo ""
def catchLiterais(linha,coluna,codigo,i):
	lit = "@"
	i = i+1
	lin = linha
	col = coluna
	while i < len(codigo) and codigo[i] != "\"":
		if codigo[i] == "\\":
			if codigo[i+1] == "\"":
				lit = lit.replace("@",codigo[i]+"@")
				lit = lit.replace("@",codigo[i+1]+"@")
				i = i+1
			i = i+1
		elif codigo[i] =="\n":
			lit = lit.replace("@",codigo[i]+"@")
			linha = linha +1
			coluna = 0
			i = i+1
		else:
			lit = lit.replace("@",codigo[i]+"@")
			i = i+1
			coluna = coluna + 1
	lit = lit.replace("@","")
	i = i+1
	coluna = coluna + 2
	escrita.append("[LITERAL,"+lit+","+str(lin)+","+str(col)+"]\n")
	return i,coluna,linha

#completa literais tipo ''
def catchLiterais2(linha,coluna,codigo,i):
	lit = "@"
	i = i+1
	lin = linha
	col = coluna
	if codigo[i] == "\\":
		lit = lit.replace("@",codigo[i]+"@")
		lit = lit.replace("@",codigo[i+1])
		i = i+3
		coluna = coluna + 4
		escrita.append("LITERAL,"+lit+","+str(lin)+","+str(col)+"]\n")
		return i,coluna,linha
	else:
		lit = lit.replace("@",codigo[i])
		i = i+2
		escrita.append("[LITERAL,"+lit+","+str(lin)+","+str(col)+"]\n")
		coluna = coluna + 3
		return i,coluna,linha


#define se e um separador e printa
def conferirSeparadores(linha,coluna,sep):
	for i in range(0,len(separador)):
		if separador[i]==sep[0]:
			escrita.append("["+separador[i]+", ,"+str(lin)+","+str(col)+"]\n")
			return True
	return False

#define se e um operador e retorna um indice
def conferirOperadores(linha,coluna,codigo,i):
	j = 0
	for j in range(0,len(operador)):
		if operador[j]==codigo[i]:
			if (j < 6)and(codigo[i+1]==operador[0]):
				ramo = "["+operador[j]+", ,"+str(lin)+","+str(col)+"]\n"
				return i+2,ramo
			if (j>3)and(j<8)and(codigo[i]==codigo[i+1]):
				ramo = "["+operador[j] + operador[j]+", ,"+str(lin)+","+str(col)+"]\n"
				return i+2,ramo
			else:
				ramo = "["+operador[j]+", ,"+str(lin)+","+str(col)+"]\n"
				return i+1,ramo
	return 0

#define se eh palavra reservada e a printa
def conferirReservada(linha,coluna,palavra):
	j = 0
	for i in range(0,len(reservadas)):
		if (len(palavra)-1 == len(reservadas[i])):
			while  j != len(reservadas[i]):
				if re.match(reservadas[i][j],palavra[j]):
					j=j+1
				else:
					break
				if (j+1 == len(palavra)):
					escrita.append("[PALAVRA RESERVADA,"+reservadas[i]+","+str(linha)+","+str(coluna)+"]\n")
					return True
			j = 0

	return False

#retira a string a ser analisada
def retiraPalavra(codigo,i,j):
	palavra = " "
	k = 0
	while i != j:
		palavra = palavra.replace(" ",codigo[i]+" ")
		i=i+1
		k=k+1
	palavra.split()
	return palavra

#retira numero se existir. Se nao, retornar a string ERRO
def retiraNumber(codigo,i,j):
	separador = False
	number = retiraPalavra(codigo,i,j)
	k = 0
	while k != len(number):
		if re.match(r"\d",number[k]):
			k = k+1
		elif re.match(r"[x\.]",number[k]):
			if separador == False:
				k = k+1
				separador = True
			else:
				return "ERRO"
		elif re.match(r"[ ;)\n]",number[k]):
			return number
		else:
			return "ERRO"

#define se e identificador ou palavra reservada
def idOuReservada(linha,coluna,codigo,i):
	j = 0
	k = i
	while re.match(r"\w",codigo[i]):
		i=i+1
	palavra = retiraPalavra(codigo,k,i)
	if conferirReservada(linha,coluna,palavra):
		return i
	else:
		escrita.append("[IDENTIFICADOR,"+palavra+","+str(linha)+","+str(coluna)+"]\n")
		if (identificador.count(palavra)==0):
			identificador.append(palavra)
		return i

#define numero
def separaNumero(linha,coluna,codigo,i):
	j = 0
	k = i
	while re.match(r"[\w\.]",codigo[i]):
		i=i+1
	number = retiraNumber(codigo,k,i)
	if number == "ERRO":
		print "ERRO - Numeral ou identificador escrito errado\nLinha: "+str(linha)+"\nColuna:"+str(coluna)+"\n"
		return i
	else:
		escrita.append("[NUMERAL,"+number+","+str(linha)+","+str(coluna)+"]\n")
		return i

"""Funcao principal"""
#Leitura do codigo
print("Digite o nome do arquivo de entrada do compilador")
arquivoEntrada = raw_input()
arq = open(arquivoEntrada, 'r')
codigo = arq.read()
arq.close()
arq = open("TabelaSimbolos.txt",'w')
arq2 = open("Tokens.txt",'w')

#Flags
i = 0
j = 0
k = 0
lin = 0
col = 0



#Percorrendo o codigo
while i != len(codigo):
	#Verifica se e \n
	if codigo[i]=='\n':
		lin = lin +1
		col = 0
		i = i+1
	elif codigo[i]==',':
		col = col + 1
		i = i + 1
		escrita.append("[comma, ,"+str(lin)+","+str(col)+"]\n")
	#Definir se e id ou Palavra reservada
	elif re.match(r"[a-zA-Z_]",codigo[i]):
		j = i
		i = idOuReservada(lin,col,codigo,i)
		col = col + i - j
	#Define se e numeral
	elif re.match(r"\d",codigo[i]):
		j = i
		i = separaNumero(lin,col,codigo,i)
		col = col + i - j
	elif re.match(r"\/",codigo[i]) and re.match(r"\/",codigo[i+1]):
		i,col,lin = catchComentarios(lin,col,codigo,i)
	elif re.match(r"\/",codigo[i]) and re.match(r"\*",codigo[i+1]):
		i,col,lin = catchComentarios2(lin,col,codigo,i)
	elif conferirOperadores(lin,col,codigo,i) != 0:
		i,ramo = conferirOperadores(lin,col,codigo,i)
		escrita.append(ramo)
		col = col +i -j
	elif re.match(r"\"",codigo[i]):
		i,col,lin = catchLiterais(lin,col,codigo,i)
	elif re.match(r"\'",codigo[i]):
		i,col,lin = catchLiterais2(lin,col,codigo,i)
	elif conferirSeparadores(lin,col,codigo[i]):
		i=i+1
		col = col + 1
	else:
		print "Erro - Simbolo desconhecido\nlinha: "+str(lin)+"\nColuna: "+str(col)+"\n"
		i = i+1
		col = col + 1
	j = i
	k = 0
arq2.writelines(escrita)
arq2.close()
#Criacao tabela de simbolos
arq = open("TabelaSimbolos.txt",'w')
arq2 = open("Tokens.txt",'r')
tokens = arq2.readlines()
numLinhas = len(tokens)
i = 0
arq2.close()
quantidadeChaves = 1
while i < numLinhas:
	if re.match(r"I",tokens[i][1]) or re.match(r"P",tokens[i][1]) or re.match(r"N",tokens[i][1])or re.match(r"L",tokens[i][1]):
		escritaTabela.append("Chave: "+ str(quantidadeChaves) + " - "+tokens[i])
		quantidadeChaves = quantidadeChaves + 1
	i=i+1

arq.writelines(escritaTabela)
arq.close()
