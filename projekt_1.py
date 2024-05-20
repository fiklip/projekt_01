"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Filip Vrbík 
email: filip.vrbik@vzp.cz
discord: filip.vrbik

"""
# zkouška uložení nové verze na github

import text

#====zadání jména a hesla====
username = input("USERNAME: ")
password = input("PASSWORD: ")

#====registrovaní uživatelé====
registr_users = {"bob": "123", 
                "ann": "pass123", 
                "mike": "password123", 
                "liz": "pass123"}



if username in registr_users.keys(): # ověření, jestli existuje registrované username, podmínka 0

    if registr_users[username] == password: # ověření správnosti hesla u registrovaného username, podmínka 1
        print("="*24)
        print(f"Welcome to the app, {username}. We have 3 texts to be analyzed.")
        print("="*24)
        text_number = input("Enter a number between 1 and 3 to select: ") # s jakým textem budu pracovat
        print("="*24)
        
        
        if text_number.isdigit() and int(text_number) in range(1,4): # ověření, jestli se zadalo správné číslo textu a zdali to bylo číslo, podmínka 2
            chosen_text = text.TEXTS[int(text_number) - 1].replace(",", "").replace(".", "") # vybraný text, s kterým pracuji, očištěno o , a .
            print(chosen_text)
            print("="*24)
            words_count = len(chosen_text.split()) # zde zjistím, kolik je v textu slov, počítáno dle mezer v textu
            print(f"There are {words_count} words in the selected text.")
            
            words_title_count = 0 # zde zjistím, kolik slov v textu začíná velkým písmenem
            words_title = chosen_text.split()
            for word in words_title:
                if word.istitle():
                    words_title_count = words_title_count + 1
                else:
                    continue
            print(f"There are {words_title_count} titlecase words in the selected text.")
            
            words_upper_count = 0 # zde zjistím, kolik slov v textu je tvořeno velkými písmeny
            words_upper = chosen_text.split()
            for word in words_upper:
                if word.isupper() and word.isalpha():
                    words_upper_count = words_upper_count + 1
                else:
                    continue
            print(f"There are {words_upper_count} uppercase words in the selected text.")
            
            words_lower_count = 0 # zde zjistím, kolik slov v textu je tvořeno malými písmeny
            words_lower = chosen_text.split()
            for word in words_lower:
                if word.islower():
                    words_lower_count = words_lower_count + 1
                else:
                    continue
            print(f"There are {words_lower_count} lowercase words in the selected text.")

            digits_count = 0 # zde zjistím, kolik je v textu čísel
            digits_sum = 0 # zde zjistím součet čísel v textu
            digits = chosen_text.split()
            for digit in digits:
                if digit.isdigit():
                    digits_count = digits_count + 1
                    digits_sum = digits_sum + int(digit)
                else:
                    continue
            print(f"There are {digits_count} numeric strings.")
            print(f"The sum of all the numbers is: {digits_sum}.")
            print("="*24)
            
            #========= sloupcový graf==========
            
            print("LEN|  OCCURENCES   |NR.")
            print("="*24)

            word_lengths = [] # zde si vytvářím nový list, do kterého se ukládá délka jednotlivých slov v očištěném vybraném textu, který je "rozsekán dle mezer"  
            for i in chosen_text.split():
                word_lengths.append(len(i))
           
            word_lengths_unique = set(word_lengths) # tato proměná obsahuje unikátní délky slov z vybraného textu

            for length in word_lengths_unique: # zde vypisuji county všech jednotlivých délek slov a vytvářím sloupcový graf
                numbers = word_lengths.count(length)
                print(f"{length:3}|  {'*' * numbers:13}|{numbers}") # :3 nebo :13 minimální šířku 3 respektive 13 znaků, díky tomu to mám zarovnané
                

           

        
        
        
        else: # ukončení podmínky 2, nesprávně zadané číslo textu
            print("Incorrect input, terminating program..")

    else: # ukončení podmínky 1, špatné password
        print("unregistered user, terminating the program..")

else: # ukončení podmínky 0, neregistrovaný username
    print("unregistered user, terminating the program..")