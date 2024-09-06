def main():
    
    with open("books/frankenstein.txt") as theFile:
        
        thefile_contents = theFile.read()
        
        words = thefile_contents.split()
        total_character_count = len(words)
        count_letters_in_file(thefile_contents)
        print(f"Total number of characters in the text: {len(words)}")
def count_letters_in_file(text):
    text = text.lower()
    character_count = {}

    for character in text:
        if character.isalpha():
            if character in character_count:
                character_count[character] += 1
            else:
                character_count[character] = 1
                print (character_count)
                total_character_count = (character_count)

    character_count_list= list(character_count.items())
    character_count_list.sort(key=lambda x: x[1], reverse=True)
    

    for character, count in character_count_list:
        
        if character == " ":
            print (f"The 'space' character was found {count} times in the text")
        elif character =='\n':
            print (f"The 'new line' character was found {count} times in the text")
        else:   
            print (f"The '{character}' character was found {count} times in the text")

main ()

