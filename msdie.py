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

    def multi_roll(self, rolls):
        values = []
        for _ in range(rolls):
            values.append(self.roll())
        return values


    def text_to_numbers(self, string):
        """
        Converts input text into numbers.
        """
        result = []
        # Split string at each text number
        str_split = string.split('  ')
        # If no text numbers return original string and not a single number
        if len(str_split) == 1:
            try:
                w2n.word_to_num(str_split)
            except:
                return string
        # Replace text numbers with digits
        else:
            for sub_str in str_split:
                word_char_search = re.search('[^a-zA-Z ]', sub_str)
                if word_char_search is None:
                    number = str(w2n.word_to_num(sub_str))
                    result.append(number)
                else:
                    result.append(sub_str)
        return ' '.join(result)


def help_info():
    print('Need to rewrite - RPN calculator usage:\nInput: Expression in Reverse Polish Notation containing whole '
          'numbers (0-999,999,999,999) and operators separated by a single space. The following '
          'operators are supported: addition (`+`), subtraction (`-`), multiplication (`*`), integer'
          ' division (`/`), and modulo (`%`).\ne.g. > 6 11 +\nNumbers can be expressed in numerical '
          'or alphabetical format but the latter format must be separated with two spaces.\ne.g. > '
          'six  eleven  +\nOutput: Whole number solution to expression.\nTo exit the calculator: '
          '`exit`, `quit` or `close`.')


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
        elif user_input in ["multiple rolls", "rolls", "m rolls", "m r"]:
            die_sides = input("    > ")
            roll_number = input("    > ")
            my_die = MSDie(int(die_sides))
            print(my_die.multi_roll(int(roll_number)))
        else:
            # number_input = MSDie.text_to_numbers(user_input)
            my_die = MSDie(int(user_input))
            print(my_die.current_value)
    print("Exiting MSDie...")


if __name__ == '__main__':
    main()
