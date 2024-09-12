from datetime import datetime

class Data:
    def __init__(self, dia, mes, ano):
        try:
            self.data = datetime(year=ano, month=mes, day=dia)
        except ValueError as e: 
            raise ValueError(f"Data inválida: {dia}/{mes}/{ano}. Erro {e}")
    
    def __str__(self):
        return self.data.strftime("%d/%m/%Y")
    
    
try: 
    data_valida = Data(6, 9, 2024 )
    print(data_valida)
except ValueError as e:
        print(e)
        
try:
    data_invalida = Data(30, 2, 2023)
    print(data_invalida)
except ValueError as e:
    print(e)