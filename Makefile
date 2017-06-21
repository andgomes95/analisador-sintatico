all:	code	clean
clean:
	rm -f *.pyc
	rm -f Tokens.txt
	rm -f TabelaSimbolos.txt
code: lexico sintatico
lexico:
	python lexico.py
sintatico:
	python sintatico.py
