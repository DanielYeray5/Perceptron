import random

class Perceptron:
    
    def __init__(self):
        self.w1 = random.uniform(-1 , 1)
        self.w2 = random.uniform(-1 , 1)
        self.bias = random.uniform(-1 , 1)
        
    def prediccion(self, x1, x2):
        resultado = x1 * self.w1 + x2 * self.w2 + self.bias
        
        if resultado >= 0: 
            return 1
        else: 
            return 0
        
def train(perceptron, TablaNand, limit_range = 0.1, generations = 25):
    
    print("Pesos iniciales: ")    
    print("w1: ", round(perceptron.w1, 2), 
            "w2: ", round(perceptron.w2, 2),
            "bias: ", round(perceptron.bias, 2)
    )
    
    for generation in range(generations):
        
        #? Recorrer las tabla NAND
        for x1, x2, y_real in TablaNand:
            
            y_prediccion = perceptron.prediccion(x1, x2)
            error = y_real - y_prediccion
            
            perceptron.w1 += limit_range * error * x1 
            perceptron.w2 += limit_range * error * x2
            perceptron.bias += limit_range * error
            
        print(f"Generación {generation + 1}: "
            f"w1: {round(perceptron.w1, 2)} "
            f"w2: {round(perceptron.w2, 2)} "
            f"bias: {round(perceptron.bias, 2)}"
            )
            
            
def prueba(perceptron, TablaNand):
    
    print("Resultado final: ")
    
    for x1, x2, _ in TablaNand:
        resultado = perceptron.prediccion(x1, x2)
        print(f"{x1} NAND {x2} = {resultado}")

def main():
    TablaNand = [
        (0,0,1),
        (0,1,1),
        (1,0,1),
        (1,1,0)
    ]
    
    perceptron = Perceptron()
    
    train(perceptron, TablaNand, limit_range=0.1, generations=18)
    
    prueba(perceptron, TablaNand)

if __name__ == "__main__":
    main()