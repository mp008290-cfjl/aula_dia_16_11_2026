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
      2
][2]  # Usado 'i_val' para evitar conflito com a variável de loop

  # 2. Calcula o determinante usando a fórmula informada:
  # detM = a*e*i + b*f*g + c*d*h - c*e*g - b*d*i - a*f*h
  det = (
      (a * e * i_val)
      + (b * f * g)
      + (c * d * h)
      - (c * e * g)
      - (b * d * i_val)
      - (a * f * h)
  )

  # 3. Exibe a matriz digitada em formato de tabela
  print("\n================================")
  print("        MATRIZ INFORMADA        ")
  print("================================")
  for linha in matriz:
    linha_formatada = " | ".join(f"{val:6g}" for val in linha)
    print(f"[ {linha_formatada} ]")
  print("================================")

  # 4. Apresenta o resultado do determinante
  print(f" O determinante (det M) é: {det}")
  print("================================")


if __name__ == "__main__":
  main()