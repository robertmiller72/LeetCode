# 286 - Walls and Gates

You are given a m x n 2D grid initialized with these three possible values.

<code>-1</code> - A wall or an obstacle.
<code>0</code> - A gate.
<code>INF</code> - Infinity means an empty room. 

We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a Gate, that room should remain filled with <code>INF</code>

	Example 1:

	Input:
	[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],
	[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]

	Output:
	[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

	Explanation:
	the 2D grid is:
	INF  -1  0  INF
	INF INF INF  -1
	INF  -1 INF  -1
	  0  -1 INF INF
	the answer is:
	  3  -1   0   1
	  2   2   1  -1
	  1  -1   2  -1
	  0  -1   3   4
<!-- -->
	Example 2:

	Input:
	[[0,-1],[2147483647,2147483647]]
	Output:
	[[0,-1],[1,2]]
