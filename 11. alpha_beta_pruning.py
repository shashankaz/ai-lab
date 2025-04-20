def alpha_beta_pruning(depth, node_index, maximizing_player, values, alpha, beta, max_depth):
    if depth == max_depth:
        return values[node_index]

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(2):  # Left and right child
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta, max_depth)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Prune
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(2):  # Left and right child
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta, max_depth)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Prune
        return min_eval
