import collections

MatchResult = collections.namedtuple('MatchResult', ('winning_team', 'losing_team'))

def can_team_a_beat_team_b(matches, team_a, team_b):
    def build_graph():
        graph = collections.defaultdict(set)
        for match in matches:
            graph[match.winning_team].add(match.losing_team)
        return graph

    def is_reachable_dfs(graph, curr, dest, visited=set()):
        if curr == dest:
            return True
        elif curr in visited or curr not in graph:
            return False
        visited.add(curr)
        return any(is_reachable_dfs(graph, team, dest) for team in graph[curr])

    return is_reachable_dfs(build_graph(), team_a, team_b)

match1 = MatchResult('B', 'D')
match2 = MatchResult('B', 'C')
match3 = MatchResult('C', 'A')
match4 = MatchResult('D', 'B')
matches = [match1, match2, match3, match4]

print(can_team_a_beat_team_b(matches, 'C', 'D'))
print(can_team_a_beat_team_b(matches, 'A', 'B'))
print(can_team_a_beat_team_b(matches, 'D', 'B'))
print(can_team_a_beat_team_b(matches, 'B', 'C'))
print(can_team_a_beat_team_b(matches, 'C', 'B'))