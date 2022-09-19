def num_combinations_for_final_score(final_score, individual_play_scores):

    num_combinations_for_score = [[1] + [0] * final_score for _ in individual_play_scores]

    for i in range(len(individual_play_scores)):
        for j in range(1, final_score + 1):
            without_this_play = (num_combinations_for_score[i-1][j] if i>=1 else 0)
            with_this_play = (num_combinations_for_score[i][j - individual_play_scores[i]] if j >= individual_play_scores[i] else 0)
            num_combinations_for_score[i][j] = (without_this_play + with_this_play)

    return num_combinations_for_score[-1][-1]

print(num_combinations_for_final_score(12, [2,3,7]))
print(num_combinations_for_final_score(12, [2,3]))
print(num_combinations_for_final_score(12, [2]))