class FA:
    transition_table = []
    initial_state = "p"
    final_state = []
    alphabet = []
    state = []
    dict = {}

    def __init__(self, t, i, f, a, s, d):
        self.transition_table = t
        self.initial_state = i
        self.final_state = f
        self.alphabet = a
        self.state = s
        self.dict = d

    def print_fa(self):
        print(self.transition_table, self.initial_state, self.final_state, self.alphabet, self.state, self.dict)

    def set_alphabet(self):
        for r in self.transition_table:
            if r[1] not in self.alphabet:
                self.alphabet.append(r[1])

    def set_state(self):
        for r in self.transition_table:
            if r[0] not in self.state:
                self.state.append(r[0])
            if r[2] not in self.state:
                self.state.append(r[2])

    def set_dict(self):
        """[all states] * [all alphabet]"""
        self.dict = dict.fromkeys(self.state)
        for s in self.state:
            self.dict[s] = dict.fromkeys(self.alphabet)
            for a in self.alphabet:
                self.dict[s][a] = []
        """transition_table to dictionary"""
        for r in self.transition_table:
            self.dict[r[0]][r[1]].append(r[2])

    def set_table(self):
        self.transition_table = []
        for s in self.state:
            for a in self.alphabet:
                self.transition_table.append((s, a, self.dict[s][a]))


class NFA(FA):
    def __init__(self, t, i, f):
        self.transition_table = t
        self.initial_state = i
        self.final_state = f

    def init_nfa(self):
        FA.set_alphabet(self)
        FA.set_state(self)
        FA.set_dict(self)
        # FA.print_fa(self)


class DFA(FA):
    def __init__(self, i, f, a, s, d):
        self.initial_state = i
        self.final_state = f
        self.alphabet = a
        self.state = s
        self.dict = d

    def init_dfa(self):
        FA.set_table(self)
        # FA.print_fa(self)

