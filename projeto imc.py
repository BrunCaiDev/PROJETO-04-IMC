nome = input ("Qual o seu nome?")
peso = float  (input("Qual é o seu peso?")) 
altura = float (input("Qual a sua altura"))

imc = peso / (altura*altura)







if imc <=18.5:
    print(f"{nome} abaixo do peso {imc}")
elif 18.5 <= imc <= 24.9 :
    print(f"{nome} peso normal  {imc}" )
elif 25.0 <= imc <= 29.9 :
    print   (f"{nome} sobrepeso {imc}") 
elif 30.0 <= imc <= 34.9 :
    print (f"{nome} obesidade grau I {imc}" )              
elif 35.0 <= imc <= 39.9 :
    print ( f"{nome} obesidade grau II {imc}") 
elif imc >= 40 :
       print (f"{nome}obesidade grau III {imc}")       
else :
     print (f"peso invalido ")
