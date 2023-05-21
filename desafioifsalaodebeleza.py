tamanho_cabelo = int(input('Digite o tamanho do cabelo: '))

if tamanho_cabelo <= 20:
   print('O valor do seu corte custa R$ 50,00.')
elif 21 <= tamanho_cabelo <= 30:
   print('O valor do seu corte custa R$ 70,00.')
elif 31 <= tamanho_cabelo <= 50:
   print('O valor do seu corte custa R$ 100,00.')
elif tamanho_cabelo > 50:
   print('Favor consultar preço na recepção.')