import time
import random
import string
import math

senha1= 'da'.lower()
autenticacao1 = 1

def leiaSenha(msg):
	ok = False
	while True:
		senha = str(input(msg))
		if senha == senha1 :
			ok = True
		else:
			print('\033[0;31mERRO! Digite a senha válida\033[m')
		if ok:
			break
	return senha

def leiaAutenticacao(msg):
	ok = False
	while True:
		autenticacao = int(input(msg))
		if autenticacao == autenticacao1 :
			ok = True
		else:
			print('\033[0;31mERRO! Digite a autenticação válida\033[m')
		if ok:
			break
	return autenticacao

def leiaOpcao(msg):
	ok = False
	while True:
		opcao = int(input(msg))
		if opcao == 1 or opcao == 2 :
			ok = True
		else:
			print('\033[0;31mERRO! Digite uma opção válida\033[m')
		if ok:
			break
	return opcao

def leiaCriptografia(msg):
	ok = False
	while True:
		criptografar = str(input(msg))
		if criptografar == 'sim' or  criptografar == 'nao' or criptografar == 'não':
			ok = True
		else:
			print('\033[0;31mERRO! Digite uma opção válida\033[m')
		if ok:
			break
	return criptografar

def leiaNcarteira(msg):
	ok = False
	while True:
		ncarteira = int(input(msg))
		if ncarteira == 1 or ncarteira == 2 or ncarteira == 3 or ncarteira == 4 or ncarteira == 5 or ncarteira == 6 :
			ok = True
		else:
			print('\033[0;31mERRO! Digite uma opção válida\033[m')
		if ok:
			break
	return ncarteira

print('')
print('Access Matheus')
print('')
senha = leiaSenha('Digite sua senha: ')
print('')
print('Etapa de verificação credencial de segurança concluida com sucesso.')
print('Por favor verifique a credencial de autentificação de triplo fator.')
print('')
autenticacao = leiaAutenticacao('Digite sua autenticação: ')
print('')
print('Etapa de verificação credencial de autenticação concluida com sucesso.')
print('')
print('Bem vindo Matheus')
print('')

saldo1 = float(276.51265865185)  # paxg
saldo2 = float(293.79469940991)  # paxg
saldo3 = float(311.67412551236)  # paxg
saldo4 = float(328.35878201318)  # paxg
saldo5 = float(508_228.49662)  # USDT
saldo6 = float(446_625.37828)  # USDT

while True:
	print('')
	print('')
	opcao = leiaOpcao('Digite o número da opção que deseja: ')


	if opcao == 1:
			print(' ')
			print('''Adaptador Ethernet Ethernet:

		   Sufixo DNS específico de conexão. . . . . . :
		   Endereço IPv6 . . . . . . . . . . : 2804:7f4:c780:3628:ada2:7b8:6f2:8c25
		   Endereço IPv6 Temporário. . . . . . . . : 2804:7f4:c780:3628:754a:1e0a:1120:728f
		   Endereço IPv6 de link local . . . . . . . . : fe80::ada2:7b8:6f2:8c25%17
		   Endereço IPv4. . . . . . . .  . . . . . . . : 192.168.15.77
		   Máscara de Sub-rede . . . . . . . . . . . . : 255.255.255.0
		   Gateway Padrão. . . . . . . . . . . . . . . : fe80::dac6:78ff:fecf:7320%17
		                                                 192.168.15.1

		Adaptador de Rede sem Fio Wi-Fi:

		   Estado da mídia. . . . . . . . . . . . . .  : mídia desconectada
		   Sufixo DNS específico de conexão. . . . . . :

		Adaptador de Rede sem Fio Conexão Local* 9:

		   Estado da mídia. . . . . . . . . . . . . .  : mídia desconectada
		   Sufixo DNS específico de conexão. . . . . . :

		Adaptador de Rede sem Fio Conexão Local* 10:

		   Estado da mídia. . . . . . . . . . . . . .  : mídia desconectada
		   Sufixo DNS específico de conexão. . . . . . :''')
			print(' ')
			print(' ')
			print(' ')
			print('A rede não possui segurança a nível de criptografia de ponta a ponta, ')
			print(' ')

			criptografar = leiaCriptografia(
				'Deseja criptografar a conexão do programa, assim criando um a canal seguro? ')

			if criptografar == 'sim'.upper().lower():
				print('')
				print(' ')
				print('''JDxK4ZlvptmPYmK3LmYd3QoSFXpHI4FBYOQJ2GBG7LrBz4lOODYq291W7lSnraA-dXOO
					u1JjP8Lsusb5jP6NyYkUFDlCBCs4Rixcx2IKhOB88opiTEBQHyTfNf2XDjDORLlaFjOlLaxr2nxnQ
					juydnq0zRsmF0m83JqQbNkcUmPTwzuVxVQ5MXnHoyjtRlxk0eR3OmKwtmG_Re5q9BYPpZQ7mepTZp
					DJ6fkJMfqYdtS_n_RH43E3Bw_LM3K90qOR''')
				print(' ')
				print(' ')


			if criptografar == 'não'.upper().lower():
				print('')
				print("Não foi possível fazer o login")
			# voltar para o menu

			if criptografar == 'nao'.upper().lower():
				print('')
				print("Não foi possível fazer o login")


	if opcao == 2:
			print('''	Carteiras dísponíveis:
			Carteira R1
			Carteira R2
			Carteira R3
			Carteira R4
			Carteira I1
			Carteira FTX''')
			print(' ')
			opcao1 = leiaCriptografia('Deseja inspecionar o circuito interno? ')
			if opcao1 == 'não'.upper().lower() or opcao1 == 'nao'.upper().lower():
				print('')
			if opcao1 == 'sim'.upper().lower():

				print('')
				ncarteira = leiaNcarteira('Digite o número da carteira: ')
				print('')

				total = float(15_896_777.39)
				# real1 = float(2_543_484.38)
				# real2 = float(2_702_452.1563)
				# real3 = float(2_861_419.9302)
				# real4 = float(3_020_387.7041)
				# real5 = float(2_622_968.26)
				# real6 = float(2_305_032.72)



				real1 = float(saldo1 * 9097.38)
				real2 = float(saldo2 * 9097.38)
				real3 = float(saldo3 * 9097.38)
				real4 = float(saldo4 * 9097.38)
				real5 = float(saldo5 * 5.07)
				real6 = float(saldo6 * 5.07)

				la1 = ''.join(random.SystemRandom().choices(string.ascii_letters, k=1))
				la2 = ''.join(random.SystemRandom().choices(string.ascii_letters, k=1))
				la3 = ''.join(random.SystemRandom().choices(string.ascii_letters, k=1))

				na1 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
				na2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
				na3 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
				na4 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
				na5 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
				na6 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
				na7 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
				na8 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])

				ID1 = (na1,na2,na3,la1,na4,na5,na6,na7,na8,"-",la2,la3)
				ID2 = (na1, na2, na3, la1, na4, na5, na6, na7, na8, "-", la2, la3)
				ID3 = (na1, na2, na3, la1, na4, na5, na6, na7, na8, "-", la2, la3)
				ID4 = (na1, na2, na3, la1, na4, na5, na6, na7, na8, "-", la2, la3)
				ID5 = (na1, na2, na3, la1, na4, na5, na6, na7, na8, "-", la2, la3)
				ID6 = (na1, na2, na3, la1, na4, na5, na6, na7, na8, "-", la2, la3)

				ta1 = 100 * random.random()
				ta1 = math.ceil(ta1)
				while ta1 < 7 and ta1 > 47:
					ta1 = 100 * random.random()
					ta1 = math.ceil(ta1)

				ta2 = 100 * random.random()
				ta2 = math.ceil(ta2)
				while ta2 < 7 and ta2 > 53:
					ta2 = 100 * random.random()
					ta2 = math.ceil(ta2)

				ta3 = 160-(ta1+ta2)

				al1 = round((100 * real1) / total,3)
				al2 = round((100 * real2) / total,3)
				al3 = round((100 * real3) / total,3)
				al4 = round((100 * real4) / total,3)
				al5 = round((100 * real5) / total,3)
				al6 = round((100 * real6) / total,3)


				if ncarteira == 1:
					print(
						'Criptomoeda: Paxos Gold (PAXG), Quantidade: {}, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%'.format(
							saldo1, al1))
					print('')
					transfer = str(input('Deseja movimentar o circuito interno? '))
					print('')
					if transfer == 'não'.upper().lower() or transfer =='nao'.upper().lower():
						print('')
					if transfer == 'sim'.upper().lower():
						print('')
						valor = float(input('Qualifique a tranferencia: '))
						print('')
						destino = leiaNcarteira('Qual a carteira de destino? (digite o número da carteira): ')
						taxa = random.choice(
							[0.001562, 0.002604, 0.002322, 0.002298, 0.002512, 0.002233, 0.001666, 0.001732, 0.001878,
							 0.001904,
							 0.002043, 0.002179, 0.002417, 0.002471, 0.002438, 0.001763, 0.001589, 0.001622, 0.001927,
							 0.001856])
						print('')
						confirmar = leiaCriptografia(
							'''		
						O valor de taxa de é {} PAXG.
						ERC-20 Transaction: Tax pending.
						Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
						ID: {}{}{}{}{}{}{}{}{}-{}{}
						Digite sim, para confirmar:'''.format(taxa,na1,na2,na3,la1,na4,na5,na6,na7,na8,la2,la3))
						if confirmar == 'sim'.upper().lower().strip():
							saldo1 = saldo1 -valor
							if destino == 1:
								saldo1 = saldo1 + valor - taxa
								al1 = (100 * real1) / total
							if destino == 2:
								saldo2 = saldo2 + valor - taxa
								al2 = (100 * real2) / total
							if destino == 3:
								saldo3 = saldo3 + valor - taxa
								al3 = (100 * real3) / total
							if destino == 4:
								saldo4 = saldo4 + valor - taxa
								al4 = (100 * real4) / total
							if destino == 5:
								saldo5 = saldo5 + valor - taxa
								saldo5 = round(saldo5, 5)
								al5 = (100 * real5) / total
							if destino == 6:
								saldo6 = saldo6 + valor - taxa
								saldo6 = round(saldo6, 5)
								al6 = (100 * real6) / total

							for c in range(1,2):
								print('Confirmação de rede pendende (0/3):  PROTOCOLO -',''.join(random.SystemRandom().choices(string.ascii_letters, k = 7)))
								time.sleep(1.5)
							for c in range(1,2):
								print('Confirmação de rede pendende (1/3):  PROTOCOLO -',''.join(random.SystemRandom().choices(string.ascii_letters, k = 7)))
								time.sleep(1.5)
							for c in range(1,2):
								print('Confirmação de rede pendende (2/3): PROTOCOLO -',''.join(random.SystemRandom().choices(string.ascii_letters, k = 7)))
								time.sleep(1.5)
							print('Confirmação de rede pendende (3/3): PROTOCOLO -',''.join(random.SystemRandom().choices(string.ascii_letters, k = 7)))

							if destino == 1:
								print('O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(saldo1, al1,na1,na2,na3,la1,na4,na5,na6,na7,na8,la2,la3))
							if destino == 2:
								print('O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(saldo2, al2,na1,na2,na3,la1,na4,na5,na6,na7,na8,la2,la3))
							if destino == 3:
								print('O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(saldo3, al3,na1,na2,na3,la1,na4,na5,na6,na7,na8,la2,la3))
							if destino == 4:
								print('O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(saldo4, al4,na1,na2,na3,la1,na4,na5,na6,na7,na8,la2,la3))
							if destino == 5:
								print('O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(saldo5, al5,na1,na2,na3,la1,na4,na5,na6,na7,na8,la2,la3))
							if destino == 6:
								print('O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(saldo6, al6,na1,na2,na3,la1,na4,na5,na6,na7,na8,la2,la3))


					else:
						print('Processo Finalizado')

				if ncarteira == 2:
					print(
						'Criptomoeda: Paxos Gold (PAXG), Quantidade: {}, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%'.format(
							saldo2, al2))
					print('')
					transfer = str(input('Deseja movimentar o circuito interno? '))
					print('')
					if transfer == 'não'.upper().lower() or transfer == 'nao'.upper().lower():
						print('')
					if transfer == 'sim'.upper().lower():
						print('')
						valor = float(input('Qualifique a tranferencia: '))
						print('')
						destino = leiaNcarteira('Qual a carteira de destino? (digite o número da carteira): ')
						taxa = random.choice(
							[0.001562, 0.002604, 0.002322, 0.002298, 0.002512, 0.002233, 0.001666, 0.001732, 0.001878,
							 0.001904,
							 0.002043, 0.002179, 0.002417, 0.002471, 0.002438, 0.001763, 0.001589, 0.001622, 0.001927,
							 0.001856])
						print('')
						confirmar = leiaCriptografia(
							'''		
                        O valor de taxa de é {} PAXG.
                        ERC-20 Transaction: Tax pending.
                        Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                        ID: {}{}{}{}{}{}{}{}{}-{}{}
                        Digite sim, para confirmar:'''.format(taxa, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2,
															  la3))
						if confirmar == 'sim'.upper().lower().strip():
							saldo2 = saldo2 - valor
							if destino == 1:
								saldo1 = saldo1 + valor - taxa
								al1 = (100 * real1) / total
							if destino == 2:
								saldo2 = saldo2 + valor - taxa
								al2 = (100 * real2) / total
							if destino == 3:
								saldo3 = saldo3 + valor - taxa
								al3 = (100 * real3) / total
							if destino == 4:
								saldo4 = saldo4 + valor - taxa
								al4 = (100 * real4) / total
							if destino == 5:
								saldo5 = saldo5 + valor - taxa
								saldo5 = round(saldo5, 5)
								al5 = (100 * real5) / total
							if destino == 6:
								saldo6 = saldo6 + valor - taxa
								saldo6 = round(saldo6, 5)
								al6 = (100 * real6) / total

							for c in range(1, ta1):
								print('Confirmação de rede pendende (0/3):  PROTOCOLO -',
									  ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))
								time.sleep(1.5)
							for c in range(1, ta2):
								print('Confirmação de rede pendende (1/3):  PROTOCOLO -',
									  ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))
								time.sleep(1.5)
							for c in range(1, ta3):
								print('Confirmação de rede pendende (2/3): PROTOCOLO -',
									  ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))
								time.sleep(1.5)
							print('Confirmação de rede pendende (3/3): PROTOCOLO -',
								  ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))

							if destino == 1:
								print(
									'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
							if destino == 2:
								print(
									'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
							if destino == 3:
								print(
									'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
							if destino == 4:
								print(
									'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
							if destino == 5:
								print(
									'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
							if destino == 6:
								print(
									'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))

					else:
						print('Processo Finalizado')

				if ncarteira == 3:
					print(
						'Criptomoeda: Paxos Gold (PAXG), Quantidade: {}, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%'.format(
							saldo3, al3))
					print('')
					transfer = str(input('Deseja movimentar o circuito interno? '))
					print('')
					if transfer == 'não'.upper().lower() or transfer == 'nao'.upper().lower():
						print('')
					if transfer == 'sim'.upper().lower():
						print('')
						valor = float(input('Qualifique a tranferencia: '))
						print('')
						destino = leiaNcarteira('Qual a carteira de destino? (digite o número da carteira): ')
						taxa = random.choice(
							[0.001562, 0.002604, 0.002322, 0.002298, 0.002512, 0.002233, 0.001666, 0.001732, 0.001878,
							 0.001904,
							 0.002043, 0.002179, 0.002417, 0.002471, 0.002438, 0.001763, 0.001589, 0.001622, 0.001927,
							 0.001856])
						print('')
						confirmar = leiaCriptografia(
							'''		
                        O valor de taxa de é {} PAXG.
                        ERC-20 Transaction: Tax pending.
                        Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                        ID: {}{}{}{}{}{}{}{}{}-{}{}
                        Digite sim, para confirmar:'''.format(taxa, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2,
															  la3))
						if confirmar == 'sim'.upper().lower().strip():
							saldo3 = saldo3 - valor
							if destino == 1:
								saldo1 = saldo1 + valor - taxa
								al1 = (100 * real1) / total
							if destino == 2:
								saldo2 = saldo2 + valor - taxa
								al2 = (100 * real2) / total
							if destino == 3:
								saldo3 = saldo3 + valor - taxa
								al3 = (100 * real3) / total
							if destino == 4:
								saldo4 = saldo4 + valor - taxa
								al4 = (100 * real4) / total
							if destino == 5:
								saldo5 = saldo5 + valor - taxa
								saldo5 = round(saldo5, 5)
								al5 = (100 * real5) / total
							if destino == 6:
								saldo6 = saldo6 + valor - taxa
								saldo6 = round(saldo6, 5)
								al6 = (100 * real6) / total

							for c in range(1, ta1):
								print('Confirmação de rede pendende (0/3):  PROTOCOLO -',
									  ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))
								time.sleep(1.5)
							for c in range(1, ta2):
								print('Confirmação de rede pendende (1/3):  PROTOCOLO -',
									  ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))
								time.sleep(1.5)
							for c in range(1, ta3):
								print('Confirmação de rede pendende (2/3): PROTOCOLO -',
									  ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))
								time.sleep(1.5)
							print('Confirmação de rede pendende (3/3): PROTOCOLO -',
								  ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))

							if destino == 1:
								print(
									'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
							if destino == 2:
								print(
									'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
							if destino == 3:
								print(
									'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
							if destino == 4:
								print(
									'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
							if destino == 5:
								print(
									'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
							if destino == 6:
								print(
									'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
					else:
						print('Processo Finalizado')

				if ncarteira == 4:
					print(
						'Criptomoeda: Paxos Gold (PAXG), Quantidade: {}, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%'.format(
							saldo4, al4))
					print('')
					transfer = str(input('Deseja movimentar o circuito interno? '))
					print('')
					if transfer == 'não'.upper().lower() or transfer == 'nao'.upper().lower():
						print('')
					if transfer == 'sim'.upper().lower():
						print('')
						valor = float(input('Qualifique a tranferencia: '))
						print('')
						destino = leiaNcarteira('Qual a carteira de destino? (digite o número da carteira): ')
						taxa = random.choice(
							[0.001562, 0.002604, 0.002322, 0.002298, 0.002512, 0.002233, 0.001666, 0.001732, 0.001878,
							 0.001904,
							 0.002043, 0.002179, 0.002417, 0.002471, 0.002438, 0.001763, 0.001589, 0.001622, 0.001927,
							 0.001856])
						print('')
						confirmar = leiaCriptografia(
							'''		
                        O valor de taxa de é {} PAXG.
                        ERC-20 Transaction: Tax pending.
                        Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                        ID: {}{}{}{}{}{}{}{}{}-{}{}
                        Digite sim, para confirmar:'''.format(taxa, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2,
															  la3))
						if confirmar == 'sim'.upper().lower().strip():
							saldo4 = saldo4 - valor
							if destino == 1:
								saldo1 = saldo1 + valor - taxa
								al1 = (100 * real1) / total
							if destino == 2:
								saldo2 = saldo2 + valor - taxa
								al2 = (100 * real2) / total
							if destino == 3:
								saldo3 = saldo3 + valor - taxa
								al3 = (100 * real3) / total
							if destino == 4:
								saldo4 = saldo4 + valor - taxa
								al4 = (100 * real4) / total
							if destino == 5:
								saldo5 = saldo5 + valor - taxa
								saldo5 = round(saldo5, 5)
								al5 = (100 * real5) / total
							if destino == 6:
								saldo6 = saldo6 + valor - taxa
								saldo6 = round(saldo6, 5)
								al6 = (100 * real6) / total


							for c in range(1, ta1):
								print('Confirmação de rede pendende (0/3):  PROTOCOLO -',
									  ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))
								time.sleep(1.5)
							for c in range(1, ta2):
								print('Confirmação de rede pendende (1/3):  PROTOCOLO -',
									  ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))
								time.sleep(1.5)
							for c in range(1, ta3):
								print('Confirmação de rede pendende (2/3): PROTOCOLO -',
									  ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))
								time.sleep(1.5)
							print('Confirmação de rede pendende (3/3): PROTOCOLO -',
								  ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))

							if destino == 1:
								print(
									'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
							if destino == 2:
								print(
									'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
							if destino == 3:
								print(
									'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
							if destino == 4:
								print(
									'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
							if destino == 5:
								print(
									'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
							if destino == 6:
								print(
									'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
					else:
						print('Processo Finalizado')

				if ncarteira == 5:
					print(
						'Criptomoeda: Theter (USDT), Quantidade: {}, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%'.format(
							saldo5, al5))
					print('')
					transfer = str(input('Deseja movimentar o circuito interno? '))
					print('')
					if transfer == 'não'.upper().lower() or transfer == 'nao'.upper().lower():
						print('')
					if transfer == 'sim'.upper().lower():
						print('')
						valor = float(input('Qualifique a tranferencia: '))
						print('')
						destino = leiaNcarteira('Qual a carteira de destino? (digite o número da carteira): ')
						taxa = random.choice(
							[0.001562, 0.002604, 0.002322, 0.002298, 0.002512, 0.002233, 0.001666, 0.001732, 0.001878,
							 0.001904,
							 0.002043, 0.002179, 0.002417, 0.002471, 0.002438, 0.001763, 0.001589, 0.001622, 0.001927,
							 0.001856])
						print('')
						confirmar = leiaCriptografia(
							'''		
                        O valor de taxa de é {} PAXG.
                        ERC-20 Transaction: Tax pending.
                        Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                        ID: {}{}{}{}{}{}{}{}{}-{}{}
                        Digite sim, para confirmar:'''.format(taxa, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2,
															  la3))
						if confirmar == 'sim'.upper().lower().strip():
							saldo5 = saldo5 - valor
							if destino == 1:
								saldo1 = saldo1 + valor - taxa
								al1 = (100 * real1) / total
							if destino == 2:
								saldo2 = saldo2 + valor - taxa
								al2 = (100 * real2) / total
							if destino == 3:
								saldo3 = saldo3 + valor - taxa
								al3 = (100 * real3) / total
							if destino == 4:
								saldo4 = saldo4 + valor - taxa
								al4 = (100 * real4) / total
							if destino == 5:
								saldo5 = saldo5 + valor - taxa
								saldo5 = round(saldo5, 5)
								al5 = (100 * real5) / total
							if destino == 6:
								saldo6 = saldo6 + valor - taxa
								saldo6 = round(saldo6, 5)
								al6 = (100 * real6) / total

							for c in range(1, ta1):
								print('Confirmação de rede pendende (0/3):  PROTOCOLO -',
									  ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))
								time.sleep(1.5)
							for c in range(1, ta2):
								print('Confirmação de rede pendende (1/3):  PROTOCOLO -',
									  ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))
								time.sleep(1.5)
							for c in range(1, ta3):
								print('Confirmação de rede pendende (2/3): PROTOCOLO -',
									  ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))
								time.sleep(1.5)
							print('Confirmação de rede pendende (3/3): PROTOCOLO -',
								  ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))

							if destino == 1:
								print(
									'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
							if destino == 2:
								print(
									'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
							if destino == 3:
								print(
									'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
							if destino == 4:
								print(
									'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
							if destino == 5:
								print(
									'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
							if destino == 6:
								print(
									'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
					else:
						print('Processo Finalizado')

				if ncarteira == 6:
					print(
						'Criptomoeda: Theter (USDT), Quantidade: {}, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%'.format(
							saldo6, al6))
					print('')
					transfer = str(input('Deseja movimentar o circuito interno? '))
					print('')
					if transfer == 'não'.upper().lower() or transfer == 'nao'.upper().lower():
						print('')
					if transfer == 'sim'.upper().lower():
						print('')
						valor = float(input('Qualifique a tranferencia: '))
						print('')
						destino = leiaNcarteira('Qual a carteira de destino? (digite o número da carteira): ')
						taxa = random.choice(
							[0.001562, 0.002604, 0.002322, 0.002298, 0.002512, 0.002233, 0.001666, 0.001732, 0.001878,
							 0.001904,
							 0.002043, 0.002179, 0.002417, 0.002471, 0.002438, 0.001763, 0.001589, 0.001622, 0.001927,
							 0.001856])
						print('')
						confirmar = leiaCriptografia(
							'''		
                        O valor de taxa de é {} PAXG.
                        ERC-20 Transaction: Tax pending.
                        Aviso: Taxa de gás inclui crosschain dinâmico proporcional ao gás.
                        ID: {}{}{}{}{}{}{}{}{}-{}{}
                        Digite sim, para confirmar:'''.format(taxa, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2,
															  la3))
						if confirmar == 'sim'.upper().lower().strip():
							saldo6 = saldo6 - valor
							if destino == 1:
								saldo1 = saldo1 + valor - taxa
								al1 = (100 * real1) / total
							if destino == 2:
								saldo2 = saldo2 + valor - taxa
								al2 = (100 * real2) / total
							if destino == 3:
								saldo3 = saldo3 + valor - taxa
								al3 = (100 * real3) / total
							if destino == 4:
								saldo4 = saldo4 + valor - taxa
								al4 = (100 * real4) / total
							if destino == 5:
								saldo5 = saldo5 + valor - taxa
								saldo5 = round(saldo5, 5)
								al5 = (100 * real5) / total
							if destino == 6:
								saldo6 = saldo6 + valor - taxa
								saldo6 = round(saldo6, 5)
								al6 = (100 * real6) / total

							for c in range(1, ta1):
								print('Confirmação de rede pendende (0/3):  PROTOCOLO -',
									  ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))
								time.sleep(1.5)
							for c in range(1, ta2):
								print('Confirmação de rede pendende (1/3):  PROTOCOLO -',
									  ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))
								time.sleep(1.5)
							for c in range(1, ta3):
								print('Confirmação de rede pendende (2/3): PROTOCOLO -',
									  ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))
								time.sleep(1.5)
							print('Confirmação de rede pendende (3/3): PROTOCOLO -',
								  ''.join(random.SystemRandom().choices(string.ascii_letters, k=7)))

							if destino == 1:
								print(
									'O saldo da carteira R1 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo1, al1, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
							if destino == 2:
								print(
									'O saldo da carteira R2 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo2, al2, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
							if destino == 3:
								print(
									'O saldo da carteira R3 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo3, al3, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
							if destino == 4:
								print(
									'O saldo da carteira R4 é {} em PAXG, Status: Chaves ativas sob gerenciamento, Tipo: Reserva, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo4, al4, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
							if destino == 5:
								print(
									'O saldo da carteira I1 é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Intermediaria, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo5, al5, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
							if destino == 6:
								print(
									'O saldo da carteira FTX é {} em USDT, Status: Chaves ativas sob gerenciamento, Tipo: Corretora, AL: {}%, ID: {}{}{}{}{}{}{}{}{}-{}{}'.format(
										saldo6, al6, na1, na2, na3, la1, na4, na5, na6, na7, na8, la2, la3))
					else:
						print('Processo Finalizado')
