#!/bin/python3

# Usando Array de Objectos, onde temos Key e valor. Exemplo:{nome: Emilton, curso: CC}

# Array de Objectos

certificacoes = [{'nome':"ECCNTP",'preco':10.500},{'nome':"ECCNDP",'preco':10.500}] 

# Array == Lista de Alunos 
alunos = [] 
x= True
while x:
	nome_aluno = input ("Digite o Nome do Aluno:")
	idade_aluno = input ("Digite a Idade do Aluno:")
	if int(idade_aluno)< 18:
		print ("Impossivel proceder com a incricao devido a idade inferior aos 18 Anos")
		x=False
	else:
		#Imprime Certificacaoes
		for indice,certificacao in enumerate(certificacoes):
			print (indice+1,"-Nome da Certificacao:",certificacao['nome'],"Preco da certificacao:",certificacao['preco'])

		# Indicar o Numero do Curso	
		curso_aluno = input ("Digite o numero referente ao Curso:")
		if  int(curso_aluno)>0 and int(curso_aluno)<4:
			mensalidade_aluno = input ("Digite 1 para pagar a primeira mensalidade e 0 para Terminar")
			if  int(mensalidade_aluno)==0:
				print ("Ate a Proxima")
				x=False
			elif int(mensalidade_aluno)==1:
				alunos.append({'nome':nome_aluno,'idade':idade_aluno,'curso':certificacoes[int(curso_aluno)-1]['nome']})
				print ("====Bem vindo a Empire CyberSecurity====")
				
				matricular=int(input ("Deseja matricular mais um Aluno? \n  Digite 1 par continuar e 0 para Terminar"))
				if matricular==0:
					for indice,aluno in enumerate(alunos):
						print (indice+1,"-Nome do Aluno:",aluno['nome'],"Idade:",aluno['idade'],"Certificacao:",aluno['curso'])
					x=False
			
		else:
			print ("Retifique o Curso")
			x=False
			# rtf 06
		
	




