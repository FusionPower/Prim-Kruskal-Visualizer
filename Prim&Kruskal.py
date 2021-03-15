# -*- coding: utf-8 -*-

import pygame
import heapq as pq
import random

def explore(u,vis,adj,q):
    
    for v,w in adj[u]:
        if not vis[v]:
            pq.heappush(q,[w,u,v])

    
def prim(adj,return_edj=0):
    
    tree=[[] for i in range(len(adj))]
    tree_edj=[]
    
    if not adj:
        return -1
    for u in adj:
        if not u:
            return -2
        for v in u:
            if not v:
                return -2
    
    q=[]
    vis=[0]*len(adj)
    vis[0]=1
    
    explore(0,vis,adj,q)
    
    while q:
        #w=weight, u=node:source (in tree), v = node:target(not in tree)
        w,u,v=pq.heappop(q)
        if not vis[v]:
            vis[v]=1
            tree[u].append([v,w])
            tree[v].append([u,w])
            tree_edj.append([w,u,v])
            explore(v,vis,adj,q)
    for i in vis:
        if not i:
            return -3
        
    return tree_edj if return_edj else tree
            
def unit_test_prim():
    test1=[[[1, 4], [7, 8]], 
           [[0, 4], [2, 8], [7, 11]], 
           [[8, 2], [5, 4], [3, 7], [1, 8]], 
           [[2, 7], [4, 9], [5, 14]], 
           [[3, 9], [5, 10]],
           [[6, 2], [2, 4], [4, 10], [3, 14]], 
           [[7, 1], [5, 2], [8, 6]], 
           [[6, 1], [8, 7], [0, 8], [1, 11]], 
           [[2, 2], [6, 6], [7, 7]]]

    ans1=[[[1, 4], [7, 8]],
          [[0, 4]],
          [[5, 4], [8, 2], [3, 7]],
          [[2, 7], [4, 9]],
          [[3, 9]],
          [[6, 2], [2, 4]],
          [[7, 1], [5, 2]],
          [[0, 8], [6, 1]],
          [[2, 2]]]

    test2=[]
    ans2=-1
    
    test3=[[],
           [[2,5],[3,1]],
           [[1,5]],
           [[1,1]]]
    
    ans3=-2
    
    test4=[[[1,2]],
           [[0,2]],
           [[3,1]],
           [[2,1]]]
    ans4=-3
    
    test5=[[[1, 4], [7, 8]], 
           [[0, 4], [2, 8], [7, 11]], 
           [[8, 2], [5, 4], [3, 7], [1, 8]], 
           [[2, 7], [], [5, 14]], 
           [[3, 9]],
           [[6, 2], [2, 4], [4, 10], [3, 14]], 
           [[7, 1], [5, 2], [8, 6]], 
           [[6, 1], [8, 7], [0, 8], [1, 11]], 
           [[2, 2], [6, 6], [7, 7]]]
            
    ans5=-2
    
    mst1=prim(test1)
    for ans,mst in zip(ans1,mst1):
        ans.sort()
        mst.sort()
    if ans1==mst1:
        print("Unit test 1: OK -> regular solution")
    else:
        print("Unit test 1: FAIL -> regular solution")
    mst2=prim(test2)
    if ans2==mst2:
        print("Unit test 2: OK -> empty tree")
    else:
        print("Unit test 2: FAIL -> empty tree")
    mst3=prim(test3)
    if ans3==mst3:
        print("Unit test 3: OK -> empty node")
    else:
        print("Unit test 3: FAIL -> empty node")
    mst4=prim(test4)
    if ans4==mst4:
        print("Unit test 4: OK -> not connected graph")
    else:
        print("Unit test 4: FAIL -> not connected graph")
    mst5=prim(test5)
    if ans5==mst5:
        print("Unit test 5: OK -> empty node")
    else:
        print("Unit test 5: Fail -> empty node")
    
    
def raiz(nodo,p):
    if p[nodo]!=-1:
        return raiz(p[nodo],p)
    return nodo

def juntar(u,v,p):
    p[raiz(u,p)]=raiz(v,p)
    
def kruskal(edges,n,return_edj=0):
    
    edges.sort()
    if n==0:
        return -1
    
    for i in edges:
        if len(i)<3:
            return -2
    
    #n==número de nodos
    p=[-1]*n
    tree=[[] for i in  range(n)]
    tree_edj=[]
    
    for w,u,v in edges:
        if raiz(u,p) != raiz(v,p):
            tree[u].append([v,w])
            tree[v].append([u,w])
            tree_edj.append([w,u,v])
            juntar(u,v,p)
    c=0
    for i in p:
        if i==-1:
            c+=1
    if c>1:
        print(c)
        return -3
    
    
    return tree_edj if return_edj else tree

def unit_test_kruskal():
    test1=[[1, 7, 6], [2, 8, 2], [2, 6, 5], [4, 0, 1], 
           [4, 2, 5], [6, 8, 6], [7, 2, 3], [7, 7, 8], 
           [8, 0, 7], [8, 1, 2], [9, 3, 4], [10, 5, 4], 
           [11, 1, 7], [14, 3, 5]]
    ans1=[[[1, 4], [7, 8]],
          [[0, 4]],
          [[5, 4], [8, 2], [3, 7]],
          [[2, 7], [4, 9]],
          [[3, 9]],
          [[6, 2], [2, 4]],
          [[7, 1], [5, 2]],
          [[0, 8], [6, 1]],
          [[2, 2]]]
    test2=[]
    ans2=-1
    
    test3=[[],[5,1,2],[1,1,3]]
    ans3=-2
    
    test4=[[2,0,1],[1,3,2]]
    ans4=-3
    
    test5=[[1, 7, 6], [2, 8, 2], [2, 6, 5], [4, 0, 1], 
           [4, 2, 5], [6, 8], [7, 2, 3], [7, 7, 8], 
           [8, 0, 7], [8, 1, 2], [9, 3, 4], [10, 5, 4], 
           [11, 1, 7], [14, 3, 5]]
            
    ans5=-2
    mst1=kruskal(test1,9)

    for ans,mst in zip(ans1,mst1):
        ans.sort()
        mst.sort()
    if ans1==mst1:
        print("Unit test 1: OK -> regular solution")
    else:
        print("Unit test 1: FAIL -> regular solution")
    mst2=kruskal(test2,0)
    if ans2==mst2:
        print("Unit test 2: OK -> empty tree")
    else:
        print("Unit test 2: FAIL -> empty tree")
    mst3=kruskal(test3,4)
    if ans3==mst3:
        print("Unit test 3: OK -> empty node")
    else:
        print("Unit test 3: FAIL -> empty node")
    mst4=kruskal(test4,4)
    if ans4==mst4:
        print("Unit test 4: OK -> not connected graph")
    else:
        print("Unit test 4: FAIL -> not connected graph")
    mst5=kruskal(test5,9)
    if ans5==mst5:
        print("Unit test 5: OK -> empty node")
    else:
        print("Unit test 5: Fail -> empty node")


def get_random_graph(nodes,max_edges,min_weight,max_weight):
    if nodes<2:
        print()
        raise Exception("Please input more than 1 node")
        return -1
    if max_edges<nodes-1:
        print()
        raise Exception ("Edges must be >= nodes-1")
        return -2
    
    node_population=[i for i in range(nodes)]        
    adj=[[] for i in range(nodes)]
    edj=[]
    
    p=[-1]*nodes
    components=nodes
    
    linked={k:{} for k in range(nodes)}
    
    
    while components<=max_edges:
        s=random.sample(node_population,2)
        u=min(s)
        v=max(s)
        max_edges-=1
            
        if not linked[u].get(v,0):
            linked[u][v]=1
            w=random.randint(min_weight,max_weight)
            adj[u].append([v,w])
            adj[v].append([u,w])
            edj.append([w,u,v])
            if raiz(u,p)!=raiz(v,p):
                juntar(u,v,p)
                components-=1
        
    

    raices=[]
    for i,v in enumerate(p):
        if v==-1:
            raices.append(i)
    
    for i in range(1,len(raices)):
        w=random.randint(min_weight,max_weight)
        u=raices[i-1]
        v=raices[i]
        adj[u].append([v,w])
        adj[v].append([u,w])
        edj.append([w,u,v])
        
    return adj,edj
        

width=700
height=500


pygame.init()
window = pygame.display.set_mode((width, height))
window.fill((0, 0, 0))


mst_edge=(125,255,125)
node_color=(255, 0, 0)
red=(255, 0, 0)
white=(255,255,255)



edge_color=white
node_radius=10

class Edge:
    def __init__(self, node1, node2,weight=0,color=white):
        self.node1=node1
        self.node2=node2
        self.weight=weight
        self.color=color
    def pos1(self):
        return self.node1.pos
    def pos2(self):
        return self.node2.pos


class Node:
    def __init__(self, x, y, color, radius):
        self.pos = (x, y)
        self.x_boundary = (x - radius, x + radius)
        self.y_boundary = (y - radius, y + radius)
        self.color = color
        self.radius = radius
        self.edges=[]

    def recalc_boundary(self):
        self.x_boundary = (
            self.pos[0] - self.radius, self.pos[0] + self.radius
        )
        self.y_boundary = (
            self.pos[1] - self.radius, self.pos[1] + self.radius
        )
    def add_edge(self):
        
        return
        
def mouse_in_node():
    pos = pygame.mouse.get_pos()
    selected_node=None
    index=None
    for i,node in enumerate(nodes):
        if (within(pos[0], *node.x_boundary) and within(pos[1], *node.y_boundary)):
            selected_node=node
            index=i
    return selected_node,index





def generate_random_graph():
    adj,edj=get_random_graph(10,16,1,10)
    nodes = []
    for i in range(len(adj)):
        x=random.randint(0,width)
        y=random.randint(0,height)
        
        nodes.append(Node(x,y,node_color,node_radius))
            
    for w,u,v in edj:
        
        u,v=min(u,v),max(u,v)
        
        new_edge=Edge(nodes[u],nodes[v],w)
        nodes[u].edges.append(new_edge)
        nodes[v].edges.append(new_edge)
    return adj,edj,nodes
    

adj,edj,nodes=generate_random_graph()

within = lambda x, low, high: low <= x <= high


selected = False
i=-1
selected_node=None

last_pos=None
drawing_edge=False


while True:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not selected_node and event.button == 1:
            pos = pygame.mouse.get_pos()
            selected_node,index=mouse_in_node()
                        
            if not selected_node:
                nodes.append(Node(pos[0], pos[1], red, 10))
            
        elif event.type==pygame.KEYDOWN:
            if event.key== pygame.K_LSHIFT:
                pos = pygame.mouse.get_pos()                
                node1,index=mouse_in_node()
                if node1:
                    last_pos=pos
            
            #Run Prim
            if event.key==pygame.K_p:
                edj_prim=prim(adj,1)
                for w,u,v in edj_prim:
                    u,v=min(u,v),max(u,v)
                    for edge in nodes[u].edges:
                        if edge.node1==nodes[u] and edge.node2==nodes[v] and edge.weight==w:
                            edge.color=mst_edge
            # Run Kruskal
            if event.key==pygame.K_k:
                edj_kruskal=kruskal(edj,len(adj),1)
                for w,u,v in edj_kruskal:
                    u,v=min(u,v),max(u,v)
                    for edge in nodes[u].edges:
                        if edge.node1==nodes[u] and edge.node2==nodes[v] and edge.weight==w:
                            edge.color=mst_edge
            
            if event.key==pygame.K_c:
                for node in nodes:
                    for edge in node.edges:
                        edge.color=white
            
            if event.key==pygame.K_g:
                adj,edj,nodes=generate_random_graph()
            
                    
        elif event.type==pygame.MOUSEMOTION and last_pos:
            current_pos = pygame.mouse.get_pos()                
            drawing_edge=True

        elif event.type==pygame.KEYUP and drawing_edge:
            node2,index=mouse_in_node()
            if node1 and node2:
                new_edge=Edge(node1,node2)
                node1.edges.append(new_edge)
                node2.edges.append(new_edge)
            last_pos=None
            drawing_edge=False
            
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_node=None
            
        
            
    if selected_node:
        selected_node.pos = pygame.mouse.get_pos()
        selected_node.recalc_boundary()
        
    window.fill((0, 0, 0))
    if drawing_edge:
        pygame.draw.line(window, red, last_pos, current_pos, 1)

    for i,node in enumerate(nodes):
        pygame.draw.circle(
            window, node.color,
            node.pos,
            node.radius
        )
        for e,edge in enumerate(node.edges):
            pygame.draw.line(window, edge.color, edge.pos1(), edge.pos2(), 1)
    
    
    pygame.display.update()