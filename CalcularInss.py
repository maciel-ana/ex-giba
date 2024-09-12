
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def calcular_inss(self):
        if self.salario > 5000:
            desconto_inss = self.salario * 0.10
        else:
            desconto_inss = 0 
        return desconto_inss

    def __str__(self):
        return f"Funcionário: {self.nome}, Salário: R${self.salario:.2f}"
    
    
nome = input("Me diga qual é seu nome:")
salario = float(input("Digite o seu salário:"))
    
funcionario = Funcionario(nome, salario)

print(funcionario)  
print(f"Desconto de INSS: R${funcionario.calcular_inss():.2f}")
    