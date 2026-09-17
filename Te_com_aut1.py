AFD = { #diccionario clave: valor
  "Inicial": "q0",
  "aceptación": {"q2"}, # la estructura {} es conjunto
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
