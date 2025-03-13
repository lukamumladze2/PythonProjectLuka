import random

def hangman():
    words = ["სახლი", "ვაშლი", "მანქანა", "სამუშაო", "კატა", "ძაღლი", "რესტორანი", "სკოლა"]
    word = random.choice(words)
    word_letters = list(word)
    alphabet = list("აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ")
    used_letters = []

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print('შენ გაქვს', lives, 'სიცოცხლე, გამოყენებული ასოები: ', ' '.join(used_letters))

        word_list = []
        for letter in word:
            if letter not in word_letters:
                word_list.append(letter)
            else:
                word_list.append('_')
        print('სიტყვა: ', ' '.join(word_list))

        user_letter = input('გამოიცანი ასო: ')
        if user_letter in alphabet:
            if user_letter not in used_letters:
                used_letters.append(user_letter)
                if user_letter in word_letters:
                    while user_letter in word_letters:
                        word_letters.remove(user_letter)
                    print('')
                else:
                    lives -= 1
                    print('ეს ასო არაა სიტყვაში.')
            else:
                print('ეს ასო უკვე გამოყენებულია, თავიდან სცადეთ.')
        else:
            print('არასწორი ასო. თავიდან სცადეთ')

    if lives == 0:
        print('თქვენ წააგეთ, სიტყვა იყო:', word)
    else:
        print('თქვენ გაიმარჯვეთ! საბოლოო სიტყვა:', word,)

user_input = input("დააჭირეთ Enter-ს თუ გინდათ რომ hangman-ის თამაში დაიწყოთ: ")
if user_input == (''
                          ''):
    hangman()