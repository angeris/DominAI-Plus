#!/usr/bin/env python
import random

NUM_PLAYERS = 4

def get_all_dominoes():
    dominoes = []
    for i in range(7):
        for j in range(i, 7):
            dominoes.append((i, j))
    return dominoes

def new_state():
    board = []
    allDominoes = get_all_dominoes()
    random.shuffle(allDominoes)
    hands = [[]] * NUM_PLAYERS
    for i in range(len(allDominoes)):
        hands[i%NUM_PLAYERS].append(allDominoes[i])
    return board, hands

def play_game(players):
    board, hands = new_state()

    turn = 0
    t = turn % NUM_PLAYERS
    while not is_game_over(board, hands):
        newPartialStates = generate_moves(board, hands[t])

        bestPartialState, bestScore = max(
            map(lambda state: (state, players[t].evaluate(state[0], state[1])),
                newPartialStates),
            key=lambda x: x[1])

        board, hands[t] = bestPartialState

        turn += 1
        t = turn % NUM_PLAYERS

    for i in range(NUM_PLAYERS):
        players[i].show_score(board, hands[i], get_final_score(board, hands))
