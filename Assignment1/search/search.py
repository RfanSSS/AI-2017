# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    def depthFirstSearch_helper(problem, current_state, move_list, visited):
        # check if current state is the goal state
        if problem.isGoalState(current_state):
            return move_list
        next_move = problem.getSuccessors(current_state)
        for moves in next_move:
            (next_state, direction, cost) = moves
            if not visited.has_key(next_state):
                visited[next_state] = 1
                move_list.append(direction)
                final_list = depthFirstSearch_helper(problem, next_state, move_list, visited)
                if final_list:
                    return final_list
                move_list.pop()
        return
    start_state = problem.getStartState()
    move_list = []
    visited_record = {}
    visited_record[start_state] = 1
    return depthFirstSearch_helper(problem, start_state, move_list, visited_record)  

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    breadthFirstTree = util.Queue()
    if problem.isGoalState(problem.getStartState()):
        return []
    breadthFirstTree.push(problem.getStartState())

    visited = {}
    visited[problem.getStartState()] = [0,0]

    final_action = []

    while not breadthFirstTree.isEmpty():
        currentState = breadthFirstTree.pop()
        #if is goal state, find parent action up to the startSate, return final action
        if problem.isGoalState(currentState):
            while visited[currentState][0] != 0:
                final_action.append(visited[currentState][1])
                currentState = visited[currentState][0]
            
            final_action.reverse()
            return final_action
        #if not goal state, find its successor, push into stack, add to visited[]
        moves = problem.getSuccessors(currentState)
        for move in moves:
            nextState, action, cost = move
            if nextState not in visited:
                breadthFirstTree.push(nextState)
                visited[nextState] = [currentState, action]

    #if no result, return null
    return

def iterativeDeepeningSearch(problem):
    def deepLimitedSearch(problem, max_depth):
        from util import Stack
        stack = Stack()
        node_visited = {}
        start_state = problem.getStartState()
        stack.push((start_state, 0))
        node_visited[start_state] = (0, 0)
        while not stack.isEmpty():
            current_state, depth = stack.pop()
            if problem.isGoalState(current_state):
                move_list = []
                temp = current_state
                start_state = problem.getStartState()
                while temp != start_state:
                    (state, direction) = node_visited[temp]
                    temp = state
                    move_list.append(direction)
                move_list.reverse()
                return move_list
            elif depth < max_depth:
                next_move = problem.getSuccessors(current_state)
                for moves in next_move:
                    (next_state, direction, cost) = moves
                    if not node_visited.has_key(next_state):
                        node_visited[next_state] = (current_state, direction)
                        stack.push((next_state, depth+1))
            #else:
        return
    move_list = None
    max_depth = 0
    while not move_list:
        move_list = deepLimitedSearch(problem, max_depth)
        max_depth += 1
    return move_list


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    ucsTree = util.PriorityQueue()
    if problem.isGoalState(problem.getStartState()):
        return []
    ucsTree.push((problem.getStartState(), 0), 0)

    visited = {}
    visited[problem.getStartState()] = [0,0]

    final_action = []

    while not ucsTree.isEmpty():
        currentState, cost = ucsTree.pop()
        #if is goal state, find parent action up to the startSate, return final action
        if problem.isGoalState(currentState):
            while visited[currentState][0] != 0:
                final_action.append(visited[currentState][1])
                currentState = visited[currentState][0]
            
            final_action.reverse()
            return final_action
        #if not goal state, find its successor, push into stack, add to visited[]
        moves = problem.getSuccessors(currentState)
        for move in moves:
            nextState, action, move_cost = move
            if nextState not in visited:
                ucsTree.push((nextState, cost+move_cost), cost+move_cost)
                visited[nextState] = [currentState, action]

    #if no result, return null
    return
    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # import the PriorityQueue Data Structure
    from util import PriorityQueue
    nodes = PriorityQueue()
    node_visited = {}
    start_state = problem.getStartState()
    gross_cost = 0 + heuristic(start_state, problem)
    nodes.push((start_state, 0, gross_cost), gross_cost)
    while not nodes.isEmpty():
        (current_state, former_cost, gross_cost) = nodes.pop()
        if problem.isGoalState(current_state):
            temp = current_state
            move_list = []
            while temp != start_state:
                (state, direction) = node_visited[temp]
                temp = state
                move_list.append(direction)
            move_list.reverse()
            return move_list
        next_move = problem.getSuccessors(current_state)
        for moves in next_move:
            (next_state, direction, cost) = moves
            if not node_visited.has_key(next_state):
                node_visited[next_state] = (current_state, direction)
                # push the node into the PriorityQueue
                gross_cost = former_cost + cost + heuristic(next_state, problem)
                nodes.push((next_state, (former_cost + cost), gross_cost), gross_cost) 

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
