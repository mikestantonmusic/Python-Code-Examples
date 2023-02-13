def main():
    print('Welcome to the random chord generator 9000. Please enter the number of chords you wish to generate. \n'
    'Please note that this program needs to be open using python or it may not work')
    try:
        length = int(input("number of chords: "))
    except (ValueError):
        print('You got an error, probably because the entered value must be an integer!')
    import random
    list1 =['A','Ab','B','Bb','C','D','Db','E','Eb','F','G','Gb']
    list2 =['Maj7','min7','min7b5','7']
    for _ in range(length):
        print(random.choice(list1),random.choice(list2))

if __name__ == "__main__":
    main()
