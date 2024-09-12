
class Estudante:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []
    
    def nota(self, nota):
        if len(self.notas) < 4:
            self.notas.append(nota)
        else: 
            print("Não é possível adicionar mais notas, o ano letivo tem apenas 4 bimestres.")
            
    def calcular_media(self):
        if len(self.notas) == 4:
            return sum(self.notas) / 4
        else:
            print("Ainda não há notas suficientes para calcular a média.")
            return None
        
    def __str__(self):
        return f"Estudante: {self.nome}, Notas: {self.notas}"
    
nome = input("Digite seu nome")
estudante = Estudante(nome)

for i in range(4):
    nota = float(input(f"Digite a nota do {i+1}º bimestre:"))
    estudante.nota(nota)
    
    
print(estudante)
media = estudante.calcular_media()

if media is not None:
    print(f"Média Anual: {media:.2f}")
        

