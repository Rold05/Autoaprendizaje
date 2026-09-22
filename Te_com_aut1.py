AFD = { #diccionario clave: valor
  "Inicial": "q0",
  "aceptación": {"q1"}, # la estructura {} es conjunto
  "delta": {
    ("q0", "b"): "q1",
    ("q0", "a"): "q2",
    ("q1", "a"): "q1",
    ("q1", "b"): "q1",
    ("q2", "a"): "q2",
    ("q2", "b"): "q2"
  }
}

def ejecutar(AFD, cadena):
  estado = AFD['Inicial'] 
  for simbolo in cadena:
    estado = AFD["delta"][(estado, simbolo)]
  return estado in AFD['aceptación'] 

cadena = "bbababababbaba"
print("La cadena", cadena, "esta:")
if ejecutar(AFD, cadena):
  print("Aceptada")
else:
  print("Rechazada")
