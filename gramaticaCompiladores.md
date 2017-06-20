#GRAMATICA

Programa:	 		atribui programa |
						 		€

atribui:			<id><=>expressão<;>

declaracao:		tipo <id> dec2 <semicolon>

tipo:					<int>|
							<float>|
							<char>

dec2:					<comma><id>dec2 |
							€

while:			<while><(>expressão<)><{>programa<}> (tratar abre e fechar chave em programa)

