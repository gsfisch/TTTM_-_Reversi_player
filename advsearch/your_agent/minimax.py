from typing import Tuple, Callable
import math


def minimax_move(state, max_depth: int, eval_func: Callable) -> Tuple[int, int]:
    """
    Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
    :param state: state to make the move (instance of GameState)
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    best_move = None
    best_score = -math.inf

    legal_moves = state.legal_moves()

    print(legal_moves)

    for move in legal_moves:
        new_state = state.next_state(move)
        score = minimax_alpha_beta(new_state, max_depth, -math.inf, math.inf, "W", eval_func)
        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def minimax_alpha_beta(state, depth, alpha, beta, player, eval_func):
    if depth == 0 or state.is_terminal:
        return eval_func(state, player)

    if player == "W":
        max_eval = -math.inf

        legal_moves = state.legal_moves()

        for move in legal_moves:
            new_state = state.next_state(move)
            evaluation = minimax_alpha_beta(new_state, depth - 1, alpha, beta, "B", eval_func)
            max_eval = max(max_eval, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf

        legal_moves = state.legal_moves()

        for move in legal_moves:
            new_state = state.next_state(move)
            evaluation = minimax_alpha_beta(new_state, depth - 1, alpha, beta, "W", eval_func)
            min_eval = min(min_eval, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        return min_eval
