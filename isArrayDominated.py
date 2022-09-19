#Static method usage - when you need a utility function that doesn't access any properties of the class,
#but makes sense that it belongs to the class

#Zip - a dictionary of tuples

#all - checks if all elements in the list are True

import collections
class Team:
    Player = collections.namedtuple('Player', ('height'))

    def __init__(self, height):
        self._players = [Team.Player(h) for h in height]

    #Checks if team0 can be placed in fromt of team1
    @staticmethod
    def valid_placement_exists(team0, team1):
        return all(a<b for a,b in zip(sorted(team0._players), sorted(team1._players)))

teamA = Team([1,2,3,5,1])
teamB = Team([2,3,4,5,2])
print(teamA.valid_placement_exists(teamA, teamB))
print(teamA.valid_placement_exists(teamB, teamA))