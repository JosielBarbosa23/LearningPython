# Calcule quantos dias faltam para seu aniversário
from datetime import datetime
dataaniv = datetime.strptime(input('Informe a data do seu aniversário: '), '%d/%m/%Y')
dataatual = datetime.now()
diasateaniv = dataaniv - dataatual
print(f'Restam {diasateaniv} para seu aniversário.')
