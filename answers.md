# CMPS 2200 Assignment 3
## Answers

**Name:**_____Sam Cohen____________________


Place all written answers from `assignment-03.md` here for easier grading.
1a) while N > 0:
        for denom in reversed(denominations):  
            if denom <= N:  
                coins.append(denom)  
                N -= denom

1b) In our algorithm, at each step, we select the highest denomination coin that is less than or equal to the remaining amount $N$. This choice seems intuitive because it allows us to minimize the number of coins needed to represent $N$. Since $N - 2^k < N$, and the greedy algorithm always selects the highest denomination coin possible at each step, applying the greedy algorithm recursively on $N - 2^k$ will also result in an optimal solution.

1c) Since there is a linear reduction of N, the work and span of this algorithm are both O(N).

2a) A simple counterexample where the greedy algorithm fails to produce the fewest number of coins in Fortuito is when the denominations are {3, 4, 5} and the amount to make change for is 7. The greedy algorithm would select 5 + 2, requiring 2 coins, whereas the optimal solution is 4 + 3, requiring only 2 coins.

2b) The optimal substructure property of this problem manifests in the minimum number of coins needed to make change from 0 to N dollars. Utilizing a bottom-up algorithm to compute these values can significantly simplify the process of finding the minimum number of coins required for any given amount.

2c)The work of this approach is proportional to the product of the number of denominations (k) and the amount to make change for (N), which is O(N). The span of this approach is also O(N), as each subproblem can be computed independently. 





