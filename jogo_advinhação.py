import random


def gerar_numero_secreto(limite_inferior, limite_superior):
  """Gera um número aleatório entre limite_inferior e limite_superior."""
  return random.randint(limite_inferior, limite_superior)



def pedir_chute(limite_inferior, limite_superior):
  """Pede ao jogador para digitar um número dentro do intervalo."""
  while True:
    try:
      chute = int(input(f"Digite um número entre {limite_inferior} e {limite_superior}: "))
      if limite_inferior <= chute <= limite_superior:
        return chute
      else:
        print("Número inválido. Tente novamente.")
    except ValueError:
      print("Entrada inválida. Digite um número inteiro.")



def verificar_chute(chute, numero_secreto):
  """Verifica se o chute é igual, maior ou menor que o número secreto."""
  if chute == numero_secreto:
    print("Parabéns! Você acertou!")
    return True
  elif chute < numero_secreto:
    print("Tente um número maior.")
  else:
    print("Tente um número menor.")
  return False



def jogar_adivinhacao():
  """Função principal para iniciar o jogo."""
  limite_inferior = 1
  limite_superior = 100
  numero_secreto = gerar_numero_secreto(limite_inferior, limite_superior)
  print("Bem-vindo ao jogo de adivinhação!")
  print(f"Estou pensando em um número entre {limite_inferior} e {limite_superior}.")


  
  acertou = False
  while not acertou:
    chute = pedir_chute(limite_inferior, limite_superior)
    acertou = verificar_chute(chute, numero_secreto)

if __name__ == "__main__":
  jogar_adivinhacao()
