import csv
import matplotlib.pyplot as plt

while True:
   opc = input (' 1- Criar arquivo\n 2- Ler arquivo\n 3- Mostrar gráfico\n 4- Sair do Programa\n escolha uma opção: ' )
  
   if opc == '1':
       x = int(input('forneça um numero de presente que deseja: \n'))

       f = open('tabela.csv', 'w', newline="")

       try:
           writer = csv.writer(f)
           writer.writerow(('presente', 'salario'))
           for c in range(0, x):
               pre = input('escreva uma presente : ')
               val = float(input('forneça o valor do produto '))
               writer.writerow((pre, val))

       finally:
           f.close()

   elif opc == '2':
       print('\n')
       try:
           print(open('tabela.csv', 'r').read())

       except:
           print('não foi possível encontrar o arquivo!')

   elif opc == '3':
       try:
           presente = []
           valor = []

           f = open('tabela.csv', 'r')
           rec = csv.DictReader(f)

           for z in rec:
               presente.append(z['presente'])
               valor.append(float(z['valor']))
           try:
               plt.figure(figsize=(6, 6))

               plt.plot(presente, valor)
               plt.show()

               plt.bar(presente, valor)
               plt.show()

               fig1, ax1 = plt.subplots(figsize=(6, 6))
               ax1.pie(valor, labels=presente, autopct='%1.1f%%', shadow=True, startangle=90)
               ax1.axis('equal')
               plt.show()


           finally:
               f.close()

       except:
           print('não foi possível encontrar o arquivo!')

   elif opc == '4':
       break