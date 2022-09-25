# The number of goals that are achieved by two football teams in matches in a league is given in the form of two lists. For each match of team B,
# we should compute the total number of matches of team A where team A has scored less than or equal to the number of goals scored by team B in that match. 
# Ex: teamA = [1, 2, 3]
# Ex: teamB = [2, 4]
# For the 2 goals scored by team B in the first match, team A has 2 matches with scores 1 and 2. 
# For the 4 goals scored by team B in the second match, team A has 3 matches with scores 1, 2 and 3.

# The naive solution is to iterate over all of the elements in team A and B for a total of O(m * n)

# Smarter solution that requires us to sort team A, and subsequently use a binary search
def counts(teamA : List[int], teamB : List[int]) -> List[int]:
    """
    Input: Number of goals achieved by teamA in various matches as an integer list.
    The number of goals achieved by teamB in various matches as an integer list
    """
    ans = []
    teamA.sort()
    for score in teamB:
      low, high = 0, len(teamA) - 1
      while low <= high:
        mid = low + high) // 2
        if teamA[mid] > score:
          high = mid - 1
        else:
          low = mid + 1
      answer.append(low)
    return answer 
