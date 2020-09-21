from typing import List



class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        connected_component_count=0
        un_reached_nodes=set()
        node_dict=dict() # Key node id, Value edge set


        for e in range(n):
            un_reached_nodes.add(e)
        for edge in edges:
            start_node=edge[0]
            end_node=edge[1]
            if start_node not in node_dict:
                node_dict[start_node]=set()
            node_dict[start_node].add(end_node)
            if end_node not in node_dict:
                node_dict[end_node]=set()
            node_dict[end_node].add(start_node)

        #----------------init  end ----------------------

        def bfs(node:int,can_reach_set:set):

            can_reach_set.add(node)
            if node not in node_dict:

                return can_reach_set
            for end_node in node_dict[node]:

                if end_node not in can_reach_set:
                    can_reach_set.add(end_node)
                    can_reach_set=can_reach_set.union(bfs(end_node,can_reach_set))
            return can_reach_set

        for e in range(n):
            if not un_reached_nodes:
                return connected_component_count

            if e not in un_reached_nodes:
                continue
            this_ele_can_reach = bfs(e, set())
            print(this_ele_can_reach)
            un_reached_nodes=un_reached_nodes-this_ele_can_reach
            connected_component_count+=1
        return connected_component_count

result=Solution().countComponents(5,[[0, 1], [1, 2], [3, 4]])
print(str(result))
assert result==2