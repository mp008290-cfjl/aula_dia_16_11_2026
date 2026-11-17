def main():
  print("--- Cálculo do Determinante de uma Matriz 3x3 ---")
  matriz = []

  for i in range(3):
    linha = []
    for j in range(3):
      valor = float(input(f"Digite o elemento [{i}][{j}]: "))
      linha.append(valor)
    matriz.append(linha)

  a = matriz[0][0]
  b = matriz[0][1]
  c = matriz[0][2]
  d = matriz[1][0]
  e = matriz[1][1]
  f = matriz[1][2]
  g = matriz[2][0]
  h = matriz[2][1]
  i_val = matriz[
