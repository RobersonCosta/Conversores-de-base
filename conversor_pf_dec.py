#!/usr/bin/env python
# -*- coding: utf-8 -*-

def exp (valor):
	contador_negativo = 0;
	contador_positivo = 0;
	while (abs(valor)<1 or abs(valor)>=2):
		if (abs(valor) == 0):
			break;
		if (abs(valor)>0 and abs(valor)<1):
			valor = abs(valor)*2;
			contador_negativo+=1;
		else:
			valor = abs(valor)/2;
			contador_positivo+=1;
	if (contador_negativo!=0):
		return -contador_negativo;
	return contador_positivo;

def mantissa (valor):
	while (abs(valor)<1 or abs(valor)>=2):
		if (abs(valor)>0 and abs(valor)<1):
			valor = abs(valor)*2;
		else:
			valor = abs(valor)/2;
	if (valor == 0):
		return "000000000";
	else:
		valor = valor-1;
	mantissa_binario = "";
	while (float(valor)!=0):
		valor = valor*2;
		if (valor<1):			
			mantissa_binario = mantissa_binario + "0";
		else:
			valor = valor-1;
			mantissa_binario = mantissa_binario + "1";
	contador=1;
	mantissa = "";
	while (contador!=10):
		if (contador>len(mantissa_binario)):
			mantissa = mantissa + "0" ;
		else:			
			mantissa = mantissa + mantissa_binario[contador-1];			
		contador+=1;
	return mantissa;

def decimal_pf(decimal):
	expoente = exp(float(decimal));
	if (expoente==0):
		valor_pf = "000000000000000";
	else:
		expoente+=(2**5)-1;	
		expoente = convert_to_base(str(expoente), 2);	
		if (len(expoente)<6):
			while (len(expoente)<6):
				expoente = "0" + expoente;
		if (len(expoente)>6):
			valor_pf = "Expoente maximo +/-32";
		else:
			mantissa_binario = mantissa(float(decimal));
			valor_pf = expoente + mantissa_binario;
			if (float(decimal)<0):	
				valor_pf = "1" + valor_pf;
			else:
				valor_pf = "0" + valor_pf;
	return valor_pf;

def pf_decimal (pf):
	expoente = int(convert_to_decimal(pf[1:7], 2));
	expoente-=31;	
	mantissa = 0;
	contador = -1;
	for i in range(7,16):
		mantissa += float(pf[i])*2**contador;		
		contador-=1;
	if (pf[0] == "1"):
		valor_decimal = -((mantissa+1)*2**expoente);
	else:
		valor_decimal = ((mantissa+1)*2**expoente);
	return valor_decimal;


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



def main():
	print("Selecione as opcoes:\n  1 - PF para Decimal\n  2 - Decimal para PF\n");
	tipo = raw_input();
	valor_entrada = raw_input("Digite um valor para ser convertido:\n");
	saida = "Opcao invalida!";
	if (tipo == '1'):
		valor_decimal = pf_decimal(valor_entrada);
		saida = str(valor_decimal);
	elif (tipo == '2'):		
		valor_pf = decimal_pf(valor_entrada);
		saida = valor_pf;
	print("\nSAIDA: "+saida);

main();