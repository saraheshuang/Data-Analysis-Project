
Copyright Jana Schaich Borg/Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)

# Queries that Test Relationships Between Test Completion and Dog Characteristics


## 1. Assess whether Dognition personality dimensions are related to the number of tests completed 

The first variable in the Dognition sPAP we want to investigate is Dognition personality dimensions.  Recall from the "Meet Your Dognition Data" video and the written description of the Dognition Data Set included with the Week 2 materials that Dognition personality dimensions represent distinct combinations of characteristics assessed by the Dognition tests.  It is certainly plausible that certain personalities of dogs might be more or less likely to complete tests.  For example, "einstein" dogs might be particularly likely to complete a lot of tests.  

To test the relationship between Dognition personality dimensions and test completion totals, we need a query that will output a summary of the number of tests completed by dogs that have each of the Dognition personality dimensions.  The features you will need to include in your query are foreshadowed by key words in this sentence.  First, the fact that you need a summary of the number of tests completed suggests you will need an aggregation function.  Next, the fact that you want a different summary for each personality dimension suggests that you will need a GROUP BY clause.  Third, the fact that you need a "summary of the number of tests completed" rather than just a "summary of the tests completed" suggests that you might have to have multiple stages of aggegrations, which in turn might mean that you will need to use a subquery.

Let's build the query step by step.

**Question 1: To get a feeling for what kind of values exist in the Dognition personality dimension column, write a query that will output all of the distinct values in the dimension column.  Use your relational schema or the course materials to determine what table the dimension column is in.  Your output should have 11 rows.**



```python
%sql select distinct dimension from dogs;
```

    11 rows affected.





<table>
    <tr>
        <th>dimension</th>
    </tr>
    <tr>
        <td>charmer</td>
    </tr>
    <tr>
        <td>protodog</td>
    </tr>
    <tr>
        <td>None</td>
    </tr>
    <tr>
        <td>einstein</td>
    </tr>
    <tr>
        <td>stargazer</td>
    </tr>
    <tr>
        <td>maverick</td>
    </tr>
    <tr>
        <td>socialite</td>
    </tr>
    <tr>
        <td>ace</td>
    </tr>
    <tr>
        <td>expert</td>
    </tr>
    <tr>
        <td>renaissance-dog</td>
    </tr>
    <tr>
        <td></td>
    </tr>
</table>



The results of the query above illustrate there are NULL values (indicated by the output value "none") in the dimension column.  Keep that in mind in case it is relevant to future queries.  

We want a summary of the total number of tests completed by dogs with each personality dimension.  In order to calculate those summaries, we first need to calculate the total number of tests completed by each dog.  We can achieve this using a subquery.  The subquery will require data from both the dogs and the complete_tests table, so the subquery will need to include a join.  We are only interested in dogs who have completed tests, so an inner join is appropriate in this case.

**Question 2: Use the equijoin syntax (described in MySQL Exercise 8) to write a query that will output the Dognition personality dimension and total number of tests completed by each unique DogID.  This query will be used as an inner subquery in the next question.  LIMIT your output to 20 rows for troubleshooting purposes.**


```python
%%sql select d.dog_guid, d.dimension, count(c.created_at) as total_tests 
    from dogs d, complete_tests c 
    where c.dog_guid=d.dog_guid group by dog_guid limit 20;
```

    20 rows affected.





<table>
    <tr>
        <th>dog_guid</th>
        <th>dimension</th>
        <th>total_tests</th>
    </tr>
    <tr>
        <td>fd27b272-7144-11e5-ba71-058fbc01cf0b</td>
        <td>charmer</td>
        <td>21</td>
    </tr>
    <tr>
        <td>fd27b5ba-7144-11e5-ba71-058fbc01cf0b</td>
        <td>protodog</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd27b6b4-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>2</td>
    </tr>
    <tr>
        <td>fd27b79a-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>11</td>
    </tr>
    <tr>
        <td>fd27b86c-7144-11e5-ba71-058fbc01cf0b</td>
        <td>einstein</td>
        <td>31</td>
    </tr>
    <tr>
        <td>fd27b948-7144-11e5-ba71-058fbc01cf0b</td>
        <td>stargazer</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd27ba1a-7144-11e5-ba71-058fbc01cf0b</td>
        <td>maverick</td>
        <td>27</td>
    </tr>
    <tr>
        <td>fd27bbbe-7144-11e5-ba71-058fbc01cf0b</td>
        <td>protodog</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd27c1c2-7144-11e5-ba71-058fbc01cf0b</td>
        <td>einstein</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd27c5be-7144-11e5-ba71-058fbc01cf0b</td>
        <td>socialite</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd27c74e-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>14</td>
    </tr>
    <tr>
        <td>fd27c7d0-7144-11e5-ba71-058fbc01cf0b</td>
        <td>socialite</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd27c852-7144-11e5-ba71-058fbc01cf0b</td>
        <td>stargazer</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd27c8d4-7144-11e5-ba71-058fbc01cf0b</td>
        <td>ace</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd27c956-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>11</td>
    </tr>
    <tr>
        <td>fd27cb72-7144-11e5-ba71-058fbc01cf0b</td>
        <td>protodog</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd27cd98-7144-11e5-ba71-058fbc01cf0b</td>
        <td>expert</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd27ce1a-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>7</td>
    </tr>
    <tr>
        <td>fd27cea6-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>2</td>
    </tr>
    <tr>
        <td>fd27cf28-7144-11e5-ba71-058fbc01cf0b</td>
        <td>charmer</td>
        <td>20</td>
    </tr>
</table>



**Question 3: Re-write the query in Question 2 using traditional join syntax (described in MySQL Exercise 8).**


```python
%%sql select d.dog_guid, d.dimension, count(c.created_at) as total_tests 
    from dogs d join complete_tests c 
    on c.dog_guid=d.dog_guid group by dog_guid 
    limit 20;
```

    20 rows affected.





<table>
    <tr>
        <th>dog_guid</th>
        <th>dimension</th>
        <th>total_tests</th>
    </tr>
    <tr>
        <td>fd27b272-7144-11e5-ba71-058fbc01cf0b</td>
        <td>charmer</td>
        <td>21</td>
    </tr>
    <tr>
        <td>fd27b5ba-7144-11e5-ba71-058fbc01cf0b</td>
        <td>protodog</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd27b6b4-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>2</td>
    </tr>
    <tr>
        <td>fd27b79a-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>11</td>
    </tr>
    <tr>
        <td>fd27b86c-7144-11e5-ba71-058fbc01cf0b</td>
        <td>einstein</td>
        <td>31</td>
    </tr>
    <tr>
        <td>fd27b948-7144-11e5-ba71-058fbc01cf0b</td>
        <td>stargazer</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd27ba1a-7144-11e5-ba71-058fbc01cf0b</td>
        <td>maverick</td>
        <td>27</td>
    </tr>
    <tr>
        <td>fd27bbbe-7144-11e5-ba71-058fbc01cf0b</td>
        <td>protodog</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd27c1c2-7144-11e5-ba71-058fbc01cf0b</td>
        <td>einstein</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd27c5be-7144-11e5-ba71-058fbc01cf0b</td>
        <td>socialite</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd27c74e-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>14</td>
    </tr>
    <tr>
        <td>fd27c7d0-7144-11e5-ba71-058fbc01cf0b</td>
        <td>socialite</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd27c852-7144-11e5-ba71-058fbc01cf0b</td>
        <td>stargazer</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd27c8d4-7144-11e5-ba71-058fbc01cf0b</td>
        <td>ace</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd27c956-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>11</td>
    </tr>
    <tr>
        <td>fd27cb72-7144-11e5-ba71-058fbc01cf0b</td>
        <td>protodog</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd27cd98-7144-11e5-ba71-058fbc01cf0b</td>
        <td>expert</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd27ce1a-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>7</td>
    </tr>
    <tr>
        <td>fd27cea6-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>2</td>
    </tr>
    <tr>
        <td>fd27cf28-7144-11e5-ba71-058fbc01cf0b</td>
        <td>charmer</td>
        <td>20</td>
    </tr>
</table>



Now we need to summarize the total number of tests completed by each unique DogID within each Dognition personality dimension.  To do this we will need to choose an appropriate aggregation function for the count column of the query we just wrote.  

**Question 4: To start, write a query that will output the average number of tests completed by unique dogs in each Dognition personality dimension.  Choose either the query in Question 2 or 3 to serve as an inner query in your main query.  If you have trouble, make sure you use the appropriate aliases in your GROUP BY and SELECT statements.**



```python
%%sql select dim, avg(total_tests), count(dogID) 
    from (select d.dog_guid as dogID, d.dimension as dim, count(c.created_at) as total_tests 
          from dogs d join complete_tests c 
          on c.dog_guid=d.dog_guid 
          group by d.dog_guid) as total
    group by dim;
```

    11 rows affected.





<table>
    <tr>
        <th>dim</th>
        <th>avg(total_tests)</th>
        <th>count(dogID)</th>
    </tr>
    <tr>
        <td>None</td>
        <td>6.9416</td>
        <td>13705</td>
    </tr>
    <tr>
        <td></td>
        <td>9.5352</td>
        <td>71</td>
    </tr>
    <tr>
        <td>ace</td>
        <td>23.3878</td>
        <td>477</td>
    </tr>
    <tr>
        <td>charmer</td>
        <td>23.2594</td>
        <td>690</td>
    </tr>
    <tr>
        <td>einstein</td>
        <td>23.2171</td>
        <td>129</td>
    </tr>
    <tr>
        <td>expert</td>
        <td>23.3926</td>
        <td>298</td>
    </tr>
    <tr>
        <td>maverick</td>
        <td>22.8199</td>
        <td>272</td>
    </tr>
    <tr>
        <td>protodog</td>
        <td>22.9336</td>
        <td>602</td>
    </tr>
    <tr>
        <td>renaissance-dog</td>
        <td>23.0157</td>
        <td>510</td>
    </tr>
    <tr>
        <td>socialite</td>
        <td>23.1194</td>
        <td>871</td>
    </tr>
    <tr>
        <td>stargazer</td>
        <td>22.7368</td>
        <td>361</td>
    </tr>
</table>



You should retrieve an output of 11 rows with one of the dimensions labeled "None" and another labeled "" (nothing is between the quotation marks).

**Question 5: How many unique DogIDs are summarized in the Dognition dimensions labeled "None" or ""? (You should retrieve values of 13,705 and 71)**


```python
%%sql select dim, avg(total_tests), count(dogID) 
    from (select d.dog_guid as dogID, d.dimension as dim, count(c.created_at) as total_tests 
          from dogs d join complete_tests c 
          on c.dog_guid=d.dog_guid 
          group by d.dog_guid) as total
    group by dim;
```

    11 rows affected.





<table>
    <tr>
        <th>dim</th>
        <th>avg(total_tests)</th>
        <th>count(dogID)</th>
    </tr>
    <tr>
        <td>None</td>
        <td>6.9416</td>
        <td>13705</td>
    </tr>
    <tr>
        <td></td>
        <td>9.5352</td>
        <td>71</td>
    </tr>
    <tr>
        <td>ace</td>
        <td>23.3878</td>
        <td>477</td>
    </tr>
    <tr>
        <td>charmer</td>
        <td>23.2594</td>
        <td>690</td>
    </tr>
    <tr>
        <td>einstein</td>
        <td>23.2171</td>
        <td>129</td>
    </tr>
    <tr>
        <td>expert</td>
        <td>23.3926</td>
        <td>298</td>
    </tr>
    <tr>
        <td>maverick</td>
        <td>22.8199</td>
        <td>272</td>
    </tr>
    <tr>
        <td>protodog</td>
        <td>22.9336</td>
        <td>602</td>
    </tr>
    <tr>
        <td>renaissance-dog</td>
        <td>23.0157</td>
        <td>510</td>
    </tr>
    <tr>
        <td>socialite</td>
        <td>23.1194</td>
        <td>871</td>
    </tr>
    <tr>
        <td>stargazer</td>
        <td>22.7368</td>
        <td>361</td>
    </tr>
</table>



It makes sense there would be many dogs with NULL values in the dimension column, because we learned from Dognition that personality dimensions can only be assigned after the initial "Dognition Assessment" is completed, which is comprised of the first 20 Dognition tests.  If dogs did not complete the first 20 tests, they would retain a NULL value in the dimension column.

The non-NULL empty string values are more curious.  It is not clear where those values would come from.  

**Question 6: To determine whether there are any features that are common to all dogs that have non-NULL empty strings in the dimension column, write a query that outputs the breed, weight, value in the "exclude" column, first or minimum time stamp in the complete_tests table, last or maximum time stamp in the complete_tests table, and total number of tests completed by each unique DogID that has a non-NULL empty string in the dimension column.** (for presentation purpose, I limit the output to 100 rows)



```python
%%sql 
    select d.breed_type, d.weight, d.exclude, d.dimension
    from complete_tests c join dogs d
    on c.dog_guid=d.dog_guid
    where d.dimension=" "
    limit 100;
```

    100 rows affected.





<table>
    <tr>
        <th>breed_type</th>
        <th>weight</th>
        <th>exclude</th>
        <th>dimension</th>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>20</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>20</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>20</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>20</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>0</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>0</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>60</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>60</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>60</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
</table>



A quick inspection of the output from the last query illustrates that almost all of the entries that have non-NULL empty strings in the dimension column also have "exclude" flags of 1, meaning that the entries are meant to be excluded due to factors monitored by the Dognition team.  This provides a good argument for excluding the entire category of entries that have non-NULL empty strings in the dimension column from our analyses.

**Question 7: Rewrite the query in Question 4 to exclude DogIDs with (1) non-NULL empty strings in the dimension column, (2) NULL values in the dimension column, and (3) values of "1" in the exclude column.  NOTES AND HINTS: You cannot use a clause that says d.exclude does not equal 1 to remove rows that have exclude flags, because Dognition clarified that both NULL values and 0 values in the "exclude" column are valid data.  A clause that says you should only include values that are not equal to 1 would remove the rows that have NULL values in the exclude column, because NULL values are never included in equals statements (as we learned in the join lessons).  In addition, although it should not matter for this query, practice including parentheses with your OR and AND statements that accurately reflect the logic you intend.  Your results should return 402 DogIDs in the ace dimension and 626 dogs in the charmer dimension.**


```python
%%sql select dim, count(dogID) from 
    (select d.dog_guid as dogID, d.dimension as dim, count(c.created_at) as total_tests , d.exclude as exc
     from dogs d join complete_tests c on c.dog_guid=d.dog_guid   
     group by d.dog_guid) as total
    where (dim!="" and dim is not Null) and (exc is Null or exc=0)
    group by dim;
```

    9 rows affected.





<table>
    <tr>
        <th>dim</th>
        <th>count(dogID)</th>
    </tr>
    <tr>
        <td>ace</td>
        <td>402</td>
    </tr>
    <tr>
        <td>charmer</td>
        <td>626</td>
    </tr>
    <tr>
        <td>einstein</td>
        <td>109</td>
    </tr>
    <tr>
        <td>expert</td>
        <td>273</td>
    </tr>
    <tr>
        <td>maverick</td>
        <td>245</td>
    </tr>
    <tr>
        <td>protodog</td>
        <td>535</td>
    </tr>
    <tr>
        <td>renaissance-dog</td>
        <td>463</td>
    </tr>
    <tr>
        <td>socialite</td>
        <td>792</td>
    </tr>
    <tr>
        <td>stargazer</td>
        <td>310</td>
    </tr>
</table>



The results of Question 7 suggest there are not appreciable differences in the number of tests completed by dogs with different Dognition personality dimensions.  Although these analyses are not definitive on their own, these results suggest focusing on Dognition personality dimensions will not likely lead to significant insights about how to improve Dognition completion rates.



## 2. Assess whether dog breeds are related to the number of tests completed

The next variable in the Dognition sPAP we want to investigate is Dog Breed.  We will run one analysis with Breed Group and one analysis with Breed Type.

First, determine how many distinct breed groups there are.

**Questions 8: Write a query that will output all of the distinct values in the breed_group field.**


```python
%sql select distinct breed_group from dogs
```

    9 rows affected.





<table>
    <tr>
        <th>breed_group</th>
    </tr>
    <tr>
        <td>Sporting</td>
    </tr>
    <tr>
        <td>Herding</td>
    </tr>
    <tr>
        <td>Toy</td>
    </tr>
    <tr>
        <td>Working</td>
    </tr>
    <tr>
        <td>None</td>
    </tr>
    <tr>
        <td>Hound</td>
    </tr>
    <tr>
        <td>Non-Sporting</td>
    </tr>
    <tr>
        <td>Terrier</td>
    </tr>
    <tr>
        <td></td>
    </tr>
</table>



You can see that there are NULL values in the breed_group field.  Let's examine the properties of these entries with NULL values to determine whether they should be excluded from our analysis.

**Question 9: Write a query that outputs the breed, weight, value in the "exclude" column, first or minimum time stamp in the complete_tests table, last or maximum time stamp in the complete_tests table, and total number of tests completed by each unique DogID that has a NULL value in the breed_group column.** (for presentation purpose, I limit 100 rows in the output)


```python
%%sql 
select d.breed_type, d.weight, d.exclude, min(c.created_at), max(c.created_at), count(c.created_at), d.dog_guid
from dogs d join complete_tests c on d.dog_guid=c.dog_guid 
where d.breed_group is Null
group by d.dog_guid
limit 100;
```

    100 rows affected.





<table>
    <tr>
        <th>breed_type</th>
        <th>weight</th>
        <th>exclude</th>
        <th>min(c.created_at)</th>
        <th>max(c.created_at)</th>
        <th>count(c.created_at)</th>
        <th>dog_guid</th>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-02-05 18:57:05</td>
        <td>2013-02-05 22:38:01</td>
        <td>20</td>
        <td>fd27bbbe-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-02-05 21:44:38</td>
        <td>2013-02-10 03:33:37</td>
        <td>20</td>
        <td>fd27c5be-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-02-06 04:45:28</td>
        <td>2014-01-06 05:58:13</td>
        <td>14</td>
        <td>fd27c74e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-05-17 17:45:46</td>
        <td>2013-06-14 23:42:53</td>
        <td>11</td>
        <td>fd27c956-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-02-06 04:44:50</td>
        <td>2013-02-06 04:48:29</td>
        <td>2</td>
        <td>fd27cea6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>90</td>
        <td>None</td>
        <td>2013-02-07 05:15:48</td>
        <td>2013-12-20 21:03:18</td>
        <td>21</td>
        <td>fd27d0b8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>70</td>
        <td>None</td>
        <td>2013-02-09 05:49:46</td>
        <td>2013-02-09 06:10:11</td>
        <td>6</td>
        <td>fd27d248-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-02-10 03:28:12</td>
        <td>2013-07-20 02:12:37</td>
        <td>28</td>
        <td>fd27d4dc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>90</td>
        <td>1</td>
        <td>2014-09-24 15:10:03</td>
        <td>2014-09-24 21:23:37</td>
        <td>20</td>
        <td>fd27d9fa-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2014-10-06 22:21:56</td>
        <td>2014-10-06 22:24:02</td>
        <td>2</td>
        <td>fd27dc52-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-02-06 18:07:18</td>
        <td>2013-02-06 18:16:13</td>
        <td>4</td>
        <td>fd27dd38-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-02-06 22:14:00</td>
        <td>2013-02-06 22:41:28</td>
        <td>6</td>
        <td>fd27e0d0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-02-10 04:06:03</td>
        <td>2015-09-28 17:33:05</td>
        <td>45</td>
        <td>fd27e454-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-02-08 04:04:51</td>
        <td>2013-02-11 03:35:44</td>
        <td>6</td>
        <td>fd27f25a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-02-07 03:00:05</td>
        <td>2013-02-07 03:16:21</td>
        <td>4</td>
        <td>fd27f868-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2014-06-23 20:46:28</td>
        <td>2014-06-23 20:50:48</td>
        <td>3</td>
        <td>fd27f9a8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-02-19 15:46:44</td>
        <td>2013-02-19 15:51:52</td>
        <td>2</td>
        <td>fd28093e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-02-16 16:29:48</td>
        <td>2013-02-28 19:30:51</td>
        <td>20</td>
        <td>fd3cd99a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-02-08 21:48:11</td>
        <td>2013-02-08 22:21:21</td>
        <td>7</td>
        <td>fd3cf678-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-02-07 23:03:17</td>
        <td>2013-02-08 18:05:43</td>
        <td>10</td>
        <td>fd3d0078-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-02-08 01:03:49</td>
        <td>2013-02-27 00:42:55</td>
        <td>14</td>
        <td>fd3d0492-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-02-12 00:00:47</td>
        <td>2013-02-20 00:07:48</td>
        <td>16</td>
        <td>fd3d064a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>70</td>
        <td>None</td>
        <td>2013-02-12 00:40:17</td>
        <td>2013-02-20 00:54:30</td>
        <td>16</td>
        <td>fd3d06e0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-03-30 15:10:46</td>
        <td>2013-03-30 15:19:27</td>
        <td>4</td>
        <td>fd3d080c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-02-08 04:28:32</td>
        <td>2014-02-05 17:05:35</td>
        <td>45</td>
        <td>fd3d0898-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-02-08 19:44:28</td>
        <td>2013-02-24 17:44:04</td>
        <td>20</td>
        <td>fd3d0938-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-02-08 19:48:21</td>
        <td>2013-02-24 18:16:21</td>
        <td>20</td>
        <td>fd3d09ce-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-02-16 03:00:16</td>
        <td>2013-03-02 04:18:06</td>
        <td>20</td>
        <td>fd3d0d48-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-02-08 04:52:30</td>
        <td>2013-02-10 01:29:53</td>
        <td>14</td>
        <td>fd3d0dde-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>10</td>
        <td>1</td>
        <td>2013-02-08 15:12:24</td>
        <td>2013-02-08 18:33:35</td>
        <td>20</td>
        <td>fd3d0f00-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>100</td>
        <td>None</td>
        <td>2013-02-08 18:06:57</td>
        <td>2013-03-17 15:38:33</td>
        <td>20</td>
        <td>fd3d0f96-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-02-12 05:13:04</td>
        <td>2013-05-19 18:54:28</td>
        <td>19</td>
        <td>fd3d1202-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-02-09 00:58:03</td>
        <td>2013-02-09 01:02:34</td>
        <td>2</td>
        <td>fd3d150e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-02-08 23:42:54</td>
        <td>2013-02-08 23:42:54</td>
        <td>1</td>
        <td>fd3d15f4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>60</td>
        <td>None</td>
        <td>2013-02-09 02:45:18</td>
        <td>2013-02-09 02:57:37</td>
        <td>4</td>
        <td>fd3d17c0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-02-08 22:19:36</td>
        <td>2013-02-08 22:46:51</td>
        <td>4</td>
        <td>fd3d1a5e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2014-04-05 22:07:37</td>
        <td>2014-04-05 22:23:43</td>
        <td>4</td>
        <td>fd3d2080-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-02-09 03:55:42</td>
        <td>2013-02-16 16:09:04</td>
        <td>20</td>
        <td>fd3d224c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-02-09 14:47:37</td>
        <td>2013-09-14 16:45:52</td>
        <td>34</td>
        <td>fd3d265c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-02-10 04:37:21</td>
        <td>2013-04-19 03:38:01</td>
        <td>25</td>
        <td>fd3d281e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-02-10 09:08:04</td>
        <td>2013-04-03 13:45:33</td>
        <td>14</td>
        <td>fd3d29d6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-02-13 16:52:17</td>
        <td>2013-02-13 17:05:30</td>
        <td>4</td>
        <td>fd3d2af8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-02-11 23:12:32</td>
        <td>2013-02-11 23:57:30</td>
        <td>6</td>
        <td>fd3d2ddc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-02-09 21:19:18</td>
        <td>2013-02-09 21:19:18</td>
        <td>1</td>
        <td>fd3d2f08-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>40</td>
        <td>None</td>
        <td>2013-02-17 12:25:25</td>
        <td>2013-05-03 20:02:33</td>
        <td>23</td>
        <td>fd3d30c0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2014-10-09 22:18:56</td>
        <td>2015-01-31 23:18:46</td>
        <td>36</td>
        <td>fd3d3156-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-02-14 00:49:14</td>
        <td>2013-02-14 00:59:39</td>
        <td>4</td>
        <td>fd3d3278-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>70</td>
        <td>None</td>
        <td>2013-02-10 03:51:05</td>
        <td>2013-02-16 04:08:51</td>
        <td>7</td>
        <td>fd3d330e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-02-12 11:13:29</td>
        <td>2013-02-19 20:01:03</td>
        <td>20</td>
        <td>fd3d343a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>1</td>
        <td>2013-02-10 19:39:00</td>
        <td>2015-07-13 00:06:52</td>
        <td>34</td>
        <td>fd3d3688-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-02-11 00:58:32</td>
        <td>2013-03-04 00:18:41</td>
        <td>17</td>
        <td>fd3d371e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-09-02 16:02:11</td>
        <td>2013-10-25 00:57:20</td>
        <td>4</td>
        <td>fd3d38d6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-09-02 16:19:31</td>
        <td>2013-09-02 16:22:22</td>
        <td>2</td>
        <td>fd3d396c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-09-02 16:12:18</td>
        <td>2013-10-25 01:04:28</td>
        <td>4</td>
        <td>fd3d39f8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>None</td>
        <td>2013-02-11 23:41:54</td>
        <td>2013-03-05 01:29:50</td>
        <td>13</td>
        <td>fd3d3bb0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-03-07 01:57:07</td>
        <td>2013-04-05 01:14:27</td>
        <td>6</td>
        <td>fd3d3c46-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-02-11 05:25:10</td>
        <td>2013-05-28 02:42:54</td>
        <td>13</td>
        <td>fd3d3ffc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-02-14 10:19:41</td>
        <td>2013-04-03 13:56:29</td>
        <td>11</td>
        <td>fd3d4092-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-02-24 02:37:26</td>
        <td>2013-07-29 22:21:04</td>
        <td>31</td>
        <td>fd3d4128-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-02-12 14:27:16</td>
        <td>2013-03-23 23:56:49</td>
        <td>23</td>
        <td>fd3d44a2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>1</td>
        <td>2013-02-11 23:42:26</td>
        <td>2013-02-12 00:22:45</td>
        <td>11</td>
        <td>fd3d452e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-03-06 01:21:23</td>
        <td>2013-03-06 01:50:02</td>
        <td>7</td>
        <td>fd3d4664-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-02-12 00:08:42</td>
        <td>2013-04-02 18:48:24</td>
        <td>16</td>
        <td>fd3d46fa-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-02-12 07:08:39</td>
        <td>2013-02-18 07:35:09</td>
        <td>20</td>
        <td>fd3d479a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-02-11 23:24:25</td>
        <td>2013-02-14 17:39:24</td>
        <td>20</td>
        <td>fd3d4830-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-02-17 17:00:21</td>
        <td>2013-02-18 16:10:03</td>
        <td>20</td>
        <td>fd3d4952-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-02-12 00:37:39</td>
        <td>2013-02-12 02:15:12</td>
        <td>20</td>
        <td>fd3d4a6a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-02-12 01:08:07</td>
        <td>2013-02-12 01:22:58</td>
        <td>4</td>
        <td>fd3d4b00-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-02-12 01:07:10</td>
        <td>2013-02-14 00:03:02</td>
        <td>20</td>
        <td>fd3d4f74-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>80</td>
        <td>None</td>
        <td>2013-02-12 03:40:54</td>
        <td>2013-02-17 19:57:11</td>
        <td>20</td>
        <td>fd3d51f4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>None</td>
        <td>2013-02-12 22:40:50</td>
        <td>2013-02-17 15:05:46</td>
        <td>20</td>
        <td>fd3d5320-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2014-01-04 13:51:25</td>
        <td>2014-01-04 14:08:07</td>
        <td>4</td>
        <td>fd3f81ea-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-02-13 06:29:56</td>
        <td>2014-09-13 02:12:53</td>
        <td>15</td>
        <td>fd3f8bcc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-02-18 21:36:18</td>
        <td>2013-02-20 16:11:08</td>
        <td>7</td>
        <td>fd3fa0b2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-02-14 22:48:29</td>
        <td>2013-03-16 21:43:00</td>
        <td>18</td>
        <td>fd3fb00c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-02-19 02:49:40</td>
        <td>2013-04-08 02:18:39</td>
        <td>20</td>
        <td>fd3fb5e8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-02-18 23:53:19</td>
        <td>2013-03-15 22:58:39</td>
        <td>4</td>
        <td>fd3fbc00-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>1</td>
        <td>2013-02-18 12:42:10</td>
        <td>2013-02-18 17:05:18</td>
        <td>19</td>
        <td>fd3fbd7c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-02-14 16:33:12</td>
        <td>2014-04-03 15:57:33</td>
        <td>40</td>
        <td>fd3fbe44-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-02-21 20:24:15</td>
        <td>2013-02-22 02:09:45</td>
        <td>6</td>
        <td>fd3fbf0c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td>2013-02-15 05:09:23</td>
        <td>2013-02-15 09:59:57</td>
        <td>20</td>
        <td>fd3fcc40-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-04-30 20:17:49</td>
        <td>2013-04-30 21:27:05</td>
        <td>20</td>
        <td>fd3fd014-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-02-18 23:41:51</td>
        <td>2013-04-24 00:09:09</td>
        <td>20</td>
        <td>fd3fd2b2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-03-03 02:45:36</td>
        <td>2013-03-05 02:06:04</td>
        <td>7</td>
        <td>fd3fd348-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-02-27 00:10:58</td>
        <td>2014-05-19 23:29:59</td>
        <td>7</td>
        <td>fd3fd514-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-02-20 20:00:32</td>
        <td>2013-02-26 13:57:36</td>
        <td>20</td>
        <td>fd3fd5aa-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-02-17 00:30:09</td>
        <td>2013-03-03 02:02:37</td>
        <td>20</td>
        <td>fd3fd74e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-03-10 16:48:42</td>
        <td>2013-03-27 01:38:18</td>
        <td>20</td>
        <td>fd3fde06-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-02-18 23:57:53</td>
        <td>2014-03-07 11:38:15</td>
        <td>44</td>
        <td>fd3fe0a4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-02-20 03:21:39</td>
        <td>2013-06-19 02:40:54</td>
        <td>23</td>
        <td>fd3fe50e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-02-18 18:16:27</td>
        <td>2013-03-08 17:42:09</td>
        <td>20</td>
        <td>fd3fe7b6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-03-03 16:38:40</td>
        <td>2013-04-26 00:35:15</td>
        <td>16</td>
        <td>fd3fed7e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td>2013-02-23 18:47:46</td>
        <td>2013-04-27 16:10:39</td>
        <td>22</td>
        <td>fd3fee14-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-03-03 16:42:12</td>
        <td>2013-03-18 17:48:27</td>
        <td>11</td>
        <td>fd3feeb4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-04-08 02:20:12</td>
        <td>2013-04-08 02:27:50</td>
        <td>4</td>
        <td>fd3fef40-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-03-01 16:06:47</td>
        <td>2013-06-28 19:51:22</td>
        <td>28</td>
        <td>fd3ff06c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-02-21 00:31:24</td>
        <td>2013-06-07 01:07:41</td>
        <td>28</td>
        <td>fd3ff47c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-02-20 23:54:39</td>
        <td>2013-06-07 00:46:51</td>
        <td>28</td>
        <td>fd3ff882-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-02-22 02:25:15</td>
        <td>2013-02-22 02:29:12</td>
        <td>2</td>
        <td>fd3ffb5c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-02-20 16:29:38</td>
        <td>2013-05-15 21:04:20</td>
        <td>15</td>
        <td>fd3ffbf2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
</table>



There are a lot of these entries and there is no obvious feature that is common to all of them, so at present, we do not have a good reason to exclude them from our analysis.  Therefore, let's move on to question 10 now....

**Question 10: Adapt the query in Question 7 to examine the relationship between breed_group and number of tests completed.  Exclude DogIDs with values of "1" in the exclude column. Your results should return 1774 DogIDs in the Herding breed group.**



```python
%%sql select breed_group, avg(total_tests), count(dogID) from 
(select d.dog_guid as dogID, d.breed_group as breed_group, count(c.created_at) as total_tests , d.exclude as exc
 from dogs d join complete_tests c on c.dog_guid=d.dog_guid   
group by d.dog_guid) as total
where exc is Null or exc=0
group by breed_group;
```

    9 rows affected.





<table>
    <tr>
        <th>breed_group</th>
        <th>avg(total_tests)</th>
        <th>count(dogID)</th>
    </tr>
    <tr>
        <td>None</td>
        <td>10.2251</td>
        <td>8564</td>
    </tr>
    <tr>
        <td></td>
        <td>19.7542</td>
        <td>179</td>
    </tr>
    <tr>
        <td>Herding</td>
        <td>11.2469</td>
        <td>1774</td>
    </tr>
    <tr>
        <td>Hound</td>
        <td>10.0603</td>
        <td>564</td>
    </tr>
    <tr>
        <td>Non-Sporting</td>
        <td>10.0197</td>
        <td>964</td>
    </tr>
    <tr>
        <td>Sporting</td>
        <td>10.9915</td>
        <td>2470</td>
    </tr>
    <tr>
        <td>Terrier</td>
        <td>9.9333</td>
        <td>780</td>
    </tr>
    <tr>
        <td>Toy</td>
        <td>8.7157</td>
        <td>1041</td>
    </tr>
    <tr>
        <td>Working</td>
        <td>10.2358</td>
        <td>865</td>
    </tr>
</table>



The results show there are non-NULL entries of empty strings in breed_group column again.  Ignoring them for now, Herding and Sporting breed_groups complete the most tests, while Toy breed groups complete the least tests.  This suggests that one avenue an analyst might want to explore further is whether it is worth it to target marketing or certain types of Dognition tests to dog owners with dogs in the Herding and Sporting breed_groups.  Later in this lesson we will discuss whether using a median instead of an average to summarize the number of completed tests might affect this potential course of action. 

**Question 11: Adapt the query in Question 10 to only report results for Sporting, Hound, Herding, and Working breed_groups using an IN clause.**


```python
%%sql select breed_group, avg(total_tests), count(dogID) from 
(select d.dog_guid as dogID, d.breed_group as breed_group, count(c.created_at) as total_tests , d.exclude as exc
 from dogs d join complete_tests c on c.dog_guid=d.dog_guid   
group by d.dog_guid) as total
where (exc is Null or exc=0) and breed_group in ("Sporting", "Hound", "Herding", "Working")
group by breed_group;
```

    4 rows affected.





<table>
    <tr>
        <th>breed_group</th>
        <th>avg(total_tests)</th>
        <th>count(dogID)</th>
    </tr>
    <tr>
        <td>Herding</td>
        <td>11.2469</td>
        <td>1774</td>
    </tr>
    <tr>
        <td>Hound</td>
        <td>10.0603</td>
        <td>564</td>
    </tr>
    <tr>
        <td>Sporting</td>
        <td>10.9915</td>
        <td>2470</td>
    </tr>
    <tr>
        <td>Working</td>
        <td>10.2358</td>
        <td>865</td>
    </tr>
</table>



Next, let's examine the relationship between breed_type and number of completed tests.  

**Questions 12: Begin by writing a query that will output all of the distinct values in the breed_type field.**


```python
%sql select distinct breed_type from dogs
```

    4 rows affected.





<table>
    <tr>
        <th>breed_type</th>
    </tr>
    <tr>
        <td>Pure Breed</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
    </tr>
</table>



**Question 13: Adapt the query in Question 7 to examine the relationship between breed_type and number of tests completed. Exclude DogIDs with values of "1" in the exclude column. Your results should return 8865 DogIDs in the Pure Breed group.**


```python
%%sql 
select breed_type, avg(total_tests) as average_tests, count(dogID)
from (select d.dog_guid as dogID, count(c.created_at) as total_tests, d.breed_type as breed_type, d.exclude as exclude 
      from dogs d join complete_tests c on d.dog_guid=c.dog_guid group by d.dog_guid ) as individual_dogs_totals
where exclude =0 or exclude is null
group by breed_type;
```

    4 rows affected.





<table>
    <tr>
        <th>breed_type</th>
        <th>average_tests</th>
        <th>count(dogID)</th>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10.6009</td>
        <td>2884</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10.2688</td>
        <td>4818</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>10.8423</td>
        <td>634</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>10.4107</td>
        <td>8865</td>
    </tr>
</table>



There does not appear to be an appreciable difference between number of tests completed by dogs of different breed types.
    
  
## 3. Assess whether dog breeds and neutering are related to the number of tests completed

To explore the results we found above a little further, let's run some queries that relabel the breed_types according to "Pure_Breed" and "Not_Pure_Breed".  

**Question 14: For each unique DogID, output its dog_guid, breed_type, number of completed tests, and use a CASE statement to include an extra column with a string that reads "Pure_Breed" whenever breed_type equals 'Pure Breed" and "Not_Pure_Breed" whenever breed_type equals anything else.  LIMIT your output to 50 rows for troubleshooting.**


```python
%%sql 
select d.dog_guid as dogID, d.breed_type as breed_type, case when d.breed_type="Pure Breed" then "Pure_Breed" else "Not_Pure_Breed" end as whether_pure,
      count(c.created_at) as total_tests, d.exclude as exclude
      from dogs d join complete_tests c on d.dog_guid=c.dog_guid 
        where d.exclude=0 or d.exclude is Null
        group by d.dog_guid
        limit 50
```

    50 rows affected.





<table>
    <tr>
        <th>dogID</th>
        <th>breed_type</th>
        <th>whether_pure</th>
        <th>total_tests</th>
        <th>exclude</th>
    </tr>
    <tr>
        <td>fd27b272-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>21</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27b5ba-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>20</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27b6b4-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>2</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27b79a-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>11</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27b948-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>20</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27bbbe-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>Not_Pure_Breed</td>
        <td>20</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27c1c2-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>20</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27c5be-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Cross Breed</td>
        <td>Not_Pure_Breed</td>
        <td>20</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27c74e-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Cross Breed</td>
        <td>Not_Pure_Breed</td>
        <td>14</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27c7d0-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>20</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27c852-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>20</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27c8d4-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>20</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27c956-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Cross Breed</td>
        <td>Not_Pure_Breed</td>
        <td>11</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27cb72-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>20</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27cd98-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>20</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27ce1a-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>7</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27cea6-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>Not_Pure_Breed</td>
        <td>2</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27cf28-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>20</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27cfaa-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>7</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27d02c-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>20</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27d0b8-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Cross Breed</td>
        <td>Not_Pure_Breed</td>
        <td>21</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27d144-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>7</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27d248-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Popular Hybrid</td>
        <td>Not_Pure_Breed</td>
        <td>6</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27d2ca-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>4</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27d34c-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>4</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27d3d8-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>4</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27d45a-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>28</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27d4dc-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>Not_Pure_Breed</td>
        <td>28</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27db08-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>14</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27db8a-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>16</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27dc52-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>2</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27dd38-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Cross Breed</td>
        <td>Not_Pure_Breed</td>
        <td>4</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27e026-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>6</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27e0d0-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>Not_Pure_Breed</td>
        <td>6</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27e1e8-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Cross Breed</td>
        <td>Not_Pure_Breed</td>
        <td>20</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27e31e-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>23</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27e454-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>Not_Pure_Breed</td>
        <td>45</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27e580-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>33</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27eae4-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>4</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27efb2-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>20</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27f110-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>7</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27f25a-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Cross Breed</td>
        <td>Not_Pure_Breed</td>
        <td>6</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27f4c6-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>4</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27f732-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>4</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27f868-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>Not_Pure_Breed</td>
        <td>4</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd27f9a8-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Cross Breed</td>
        <td>Not_Pure_Breed</td>
        <td>3</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd28010a-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>2</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd280236-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>2</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd280344-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>6</td>
        <td>None</td>
    </tr>
    <tr>
        <td>fd280826-7144-11e5-ba71-058fbc01cf0b</td>
        <td>Pure Breed</td>
        <td>Pure_Breed</td>
        <td>4</td>
        <td>None</td>
    </tr>
</table>



**Question 15: Adapt your queries from Questions 7 and 14 to examine the relationship between breed_type and number of tests completed by Pure_Breed dogs and non_Pure_Breed dogs.  Your results should return 8336 DogIDs in the Not_Pure_Breed group.**


```python
%%sql select avg(total_tests), whether_pure from
      (select d.dog_guid as dogID, d.breed_type as breed_type, case when d.breed_type="Pure Breed" then "Pure_Breed" else "Not_Pure_Breed" end as whether_pure,
      count(c.created_at) as total_tests, d.exclude as exclude
      from dogs d join complete_tests c on d.dog_guid=c.dog_guid 
        where d.exclude=0 or d.exclude is Null
        group by d.dog_guid) as pure_group
    group by whether_pure;
```

    2 rows affected.





<table>
    <tr>
        <th>avg(total_tests)</th>
        <th>whether_pure</th>
    </tr>
    <tr>
        <td>10.4273</td>
        <td>Not_Pure_Breed</td>
    </tr>
    <tr>
        <td>10.4107</td>
        <td>Pure_Breed</td>
    </tr>
</table>



**Question 16: Adapt your query from Question 15 to examine the relationship between breed_type, whether or not a dog was neutered (indicated in the dog_fixed field), and number of tests completed by Pure_Breed dogs and non_Pure_Breed dogs. There are DogIDs with null values in the dog_fixed column, so your results should have 6 rows, and the average number of tests completed by non-pure-breeds who are neutered is 10.5681.**


```python
%%sql select avg(total_tests), whether_pure, dog_fixed from
      (select d.dog_guid as dogID, d.breed_type as breed_type, d.dog_fixed as dog_fixed, case when d.breed_type="Pure Breed" then "Pure_Breed" else "Not_Pure_Breed" end as whether_pure,
      count(c.created_at) as total_tests, d.exclude as exclude
      from dogs d join complete_tests c on d.dog_guid=c.dog_guid 
        where d.exclude=0 or d.exclude is Null
        group by d.dog_guid) as pure_group
    group by whether_pure, dog_fixed
    
```

    6 rows affected.





<table>
    <tr>
        <th>avg(total_tests)</th>
        <th>whether_pure</th>
        <th>dog_fixed</th>
    </tr>
    <tr>
        <td>9.9897</td>
        <td>Not_Pure_Breed</td>
        <td>None</td>
    </tr>
    <tr>
        <td>8.6807</td>
        <td>Not_Pure_Breed</td>
        <td>0</td>
    </tr>
    <tr>
        <td>10.5681</td>
        <td>Not_Pure_Breed</td>
        <td>1</td>
    </tr>
    <tr>
        <td>8.2815</td>
        <td>Pure_Breed</td>
        <td>None</td>
    </tr>
    <tr>
        <td>9.3788</td>
        <td>Pure_Breed</td>
        <td>0</td>
    </tr>
    <tr>
        <td>10.6987</td>
        <td>Pure_Breed</td>
        <td>1</td>
    </tr>
</table>



These results suggest that although a dog's breed_type doesn't seem to have a strong relationship with how many tests a dog completed, neutered dogs, on average, seem to finish 1-2 more tests than non-neutered dogs.  It may be fruitful to explore further whether this effect is consistent across different segments of dogs broken up according to other variables.  If the effects are consistent, the next step would be to seek evidence that could clarify whether neutered dogs are finishing more tests due to traits that arise when a dog is neutered, or instead, whether owners who are more likely to neuter their dogs have traits that make it more likely they will want to complete more tests.


## 4. Other dog features that might be related to the number of tests completed, and a note about using averages as summary metrics

Two other dog features included in our sPAP were speed of game completion and previous behavioral training.  Examing the relationship between the speed of game completion and number of games completed is best achieved through creating a scatter plot with a best fit line and/or running a statistical regression analysis.  It is possible to achieve the statistical regression analysis through very advanced SQL queries, but the strategy that would be required is outside the scope of this course.  Therefore, I would recommend exporting relevant data to a program like Tableau, R, or Matlab in order to assess the relationship between the speed of game completion and number of games completed.  

Unfortunately, there is no field available in the Dognition data that is relevant to a dog's previous behavioral training, so more data would need to be collected to examine whether previous behavioral training is related to the number of Dognition tests completed.

One last issue I would like to address in this lesson is the issue of whether an average is a good summary to use to represent the values of a certain group.  Average calculations are very sensitive to extreme values, or outliers, in the data.  This video provides a nice demonstration of how sensitive averages can be:

http://www.statisticslectures.com/topics/outliereffects/

Ideally, you would summarize the data in a group using a median calculation when you either don't know the distribution of values in your data or you already know that outliers are present (the definition of median is covered in the video above).  Unfortunately, medians are more computationally intensive than averages, and there is no pre-made function that allows you to calculate medians using SQL.  If you wanted to calculate the median, you would need to use an advanced strategy such as the ones described here:

https://www.periscopedata.com/blog/medians-in-sql.html

Despite the fact there is no simple way to calculate medians using SQL, there is a way to get a hint about whether average values are likely to be wildly misleading.  As described in the first video (http://www.statisticslectures.com/topics/outliereffects/), strong outliers lead to large standard deviation values.  Fortunately, we *CAN* calculate standard deviations in SQL easily using the STDDEV function.  Therefore, it is good practice to include standard deviation columns with your outputs so that you have an idea whether the average values outputted by your queries are trustworthy.  Whenever standard deviations are a significant portion of the average values of a field, and certainly when standard deviations are larger than the average values of a field, it's a good idea to export your data to a program that can handle more sophisticated statistical analyses before you interpret any results too strongly.  

Let's practice including standard deviations in our queries and interpretting their values.

**Question 17: Adapt your query from Question 7 to include a column with the standard deviation for the number of tests completed by each Dognition personality dimension.**



```python
%%sql select dim, count(dogID), AVG(total_tests), STDDEV(total_tests) from 
(select d.dog_guid as dogID, d.dimension as dim, count(c.created_at) as total_tests , d.exclude as exc
 from dogs d join complete_tests c on c.dog_guid=d.dog_guid   
group by d.dog_guid) as total
where (dim!="" and dim is not Null) and (exc is Null or exc=0)
group by dim;
```

    9 rows affected.





<table>
    <tr>
        <th>dim</th>
        <th>count(dogID)</th>
        <th>AVG(total_tests)</th>
        <th>STDDEV(total_tests)</th>
    </tr>
    <tr>
        <td>ace</td>
        <td>402</td>
        <td>23.5100</td>
        <td>5.4896</td>
    </tr>
    <tr>
        <td>charmer</td>
        <td>626</td>
        <td>23.3594</td>
        <td>5.1919</td>
    </tr>
    <tr>
        <td>einstein</td>
        <td>109</td>
        <td>23.2385</td>
        <td>5.3155</td>
    </tr>
    <tr>
        <td>expert</td>
        <td>273</td>
        <td>23.4249</td>
        <td>4.7589</td>
    </tr>
    <tr>
        <td>maverick</td>
        <td>245</td>
        <td>22.7673</td>
        <td>4.7353</td>
    </tr>
    <tr>
        <td>protodog</td>
        <td>535</td>
        <td>22.9570</td>
        <td>5.3742</td>
    </tr>
    <tr>
        <td>renaissance-dog</td>
        <td>463</td>
        <td>23.0410</td>
        <td>4.9508</td>
    </tr>
    <tr>
        <td>socialite</td>
        <td>792</td>
        <td>23.0997</td>
        <td>4.9748</td>
    </tr>
    <tr>
        <td>stargazer</td>
        <td>310</td>
        <td>22.7968</td>
        <td>4.8254</td>
    </tr>
</table>



The standard deviations are all around 20-25% of the average values of each personality dimension, and they are not appreciably different across the personality dimensions, so the average values are likely fairly trustworthy.  Let's try calculating the standard deviation of a different measurement.

**Question 18: Write a query that calculates the average amount of time it took each dog breed_type to complete all of the tests in the exam_answers table. Exclude negative durations from the calculation, and include a column that calculates the standard deviation of durations for each breed_type group:**



```python
%%sql 
select avg(timestampdiff(minute, e.start_time, e.end_time)) as average_duration, 
stddev(timestampdiff(minute, e.start_time, e.end_time)) as std_timediff, 
d.breed_type as breed_type
from exam_answers e join dogs d 
on d.dog_guid=e.dog_guid
where timestampdiff(minute, e.start_time, e.end_time)>0
group by breed_type;

```

    4 rows affected.





<table>
    <tr>
        <th>average_duration</th>
        <th>std_timediff</th>
        <th>breed_type</th>
    </tr>
    <tr>
        <td>11810.3230</td>
        <td>59113.4558</td>
        <td>Cross Breed</td>
    </tr>
    <tr>
        <td>9145.1575</td>
        <td>48748.6268</td>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
    </tr>
    <tr>
        <td>7734.0763</td>
        <td>45577.6582</td>
        <td>Popular Hybrid</td>
    </tr>
    <tr>
        <td>12311.2558</td>
        <td>60997.3543</td>
        <td>Pure Breed</td>
    </tr>
</table>



This time many of the standard deviations have larger magnitudes than the average duration values.  This suggests  there are outliers in the data that are significantly impacting the reported average values, so the average values are not likely trustworthy. These data should be exported to another program for more sophisticated statistical analysis.

**In the next lesson, we will write queries that assess the relationship between testing circumstances and the number of tests completed.  Until then, feel free to practice any additional queries you would like to below!**


```python

```
