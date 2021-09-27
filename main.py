'''
'''

class DFA:

    def __init__(self, states: list, initial: str, accepting: list, alphabet: list, transitions: list) -> None:
        self.states = states
        self.initial = initial
        self.accepting = accepting
        self.alphabet = alphabet
        self.transitions = transitions


def main():

    with open("input.txt") as file:
        print(file.readlines())