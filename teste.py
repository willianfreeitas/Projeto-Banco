from models.cliente import Cliente
from models.conta import Conta


Willian: Cliente = Cliente('Willian Freitas', 'willian@email.com', '123.456.789-00', '11/11/1999')
Maria: Cliente = Cliente('Maria Zinha', 'maria@zinha.com', '987.654.321-00', '12/12/1994')

print(Willian)
print(Maria)

contaw: Conta = Conta(Willian)
contam: Conta = Conta(Maria)

print(contaw)
print(contam)
