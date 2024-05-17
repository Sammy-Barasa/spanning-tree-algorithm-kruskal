
import random

# input the graph data
def get_alphabet(number):
    alphabet_list = [chr(i) for i in range(65,91)]
    return alphabet_list[number]
def get_alphabet_for_list(num_list):
    new_list =num_list.copy()
    for i in range(0,len(num_list)):
        new_list[i]=get_alphabet(new_list[i])
    return new_list
def build_graph():
    num_nodes = None
    try:
        num_nodes = int(input("Please input the number of nodes or vertices of the graph\n"))
    except ValueError:
        print("Must input an integer\n")
    # visualize graph in a table format

    n = num_nodes if num_nodes is not None else 7

    # n = lambda num: num if user_input_num_nodes else 7 # number of graph nodes. By default,we name alphabetically

    graph_table=[[None] * n for _ in range(n)]
    # print(graph_table)
    for i in range(0,n):
        for j in range(0,n):
            inp = input(f"Please input value of edge between node {get_alphabet(i)} and {get_alphabet(j)}. press enter if null/None\n")
            if inp=="":
                continue
            else:
                graph_table[i][j]=int(inp)

    print(graph_table)
    return graph_table

def show_graph_table(graph_table_dat):
    graph_table_value = graph_table_dat.copy()
    n = len(graph_table_value)
    header = []
    for i in range(0,n):
        header.append(f"{get_alphabet(i)}")
        # for j in range(0,n):
        graph_table_value[i].insert(0,get_alphabet(i))
    header.insert(0," ")
    graph_table_value.insert(0,header)
  
    for i in range(0,len(graph_table_value)):
        for j in range(0,len(graph_table_value)):
            if graph_table_value[i][j]==None:
                graph_table_value[i][j]="-"
            print(graph_table_value[i][j], end="\t")  # Separate elements by tabs
        print() 



def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end="\t")  # Separate elements by tabs
        print()  # Move to the next row after printing all elements of the current row

def graph_info(graph_data):
    graph_table_data = graph_data.copy()
    global_min = {}
    global_max = {}

    max_val = random.randint(1,10)
    min_val = random.randint(950,1000)
    max_node = []
    min_node = []
    total_network_cost = 0


    for i in range(0,len(graph_table_data)):
        for j in range(0,len(graph_table_data)):
            current_edge_cost=graph_table_data[i][j]
            # print(type(current_edge_cost))
            # print(current_edge_cost)
            # print(f"cost at: {i},{j}={current_edge_cost}")
            if current_edge_cost == None:
                # print(type(current_edge_cost))
                # print(current_edge_cost)
                continue
            else:
                current_edge_cost=int(current_edge_cost)
                total_network_cost=total_network_cost+current_edge_cost
                if current_edge_cost >= max_val:
                    max_val = current_edge_cost
                    if i and j in max_node:
                        continue
                    else:
                        max_node = [i,j]
            
                elif current_edge_cost <= min_val:
                    min_val = current_edge_cost
                    if i and j in min_node:
                        continue
                    else:
                        min_node = [i,j]
            
    global_min["node"]=min_node
    global_min["val"] = min_val
    global_max["node"] = max_node
    global_max["val"] = max_val
    global_max["alias"] = [get_alphabet(max_node[0]),get_alphabet(max_node[1])]
    global_min["alias"] = [get_alphabet(min_node[0]),get_alphabet(min_node[1])]
    data = {"global_min":global_min,"global_max":global_max,"total_network_cost":int(total_network_cost/2)}

    return data

def traverse_nodes(graph_table):
    graph_table = graph_table.copy()
    current_node = None
    next_possible_nodes =[]
    for i in range(0,len(graph_table)):
        current_node = i
        for j in range(0,len(graph_table)):
            if j is not None:
                next_possible_nodes.append(j)
    return {"current_node":current_node,"next_possible_nodes":next_possible_nodes}

def traverse_nodes_single(graph_table,i):
    current_node = i
    next_possible_nodes_ =[]
    
    for j in range(0,len(graph_table[i])):
        if graph_table[i][j] is not None:
            next_possible_nodes_.append(j)

    print(next_possible_nodes_)
    return {"current_node":current_node,"next_possible_nodes":next_possible_nodes_}
def maximum_saving(total,actual_save):
    max_saving = total-actual_save
    print(f"maximum saving is: {max_saving}")
    return max_saving


def krusals_algorithm(graph_table):
    
    current_node = None
    next_possible_nodes = []
    next_chosen_node = None
    next_chosen_node_cost = None
    cummulative_least_cost = 0
    cummulative_cost_between_next_possible_nodes = []
    graph_data = graph_info(graph_data=graph_table)
    print(graph_data)
    least_info_node = graph_data["global_min"]["node"]
    # least_node_cost = graph_data["global_min"]["val"]
    total_network_cost = graph_data["total_network_cost"]
    
    start_node = least_info_node
    paths_results = {"edges":[],"edges_alias":[],"cummulative_cost":[],"visited_nodes":[],"visited_nodes_alias":[]}
    print("start_node: ",start_node)
    for i in range(0,len(least_info_node)):
        edges = []
        visited_node = []
        edges_alias =[]
        
        current_node = start_node[i]
        print("path No.",i)
        while True:
            # get next possible nodes from current nodes
     
            result = traverse_nodes_single(graph_table,current_node)
            if current_node != result["current_node"]:
                break
            print("current node: ",get_alphabet(result["current_node"]))
            next_possible_nodes = result["next_possible_nodes"]
            
            next_possible_nodes = [x for x in next_possible_nodes if x not in visited_node]
            if len(next_possible_nodes)==0 and len(graph_table)-len(visited_node)==1:
                # last node has introduced a second path on already node
                print("last node has introduced a second path on already node")
                next_possible_nodes = result["next_possible_nodes"]
            
            print("next_possible_nodes: ",get_alphabet_for_list(next_possible_nodes))
            cost_between_next_possible_nodes = cummulative_least_cost
            for k in range(0,len(next_possible_nodes)):
                print(graph_table[current_node][next_possible_nodes[k]])
                cummulative_cost_between_next_possible_nodes.append(graph_table[current_node][next_possible_nodes[k]]+cummulative_least_cost)
            
            # choose next node by least cost
            k=cummulative_cost_between_next_possible_nodes.index(min(cummulative_cost_between_next_possible_nodes))
            # print("k: ",k)
            # if graph_table[current_node[0]][next_possible_nodes[k]] and current_node[0]:
            if current_node not in visited_node:   
                # print("reps",next_possible_nodes[k])
                next_chosen_node = next_possible_nodes[k]
                next_chosen_node_cost = graph_table[current_node][next_possible_nodes[k]]
                cost_between_next_possible_nodes += graph_table[current_node][next_possible_nodes[k]]
                    
            # cummulative cost add
            cummulative_least_cost+=next_chosen_node_cost
            print("cummulative: ",cummulative_least_cost)
            print("next chosen: ",get_alphabet(next_chosen_node))

            # break
            # move to next node
            visited_node.append(current_node)
            print("visited: ",visited_node)
            edges.append([current_node,next_chosen_node,next_chosen_node_cost])
            edges_alias.append([get_alphabet(current_node),get_alphabet(next_chosen_node),next_chosen_node_cost])
            # current_node = [current_node,next_chosen_node]
            current_node = next_chosen_node
            cummulative_cost_between_next_possible_nodes=[]
            # cost_between_next_possible_nodes = random.randint(800,900)
            # breakrules
            
            if cummulative_least_cost>=total_network_cost:
                break
            if len(visited_node) == len(graph_table):
                print("all_nodes_visited")
                break
        paths_results["edges"].append(edges)
        paths_results["edges_alias"].append(edges_alias)
        paths_results["cummulative_cost"].append(cummulative_least_cost)
        paths_results["visited_nodes"].append(visited_node)
        paths_results["visited_nodes_alias"].append(get_alphabet_for_list(visited_node))
        edges = []
        edges_alias=[]
        visited_node = []
        next_chosen_node = None
        next_chosen_node_cost = None
        cummulative_least_cost = 0
        cummulative_cost_between_next_possible_nodes = []


    print("at 231")
    print(len(paths_results["edges"][0]))

    if len(paths_results["edges"][0]) == len(graph_table)-1:
        print("spanning tree satiesfies: (V-1) Edges")
        return paths_results
    else:
    #  select the edges and comb the edges to find final node

        selected= paths_results["cummulative_cost"].index(min(paths_results["cummulative_cost"]))

        selected_path = {}

        # filtered_data = {}

        for key, value in paths_results.items():
            if isinstance(value, list):
                selected_path[key] =  value[selected]
            else:
                selected_path[key] = value

        # get_last two edges, find which has minimum cost
        last_two_edges = selected_path["edges"][-2:]
        

        max_index = None
        max_value = float('-inf')

        for index, inner_list in enumerate(last_two_edges):
            if inner_list[2] > max_value:
                max_value = inner_list[2]
                max_index = index

        index_of_target_to_be_deleted =selected_path["edges"].index(last_two_edges[max_index])
    

        for key, value in selected_path.items():
            if isinstance(value, list):
                del selected_path[key][index_of_target_to_be_deleted]
            else:
                selected_path[key] = value

        # update_ cummulative_least_count value
        new_count_val = 0
        for i in range(0,len(selected_path["edges"])):
            for j in range(0,len(selected_path["edges"][i])):
                if j ==2:
                    new_count_val+= selected_path["edges"][i][j]
        selected_path["cummulative_cost"] = new_count_val
        print("Final results:")
        print(selected_path)
        print("Resulting connected network:")
        print(selected_path["edges_alias"])
        print(f"Result newtwork cost is: {new_count_val}")
        maximum_saving(total_network_cost,new_count_val)
        return selected_path






# graph_table=build_graph()
graph_table=[[None, 14, 10, 19, None, None, None], [14, None, None, 15, 18, None, None], [10, None, None, 26, None, 29, None], [19, 15, 26, None, 16, 17, 21], [None, 18, None, 16, None, None, 9], [None, None, 29, 17, None, None, 25], [None, None, None, 21, 9, 25, None]]

data = graph_info(graph_data=graph_table)
traverse_nodes(graph_table)
krusals_algorithm(graph_table)
show_graph_table(graph_table_dat=graph_table)

