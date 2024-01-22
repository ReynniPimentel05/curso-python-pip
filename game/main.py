import random

options = ('python', 'javascript', 'c++')

rounds = 1
user_wins = 0
computer_wins = 0

while True:

  print('*' * 10)
  print('ROUND',rounds)
  print('*' * 10)

  print("computer_wins", computer_wins)
  print("user_wins", user_wins)
  
  user_option=input("python', 'javaScript' o 'C++' => ").lower()
  rounds += 1 
  
  if user_option not in options:
    print('Esa opcion no es valida')
    continue
  computer_option= random.choice(options)
    
  print('user option =>', user_option)
  print('computer option =>', computer_option)
    
  if user_option == computer_option:
      print("Empate!")
  elif user_option =='python':
    if computer_option == 'javascript':
        print("python gana a javascript")
        print("Usted ha ganado!")
        user_wins += 1
    else:
      print("c++ gana a python")
      print("computer ha ganado!")
      computer_wins += 1
  elif user_option == 'c++':
    if computer_option == 'python':
       print("c++ gana a python")
       print("Usted ha ganado!")
       user_wins += 1
    else:
      print("javascript gana a c++")
      print("computer ha ganado!")
      computer_wins += 1
  elif user_option == 'javascript':
    if computer_option == 'c++':
       print("Javascript gana a c++")
       print("Usted ha ganado!")
       user_wins += 1
    else:
       print("python gana a Javascript")
       print("computer ha ganado!")
       computer_wins += 1
  elif user_option == 'c++':
    if computer_option == 'Javascript':
       print("javascript gana a c++")
       print("Computer ha ganado!")
       computer_wins += 1
    else:
       print("c++ gana a python")
       print("Usted ha ganado!")
       user_wins += 1

  
  if computer_wins == 3:
     print("El ganador definitivo es el computador")
     break

  if user_wins == 3:
     print("Usted es el ganador definitivo")
     break
     