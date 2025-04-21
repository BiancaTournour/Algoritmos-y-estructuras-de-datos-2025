def romano_a_decimal(romano: str):
    valores = { 'I': 1, 'V': 5, 'X': 10,'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    if len(romano) == 1:
        return valores[romano]
    
    actual = valores[romano[0]]
    siguiente = valores[romano[1]]

    if actual >= siguiente:
           return actual+romano_a_decimal(romano[1:])
    else:
         return -actual + romano_a_decimal(romano[1:])    
            
romano = input("ingrese un numero romano: ").upper()
decimal = romano_a_decimal(romano)
print (decimal)