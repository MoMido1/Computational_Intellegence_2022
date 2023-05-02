# LAB1 -Hill Climping
- In this code will approach a Hill climping algorithm


## Assumptions:
- we use a `Tweak` function that takes a random point and tries to find the local optima.
- for the set covering problem it is assumed here that the tweak will be either:-
- - removing an already discovered number in a previous node and replacing it with a new one and then searching for this new node in the given set.
- - if the node contains all undiscovered numbers so we will add a new one and search as well to find it if we can in the close neighbourhood.
- Two approaches were attempted :- 
- - First improvement with selecting the first node that is discovered
- - steepest step and that is by selected the hole neighbourhood and selecting the best one out of the discovered nodes.

## Expectations:
- for the set covering problem it is expected that finding a close point or a state will be defficult.
- because the nodes are selected in a random way and of multiple numberes.
- we can expect to see higher weights and relatively increase in the node numbers to cover.

## Result

```
For N = 5 => the list has a weight W = 5 and we used 3 nodes to cover it
For N = 10 => the list has a weight W = 24 and we used 7 nodes to cover it
For N = 20 => the list has a weight W = 59 and we used 9 nodes to cover it
For N = 100 => the list has a weight W = 347 and we used 14 nodes to cover it
For N = 500 => the list has a weight W = 2991 and we used 20 nodes to cover it
For N = 1000 => the list has a weight W = 5797 and we used 19 nodes to cover it
```

- for smaller numbers of N the algorithm could function in a better way as it could find nodes that are close to each other and similar.
- however we see for higher N the outcome is not very good as compared to the previous A* algorithm
