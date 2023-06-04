import json
visited=[]
def input1():
	fp=open('graph.txt','r')
	graph1=fp.read()
	graph2=json.loads(graph1)
	print(graph2)
	return graph2

def DFS(node,graph):
	visited.append(node)
	for child in graph[node]:
		if child not in visited:
			DFS(child,graph)
	return visited

def BFS(node,visitedgraph):
	visited=[]
	queue=[]
	visited.append(node)
	queue.append(node)
	while queue:
		m=queue.pop(0)
		for child in graph[m]:
			if child not in visited:
				visited.append(child)
				queue.append(child)
	return visited
def clearVisited(visited):
	while True:
		visited.pop()

def menu():
	flag=True
	while(flag):
		print("1.DFS 2.BFS 3.Exit")
		choice=input("Enter Your choice:\n")
		node=input("Enter the starting node:\n")
		if choice=="1":
			print("DFS of Graph is:",DFS(node,graph))
		elif choice=="2":
			print("BFS of graph",BFS(node,graph))
		elif choice=="3":
			flag=False

graph=input1()
menu()