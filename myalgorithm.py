import itertools
import random


class Enigma(object):
    def __init__(self, plugboard, rotor, reflector, offset1=0, offset2=0, offset3=0):
        self.plugboard_dict = {"forward": plugboard, "backward": {v: k for k, v in plugboard.items()}}
        # self.plugboard_backward = {v: k for k, v in plugboard.items()}
        self.rotor1_dict = {"forward": rotor[0], "backward": {v: k for k, v in rotor[0].items()}}
        # self.rotor1_backward = {v: k for k, v in rotor1.items()}
        self.rotor2_dict = {"forward": rotor[1], "backward": {v: k for k, v in rotor[1].items()}}
        # self.rotor2_backward = {v: k for k, v in rotor2.items()}
        self.rotor3_dict = {"forward": rotor[2], "backward": {v: k for k, v in rotor[2].items()}}
        #  self.rotor3_backward = {v: k for k, v in rotor3.items()}
        self.reflector_dict = reflector
        self.init_offset1 = offset1
        self.init_offset2 = offset2
        self.init_offset3 = offset3

        # self.offset1 = offset1
        #  self.offset2 = offset2
        #  self.offset3 = offset3
        self.max_offset = len(self.plugboard_dict["forward"]) - 1
        # self.reflector_backward = {v: k for k, v in reflector.items()}

    def plugboard(self, direction, char):
        return self.plugboard_dict[direction][char]

        # self.plugboard_forward = {'A': 'B', 'B': 'A', 'C': 'D', 'D': 'C'}
        #  self.plugboard_backward = {'A': 'B', 'B': 'A', 'C': 'D', 'D': 'C'}

    def rotor1(self, direction, char):
        if ord(char) - self.offset1 < ord('A'):
            char = chr(ord(char) + self.max_offset + 1)
        char = chr(ord(char) - self.offset1)

        char = self.rotor1_dict[direction][char]

        if ord(char) + self.offset1 > ord('A') + self.max_offset:
            char = chr(ord(char) - self.max_offset - 1)
        char = chr(ord(char) + self.offset1)
        return char
        # return self.rotor1[direction][chr(ord(char) - offset)]
        # self.rotor1_forward = {'A': 'D', 'B': 'C', 'C': 'B', 'D': 'A'}
        #  self.rotor1_backward = {'D': 'A', 'C': 'B', 'B': 'C', 'A': 'D'}

    def rotor2(self, direction, char):  # a b c d a b c d
        if ord(char) - self.offset2 < ord('A'):
            char = chr(ord(char) + self.max_offset + 1)
        char = chr(ord(char) - self.offset2)

        char = self.rotor2_dict[direction][char]

        if ord(char) + self.offset2 > ord('A') + self.max_offset:
            char = chr(ord(char) - self.max_offset - 1)
        char = chr(ord(char) + self.offset2)
        return char

    #        char = chr(ord(char) - self.offset2)
    #       char = self.rotor2_dict[direction][char]
    #      char = chr(ord(char) + self.offset2)

    # self.rotor2_forward = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'A'}
    #  self.rotor2_backward = {'B': 'A', 'C': 'B', 'D': 'C', 'A': 'D'}

    def rotor3(self, direction, char):
        if ord(char) - self.offset3 < ord('A'):
            char = chr(ord(char) + self.max_offset + 1)
        char = chr(ord(char) - self.offset3)

        char = self.rotor3_dict[direction][char]

        if ord(char) + self.offset3 > ord('A') + self.max_offset:
            char = chr(ord(char) - self.max_offset - 1)
        char = chr(ord(char) + self.offset3)
        return char

    # self.rotor3_forward = {'D': 'A', 'A': 'C', 'B': 'D', 'C': 'B'}
    #  self.rotor3_backward = {'A': 'D', 'C': 'A', 'D': 'B', 'B': 'C'}
    def reflector(self, char):
        return self.reflector_dict[char]

    def add_offset(self):
        self.offset1 += 1
        if self.offset1 > self.max_offset:
            self.offset1 = 0
            self.offset2 += 1
            if self.offset2 > self.max_offset:
                self.offset2 = 0
                self.offset3 += 1
                if self.offset3 > self.max_offset:
                    self.offset3 = 0

    def coder(self, str):
        answer = []
        self.offset1 = self.init_offset1
        self.offset2 = self.init_offset2
        self.offset3 = self.init_offset3
        for char in list(str):
            char = self.plugboard("forward", char)
            char = self.rotor1("forward", char)
            char = self.rotor2("forward", char)
            char = self.rotor3("forward", char)
            char = self.reflector(char)
            char = self.rotor3("backward", char)
            char = self.rotor2("backward", char)
            char = self.rotor1("backward", char)
            char = self.plugboard("backward", char)
            answer.append(char)
            self.add_offset()
            # print(self.offset1, self.offset2, self.offset3)
        return "".join(answer)


if __name__ == '__main__':
    # s = string.ascii_uppercase
    s = 'ABCDEF'
    s_list = list(s)
    plugboard_list = random.sample(s, len(s))
    rotor1_list = random.sample(s, len(s))
    rotor2_list = random.sample(s, len(s))
    rotor3_list = random.sample(s, len(s))
    reflector_list = random.sample(s, len(s))
    plugboard = dict(zip(s_list, plugboard_list))
    rotor1 = dict(zip(s_list, rotor1_list))
    rotor2 = dict(zip(s_list, rotor2_list))
    rotor3 = dict(zip(s_list, rotor3_list))
    rotor = [rotor1, rotor2, rotor3]
    # reflector = dict(zip(s_list, reflector_list))
    # plugboard = {'A': 'B',
    #              'B': 'C',
    #              'C': 'D',
    #              'D': 'E',
    #              'E': 'F',
    #              'F': 'A'}
    # plugboard = {'A': 'B', 'B': 'A', 'C': 'D', 'D': 'C', 'E': 'E'}
    # rotor1 = {'A': 'D', 'B': 'C', 'C': 'B', 'D': 'A', 'E': 'E'}
    # rotor2 = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'A', 'E': 'E'}
    # rotor3 = {'D': 'A', 'A': 'C', 'B': 'D', 'C': 'B', 'E': 'E'}
    # rotor = [rotor1, rotor2, rotor3]
    print(list(itertools.combinations(s_list, 2)))
    reflector = {'A': 'B', 'B': 'A', 'C': 'D', 'D': 'C', 'E': 'F', 'F': 'E'}  # should be a pair combination
    enigma = Enigma(plugboard, rotor, reflector)  # , offset1, offset2, offset3)
    str1 = 'ABCDEF'
    str2 = enigma.coder(str1)
    print('hello world')
    print(str1)
    print('encode with enigma')
    print(str2)
    print('decode with enigma')
    str3 = enigma.coder(str2)
    print(str3)
