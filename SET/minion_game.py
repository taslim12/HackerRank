def minion_game(string):
    # your code goes here
    given_input = string.upper()
    vowels = ['A','E','I','O','U']
    vowel_words = [x for x in given_input if x in vowels]
    cons_words = [x for x in given_input if x not in vowels]
    Stuart_1 = list(set(cons_words))
    Kevin_1 = list(set(vowel_words))
    print(vowel_words)
    print(cons_words)
    print(Stuart_1)
    print(Kevin_1)

if __name__ == '__main__':
    s = input()
    minion_game(s)