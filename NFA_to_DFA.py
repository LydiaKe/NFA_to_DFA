from FA import FA, NFA, DFA
import random

# input: a nfa
# return: a dfa
def NFA_to_DFA(nfa):
    state = []
    dic = {}
    com_state = []
    com_dic = {}
    state.append(nfa.initial_state)
    # add initial_state to DFA
    dic[nfa.initial_state] = dict.fromkeys(nfa.alphabet)
    for a in nfa.alphabet:
        if len(nfa.dict[nfa.initial_state][a]) == 1:
            if nfa.dict[nfa.initial_state][a][0] not in state:
                state.append(nfa.dict[nfa.initial_state][a][0])
                dic[nfa.initial_state][a] = nfa.dict[nfa.initial_state][a][0]
            else:
                dic[nfa.initial_state][a] = nfa.dict[nfa.initial_state][a][0]
        elif len(nfa.dict[nfa.initial_state][a]) > 1:
            if set(nfa.dict[nfa.initial_state][a]) not in com_state:
                new_state = " ".join(nfa.dict[nfa.initial_state][a])
                dic[nfa.initial_state][a] = new_state
                state.append(new_state)
                com_state.append(set(nfa.dict[nfa.initial_state][a]))
                com_dic[len(com_state) - 1] = len(state) - 1
            else:
                dic[nfa.initial_state][a] = state[com_dic[com_state.index(set(nfa.dict[nfa.initial_state][a]))]]
    # if any new state is present in the transition table, add transitions of that state in the transition table
    while set(state) - set(dic.keys()) != set():
        add_state = (set(state) - set(dic.keys())).pop()
        dic[add_state] = dict.fromkeys(nfa.alphabet)
        if add_state in nfa.state:
            for a in nfa.alphabet:
                if len(nfa.dict[add_state][a]) == 1:
                    if nfa.dict[add_state][a][0] not in state:
                        state.append(nfa.dict[add_state][a][0])
                        dic[add_state][a] = nfa.dict[add_state][a][0]
                    else:
                        dic[add_state][a] = nfa.dict[add_state][a][0]
                elif len(nfa.dict[add_state][a]) > 1:
                    if set(nfa.dict[add_state][a]) not in com_state:
                        new_state = " ".join(nfa.dict[add_state][a])
                        dic[add_state][a] = new_state
                        state.append(new_state)
                        com_state.append(set(nfa.dict[add_state][a]))
                        com_dic[len(com_state) - 1] = len(state) - 1
                    else:
                        dic[add_state][a] = state[com_dic[com_state.index(set(nfa.dict[add_state][a]))]]
        else:
            for a in nfa.alphabet:
                in_state = add_state.split(" ")
                out_state = set()
                for s in in_state:
                    out_state = out_state | set(nfa.dict[s][a])
                if len(out_state) == 1:
                    if list(out_state)[0] not in state:
                        state.append(list(out_state)[0])
                        dic[add_state][a] = list(out_state)[0]
                    else:
                        dic[add_state][a] = list(out_state)[0]
                elif len(out_state) > 1:
                    if out_state not in com_state:
                        new_state = " ".join(out_state)
                        dic[add_state][a] = new_state
                        state.append(new_state)
                        com_state.append(set(out_state))
                        com_dic[len(com_state) - 1] = len(state) - 1
                    else:
                        dic[add_state][a] = state[com_dic[com_state.index(set(out_state))]]

    # find all the final states
    final = []
    for s in state:
        if s in nfa.final_state:
            final.append(s)
            continue
        l = set(s.split(" "))
        if l & set(nfa.final_state) != set():
            final.append(state[com_dic[com_state.index(l)]])

    # create a trash node
    trash = "t" + str(random.randint(100,1000))
    while trash in state:
        trash = "t" + str(random.randint(100, 1000))
    # if the next state for a (state,alphabet) pair is 'None', assign the trash node to this pair.
    flag = True
    for s in state:
        for a in nfa.alphabet:
            if dic[s][a] is None:
                if flag:
                    dic[s][a] = trash
                    state.append(trash)
                    dic[trash] = dict.fromkeys(nfa.alphabet)
                    flag = False
                else:
                    dic[s][a] = trash

    dfa = DFA(i=nfa.initial_state, f=final, a=nfa.alphabet, s=state, d=dic)
    return dfa

