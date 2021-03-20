class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set()
        def dfs(room):
            visited.add(room)
            for i in rooms[room]:
                 if i not in visited:
                        dfs(i)
        dfs(0)
        return len(rooms)==len(visited)
        #Rooms is the input
        #room is the variable
        #we make visited as set bcz there we dont want to repeat
        #makde function of dfs then we all dfs by room zero 
        
