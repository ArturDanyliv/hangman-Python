import sys       #zakonczenie dzialanie aplikacji



no_of_tries= 5           #mamy 5 szans 4 razy mozemy sie pomylic
word = "Artur"              #slowo ktore bedziemy zgadywac
used_letter = []                 #zeby uzytkownik wiedzial jakie litery wpisywal 

user_word = []

def find_indexes(word,letter):                    #wyszuka wszystkie litery na a
    indexes = [] 
    for index,letter_in_word in enumerate(word):  #k-1 a-2 m-3
        if letter == letter_in_word:
            indexes.append(index)
    return indexes

def show_state_of_game():                            #slowo uzytkownika za kazdym razem gdy wyswietlamy litere 
    print()
    print(user_word)
    print("Pozostało prób",no_of_tries)
    print("Uzyte litery:",used_letter)
    print()

for _ in word:                                       # zamiast letter _
    user_word.append("_")                            # jak uzytkowni zgadnie litere a to _a_ _ _ 
    

while True:
    letter = input("Podaj litere : ") #pytamy uzytkownika o litere            #pokazujemy uzytkowniku stan gry ipoazac
    used_letter.append(letter)        #jaka litere podal uzytkownik           #  ze uzytkownik odgagl haslo
     
    found_indexes = (find_indexes(word,letter))
    
    if len(found_indexes) == 0:
        print("Niema takiej litery.")
        no_of_tries -= 1
        #print("Pozostało prób:",no_of_tries)     #pokazuje ile pozostalo prob do uzycia   

        

        if no_of_tries == 0:
            print("Koniec gry :(")
    #find_indexes(word,letter)
    #print(word.index(letter))  #czy litera podana przez uzytkownika znajduje sie w slowie
            sys.exit(0)
    else:           
        for index in found_indexes:                      #jezeli litery w slowie zostana znalezione
            user_word[index]= letter                     #podmieniac znaki w naszym slowie 
            #print(user_word)                             # _ _ _ _ _ = _ a _ i _
            if "".join(user_word) == word:               #w momence gdy odgadniemy slowo konczymy gre
                print("Brawo to jest to slowo")   
                sys.exit(0) 
    #print("Uzycie litery :", used_letter)                #['k']
    show_state_of_game()
    
    