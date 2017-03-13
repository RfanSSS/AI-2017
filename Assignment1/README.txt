How to run the maze agent with different searching methods:

1. Depth First Search:
	tinyMaze:   python pacman.py -l tinyMaze -p SearchAgent
	mediumMaze: python pacman.py -l mediumMaze -p SearchAgent
	bigMaze:    python pacman.py -l bigMaze -z .5 -p SearchAgent
	openMaze:   python pacman.py -l openMaze -z .5 -p SearchAgent
	(Note: Since this code used recursion method on DFS, the search behavior may different from the code using stack for DFS)

2. Breadthfist First Search:
	tinyMaze:   python pacman.py -l tinyMaze -p SearchAgent -a fn=bfs
	mediumMaze: python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
	bigMaze:    python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
	openMaze:   python pacman.py -l openMaze -p SearchAgent -a fn=bfs

3.Iterative Deepening Search:
	tinyMaze:   python pacman.py -l tinyMaze -p SearchAgent -a fn=iterativeDeepeningSearch
	mediumMaze: python pacman.py -l mediumMaze -p SearchAgent -a fn=iterativeDeepeningSearch
	bigMaze:    python pacman.py -l bigMaze -p SearchAgent -a fn=iterativeDeepeningSearch -z .5
	openMaze:   python pacman.py -l openMaze -p SearchAgent -a fn=iterativeDeepeningSearch

4.Uniform Cost Search:
	mediumMaze:       python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
	mediumDottedMaze: python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
	mediumScaryMaze:  python pacman.py -l mediumScaryMaze -p StayWestSearchAgent

5. Cost Function Changed:
	In tinyMaze, mediumMaze, bigMaze, dottedMaze: please first COMMENT out the original code between Line 198 and Line 205 in "searchAgents.py" and UNCOMMENT the Line 207 to Line 220 in "searchAgents.py" to run a search the Uniform Cost Search in a changed environment. (Here we changed the cost of moving North and East to 2 and the cost of moving Sounth and West to 0.5)
	To run the maze:
		tinyMaze:         python pacman.py -l tinyMaze -p SearchAgent -a fn=ucs
		mediumMaze:       python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
		bigMaze:          python pacman.py -l bigMaze -p SearchAgent -a fn=ucs
		mediumDottedMaze: python pacman.py -l mediumDottedMaze -p SearchAgent -a fn=ucs

	In Medium Scary Maze: please first COMMENT out the original code between Line 198 and Line 205 in "searchAgents.py" and then UNCOMMENT the Line 221 to Line 236 to make the pacman run away from the ghost, where we made the cost of moving West and South much cheaper than move to other directions
	To run the maze:
		mediumScaryMaze:  python pacman.py -l mediumScaryMaze -p SearchAgent -a fn=ucs

6. A* Search:
	tinyMaze:   python pacman.py -l tinyMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
	mediumMaze: python pacman.py -l mediumMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
	bigMaze:    python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
	openMaze:   python pacman.py -l openMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic


	
		
