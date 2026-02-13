def verificador_media(media:int|float) -> str:
   """"Está função retorna se o aluno passou ou não de ano"""

   if media >= 7:
      return "Aprovado"
   elif media < 5:
      return "Reprovado"
   else:
      return "Recuperação"
   
#if __name__ == "__main__":
   #print(verificador_media(6))
