from typing import List, Tuple, Set, Optional


class WaterJugDFS:
    """Solves the Water Jug Problem using DFS algorithm."""
    
    def __init__(self, jug1_capacity: int, jug2_capacity: int, target: int):
        """
        Initialize the Water Jug Problem solver.
        
        Args:
            jug1_capacity: Capacity of first jug
            jug2_capacity: Capacity of second jug
            target: Target amount of water to measure
        """
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target = target
        self.visited = set()
        self.path = []
    
    def is_goal_state(self, jug1: int, jug2: int) -> bool:
        """Check if current state is the goal state."""
        return jug1 == self.target or jug2 == self.target
    
    def get_next_states(self, jug1: int, jug2: int) -> List[Tuple[int, int]]:
        """Generate all possible next states from current state."""
        next_states = []
        
        # 1. Fill jug1
        if jug1 != self.jug1_capacity:
            next_states.append((self.jug1_capacity, jug2))
        
        # 2. Fill jug2
        if jug2 != self.jug2_capacity:
            next_states.append((jug1, self.jug2_capacity))
        
        # 3. Empty jug1
        if jug1 != 0:
            next_states.append((0, jug2))
        
        # 4. Empty jug2
        if jug2 != 0:
            next_states.append((jug1, 0))
        
        # 5. Pour from jug1 to jug2
        if jug1 > 0 and jug2 < self.jug2_capacity:
            pour_amount = min(jug1, self.jug2_capacity - jug2)
            next_states.append((jug1 - pour_amount, jug2 + pour_amount))
        
        # 6. Pour from jug2 to jug1
        if jug2 > 0 and jug1 < self.jug1_capacity:
            pour_amount = min(jug2, self.jug1_capacity - jug1)
            next_states.append((jug1 + pour_amount, jug2 - pour_amount))
        
        return next_states
    
    def dfs(self, jug1: int = 0, jug2: int = 0, depth: int = 0, max_depth: int = 100) -> bool:
        """
        Depth-First Search to find solution to Water Jug Problem.
        
        Args:
            jug1: Current amount in jug1
            jug2: Current amount in jug2
            depth: Current depth in search tree
            max_depth: Maximum depth to prevent infinite loops
            
        Returns:
            True if solution found, False otherwise
        """
        if depth > max_depth:
            return False
        
        state = (jug1, jug2)
        
        if state in self.visited:
            return False
        
        self.visited.add(state)
        self.path.append(state)
        
        if self.is_goal_state(jug1, jug2):
            return True
        
        for next_jug1, next_jug2 in self.get_next_states(jug1, jug2):
            if self.dfs(next_jug1, next_jug2, depth + 1, max_depth):
                return True
        
        self.path.pop()
        return False
    
    def solve(self) -> Optional[List[Tuple[int, int]]]:
        """Solve the water jug problem."""
        self.visited.clear()
        self.path.clear()
        
        if self.dfs():
            return self.path
        return None


# Example 1: 4L and 3L jugs, measure 2L
solver1 = WaterJugDFS(jug1_capacity=4, jug2_capacity=3, target=2)
solution1 = solver1.solve()
print("Example 1: 4L and 3L jugs, measure 2L")
print(solution1)

print()

# Example 2: 3L and 5L jugs, measure 4L
solver2 = WaterJugDFS(jug1_capacity=3, jug2_capacity=5, target=4)
solution2 = solver2.solve()
print("Example 2: 3L and 5L jugs, measure 4L")
print(solution2)

print()

# Example 3: 5L and 2L jugs, measure 1L
solver3 = WaterJugDFS(jug1_capacity=5, jug2_capacity=2, target=1)
solution3 = solver3.solve()
print("Example 3: 5L and 2L jugs, measure 1L")
print(solution3)
