import random
import re
from word2number import w2n

class MSDie:
    """
    Multi-sided die

    Instance variables:
        current_value
        num_sides

    """

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self):
        self.current_value = random.randrange(1, self.num_sides+1)
        return self.current_value

    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        return "MSDie({}) : {}".format(self.num_sides, self.current_value)

    def multi_roll(self, rolls):
        roll_values = {i: 0 for i in range(1, self.num_sides+1)}
        for _ in range(rolls):
            roll_values[self.roll()] += 1
        return roll_values


def text_to_numbers(string):
    """
    Converts input text into numbers.
    """
    result = []
    # Split string at each text digit
    str_split = string.split('  ')
    for sub_str in str_split:
        word_char_search = re.search('[^a-zA-Z ]', sub_str)
        if word_char_search is None:
            number = str(w2n.word_to_num(sub_str))
            result.append(number)
        else:
            result.append(sub_str)
    return ' '.join(result)


def help_info():
    print('MSDie Usage:\nTo roll a die of n sides enter the desired value of n.\ne.g. > 5\n'
          'To re-roll the previously given die enter \'roll\' or \'r\'.\ne.g. > roll\nTo roll '
          'a die of n sides x number of times enter \'multi roll\' or \'m r\' followed by n '
          'then x.The result will be given as a dictionary of the occurrences of each side of the '
          'die.\ne.g. > m r \n> 5 \n> 10. \nInput format: \nInteger number of sides must be '
          'expressed in numerical or alphabetical format but the latter format must be separated '
          'with a single space.\ne.g. > sixty eight. \nTo exit the MSDie: `exit`, `quit` or '
          '`close`.')


def main():
    print("Welcome to MSDie, for help enter: `help` or `?`")
    user_input = ""
    while user_input not in ["exit", "quit", "close"]:
        user_input = input("> ")
        if user_input.lower() in ["help", "?"]:
            help_info()
        elif user_input in ["exit", "quit", "close"]:
            break
        elif user_input in ["roll", "r"]:
            try:
                print(my_die.roll())
            except:
                print("Error: please enter number of sides")
        elif user_input in ["multiple rolls", "m r"]:
            die_sides = input("    > ")
            roll_number = input("    > ")
            my_die = MSDie(int(text_to_numbers(die_sides)))
            print(my_die.multi_roll(int(text_to_numbers(roll_number))))
        else:
            number_input = text_to_numbers(user_input)
            my_die = MSDie(int(number_input))
            print(my_die)
    print("Exiting MSDie...")


if __name__ == '__main__':
    main()
