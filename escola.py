def verificador_media(media:int|float) -> str :
   """"Está função retorna se o aluno passou ou não de ano"""

   #Testando para ver se a média é um número
   if not isinstance(media, (int, float)):
      raise TypeError("Tipo inválido, a entrada deve ser númerica")

   if media < 0:
      raise ValueError("O valor deve ser menor ou igual a 0 ou igual a 10")
   
   if media > 10:
      raise ValueError("O valor deve ser maior ou igual a 0 ou igual a 10")
   
   if media >= 7:
      return "Aprovado"
   elif media <= 4:
      return "Reprovado"
   else:
      return "Recuperação"
   

   
#if __name__ == "__main__":
   #print(verificador_media(6))
