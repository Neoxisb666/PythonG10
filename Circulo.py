import math 
def calcularAreaPerimetro ():
    try: 
        radio = float(input("ingrese el radio: "))
        if radio < 0:
            raise ValueError("El radio no puede ser negativo")
        
        #area = math.pi * (pow(radio))
        area = math.pi * (radio ** 2)

        perimetro = 2 * math.pi * radio

        print(f"area del circulo es: {area:.2f}")
        print(f"perimetro del circulo es: {area:.3f}")

    except ValueError as e:
        print (f"error: {e} " )
    except ValueError as e:
        print (f"error inesperado: {e}")
        