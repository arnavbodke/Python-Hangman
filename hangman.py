import random

word_list = ['abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar', 'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords', 'caliph', 'cobweb', 'cockiness', 'croquet', 'crypt', 'curacao', 'cycle', 'daiquiri', 'dirndl', 'disavow', 'dizzying', 'duplex', 'dwarves', 'embezzle', 'equip', 'espionage', 'exodus', 'faking', 'fishhook', 'fixable', 'fjord', 'flapjack', 'flopping', 'fluffiness', 'flyby', 'foxglove', 'frazzled', 'frizzled', 'fuchsia', 'funny', 'gabby', 'galaxy', 'galvanize', 'gazebo', 'gizmo', 'glowworm', 'glyph', 'gnarly', 'gnostic', 'gossip', 'grogginess', 'haiku', 'haphazard', 'hyphen', 'iatrogenic', 'icebox', 'injury', 'ivory', 'ivy', 'jackpot', 'jaundice', 'jawbreaker', 'jaywalk', 'jazziest', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey', 'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo', 'keyhole', 'khaki', 'kilobyte', 'kiosk', 'kitsch', 'kiwifruit', 'klutz', 'knapsack', 'larynx', 'lengths', 'lucky', 'luxury', 'lymph', 'marquis', 'matrix', 'megahertz', 'microwave', 'mnemonic', 'mystify', 'naphtha', 'nightclub', 'nowadays', 'numbskull', 'nymph', 'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 'phlegm', 'pixel', 'pizazz', 'pneumonia', 'polka', 'pshaw', 'psyche', 'puppy', 'puzzling', 'quartz', 'queue', 'quips', 'quixotic', 'quiz', 'quizzes', 'quorum', 'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw', 'schnapps', 'scratch', 'shiv', 'snazzy', 'sphinx', 'spritz', 'squawk', 'staff', 'strength', 'strengths', 'stretch', 'stronghold', 'stymied', 'subway', 'swivel', 'syndrome', 'thriftless', 'thumbscrew', 'topaz', 'transcript', 'transgress', 'transplant', 'twelfth', 'twelfths', 'unknown', 'unworthy', 'unzip', 'uptown', 'vaporize', 'vixen', 'vodka', 'voodoo', 'vortex', 'voyeurism', 'walkway', 'waltz', 'wave', 'wavy', 'waxy', 'wellspring', 'wheezy', 'whiskey', 'whizzing', 'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy', 'wristwatch', 'wyvern', 'xylophone', 'yachtsman', 'yippee', 'yoked', 'youthful', 'yummy', 'zephyr', 'zigzag', 'zigzagging', 'zilch', 'zipper', 'zodiac', 'zombie', 'apple', 'banana', 'orange', 'grape', 'lemon', 'melon', 'pear', 'peach', 'plum', 'berry', 'chair', 'table', 'window', 'door', 'car', 'bike', 'bus', 'train', 'plane', 'boat', 'sun', 'moon', 'star', 'cloud', 'rain', 'snow', 'tree', 'plant', 'flower', 'grass', 'house', 'school', 'book', 'pen', 'pencil', 'paper']
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print('')
print("HANGMAN")
print('''
How to Play:      
- A random word will be selected and hidden.
- It will appear as a series of underscores '_', where each underscore represents a letter in the word.
- You will be prompted to guess a letter.
- If your guess is correct, the letter will be revealed in its correct position(s).
- If your guess is incorrect, a part of the hangman drawing will appear, and you lose a life.
- You have 6 lives at the start of the game.
- Each incorrect guess reduces your lives by one.
- If you lose all lives, the hangman figure will be completed, and you lose the game. 
''')

pan = 'y'
while pan == 'y':
    word_list = word_list
    a1 = random.choice(word_list)
    print(f"Selected word is of {len(a1)} letters")

    placeholder = ""
    for i in a1:
        placeholder += '_'

    print(placeholder)
    s = 1
    p = []
    l = 6
    while s == 1:
        a2 = input("Enter a Letter : ").lower()
        w = ""
        if a2 in p:
            print(f"You've already guessed '{a2}'")
        for i in a1:
            if a2 == i:
                w += i
                p.append(i)
            elif i in p:
                w += i
            else:
                w += '_'

        if a2 not in a1:
            if l == 0:
                s = 0
                print(f"YOU LOSE\nCorrect Word : {a1}")
                pan = input("Press 'Y' to Play Again or 'N' to Stop : ").lower()
            else:
                l = l - 1
                print(stages[l])
                print(f"'{a2}' is not in the selected word")
                print(w)
                print(f'{l}/6 LIVES LEFT')

        if a2 in a1:
            print(stages[l])
            print(w)
            print(f'{l}/6 LIVES LEFT')


        if '_' not in w:
            print("YOU WIN")
            pan = input("Press 'Y' to Play Again or 'N' to Stop : ").lower()
            s = 0
