id1 = int(input("Digite sua primeira idade: "))
id2 = int(input("Digite sua segunda idade: "))
idade = int(id1 + id2) 

if idade < 18:
  print("menor de idade") 
elif idade >= 18 and idade <= 30:
  print("Jovem")
elif idade >= 30 and idade <= 50:
  print("Adulto maduro")
elif idade >= 50 and idade <= 70:
  print("Velho")
elif idade >= 70 and idade <= 110:
  print("Idoso")
elif idade >= 110: 
  print("morto")




