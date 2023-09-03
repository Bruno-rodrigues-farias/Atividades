print("Hello, world")


#ATIVIDADE 6
# for i in range (1, 11):
#    for j in range (1, 11):
#         multiplicacao = i * j
#     print(f"A mutilplicação de :{i} x {j} = {multiplicacao} ")



# x = 1
# y = 1

# while x <=10:
    
#     while y <= 10:
#         multi = x * y

#         print(f"{x} x {y} = {multi}")

#         y += 1
        
#     x += 1  
#     y = 1


    #ATIVIDADE 4
# calculador_notas = 0
# voltas = 0

# while True:
#     nota = float(input("Digite uma nota: "))

#     if nota == -1:
#         break

#     calculador_notas += nota
#     voltas +=1

# media = calculador_notas / voltas

# print(media)



aculador_notas = 0 
voltas = 0

while True:
    nota = input("Digite uma nota: ")

    if nota not in "12345678910":
        print("Número não encontrado")
    else:
        nota = float(nota)

        if nota >= 0 and nota <= 10:
            aculador_notas += nota
            voltas += 1

            escolha = input("Quer adicionar mais uma nota (s/n)")

            if escolha.lower() == "n" or escolha.lower() == "não":
                break
        else:
                print("Nota apenas entre 0 a 10")

media = aculador_notas / voltas
print(media) 