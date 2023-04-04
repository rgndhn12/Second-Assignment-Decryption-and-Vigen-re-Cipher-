#Dahan, Regine Fae M. (BSCPE 1-5) Second Code

def main():
    import pyfiglet
    import time

    #Introduction
    the_intro ='Starting...'
    print(pyfiglet.figlet_format(the_intro,font="digital"))
    time.sleep(3)
    print('Hello! This program is entitled DECRYPTION! It will accept a\nstring as encrypted text, then the program will decrypt it.')
    time.sleep(2)

    now_begin ='Let\'s start'
    print(pyfiglet.figlet_format(now_begin,font="bubble"))
    time.sleep (2)
    
    #User Input
    user_input = input (' Type your string >>> ')
    the_output = ''

    #Decryption 
    for i in range (len(user_input)):

        if user_input[i] == '*':
            the_output += 'a'
        
        elif user_input[i] == '&':
            the_output += 'e'

        elif user_input[i] == '#':
            the_output += 'i'
        
        elif user_input[i] == '+':
            the_output += 'o'
        
        elif user_input[i] == '!':
            the_output += 'u'
        
        else:
            the_output += user_input[i]

    #Displaying Output
    time.sleep(1)
    the_decryption = ' Decrypting the string...'
    print(pyfiglet.figlet_format(the_decryption,font="digital"))
    time.sleep(2)
    print ('The string\'s decryption is >>>',the_output)
    
    #Try Again?
    time.sleep(2)
    while True:
        print('==========================================================================')
        try_again = input (' PRESS 1 if you want to try again. PRESS 2 if otherwise. ')

        if (try_again == '1'):
            main()
        elif (try_again == '2'):
            print(' Thank you for using my program : ) ')
            exit()
        else:
            print('Invalid.')
main()