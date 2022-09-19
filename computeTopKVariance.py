import collections
import heapq
import functools

def compute_top_k_variance(students, scores, k):
    all_scores = collections.defaultdict(list)
    for student, score in zip(students, scores):
        all_scores[student].append(score)

    top_k_scores = {student : heapq.nlargest(k, scores) for student, scores in all_scores.items() if len(scores) >= k}

    return {student : functools.reduce(lambda variance, score: variance + (score - mean) ** 2, scores, 0) for student, scores, mean in (student, scores, sum(scores)/k) for student, scores in top_k_scores.items()}

compute_top_k_variance(['Jessie', 'Jane', 'Team Rocket', 'Pikachu', 'Charlizard'], [100.0, 210.0, 130.12, 401.56, 502.79], 1)