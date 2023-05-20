# Lab 2: Set Covering with EA

-In this code 4 Algorithms were implemented:-

* ## ( 1 + 1) - ES
* ## ( 1 + λ ) - ES
* ## ( 1 , λ ) - ES
* ## ( μ + λ ) - ES

- N parameters were used with the ranges `[ 5 , 10 , 20 , 100 ]`

- with some assumptions for hyper parameters that we will discover:-

# Results and Deductions
 ## ( 1 + 1) - ES Algorithm
- In this algorithm we assumed that for `σ = 0.001 * N` and that allows for us to have a controllable range of numbers according to the number of the samples to cover.
- Then by using the Gaussian normal distribution we could get the new offspring point.


- To increase our possiblity to find better nodes and fast we will only tweak the old repeated covered numbers.



|N | σ | W |Nodes Used|
|---|-------|-----|---|
|5| 0.001* 5 | 10 |  9|
|5| 0.001* 5 | 10 |  9|
|5| 0.001* 5 | 9 |  8|
|10| 0.001* 10 | 33 |  10|
|10| 0.001* 10 | 28 |  9|
|10| 0.001* 10 | 28 |  9|
|20| 0.001* 20 | 40 |  7|
|20| 0.001* 20 | 46 |  8|
|20| 0.001* 20 | 35 |  6|
|100| 0.001* 100 | 373 |  13|
|100| 0.001* 100 | 314 |  11|
|100| 0.001* 100 | 31 |  11|

* as we see from applying the algorithm multiple times the outcome is not expected as each time the algorithm might take a different approach but also this could differ if we adjusted the hyper parameter value (σ)

|N | σ | W |Nodes Used|
|---|-------|-----|---|
|5| 0.0001* 5 | 14 |  12|
|5| 0.01* 5 | 9 |  8|
|5| 0.1* 5 | 9 |  8|
|10| 0.0001* 10 | 33 |  10|
|10| 0.01* 10 | 28 |  9|
|10| 0.1* 10 | 24 |  7|
|20| 0.0001* 20 | 35 |  6|
|20| 0.01* 20 | 35 |  6|
|20| 0.1* 20 | 29 |  5|
|100| 0.0001* 100 | 373 |  13|
|100| 0.01* 100 | 314 |  11|
|100| 0.1* 100 | 220 |  8|

* in this case it is noted that by increasing the range of exploration the algorithm could manage to find new tweaks that serves to improve the offspring selection

## ( 1 + λ) - ES Algorithm
- In this algorithm we assumed that for `σ = 0.01 ` and `λ is to be modified`
- Then by using the Gaussian normal distribution we could get new **λ** offspring points and then select the best one out of them.

- Theoretically it is expected that this algorithm will perform much better than the (1 + 1 )

- for selecting th number of offsprings members λ we could see that it is also a problem specific so it will be calculated as a ratio of the `N` parameter for example ` 0.2 * N `

|N | σ |λ| W |Nodes Used|
|---|----|-------|-----|---|
|5| 0.01 |0.01| 10 |  9|
|5| 0.01 |0.1| 8 |  7|
|5| 0.01 |0.2| 9 |  8|
|10| 0.01 |0.01| 28 |  9|
|10| 0.01 |0.1| 28 |  9|
|10| 0.01 |0.2|28 |  9|
|20| 0.01 |0.01| 35 |  6|
|20| 0.01 |0.1| 35 |  6|
|20| 0.01 |0.2| 35 |  6|
|100| 0.01 |0.01| 242 |  9|
|100| 0.01  |0.1| 339 |  12|
|100| 0.01  |0.2| 172 |  6|

* as expected theoretically when increasing the number of offspring better results are found and the faster we get to our solution


## ( 1 , λ) - ES Algorithm
- same as the previous concept but in our case we only have the children to select from 
- we will also lock the best parameters so far to be `λ =0.2 and σ = 0.01` 


|N | W |Nodes Used|
|---|---|---|
|5| 10 |  9|
|10| 28 |  9|
|20| 35 |  6|
|100|190 |  7|

* Now we can't realy compare the results with the (1 + λ) algorithm as here it depends on the parent that was selected in the beginning if it was the best then our tweak is not doing the best job it actually makes things worse but if it could improve then we will get better results

* At some times these two algorithms could produce the exact results 

## ( μ + λ) - ES Algorithm
- we select the best μ offspring out of `μ + λ `individuals
- using Tournament selection technique to sort first our nodes to select the best μ parents.
- in our approach we used the maximum selective pressure by doing such thing we can guarantee the best results possible
- to know the best parents here we use the state with the most new numbers and less old discovered numbers
- adjusting the values of `μ` and `λ` will guarantee a controll of the parents and the offspring
- `μ` and `λ` are population dependent so we will use the population as a reference like : `0.2 * N`

|μ |λ |N| W |Nodes Used|
|---|---|---|---|---|
|0.01|0.1 |5| 25 |  25|
|0.2|0.4 |5| 25 |  25|
|0.4|0.7 |5| 25 |  25|
|0.01|0.1|10| 100 |  50|
|0.2|0.4|10| 100 |  50|
|0.4|0.7|10| 100 |  50|
|0.01|0.1|20| 102 |  34|
|0.2|0.4|20| 176 |  34|
|0.4|0.7|20| 138 |  34|
|0.01|0.1|100|7686 |  427|
|0.2|0.4|100|266 |  12|
|0.4|0.7|100|281 |  13|

* as noted this technique will work more effeciently on larger population and by increasing the number of parents and the number of the offsprings will introduce better results.




