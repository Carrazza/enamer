#!/usr/bin/python3
import argparse
import sys
import string


parser = argparse.ArgumentParser(description="My parser")
parser.add_argument('-b',"--big",default=False,action='store_true',help="If a person has multiple surnames, it generates a email for each one of them")
parser.add_argument('-d',required=True,action='store', type=str,help="Domain to be used in the emails")
parsed_args = parser.parse_args()


lines=[] 


#Removedor de banner do harvest
#Basicamente ignora as primeiras linhas 
count=25
for linenum, line in enumerate(sys.stdin):
	line = line.rstrip()
	
	#pelo menos quando eu usei, ele meteu um \n inicial no arquivo. Levando isso em conta para arquivos que começam com \n e sem 
	if(linenum == 0):
		if(line == ""): count=26

	if 'q' == line:
		break
	
	if (linenum==count): break
#


#Removendo mais lixo + adicionando nomes numa lista
for line in sys.stdin:

	#rstrip tira \n e esses caracteres bobos 
	line = line.rstrip()
	
	if 'q' == line:
		break
	
	#Mais lixo do harvester sendo removido
	if "*" in line or "Searching" in line or line == "": continue

	lines.append(line.lower())



for name in lines:


	#The harvester tem mania de pegar nomes e especificar cargos, tipo
	#Doutor Simpático - Sr. Solutions Architect 
	#com essa linha, eu identifico se há essa definicição de cargo e removo da equação
	if("-" in name): name = name[0:name.index("-")].rstrip()
	
	listOfNames = name.split()

	firstName=listOfNames[0]

	listOfSobrenomes = listOfNames[1:]

	#Removedor de pontuação 
	rm = lambda x:x.translate(str.maketrans('', '', string.punctuation))
	printFunction = lambda x,y: print(f"{x}.{y}@{parsed_args.d}")
	secondName = ""

	for sobrenome in listOfSobrenomes:
		
		sobrenome = rm(sobrenome)

		#Roberto de oliveira -> roberto.oliveira ignorar o "de"
		if sobrenome == "de": continue

		secondName = sobrenome
	
		if(parsed_args.big ): printFunction(firstName,secondName)

		else: break
	


	if(parsed_args.big == False): printFunction(firstName,secondName)

	pass