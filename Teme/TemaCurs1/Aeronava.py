class Aeronava():
    def __init__(self , tip , cantitate , cost , autonomie , vizibilitate_minima):
        self.tip = tip
        self.cantitate = cantitate
        self.cost = cost
        self.autonomie = autonomie
        self.vizibilitate_minima = vizibilitate_minima
    
    def afis(self):
        print(f"Tip: {self.tip}")
        print(f"Cantitate: {self.cantitate}")
        print(f"Cost: {self.cost} unități")
        print(f"Autonomie: {self.autonomie} km")
        print(f"Vizibilitate minimă: {self.vizibilitate_minima} m")
        print("-" * 30)