def char_count(data):
    print(len(data)," Characters with spaces")
    d = data.replace(" ","")
    print(len(d)," Characters without spaces")
    

def word_count(data):
    wc = data.split()
    print(len(wc)," words are present")
   

def sentence_count(data):
    data = data.strip() 
    sc = [s for s in data.split('.') if s.strip()]  
    print(len(sc), "sentences are present")



data = input("Enter your text.....")
while True:
    try:
        choice =int(input("""
             Enter
             1 to count the characters.
             2 to count the words.
             3 to count the sentences.
             4 to exit....."""))
    except ValueError:
        print("\nPlease enter a valid number.")
        continue    

    if choice == 1:
        char_count(data)
    elif choice == 2:
        word_count(data)
    elif choice == 3:
        sentence_count(data)
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
 

    