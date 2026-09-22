AFD = { #diccionario clave: valor
  "Inicial": "q0",
  "aceptación": {"q0", "q1","q2"}, # la estructura {} es conjunto
  "delta": {
    ("q0", "a"): "q1",
    ("q0", "b"): "q0",
    ("q1", "a"): "q2",
    ("q1", "b"): "q1",
    ("q2", "a"): "q3",
    ("q2", "b"): "q2",
    ("q3", "a"): "q3",
    ("q3", "b"): "q3"
  }
}

def ejecutar(AFD, cadena):
  estado = AFD['Inicial'] 
  for simbolo in cadena:
    estado = AFD["delta"][(estado, simbolo)]
  return estado in AFD['aceptación'] 


def ejecutar_traza(AFD, cadena): # la traza se calcula dentro del AFD al leer una cadena
  lista_tranciciones = []
  estado_actual = AFD['Inicial'] 
  print(estado_actual)
  #ahoraimprimimos cada elemento del afd que visitamos
  for simbolo in cadena:
    estado_nuevo = AFD ['delta'][(estado_actual,simbolo)]
    estado_actual = estado_nuevo
    print("->",estado_actual)
  print()
  print("ACEPTADA" if estado_actual in AFD["aceptación"] else "Rechazada")  
  print("La lista final de tranciciones es ", lista_tranciciones)

cadena = "bbbaaaab"
print("La cadena", cadena, "esta:")
if ejecutar(AFD, cadena):
  print("Aceptada")
else:
  print("Rechazada")
ejecutar_traza(AFD, cadena)
