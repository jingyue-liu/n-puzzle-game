import sys
from collections import deque
from sets import Set
import copy
import time
import heapq
import pickle
import math
#import resource


nodes_expanded = 0
cost_of_path = 0
start_time = time.time()

	
goal_state = "0,1,2,3,4,5,6,7,8"

class Node:
	def __init__(self,state,parent,operator,depth):
		self.state = state
		self.parent = parent
		self.operator = operator
		self.depth = depth

		

def move_up(state):
	new_state = copy.deepcopy(state)
	index = state.index('0')
	index_list = []
	for i in range(size,size*size):
		index_list.append(i)
	if (index in index_list):
		temp = state[index-size]
		new_state[index-size] = '0'
		new_state[index] = temp
		#print "new_state return up"
		#print new_state
		return new_state
	else:
		return None
	
def move_down(state):
	new_state = copy.deepcopy(state)
	index = state.index('0')
	index_list = []
	for i in range(size*size-size):
		index_list.append(i)
	if (index in index_list):
		temp = state[index+size]
		new_state[index+size] = '0'
		new_state[index] = temp
		#print "new_state return down"
		#print new_state
		return new_state
	else:
		return None
	
def move_left(state):
	new_state = copy.deepcopy(state)
	index = state.index('0')
	index_list = []
	for i in range(size*size):
		if (i % size != 0):
			index_list.append(i)
	if (index in index_list):
		temp = state[index-1]
		new_state[index-1] = '0'
		new_state[index] = temp
		#print "new_state return left"
		#print new_state
		return new_state
	else:
		return None
	
def move_right(state):
	new_state = copy.deepcopy(state)
	index = state.index('0')
	index_list = []
	for i in range(size*size):
		if (i % size != size-1):
			index_list.append(i)
	if (index in index_list):
		temp = state[index+1]
		new_state[index+1] = '0'
		new_state[index] = temp
		#print "new_state return right"
		#print new_state
		return new_state
	else:
		return None
		
def create_node(state,parent,operator,depth):
	return Node(state,parent,operator,depth)

	
def node_successor(node):
	successor = []
	if (move_up(node.state) is not None):
		successor.append(create_node(move_up(node.state),node,"Up",node.depth+1))
	if (move_down(node.state) is not None):
		successor.append(create_node(move_down(node.state),node,"Down",node.depth+1))
	if (move_left(node.state) is not None):
		successor.append(create_node(move_left(node.state),node,"Left",node.depth+1))
	if (move_right(node.state) is not None):
		successor.append(create_node(move_right(node.state),node,"Right",node.depth+1))
	return successor
					

def bfs(start_state,goal_state):
	frontier = deque()
	frontier.appendleft(create_node(start_state,None,None,0))
	global max_fringe_size
	max_fringe_size = len(frontier)
	global max_search_depth
	max_search_depth = 0
	explored = Set()
	while (len(frontier)>0):
		node = frontier.pop()
		temp = node.state
		visited = ','.join(temp)
		explored.add(visited)
		if (visited ==goal_state):
			global search_depth
			search_depth = node.depth
			global fringe_size
			fringe_size = len(frontier)
			move = []
			temp2 = node
			while(1):
				move.append(temp2.operator)
				global cost_of_path
				cost_of_path += 1
				if (temp2.depth <=1):
					move = move[::-1]
					break
				temp2 = temp2.parent
			return move
		else:
			global nodes_expanded
			nodes_expanded += 1
			for node in node_successor(node):
				temp = ','.join(node.state)
				if not(temp in explored):
					frontier.appendleft(node)
					explored.add(temp)
					if (node.depth>max_search_depth):
						max_search_depth = node.depth
			if (len(frontier)>max_fringe_size):
				max_fringe_size = len(frontier)
			


def dfs(start_state,goal_state):
	frontier = []
	frontier.append(create_node(start_state,None,None,0))
	global max_fringe_size
	max_fringe_size = len(frontier)
	global max_search_depth
	max_search_depth = 0
	explored = Set()
	while (len(frontier)>0):
		node = frontier.pop()
		temp = node.state
		visited = ','.join(temp)
		explored.add(visited)
		if (visited ==goal_state):
			global search_depth
			search_depth = node.depth
			global fringe_size
			fringe_size = len(frontier)
			move = []
			temp2 = node
			while(1):
				move.append(temp2.operator)
				global cost_of_path
				cost_of_path += 1
				if (temp2.depth <=1):
					move = move[::-1]
					break
				temp2 = temp2.parent
			return move
		else:
			global nodes_expanded
			nodes_expanded += 1
			for node in reversed(node_successor(node)):
				temp = ','.join(node.state)
				if not(temp in explored):
					frontier.append(node)
					explored.add(temp)
					if (node.depth>max_search_depth):
						max_search_depth = node.depth
			if (len(frontier)>max_fringe_size):
				max_fringe_size = len(frontier)
			


def ast(start_state,goal_state):
	frontier = []
	counter = 1
	node_initial = create_node(start_state,None,None,0)
	heapq.heappush(frontier,(cost_f(node_initial),0,counter,node_initial))
	node_state = {}
	node_key = {}
	node_state[','.join(start_state)] = create_node(start_state,None,None,0)
	node_key[node_initial] = cost_f(node_initial),0,counter
	global max_fringe_size
	max_fringe_size = len(frontier)
	global max_search_depth
	max_search_depth = 0
	explored = Set()
	while (len(frontier)>0):
		node = heapq.heappop(frontier)[3]
		temp = node.state
		visited = ','.join(temp)
		node_state.pop(visited)
		node_key.pop(node)
		explored.add(visited)
		if (visited ==goal_state):
			global search_depth
			search_depth = node.depth
			global fringe_size
			fringe_size = len(frontier)
			move = []
			temp2 = node
			while(1):
				move.append(temp2.operator)
				global cost_of_path
				cost_of_path += 1
				if (temp2.depth <=1):
					move = move[::-1]
					break
				temp2 = temp2.parent
			return move
		else:
			global nodes_expanded
			nodes_expanded += 1
			for node in node_successor(node):
				temp = ','.join(node.state)
				if not(temp in explored):
					counter += 1
					if (node.operator == "Up"):
						uplr = 1
					if (node.operator == "Down"):
						uplr = 2
					if (node.operator == "Left"):
						uplr = 3
					if (node.operator == "Right"):
						uplr = 4
					heapq.heappush(frontier,(cost_f(node),uplr,counter,node))
					explored.add(temp)
					node_state[temp] = node
					node_key[node] = cost_f(node),uplr,counter
					
				elif ( temp in node_state and node_state[temp] in node_key):
					if (node_key[node_state[temp]][0],node_key[node_state[temp]][1],node_key[node_state[temp]][2],node_state[temp]) in frontier:
						index = frontier.index((node_key[node_state[temp]][0],node_key[node_state[temp]][1],node_key[node_state[temp]][2],node_state[temp]))
						counter += 1
						if (node.operator == "Up"):
							uplr = 1
						if (node.operator == "Down"):
							uplr = 2
						if (node.operator == "Left"):
							uplr = 3
						if (node.operator == "Right"):
							uplr = 4
						if (cost_f(node) < node_key[node_state[temp]][0]):
							frontier.remove(frontier[index])
							heapq.heapify(frontier)
							heapq.heappush(frontier,(cost_f(node),uplr,counter,node))
							node_state[temp] = node
							node_key[node] = cost_f(node),uplr,counter
			if (node.depth>max_search_depth):
				max_search_depth = node.depth 
			if (len(frontier)>max_fringe_size):
				max_fringe_size = len(frontier)
			

def dls(start_state,goal_state,limit,nodes_expanded,max_fringe_size,max_search_depth):
	depth_limit = limit
	frontier = []
	node_cost = {}
	start_node = create_node(start_state,None,None,0)
	frontier.append(start_node)
	node_cost[','.join(start_node.state)] = cost_f(start_node)
	max_fringe_size = len(frontier)
	max_search_depth = 0
	result = {}
	#second_cheaper = []
	while (len(frontier)>0):
		node = frontier.pop()
		temp = node.state
		visited = ','.join(temp)
		node_cost[visited] = cost_f(node)
		if (cost_f(node)> depth_limit):
			#second_cheaper.append(cost_f(node))
			continue
		if (visited ==goal_state):
			search_depth = node.depth
			fringe_size = len(frontier)
			move = []
			temp2 = node
			cost_of_path = 0
			while(1):
				move.append(temp2.operator)
				cost_of_path += 1
				if (temp2.depth <=1):
					move = move[::-1]
					break
				temp2 = temp2.parent
			result['cut_off'] = False
			result['path_to_goal'] = move
			result['cost_of_path']=cost_of_path
			result['nodes_expanded']=nodes_expanded
			result['fringe_size']=fringe_size
			result['max_fringe_size']=max_fringe_size
			result['search_depth']=search_depth
			result['max_search_depth']=max_search_depth
			return result
		else:
			nodes_expanded += 1
			for node in reversed(node_successor(node)):
				temp = ','.join(node.state)
				if cost_f(node) > limit:
					#second_cheaper.append(cost_f(node))
					continue
				else:
					if not(temp in node_cost):
						frontier.append(node)
						node_cost[temp] = cost_f(node)
					elif (cost_f(node) < node_cost[temp]):
						frontier.append(node)
						node_cost[temp] = cost_f(node)
					if (node.depth>max_search_depth):
						max_search_depth = node.depth
			if (len(frontier)>max_fringe_size):
				max_fringe_size = len(frontier)
			
	result['cut_off'] = True
	#result['second_cheaper']=second_cheaper
	result['nodes_expanded']=nodes_expanded
	result['max_fringe_size']=max_fringe_size
	result['max_search_depth']=max_search_depth
	return result
	
				
def ida (start_state,goal_state):
	limit = cost_f(create_node(start_state,None,None,0))
	global max_fringe_size
	max_fringe_size = 1
	global max_search_depth
	max_search_depth = 0
	global nodes_expanded
	nodes_expanded = 0
	global cost_of_path
	global fringe_size
	global search_depth
	while True:
		function = dls(start_state,goal_state,limit,nodes_expanded,max_fringe_size,max_search_depth)
		if function['cut_off'] == True:
			limit += 1
			#limit =min(function['second_cheaper'])
			if (function['nodes_expanded']>nodes_expanded):
				nodes_expanded=function['nodes_expanded']
			if (function['max_fringe_size']>max_fringe_size):
				max_fringe_size=function['max_fringe_size']
			if (function['max_search_depth']>max_search_depth):
				max_search_depth=function['max_search_depth']
		else:
			if (function['nodes_expanded']>nodes_expanded):
				nodes_expanded=function['nodes_expanded']
			if (function['max_fringe_size']>max_fringe_size):
				max_fringe_size=function['max_fringe_size']
			if (function['max_search_depth']>max_search_depth):
				max_search_depth=function['max_search_depth']
			cost_of_path = function['cost_of_path']
			fringe_size = function['fringe_size']
			search_depth = function['search_depth']
			return function['path_to_goal']
				
				
def cost_f(node):
	h = 0
	g = node.depth	
	board = []
	for i in range(size):
		board.append([])
	i = 0
	for row in range(size):
		for col in range(size):
			board[row].append(node.state[i])
			i +=1
	for ele in range(1,size*size):
		goal_index = index_2d(goal_state_2d,ele)
		board_index = index_2d(board,str(ele))
		h += abs(goal_index[0]-board_index[0])+abs(goal_index[1]-board_index[1])
	f = g + h
	return f
	
	
def index_2d(list,ele):
	for i,j in enumerate(list):
		if ele in j:
			return [i,j.index(ele)]
	
				
			
def main():
	data = sys.argv[2];
	start_state = data.split(",")
	size_sq = len(start_state)
	global size
	size = int(math.sqrt(size_sq))
	global goal_state_2d
	goal_state_2d = []
	for i in range(size):
		goal_state_2d.append([])
	i=0
	for j in range(size):
		for k in range(size):
			goal_state_2d[j].append(i)
			i+=1	
	global goal_state
	start_goal = ""
	for i in range(size*size-1):
		start_goal = start_goal+str(i)+","
	goal_state = start_goal + str(size*size-1)
	if (sys.argv[1]=="bfs"):
		result = bfs(start_state,goal_state)
	if (sys.argv[1]=="dfs"):
		result = dfs(start_state,goal_state)
	if (sys.argv[1]=="ast"):
		result = ast(start_state,goal_state)
	if (sys.argv[1]=="ida"):
		result = ida(start_state,goal_state)
	
	#max_ram_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
	#max_ram_usage = max_ram_usage/1000
	#max_ram_usage = "%.8f" % max_ram_usage 
	running_time = time.time() - start_time
	running_time = "%.8f" % running_time
	print "path_to_goal:", 
	print result
	print "cost_of_path:",
	print cost_of_path
	print "nodes_expanded:",
	print nodes_expanded
	print "fringe_size:",
	print fringe_size
	print "max_fringe_size:",
	print max_fringe_size
	print "search_depth:",
	print search_depth
	print "max_search_depth:",
	print max_search_depth
	print "running_time:",
	print running_time
	#print "max_ram_usage:",
	#print max_ram_usage
	file = open("output.txt","w")
	file.write("path_to_goal: "),
	file.write(str(result)+'\n')
	file.write("cost_of_path: "),
	file.write(str(cost_of_path)+'\n')
	file.write("nodes_expanded: "),
	file.write(str(nodes_expanded)+'\n')
	file.write("fringe_size: "),
	file.write(str(fringe_size)+'\n')
	file.write("max_fringe_size: "),
	file.write(str(max_fringe_size)+'\n')
	file.write("search_depth: "),
	file.write(str(search_depth)+'\n')
	file.write("max_search_depth: "),
	file.write(str(max_search_depth)+'\n')
	file.write("running_time: "),
	file.write(running_time+'\n')
	#file.write("max_ram_usage: "),
	#file.write(max_ram_usage+'\n')
	
	
if __name__ =="__main__":
	main()
		
	
	
