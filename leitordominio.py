#!/bin/python3

import socket

# r de read  / w de write
# open abre um ficheiros

dominios = open("dominios.txt","r") 

# readlines() metodo que le cada linha do meu ficheiro

for dominio in dominios.readlines(): 
	l=dominio.replace('\n','') ### SO DA ERRO
	ips=socket.gethostbyname(l)
	print (ips)
	
