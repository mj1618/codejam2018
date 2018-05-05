from collections import defaultdict, deque
from itertools import count
def aho_corasick():
    G = defaultdict(count(1).next)  # transitions
    W = defaultdict(set)                # alphabet
    F = defaultdict(lambda: 0)          # fallbacks
    O = defaultdict(set)                # outputs

    # automaton
    return G, W, F, O
def add_word(word, G, W, F, O):
    state = 0
    # add transitions between states
    for w in word:
        W[state].add(w)
        state = G[state, w]

    # add output
    O[state].add(word)
def build_fsa(G, W, F, O):
    # initial states
    queue = deque(G[0, w] for w in W[0])

    while queue:
        state = queue.popleft()

        # for each letter in alphabet
        for w in W[state]:
            # find fallback state
            t = F[state]
            while t and (t, w) not in G:
                t = F[t]

            # for next state define its fallback and output
            s = G[state, w]
            F[s] = G[t, w] if (t, w) in G else 0
            O[s] |= O[F[s]]

            queue.append(s)
def search(text, G, W, F, O):
    state = 0

    for i, t in enumerate(text):
        # fallback
        while state and (state, t) not in G:
            state = F[state]

        # transition
        state = G[state, t] if (state, t) in G else 0

        # output
        if O[state]:
            print('@', i, O[state])

AC = aho_corasick()
add_word('a', *AC)
add_word('b', *AC)
add_word('c', *AC)
add_word('db', *AC)
add_word('dd', *AC)
add_word('xv', *AC)

build_fsa(*AC)
print AC[0]
print AC[1]
search('abcdbddbxv', *AC)
