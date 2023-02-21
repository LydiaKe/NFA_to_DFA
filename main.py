"""
some example test cases:
test case 1
t = (q0, a, q0), (q0, b, q0), (q0, a, q1), (q1, b, q2)
i = q0
f = q2
test case 2
t = (q0, 0, q0), (q0, 1, q1), (q1, 0, q1), (q1, 1, q1), (q1, 0, q2),(q2, 0, q2), (q2, 1, q2), (q2, 1, q1)
i = q0
f = q2
test case 3
t = (q0, 0, q0), (q0, 0, q1), (q0, 1, q1), (q1, 1, q1), (q1, 1, q0)
i = q0
f = q1
"""
# add readme and comment
# trash node
from FA import FA, NFA, DFA
from NFA_to_DFA import  NFA_to_DFA


relation = input("Please input the relation:\n")
initial = input("Please input the initial state:\n")
final = input("Please input the final state:\n")

relation = relation.split(",")
table = []
for r in range(0, len(relation), 3):
    relation[r] = relation[r].replace("(", "").strip()
    relation[r + 1] = relation[r + 1].strip()
    relation[r + 2] = relation[r + 2].replace(")", "").strip()
    table.append((relation[r], relation[r + 1], relation[r + 2]))

final = final.split(",")

nfa = NFA(t=table, i=initial, f=final)
nfa.init_nfa()

dfa = NFA_to_DFA(nfa)

dfa.init_dfa()

print("The transitive function of the DFA:", dfa.dict)
print("The final state(s):", dfa.final_state)
