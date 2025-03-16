# Matriz 3D: [Ciudad][Semanas][Días]
ciudades = ["El Coca", "Lago Agrio", "El Sacha"]
semanas= ["semana1", "semana2", "semana3", "semana4"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Matriz tridimensional (3D) con temperaturas [3 ciudades][4 semanas][7 días]
temperaturas = [
    # El Coca
    [
        [28, 28, 30, 25, 27, 29, 30],  # semana 1
        [25, 29, 31, 28, 28, 30, 29],  # semana 2
        [25, 28, 29, 29, 27, 27, 28],  # semana 3
        [26, 29, 28, 28, 30, 29, 28]   # semana 4
    ],
    # Lago Agrio
    [   [29, 28, 28, 29, 30, 29, 31],  # semana 1
        [29, 29, 30, 27, 26, 27, 29],  # semana 2
        [28, 29, 29, 30, 29, 29, 30],  # semana 3
        [27, 28, 28, 29, 30, 30, 31]   # semana 4
        
    ],
    # El Sacha
    [   [31, 29, 28, 29, 30, 30, 31],  # semana 1
        [32, 29, 30, 28, 28, 29, 29],  # semana 2
        [29, 29, 28, 28, 29, 30, 30],  # semana 3
        [28, 29, 29, 30, 30, 31, 32]   # semana 4
        
    ]
]

# 🔹 Iterar sobre la matriz 3D
for h, ciudad in enumerate(ciudades):
    print(f"\n Ciudad: {ciudad}")
    
    total_temperaturas = 0  
    total_dias = 0  
    
    for i, semana in enumerate(temperaturas[h]):
        print(f"   Semana {i + 1}:")
        
        suma_semana = sum(semana)
        for j, temp in enumerate(semana):
            print(f"    {dias_semana[j]}: {temp}°C")

        promedio_semana = suma_semana / len(semana)
        print(f"     Promedio semanal: {promedio_semana:.2f}°C")

        total_temperaturas += suma_semana
        total_dias += len(semana)

    #  Promedio total por ciudad
    promedio_ciudad = total_temperaturas / total_dias
    print(f"   Promedio total en {ciudad}: {promedio_ciudad:.2f}°C")


