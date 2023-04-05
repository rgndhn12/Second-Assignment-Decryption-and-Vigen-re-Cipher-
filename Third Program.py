#Dahan, Regine Fae M. (BSCPE 1-5) Third Code

def main():

    import pyfiglet
    import time

    #Introduction
    the_intro ='Starting...'
    print(pyfiglet.figlet_format(the_intro,font="digital"))
    time.sleep(3)
    print('Hello! This program is entitled THE VIGENÉRE CIPHER!')
    time.sleep(2)

    now_begin ='Let\'s start'
    print(pyfiglet.figlet_format(now_begin,font="bubble"))
    time.sleep (2)

    #Vigenére Cipher
    def encrypt(text, key):
        letters = list("abcdefghijklmnopqrstuvwxyz")
        key_list = []
        encrypted = []
    
        for i in range(len(text)):
            for i in key:
                if (len(key_list) == len(text)):
                    break
                else:
                    key_list.append(letters.index(i))
    
        for i in range(len(text)):
            add = (letters.index(text[i]) + key_list[i])
            encrypted.append(letters[add % 26].upper())
    
        return ' '.join(encrypted)

    #User Input
    user_input = (input("Enter a message: ")).lower()
    keyword = (input("Enter a key: ")).lower()
    print('=========================================PLEASE WAIT=========================================')

    #Output
    time.sleep (2)
    print('The output of your message and key is>>>',encrypt(user_input, keyword))

    #Try Again?
    time.sleep(2)
    while True:
        print('=========================================================================================')
        try_again = input (' PRESS 1 if you want to try again. PRESS 2 if otherwise. ')

        if (try_again == '1'):
            main()
        elif (try_again == '2'):
            print(' Thank you for using my program : ) ')
            exit()
        else:
            print('Invalid.')
            
main()
       