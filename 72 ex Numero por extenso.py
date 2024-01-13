# Create a program that uses a tuple filled with a count in words from zero to twenty.
# Your program should read a number from the keyboard (between 0 and 20) and display the entered number in words.

words = ("zero", "one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine", "ten", "eleven",
        "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen", "twenty")

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

while True:
    choice = int(input('Choose a number between 0 and 20: '))
    
    if 0 <= choice <=20: # Display the chosen number in words if it's within the range
        print(f'You chose the number {words[choice]}.') # espaço reservado que será substituído 
# pelo valor no índice choice da tupla words
    else:
        print('Try again. Number out of supported range.')
        continue # Go back to the beginning of the loop
    
    answer = input('Do you want to continue? [Y/N] ')
    if answer in 'N/n':
        break    
       
#  espaço reservado que será substituído 
# pelo valor no índice escolha da tupla extenso
# A associação entre o número e sua representação por extenso ocorre por meio do índice na 
# tupla extenso. No código fornecido, a variável escolha armazena o número digitado pelo usuário. 
# Em seguida, essa variável é usada como índice na tupla extenso para obter a representação por extenso correspondente.
# A associação entre o número digitado (escolha) e sua representação por extenso ocorre 
# automaticamente devido ao uso do índice na tupla.


