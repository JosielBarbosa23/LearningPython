import logging

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a', format='%(levelname)s - %(message)s - %(asctime)s')

try:
    email = input('Digite seu e-mail: ')
    senha = int(input('Informe sua senha bancária: '))
    print('Login feito com sucesso.')
    logging.info(f'{email} fez login no aplicativo bancário.')
except ValueError as erro:
    print('Digite apenas números!')
    logging.info(erro)
