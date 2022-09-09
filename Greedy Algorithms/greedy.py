"""
Advantages of Greedy Approach

The algorithm is easier to describe.
This algorithm can perform better than other algorithms (but, not in all cases).

Drawback of Greedy Approach

As mentioned earlier, the greedy algorithm doesn't always produce the optimal solution. 
This is the major disadvantage of the algorithm

Greedy Approach

1. Let's start with the root node 20. The weight of the right child is 3 and the weight of the left child is 2.

2. Our problem is to find the largest path. And, the optimal solution at the moment is 3. 
So, the greedy algorithm will choose 3.

3. Finally the weight of an only child of 3 is 1. This gives us our final result 20 + 3 + 1 = 24.

However, it is not the optimal solution. There is another path that carries more weight (20 + 2 + 10 = 32)
as shown in the image below.

Greedy Algorithm
To begin with, the solution set (containing answers) is empty.
At each step, an item is added to the solution set until a solution is reached.
If the solution set is feasible, the current item is kept.
Else, the item is rejected and never considered again.
Let's now use this algorithm to solve a problem.
"""