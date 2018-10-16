#!/usr/bin/env python
# -*- coding: utf-8 -*-

def convert_to_base (decimal, n):
	dicionario = "0123456789ABCDEFGHIJKLMNOPQRSTUXYZ";
	decimal = decimal.upper();
	if(decimal == 0):
		return 0;
	else:
		convertido = "";
		while (decimal>0):
			resto = int(decimal)%n;
			decimal = int(decimal)/n;
			convertido = str(dicionario[resto]) + convertido;
		return convertido;	

def convert_to_decimal (valor, n):
	dicionario = "0123456789ABCDEFGHIJKLMNOPQRSTUXYZ";
	valor = valor.upper();
	if(valor == 0):
		return 0;
	else:
		convertido = 0;
		valor_invertido = '';
		for var in valor:
			valor_invertido = var + valor_invertido;
		for i in range(len(valor_invertido)):
			for j in range(len(dicionario)):
				if dicionario[j] == valor_invertido[i]:
					convertido+= int(j)*int((n**i));
		return str(convertido);  	








print("Escolha um dos tipos de entrada:\n  1 - Binario\n  2 - Hexadecimal\n  3 - Decimal\n  4 - Inserir base diferente (limite 33)");
tipo = raw_input();
valor_entrada = raw_input("Digite um valor para ser convertido:\n");
saida = "Opcao invalida!";
if (tipo == '1'):
	print("Escolha uma das opcoes de conversao:\n  1 - Hexadecimal\n  2 - Decimal\n  3 - Inserir base diferente (limite 33)");
	entrada = raw_input();
	if (entrada=='1'):
		saida = convert_to_decimal(valor_entrada, 2);
		saida = decimal_to_base(saida, 16);
	elif entrada=='2':
		saida = binario_to_decimal(valor_entrada, 2);
	elif entrada == '3':
		print("Insira a base desejada (LIMITE 33):");
		base = raw_input();		
		if (int(base)>2 and int(base)<=33):
			saida = convert_to_base(valor_entrada, int(base));
		else:
			saida = "Opcao invalida!";
	print("\nSAIDA: "+saida);
elif (tipo == '2'):		
	print("Escolha uma das opcoes de conversao:\n  1 - Binario\n  2 - Decimal\n  3 - Inserir base diferente (limite 33)");
	entrada = raw_input();
	if (entrada=='1'):
		saida = convert_to_decimal(valor_entrada, 16);
		saida = convert_to_base(saida, 2);
	elif entrada=='2':
		saida = convert_to_decimal(valor_entrada, 16);
	elif entrada == '3':
		print("Insira a base desejada (LIMITE 33):");
		base = raw_input();		
		if (int(base)>2 and int(base)<=33):
			saida = convert_to_base(valor_entrada, int(base));
		else:
			saida = "Opcao invalida!";
	print("\nSAIDA: "+saida);
elif (tipo == '3'):	
	print("Escolha uma das opcoes de conversao:\n  1 - Binario\n  2 - Hexadecimal\n  3 - Inserir base diferente (limite 33)");
	entrada = raw_input();
	if (entrada=='1'):
		saida = convert_to_base(valor_entrada, 2);
	elif entrada=='2':
		saida = convert_to_base(valor_entrada, 16);
	elif entrada == '3':
		print("Insira a base desejada (MAIOR QUE 2 E LIMITE 33):");
		base = raw_input();		
		if (int(base)>2 and int(base)<=33):
			saida = convert_to_base(valor_entrada, int(base));
		else:
			saida = "Opcao invalida!";
	print("\nSAIDA: "+saida);
elif (tipo == '4'):
	print("Insira a base desejada (LIMITE 33):");
	base = raw_input();			
	if (int(base)>2 and int(base)<=33):
		saida = convert_to_decimal(valor_entrada, int(base));	
		print("Escolha uma das opcoes de conversao:\n  1 - Binario\n  2 - Hexadecimal\n  3 - Decimal\n  4 - Inserir base diferente (limite 33)");
		entrada = raw_input();
		if (entrada=='1'):
			saida = convert_to_base(saida, 2);
		elif entrada=='2':
			saida = convert_to_base(saida, 16);
		elif entrada=='3':
			saida = convert_to_decimal(saida, 10);
		elif entrada=='4':
			print("Insira a base desejada (MAIOR QUE 2 E LIMITE 33):");
			base = raw_input();		
			if (int(base)>2 and int(base)<=33):
				saida = convert_to_base(saida, int(base));
			else:
				saida = "Opcao invalida!";
	else: 
		saida = "Opcao invalida!";
	print("\nSAIDA: "+saida);	