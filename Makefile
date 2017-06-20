all:	code	clean	
clean:
	rm -f *.pyc
	rm -f Tokens.txt
	rm -f TabelaSimbolos.txt	
code:
	python	lexico.py	&&	python	sintatico.py

