# Genetic Algorithms GA on Set Covering Problem

- In this code we implemented 3 different Genetic Operators with 2 ways of parent selection:-
# Set Covering Problem
- for `PROBLEM_SIZE` it is slected to be the number of numbers to cover that is [ 5, 10, 20, 100, 500, 1000 ]

- The `POPULATION` will be a random number generated from the `PROBLEM_SIZE` 

- The `OFFSPRINGS` number will be a percentage of the `POPULATION_SIZE` and it will be used as a hyper parameter that will help finding the solution with less or more generations.

# *Genetic Operators used*
 ##  1 - Mutation Operator
 - In this operator we mutate the gene by changing a specific loci in it and this is used more often if the population reached saturation with the same individuals.
 ##  2 - Cross Over (One Cut)
- One cut cross over to produce the new generation that depends on 2 parents.
 ##  3 - Elitism 
 - By preserving for the best individuals for the next generation and these were estimatated to be the best `0.01` of the population
***
- Our algorithms uses all of these operators and in each generation a random selection for each operator is used to randomly select an operator with a probability for each Genetic Operator

`Mutation` -- > 0.1

`Cross over` -- > 0.5

`Elitism` -- > 0.4



# *Parental Selection*
 ## 1- Random selection for parent
 ## 2- Tournament Selection
- we select with a low selective pressure to allow the weak individuals to participate more the in next generations.

- `Selective_Pressure` => 2 Individuals


- with some assumptions for hyper parameters that we will discover:-

# Results and Deductions
## SOLUTION FOUND AFTER (...) GENERATION

 |PROBLEM SIZE|OFFSPRING_SIZE = 0.05|OFFSPRING_SIZE = 0.1|OFFSPRING_SIZE = 0.2|
 |---|---|---|---|
 |5|88|29|36|
 |5|89|67|15|
 |5|81|31|46|
 |10|74|101|34|
 |10|111|104|46|
 |10|106|46|36|
 |20|318|86|71|
 |20|117|80|40|
 |20|160|66|52|
 |100|702|395|226|
 |100|722|311|263|
 |100|797|350|324|
 |500|2631|1073|925|
 |500|2410|1361|597|
 |500|3369|1042|673|
 |1000|2225|2225|1663|
 |1000|4327|3393|1583|
 |1000|4257|1961|1070|

 * by comparing the results it seems like by increasing the offspring size we reach to a solution faster in much less generation.

 - Multiple methods could be implemented to find out the best parameters like optimizing the selective pressure and probability of using different Genetic Operators 
 
 ## FIXING the OFFSPRING_SIZE at 0.2
 - Changing the probability of selection for different Genetic operators

`Mutation` -> M

`Cross_Over` ->  CO

`Elitism` -> E

 |PROBLEM SIZE|M = 0.1 ,CO =0.8,E =0.1|M = 0.8 ,CO =0.1,E =0.1|M = 0.1 ,CO =0.1,E =0.8|
 |---|---|---|---|
 |5|63|37|53|
 |10|32|30|46|
 |20|52|61|65|
 |100|238|290|236|
 |500|644|1034|740|
 |1000|1145|1605|1238|
 
* we could get some interresting results by applying this algorithm with diverse usage of operators.

- As a single operator could get stuck after some time for not being able to change the population and at that time we need to change the operator