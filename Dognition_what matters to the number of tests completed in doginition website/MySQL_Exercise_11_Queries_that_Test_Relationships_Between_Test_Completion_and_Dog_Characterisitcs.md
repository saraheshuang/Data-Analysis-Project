
Copyright Jana Schaich Borg/Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)

# MySQL Exercise 11: Queries that Test Relationships Between Test Completion and Dog Characteristics

This lesson we are going to integrate all the SQL syntax we've learned so far to start addressing questions in our Dognition Analysis Plan.  I summarized the reasons having an analysis plan is so important in the "Start with an Analysis Plan" video accompanying this week's materials.  Analysis plans ensure that you will address questions that are relevant to your business objectives as quickly and efficiently as possible.  The quickest way to narrow in the factors in your analysis plan that are likely to create new insights is to combine simple SQL calculations with visualization programs, like Tableau, to identify which factors under consideration have the strongest effects on the business metric you are tasked with improving.  You can then design more nuanced statistical models in other software, such as R, based on the factors you have confirmed are likely to be important for understanding and changing your business metric. 

<img src="https://duke.box.com/shared/static/davndrvd4jb1awwuq6sd1rgt0ck4o8nm.jpg" width=400 alt="SELECT FROM WHERE ORDER BY" />

I describe a method for designing analysis plans in the Data Visualization and Communication with Tableau course earlier in this Specialization.  I call that method Structured Pyramid Analysis Plans, or "sPAPs".  I have provided a skeleton of an sPAP for the Dognition data set with the materials for this course that I will use as a road map for the queries we will design and practice in the next two lessons.  To orient you, the SMART goal of the analysis project is at the top of the pyramid.  This is a specific, measurable, attainable, relevant, and time-bound version of the general project objective, which is to make a recommendation to Dognition about what they could do to increase the number of tests customers complete. The variables you will use to assess the goal should be filled out right under where the SMART goal is written.  Then under those variables, you will see ever-widening layers of categories and sub-categories of issues that will be important to analyze in order to achieve your SMART goal.  
   
In this lesson, we will write queries to address the issues in the left-most branch of the sPAP.  These issues all relate to "Features of Dogs" that could potentially influence the number of tests the dogs will ultimately complete.  We will spend a lot of time discussing and practicing how to translate analysis questions described in words into queries written in SQL syntax.

To begin, load the sql library and database, and make the Dognition database your default database:


```python
%load_ext sql
%sql mysql://studentuser:studentpw@mysqlserver/dognitiondb
%sql USE dognitiondb
```

    0 rows affected.





    []



<img src="https://duke.box.com/shared/static/p2eucjdttai08eeo7davbpfgqi3zrew0.jpg" width=600 alt="SELECT FROM WHERE" />

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

**Question 2: Use the equijoin syntax (described in MySQL Exercise 8) to write a query that will output the Dognition personality dimension and total number of tests completed by each unique DogID.  This query will be used as an inner subquery in the next question.  LIMIT your output to 100 rows for troubleshooting purposes.**


```python
%sql select d.dog_guid, d.dimension, count(c.created_at) as total_tests from dogs d, complete_tests c where c.dog_guid=d.dog_guid group by dog_guid limit 100;
```

    100 rows affected.





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
    <tr>
        <td>fd27cfaa-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>7</td>
    </tr>
    <tr>
        <td>fd27d02c-7144-11e5-ba71-058fbc01cf0b</td>
        <td>stargazer</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd27d0b8-7144-11e5-ba71-058fbc01cf0b</td>
        <td>renaissance-dog</td>
        <td>21</td>
    </tr>
    <tr>
        <td>fd27d144-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>7</td>
    </tr>
    <tr>
        <td>fd27d1c6-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>7</td>
    </tr>
    <tr>
        <td>fd27d248-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>6</td>
    </tr>
    <tr>
        <td>fd27d2ca-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>4</td>
    </tr>
    <tr>
        <td>fd27d34c-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>4</td>
    </tr>
    <tr>
        <td>fd27d3d8-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>4</td>
    </tr>
    <tr>
        <td>fd27d45a-7144-11e5-ba71-058fbc01cf0b</td>
        <td>stargazer</td>
        <td>28</td>
    </tr>
    <tr>
        <td>fd27d4dc-7144-11e5-ba71-058fbc01cf0b</td>
        <td>maverick</td>
        <td>28</td>
    </tr>
    <tr>
        <td>fd27d770-7144-11e5-ba71-058fbc01cf0b</td>
        <td>socialite</td>
        <td>25</td>
    </tr>
    <tr>
        <td>fd27d9fa-7144-11e5-ba71-058fbc01cf0b</td>
        <td>einstein</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd27db08-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>14</td>
    </tr>
    <tr>
        <td>fd27db8a-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>16</td>
    </tr>
    <tr>
        <td>fd27dc52-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>2</td>
    </tr>
    <tr>
        <td>fd27dd38-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>4</td>
    </tr>
    <tr>
        <td>fd27e026-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>6</td>
    </tr>
    <tr>
        <td>fd27e0d0-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>6</td>
    </tr>
    <tr>
        <td>fd27e1e8-7144-11e5-ba71-058fbc01cf0b</td>
        <td>charmer</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd27e31e-7144-11e5-ba71-058fbc01cf0b</td>
        <td>socialite</td>
        <td>23</td>
    </tr>
    <tr>
        <td>fd27e454-7144-11e5-ba71-058fbc01cf0b</td>
        <td>maverick</td>
        <td>45</td>
    </tr>
    <tr>
        <td>fd27e580-7144-11e5-ba71-058fbc01cf0b</td>
        <td>stargazer</td>
        <td>33</td>
    </tr>
    <tr>
        <td>fd27e9a4-7144-11e5-ba71-058fbc01cf0b</td>
        <td>protodog</td>
        <td>22</td>
    </tr>
    <tr>
        <td>fd27eae4-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>4</td>
    </tr>
    <tr>
        <td>fd27ed46-7144-11e5-ba71-058fbc01cf0b</td>
        <td>maverick</td>
        <td>25</td>
    </tr>
    <tr>
        <td>fd27efb2-7144-11e5-ba71-058fbc01cf0b</td>
        <td>einstein</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd27f110-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>7</td>
    </tr>
    <tr>
        <td>fd27f25a-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>6</td>
    </tr>
    <tr>
        <td>fd27f4c6-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>4</td>
    </tr>
    <tr>
        <td>fd27f732-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>4</td>
    </tr>
    <tr>
        <td>fd27f868-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>4</td>
    </tr>
    <tr>
        <td>fd27f9a8-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>3</td>
    </tr>
    <tr>
        <td>fd28010a-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>2</td>
    </tr>
    <tr>
        <td>fd280236-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>2</td>
    </tr>
    <tr>
        <td>fd280344-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>6</td>
    </tr>
    <tr>
        <td>fd280826-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>4</td>
    </tr>
    <tr>
        <td>fd2808b2-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>11</td>
    </tr>
    <tr>
        <td>fd28093e-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>2</td>
    </tr>
    <tr>
        <td>fd2809c0-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>4</td>
    </tr>
    <tr>
        <td>fd3ccd24-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>4</td>
    </tr>
    <tr>
        <td>fd3ccf2c-7144-11e5-ba71-058fbc01cf0b</td>
        <td>einstein</td>
        <td>22</td>
    </tr>
    <tr>
        <td>fd3cd40e-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>10</td>
    </tr>
    <tr>
        <td>fd3cd4d6-7144-11e5-ba71-058fbc01cf0b</td>
        <td>charmer</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd3cd8d2-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>7</td>
    </tr>
    <tr>
        <td>fd3cd99a-7144-11e5-ba71-058fbc01cf0b</td>
        <td>renaissance-dog</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd3cec50-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>4</td>
    </tr>
    <tr>
        <td>fd3cf5c4-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>4</td>
    </tr>
    <tr>
        <td>fd3cf678-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>7</td>
    </tr>
    <tr>
        <td>fd3cf718-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>17</td>
    </tr>
    <tr>
        <td>fd3cf8ee-7144-11e5-ba71-058fbc01cf0b</td>
        <td>protodog</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd3cf984-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>4</td>
    </tr>
    <tr>
        <td>fd3cfa1a-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>4</td>
    </tr>
    <tr>
        <td>fd3cfab0-7144-11e5-ba71-058fbc01cf0b</td>
        <td>charmer</td>
        <td>38</td>
    </tr>
    <tr>
        <td>fd3cfcfe-7144-11e5-ba71-058fbc01cf0b</td>
        <td>socialite</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd3cfd94-7144-11e5-ba71-058fbc01cf0b</td>
        <td>expert</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd3cfe2a-7144-11e5-ba71-058fbc01cf0b</td>
        <td>socialite</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd3cfeb6-7144-11e5-ba71-058fbc01cf0b</td>
        <td>protodog</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd3cff4c-7144-11e5-ba71-058fbc01cf0b</td>
        <td>charmer</td>
        <td>21</td>
    </tr>
    <tr>
        <td>fd3d0078-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>10</td>
    </tr>
    <tr>
        <td>fd3d01ae-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>11</td>
    </tr>
    <tr>
        <td>fd3d03fc-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>4</td>
    </tr>
    <tr>
        <td>fd3d0492-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>14</td>
    </tr>
    <tr>
        <td>fd3d05be-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>11</td>
    </tr>
    <tr>
        <td>fd3d064a-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>16</td>
    </tr>
    <tr>
        <td>fd3d06e0-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>16</td>
    </tr>
    <tr>
        <td>fd3d0776-7144-11e5-ba71-058fbc01cf0b</td>
        <td>einstein</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd3d080c-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>4</td>
    </tr>
    <tr>
        <td>fd3d0898-7144-11e5-ba71-058fbc01cf0b</td>
        <td>socialite</td>
        <td>45</td>
    </tr>
    <tr>
        <td>fd3d0938-7144-11e5-ba71-058fbc01cf0b</td>
        <td>socialite</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd3d09ce-7144-11e5-ba71-058fbc01cf0b</td>
        <td>ace</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd3d0b7c-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>7</td>
    </tr>
    <tr>
        <td>fd3d0c12-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>4</td>
    </tr>
    <tr>
        <td>fd3d0cb2-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>5</td>
    </tr>
    <tr>
        <td>fd3d0d48-7144-11e5-ba71-058fbc01cf0b</td>
        <td>expert</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd3d0dde-7144-11e5-ba71-058fbc01cf0b</td>
        <td>None</td>
        <td>14</td>
    </tr>
    <tr>
        <td>fd3d0f00-7144-11e5-ba71-058fbc01cf0b</td>
        <td>expert</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd3d0f96-7144-11e5-ba71-058fbc01cf0b</td>
        <td>socialite</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd3d102c-7144-11e5-ba71-058fbc01cf0b</td>
        <td>charmer</td>
        <td>20</td>
    </tr>
    <tr>
        <td>fd3d10cc-7144-11e5-ba71-058fbc01cf0b</td>
        <td>ace</td>
        <td>20</td>
    </tr>
</table>



**Question 3: Re-write the query in Question 2 using traditional join syntax (described in MySQL Exercise 8).**


```python
%sql select d.dog_guid, d.dimension, count(c.created_at) as total_tests from dogs d join complete_tests c on c.dog_guid=d.dog_guid group by dog_guid limit 100;
```

Now we need to summarize the total number of tests completed by each unique DogID within each Dognition personality dimension.  To do this we will need to choose an appropriate aggregation function for the count column of the query we just wrote.  

**Question 4: To start, write a query that will output the average number of tests completed by unique dogs in each Dognition personality dimension.  Choose either the query in Question 2 or 3 to serve as an inner query in your main query.  If you have trouble, make sure you use the appropriate aliases in your GROUP BY and SELECT statements.**



```python
%%sql select dim, avg(total_tests), count(dogID) from 
(select d.dog_guid as dogID, d.dimension as dim, count(c.created_at) as total_tests from dogs d join complete_tests c on c.dog_guid=d.dog_guid group by d.dog_guid) as total
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

```

It makes sense there would be many dogs with NULL values in the dimension column, because we learned from Dognition that personality dimensions can only be assigned after the initial "Dognition Assessment" is completed, which is comprised of the first 20 Dognition tests.  If dogs did not complete the first 20 tests, they would retain a NULL value in the dimension column.

The non-NULL empty string values are more curious.  It is not clear where those values would come from.  

**Question 6: To determine whether there are any features that are common to all dogs that have non-NULL empty strings in the dimension column, write a query that outputs the breed, weight, value in the "exclude" column, first or minimum time stamp in the complete_tests table, last or maximum time stamp in the complete_tests table, and total number of tests completed by each unique DogID that has a non-NULL empty string in the dimension column.**



```python
%%sql select d.breed_type, d.weight, d.exclude, d.dimension
from complete_tests c join dogs d
on c.dog_guid=d.dog_guid
where d.dimension=" ";
```

    677 rows affected.





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
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
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
        <td>Pure Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
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
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
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
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>190</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>190</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>190</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>190</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>190</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
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
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
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
        <td>Pure Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>160</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>160</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>160</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>160</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>160</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>160</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>160</td>
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
        <td>0</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>10</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>10</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>10</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>10</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>10</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>10</td>
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
        <td>Pure Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
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
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>190</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>190</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>190</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>190</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>190</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>190</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>190</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>190</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>190</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>90</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>90</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>90</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>90</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>90</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>90</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>90</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>100</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>100</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>100</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>100</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>100</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>100</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>100</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>100</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>100</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>100</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>100</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
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
        <td>Cross Breed</td>
        <td>80</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>80</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>80</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>80</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
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
        <td>60</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
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
        <td>30</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>100</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>100</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>100</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>100</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>100</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>100</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>100</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>100</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>100</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>100</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>100</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>100</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>100</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>100</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>70</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
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
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
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
        <td>Pure Breed</td>
        <td>10</td>
        <td>1</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>0</td>
        <td></td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>0</td>
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

**Question 9: Write a query that outputs the breed, weight, value in the "exclude" column, first or minimum time stamp in the complete_tests table, last or maximum time stamp in the complete_tests table, and total number of tests completed by each unique DogID that has a NULL value in the breed_group column.**


```python
%%sql select d.breed_type, d.weight, d.exclude, min(c.created_at), max(c.created_at), count(c.created_at), d.dog_guid
from dogs d join complete_tests c on d.dog_guid=c.dog_guid 
where d.breed_group is Null
group by d.dog_guid;
```

    8816 rows affected.





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
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-02-28 15:52:03</td>
        <td>2014-02-09 17:19:39</td>
        <td>38</td>
        <td>fd3ffe36-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td>2013-02-22 17:55:10</td>
        <td>2013-05-31 17:16:12</td>
        <td>23</td>
        <td>fd3ffecc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2014-01-01 04:51:23</td>
        <td>2014-01-01 05:04:24</td>
        <td>4</td>
        <td>fd400084-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>80</td>
        <td>None</td>
        <td>2013-02-20 03:30:12</td>
        <td>2013-02-20 03:34:18</td>
        <td>2</td>
        <td>fd400458-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2014-03-30 18:48:20</td>
        <td>2014-03-30 18:52:45</td>
        <td>2</td>
        <td>fd400c78-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-02-24 18:35:25</td>
        <td>2013-03-03 22:10:07</td>
        <td>20</td>
        <td>fd401efc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>None</td>
        <td>2013-02-23 22:02:54</td>
        <td>2013-03-18 23:01:27</td>
        <td>20</td>
        <td>fd40241a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-02-21 21:02:44</td>
        <td>2015-01-02 13:23:58</td>
        <td>15</td>
        <td>fd402a5a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>80</td>
        <td>None</td>
        <td>2013-03-02 00:30:06</td>
        <td>2013-03-02 00:37:38</td>
        <td>3</td>
        <td>fd403036-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-12-04 18:01:11</td>
        <td>2013-12-05 02:07:31</td>
        <td>7</td>
        <td>fd404832-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-12-04 18:15:35</td>
        <td>2013-12-05 01:53:01</td>
        <td>7</td>
        <td>fd4048c8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-03-19 00:42:06</td>
        <td>2013-03-19 00:53:22</td>
        <td>4</td>
        <td>fd404954-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-02-23 15:23:42</td>
        <td>2013-02-23 15:34:41</td>
        <td>4</td>
        <td>fd404b8e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>1</td>
        <td>2013-02-21 19:01:12</td>
        <td>2013-06-12 13:06:03</td>
        <td>20</td>
        <td>fd404d3c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-02-22 21:38:51</td>
        <td>2013-02-23 22:48:03</td>
        <td>14</td>
        <td>fd404dc8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-02-21 22:18:15</td>
        <td>2014-01-30 01:36:39</td>
        <td>32</td>
        <td>fd404e54-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-02-22 00:19:59</td>
        <td>2013-12-12 23:49:56</td>
        <td>12</td>
        <td>fd404eea-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-04-22 21:07:49</td>
        <td>2013-04-25 18:19:39</td>
        <td>20</td>
        <td>fd4052b4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-06-26 17:57:35</td>
        <td>2013-06-26 18:08:34</td>
        <td>4</td>
        <td>fd405610-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td>2013-02-25 20:03:44</td>
        <td>2013-04-15 00:45:46</td>
        <td>20</td>
        <td>fd405732-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>90</td>
        <td>None</td>
        <td>2013-02-27 12:58:09</td>
        <td>2013-03-06 13:41:04</td>
        <td>20</td>
        <td>fd4057be-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-03-08 02:13:41</td>
        <td>2013-11-27 23:15:25</td>
        <td>22</td>
        <td>fd405a70-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>1</td>
        <td>2013-02-22 11:25:02</td>
        <td>2013-07-12 07:23:31</td>
        <td>31</td>
        <td>fd405b88-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>None</td>
        <td>2013-02-23 00:30:03</td>
        <td>2014-08-29 17:59:51</td>
        <td>3</td>
        <td>fd406628-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-02-23 02:02:44</td>
        <td>2013-02-26 01:20:15</td>
        <td>5</td>
        <td>fd406b1e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-02-24 15:56:53</td>
        <td>2013-02-25 00:14:37</td>
        <td>20</td>
        <td>fd406d94-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-02-24 03:18:48</td>
        <td>2013-03-08 03:55:14</td>
        <td>20</td>
        <td>fd406fce-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-02-23 23:28:34</td>
        <td>2013-04-17 17:35:24</td>
        <td>22</td>
        <td>fd407050-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-02-23 20:22:33</td>
        <td>2014-03-07 18:25:08</td>
        <td>29</td>
        <td>fd4070dc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-03-24 19:24:21</td>
        <td>2013-08-10 18:42:27</td>
        <td>20</td>
        <td>fd4071f4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-02-24 21:46:22</td>
        <td>2013-08-10 18:20:59</td>
        <td>22</td>
        <td>fd407280-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-02-24 00:13:33</td>
        <td>2013-02-24 00:36:49</td>
        <td>5</td>
        <td>fd4075b4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>40</td>
        <td>None</td>
        <td>2013-02-24 01:56:03</td>
        <td>2013-03-05 04:39:54</td>
        <td>16</td>
        <td>fd407636-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-03-17 17:15:08</td>
        <td>2013-07-21 18:55:30</td>
        <td>20</td>
        <td>fd4077d0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-03-23 06:10:42</td>
        <td>2013-03-23 06:57:04</td>
        <td>14</td>
        <td>fd407866-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-02-24 09:35:53</td>
        <td>2013-02-28 07:35:37</td>
        <td>20</td>
        <td>fd407a8c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-02-27 01:32:03</td>
        <td>2013-02-27 01:56:21</td>
        <td>6</td>
        <td>fd407b18-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2014-04-30 20:21:58</td>
        <td>2014-04-30 20:32:21</td>
        <td>4</td>
        <td>fd407e56-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-04-28 14:31:32</td>
        <td>2013-05-09 00:29:22</td>
        <td>20</td>
        <td>fd40807c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-03-24 23:00:52</td>
        <td>2013-03-24 23:14:25</td>
        <td>4</td>
        <td>fd408220-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-02-26 02:56:15</td>
        <td>2014-03-28 16:08:32</td>
        <td>21</td>
        <td>fd409224-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>80</td>
        <td>None</td>
        <td>2013-03-09 03:38:09</td>
        <td>2013-03-09 05:04:50</td>
        <td>20</td>
        <td>fd409346-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-02-25 13:55:53</td>
        <td>2013-02-25 15:07:35</td>
        <td>20</td>
        <td>fd4093dc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-02-25 16:41:44</td>
        <td>2013-03-07 19:31:01</td>
        <td>4</td>
        <td>fd40a3c2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-04-16 17:48:14</td>
        <td>2013-04-16 18:13:37</td>
        <td>7</td>
        <td>fd40b06a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-03-02 19:32:43</td>
        <td>2013-09-04 20:22:30</td>
        <td>22</td>
        <td>fd40b970-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-07 09:05:11</td>
        <td>2013-05-07 11:44:06</td>
        <td>20</td>
        <td>fd40cae6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-02-25 23:24:51</td>
        <td>2013-02-26 23:01:34</td>
        <td>20</td>
        <td>fd40cc94-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-02-27 19:01:46</td>
        <td>2013-09-11 18:34:25</td>
        <td>25</td>
        <td>fd40cdac-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-08-25 03:11:24</td>
        <td>2013-08-25 03:21:20</td>
        <td>4</td>
        <td>fd40d568-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>70</td>
        <td>None</td>
        <td>2013-02-26 20:37:00</td>
        <td>2013-04-28 23:37:42</td>
        <td>20</td>
        <td>fd40d70c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>80</td>
        <td>None</td>
        <td>2013-02-27 01:34:21</td>
        <td>2013-02-27 02:07:33</td>
        <td>4</td>
        <td>fd40d93c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-03-09 20:33:40</td>
        <td>2013-03-09 22:48:41</td>
        <td>20</td>
        <td>fd40db76-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-03-25 01:28:49</td>
        <td>2013-03-25 02:07:02</td>
        <td>7</td>
        <td>fd40dc02-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>1</td>
        <td>2013-02-27 15:21:06</td>
        <td>2013-02-28 02:00:03</td>
        <td>20</td>
        <td>fd40debe-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-03-10 15:50:41</td>
        <td>2013-03-10 16:26:07</td>
        <td>6</td>
        <td>fd40dfd6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-02-27 20:56:07</td>
        <td>2013-03-24 23:11:31</td>
        <td>16</td>
        <td>fd40e058-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-02-28 01:03:06</td>
        <td>2013-06-28 17:37:57</td>
        <td>10</td>
        <td>fd40eb0c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-03-15 18:52:08</td>
        <td>2013-03-15 19:04:15</td>
        <td>4</td>
        <td>fd40ebe8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-03-02 20:56:57</td>
        <td>2013-06-10 21:07:15</td>
        <td>21</td>
        <td>fd40ecc4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>90</td>
        <td>None</td>
        <td>2013-03-02 14:24:27</td>
        <td>2013-03-05 02:10:22</td>
        <td>16</td>
        <td>fd40ef4e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-03-01 02:16:10</td>
        <td>2015-06-27 20:34:07</td>
        <td>29</td>
        <td>fd40f4e4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>70</td>
        <td>None</td>
        <td>2013-02-28 22:44:40</td>
        <td>2014-01-02 01:49:12</td>
        <td>20</td>
        <td>fd40fcaa-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-03-01 00:45:56</td>
        <td>2013-03-01 20:07:28</td>
        <td>16</td>
        <td>fd4100ba-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>10</td>
        <td>None</td>
        <td>2013-03-02 00:22:34</td>
        <td>2013-03-03 17:48:36</td>
        <td>20</td>
        <td>fd410146-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-03-01 01:51:24</td>
        <td>2013-03-01 01:59:53</td>
        <td>3</td>
        <td>fd41025e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-03-03 18:31:54</td>
        <td>2013-03-03 18:49:19</td>
        <td>4</td>
        <td>fd410402-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>None</td>
        <td>2013-03-21 04:51:00</td>
        <td>2013-03-21 05:01:55</td>
        <td>4</td>
        <td>fd41059c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-03-01 18:28:39</td>
        <td>2013-04-28 15:23:38</td>
        <td>18</td>
        <td>fd4108e4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-03-02 17:30:11</td>
        <td>2013-03-11 19:31:04</td>
        <td>7</td>
        <td>fd4109f2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td>2013-03-02 21:36:30</td>
        <td>2013-03-31 21:41:24</td>
        <td>20</td>
        <td>fd410a7e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-03-07 21:48:52</td>
        <td>2013-03-15 00:29:01</td>
        <td>20</td>
        <td>fd410e5c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>1</td>
        <td>2013-03-05 16:19:34</td>
        <td>2013-04-30 23:54:45</td>
        <td>20</td>
        <td>fd4111f4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-03-02 00:38:13</td>
        <td>2013-03-02 21:41:41</td>
        <td>20</td>
        <td>fd4112ee-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>70</td>
        <td>None</td>
        <td>2013-03-02 02:51:56</td>
        <td>2013-03-02 05:08:20</td>
        <td>16</td>
        <td>fd41144c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-03-02 03:38:14</td>
        <td>2013-03-02 04:38:27</td>
        <td>16</td>
        <td>fd4114c4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-09-12 14:21:59</td>
        <td>2013-09-13 09:43:16</td>
        <td>6</td>
        <td>fd411956-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-03-02 18:10:20</td>
        <td>2014-05-11 16:40:43</td>
        <td>9</td>
        <td>fd411bea-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-04-23 03:08:11</td>
        <td>2013-04-26 03:23:21</td>
        <td>6</td>
        <td>fd412b62-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>30</td>
        <td>1</td>
        <td>2013-03-02 21:40:48</td>
        <td>2013-03-03 16:29:46</td>
        <td>20</td>
        <td>fd413080-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-04-01 18:14:12</td>
        <td>2013-04-14 22:19:42</td>
        <td>20</td>
        <td>fd413422-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>30</td>
        <td>None</td>
        <td>2013-03-31 16:22:09</td>
        <td>2013-03-31 21:06:31</td>
        <td>20</td>
        <td>fd4134d6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-03-04 18:51:09</td>
        <td>2013-03-04 19:49:58</td>
        <td>7</td>
        <td>fd413bde-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-03-02 21:38:03</td>
        <td>2013-03-08 01:31:10</td>
        <td>20</td>
        <td>fd4148cc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>40</td>
        <td>None</td>
        <td>2013-03-02 22:20:42</td>
        <td>2013-03-04 00:11:09</td>
        <td>7</td>
        <td>fd414944-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>10</td>
        <td>None</td>
        <td>2013-03-02 23:22:27</td>
        <td>2013-03-26 00:03:18</td>
        <td>16</td>
        <td>fd414c78-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>90</td>
        <td>None</td>
        <td>2013-08-10 22:48:21</td>
        <td>2014-03-31 02:50:45</td>
        <td>20</td>
        <td>fd414cf0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>80</td>
        <td>None</td>
        <td>2013-08-10 23:37:34</td>
        <td>2014-04-01 03:17:29</td>
        <td>20</td>
        <td>fd414d68-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-08-10 23:23:26</td>
        <td>2014-03-31 02:33:24</td>
        <td>20</td>
        <td>fd414de0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-08-10 23:10:50</td>
        <td>2014-03-31 02:12:36</td>
        <td>20</td>
        <td>fd414e4e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-03-03 02:12:05</td>
        <td>2013-03-12 04:30:51</td>
        <td>20</td>
        <td>fd414ec6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-06-15 18:19:42</td>
        <td>2013-06-15 18:31:44</td>
        <td>4</td>
        <td>fd414fac-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-03-04 01:21:18</td>
        <td>2013-04-08 21:45:10</td>
        <td>20</td>
        <td>fd415024-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>None</td>
        <td>2013-03-03 00:59:33</td>
        <td>2013-03-03 01:09:12</td>
        <td>4</td>
        <td>fd41509c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>80</td>
        <td>None</td>
        <td>2013-03-03 19:04:58</td>
        <td>2013-03-08 01:22:02</td>
        <td>10</td>
        <td>fd41525e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-03-04 17:57:19</td>
        <td>2013-03-05 17:20:52</td>
        <td>2</td>
        <td>fd4154a2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-06-14 21:53:46</td>
        <td>2015-09-27 18:51:40</td>
        <td>13</td>
        <td>fd415600-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-03-03 06:47:10</td>
        <td>2013-03-03 07:16:48</td>
        <td>4</td>
        <td>fd4157c2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>70</td>
        <td>None</td>
        <td>2014-06-10 00:26:15</td>
        <td>2014-06-10 00:26:15</td>
        <td>1</td>
        <td>fd415920-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-03-03 18:37:47</td>
        <td>2013-03-03 18:47:47</td>
        <td>4</td>
        <td>fd415c4a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>70</td>
        <td>None</td>
        <td>2013-03-03 17:37:18</td>
        <td>2013-05-23 03:45:46</td>
        <td>16</td>
        <td>fd415cc2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>None</td>
        <td>2013-03-03 22:33:47</td>
        <td>2013-03-03 23:10:24</td>
        <td>6</td>
        <td>fd415f92-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>None</td>
        <td>2013-03-03 20:18:48</td>
        <td>2013-03-03 21:59:54</td>
        <td>6</td>
        <td>fd4161c2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-08-12 18:12:09</td>
        <td>2015-09-12 00:32:27</td>
        <td>17</td>
        <td>fd416276-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>80</td>
        <td>None</td>
        <td>2013-03-17 00:56:44</td>
        <td>2014-03-09 23:56:23</td>
        <td>23</td>
        <td>fd41674e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2014-03-09 22:30:11</td>
        <td>2015-09-06 22:35:11</td>
        <td>6</td>
        <td>fd4168b6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-03-18 00:13:45</td>
        <td>2013-04-22 23:45:12</td>
        <td>20</td>
        <td>fd416c62-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-03-04 07:27:57</td>
        <td>2013-03-04 07:31:57</td>
        <td>2</td>
        <td>fd417248-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-03-16 00:06:05</td>
        <td>2015-08-12 23:42:08</td>
        <td>4</td>
        <td>fd417572-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-08-10 16:26:50</td>
        <td>2013-08-10 16:32:01</td>
        <td>3</td>
        <td>fd417658-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-03-11 00:54:27</td>
        <td>2013-05-28 01:19:12</td>
        <td>20</td>
        <td>fd417cac-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-12-30 21:29:55</td>
        <td>2013-12-30 21:39:38</td>
        <td>4</td>
        <td>fd417d92-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-03-09 19:51:17</td>
        <td>2013-06-01 14:02:00</td>
        <td>23</td>
        <td>fd4188c8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-03-06 00:11:14</td>
        <td>2013-03-06 00:11:14</td>
        <td>1</td>
        <td>fd4189ae-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-03-12 01:47:44</td>
        <td>2013-03-12 02:19:25</td>
        <td>7</td>
        <td>fd418bde-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-03-07 00:10:29</td>
        <td>2013-03-08 02:04:14</td>
        <td>14</td>
        <td>fd418ef4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>1</td>
        <td>2014-12-19 21:34:26</td>
        <td>2014-12-19 21:45:43</td>
        <td>3</td>
        <td>fd4191ec-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>None</td>
        <td>2013-03-20 22:13:10</td>
        <td>2013-03-21 23:20:21</td>
        <td>17</td>
        <td>fd41967e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-03-13 19:32:05</td>
        <td>2013-03-20 15:04:39</td>
        <td>15</td>
        <td>fd4196ec-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-10-08 18:33:05</td>
        <td>2013-10-08 18:57:30</td>
        <td>7</td>
        <td>fd41a1aa-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-03-06 22:23:42</td>
        <td>2013-06-21 22:59:00</td>
        <td>28</td>
        <td>fd41a574-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-03-06 23:01:23</td>
        <td>2013-04-18 00:45:12</td>
        <td>12</td>
        <td>fd41a8a8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-03-18 15:43:42</td>
        <td>2013-03-18 20:53:15</td>
        <td>20</td>
        <td>fd41a952-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>40</td>
        <td>None</td>
        <td>2013-03-07 00:53:29</td>
        <td>2013-03-09 01:11:24</td>
        <td>20</td>
        <td>fd41acb8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-03-07 16:20:38</td>
        <td>2013-03-07 16:37:15</td>
        <td>3</td>
        <td>fd41b6ea-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>90</td>
        <td>None</td>
        <td>2013-07-06 00:14:06</td>
        <td>2013-07-06 00:17:49</td>
        <td>2</td>
        <td>fd41baaa-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-03-09 02:42:12</td>
        <td>2013-04-01 04:13:00</td>
        <td>20</td>
        <td>fd41bf6e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>None</td>
        <td>2013-11-04 20:19:25</td>
        <td>2015-03-27 16:26:49</td>
        <td>24</td>
        <td>fd41c108-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-03-09 02:52:13</td>
        <td>2013-03-17 22:59:55</td>
        <td>16</td>
        <td>fd41c4d2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2014-06-13 14:28:50</td>
        <td>2014-06-16 21:57:19</td>
        <td>14</td>
        <td>fd41c720-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-03-09 04:49:19</td>
        <td>2013-03-20 01:51:35</td>
        <td>20</td>
        <td>fd41c8b0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-05-01 01:06:02</td>
        <td>2014-02-13 02:19:36</td>
        <td>22</td>
        <td>fd41d030-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td>2013-03-10 01:16:20</td>
        <td>2013-09-05 18:22:20</td>
        <td>18</td>
        <td>fd41d0c6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-03-10 15:56:48</td>
        <td>2013-03-10 16:08:46</td>
        <td>4</td>
        <td>fd41d166-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-08-06 01:28:04</td>
        <td>2014-02-13 02:27:39</td>
        <td>22</td>
        <td>fd41d580-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-06-26 20:08:53</td>
        <td>2013-06-26 23:01:17</td>
        <td>6</td>
        <td>fd41d620-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-11-22 21:31:23</td>
        <td>2013-11-22 21:45:37</td>
        <td>4</td>
        <td>fd41d74c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-03-10 23:00:23</td>
        <td>2013-07-05 20:20:02</td>
        <td>20</td>
        <td>fd41d7b0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-03-11 23:46:34</td>
        <td>2013-03-12 00:15:40</td>
        <td>7</td>
        <td>fd41da08-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-03-24 14:01:43</td>
        <td>2014-02-15 17:26:50</td>
        <td>20</td>
        <td>fd41dad0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-03-12 01:17:46</td>
        <td>2014-03-30 23:12:52</td>
        <td>7</td>
        <td>fd41dc60-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-03-12 06:44:44</td>
        <td>2013-03-12 08:41:32</td>
        <td>20</td>
        <td>fd41dcc4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-03-25 00:25:35</td>
        <td>2015-07-21 23:16:18</td>
        <td>15</td>
        <td>fd41dd8c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>None</td>
        <td>2013-03-13 09:58:50</td>
        <td>2013-03-13 13:30:32</td>
        <td>20</td>
        <td>fd41df76-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>1</td>
        <td>2013-03-14 16:41:54</td>
        <td>2013-03-19 20:03:09</td>
        <td>20</td>
        <td>fd41e106-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-03-24 16:03:32</td>
        <td>2013-03-24 16:11:56</td>
        <td>4</td>
        <td>fd41e6ce-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-03-18 23:47:14</td>
        <td>2014-01-02 18:37:47</td>
        <td>23</td>
        <td>fd41ee6c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-02 20:38:41</td>
        <td>2013-05-02 21:08:12</td>
        <td>6</td>
        <td>fd41f0b0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-04-18 03:28:15</td>
        <td>2013-04-30 02:55:07</td>
        <td>6</td>
        <td>fd41f574-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-03-29 15:30:32</td>
        <td>2013-10-07 12:58:00</td>
        <td>20</td>
        <td>fd41f95c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-03-16 19:35:29</td>
        <td>2013-03-16 20:01:06</td>
        <td>4</td>
        <td>fd41fe20-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>60</td>
        <td>1</td>
        <td>2013-03-17 19:14:14</td>
        <td>2014-05-13 14:11:44</td>
        <td>37</td>
        <td>fd420276-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-03-15 22:04:01</td>
        <td>2013-04-25 03:30:52</td>
        <td>20</td>
        <td>fd4202f8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-04-20 22:42:18</td>
        <td>2013-04-20 23:10:15</td>
        <td>7</td>
        <td>fd42125c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-03-17 13:34:19</td>
        <td>2013-03-23 14:01:26</td>
        <td>14</td>
        <td>fd4214be-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-03-17 18:12:09</td>
        <td>2013-03-17 18:16:43</td>
        <td>2</td>
        <td>fd4215ea-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-03-18 01:16:40</td>
        <td>2013-03-18 01:27:22</td>
        <td>4</td>
        <td>fd4217d4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>1</td>
        <td>2015-05-16 20:48:46</td>
        <td>2015-05-23 15:52:40</td>
        <td>20</td>
        <td>fd421838-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2015-05-26 00:12:06</td>
        <td>2015-05-26 00:22:40</td>
        <td>4</td>
        <td>fd421a7c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-03-19 16:31:57</td>
        <td>2013-04-30 00:36:54</td>
        <td>20</td>
        <td>fd422148-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-03-19 16:56:00</td>
        <td>2013-04-08 00:21:08</td>
        <td>20</td>
        <td>fd4221ac-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>110</td>
        <td>None</td>
        <td>2013-03-28 10:56:41</td>
        <td>2013-03-28 11:01:48</td>
        <td>2</td>
        <td>fd4222ce-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-03-23 12:11:43</td>
        <td>2013-03-23 12:15:19</td>
        <td>2</td>
        <td>fd422576-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-21 19:06:47</td>
        <td>2014-03-18 20:30:25</td>
        <td>4</td>
        <td>fd4226d4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-03-25 03:48:45</td>
        <td>2013-03-27 04:43:36</td>
        <td>20</td>
        <td>fd423034-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-03-22 04:12:30</td>
        <td>2013-04-30 05:05:40</td>
        <td>20</td>
        <td>fd423098-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-03-26 01:01:34</td>
        <td>2013-04-02 02:04:01</td>
        <td>20</td>
        <td>fd423462-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-03-21 17:08:01</td>
        <td>2013-03-26 17:57:21</td>
        <td>11</td>
        <td>fd4234c6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-03-23 00:06:10</td>
        <td>2013-04-03 19:23:44</td>
        <td>20</td>
        <td>fd42358e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-03-21 23:44:12</td>
        <td>2013-03-23 00:25:17</td>
        <td>20</td>
        <td>fd4236b0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-03-30 01:33:06</td>
        <td>2013-05-01 00:53:36</td>
        <td>25</td>
        <td>fd423b42-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-03-22 18:54:01</td>
        <td>2013-03-22 19:04:28</td>
        <td>4</td>
        <td>fd423c0a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>70</td>
        <td>None</td>
        <td>2013-09-21 22:55:43</td>
        <td>2013-10-13 16:16:59</td>
        <td>7</td>
        <td>fd423e4e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-03-24 20:15:08</td>
        <td>2013-03-25 01:46:12</td>
        <td>20</td>
        <td>fd423eb2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-03-27 05:16:09</td>
        <td>2013-03-27 06:10:44</td>
        <td>10</td>
        <td>fd423fd4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-03-23 17:49:44</td>
        <td>2013-03-24 01:39:31</td>
        <td>20</td>
        <td>fd424092-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2014-05-25 23:33:31</td>
        <td>2014-05-25 23:38:22</td>
        <td>2</td>
        <td>fd42415a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-03-24 14:56:58</td>
        <td>2013-03-24 15:04:29</td>
        <td>2</td>
        <td>fd424218-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td>2013-03-24 17:53:41</td>
        <td>2013-03-30 21:14:53</td>
        <td>11</td>
        <td>fd424678-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>None</td>
        <td>2013-03-27 16:44:07</td>
        <td>2013-04-01 18:00:47</td>
        <td>20</td>
        <td>fd4246dc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-04-09 00:36:45</td>
        <td>2013-06-23 18:31:52</td>
        <td>20</td>
        <td>fd424862-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-03-24 17:21:23</td>
        <td>2013-03-29 18:45:00</td>
        <td>20</td>
        <td>fd4248d0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-03-24 19:06:31</td>
        <td>2013-03-24 19:19:55</td>
        <td>4</td>
        <td>fd424aba-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-03-24 20:40:04</td>
        <td>2013-03-24 20:44:22</td>
        <td>2</td>
        <td>fd424b1e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-03-24 20:58:10</td>
        <td>2013-03-24 21:12:18</td>
        <td>4</td>
        <td>fd424b78-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-06-24 02:19:58</td>
        <td>2013-06-24 02:19:58</td>
        <td>1</td>
        <td>fd424f9c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>70</td>
        <td>None</td>
        <td>2013-03-25 22:36:35</td>
        <td>2013-03-28 21:19:49</td>
        <td>7</td>
        <td>fd4258ca-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-03-28 02:06:12</td>
        <td>2013-03-31 01:43:10</td>
        <td>11</td>
        <td>fd425e74-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>0</td>
        <td>None</td>
        <td>2014-07-31 19:37:19</td>
        <td>2014-08-05 19:46:01</td>
        <td>20</td>
        <td>fd426bf8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-04-03 23:54:38</td>
        <td>2013-04-05 00:22:11</td>
        <td>6</td>
        <td>fd4271fc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>None</td>
        <td>2013-03-26 23:35:56</td>
        <td>2013-04-23 02:19:38</td>
        <td>6</td>
        <td>fd42727e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-03-30 13:44:52</td>
        <td>2013-04-09 00:40:45</td>
        <td>20</td>
        <td>fd42740e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>80</td>
        <td>None</td>
        <td>2013-03-28 01:31:42</td>
        <td>2013-03-28 01:31:42</td>
        <td>1</td>
        <td>fd427616-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-04-06 14:46:12</td>
        <td>2013-04-08 00:06:31</td>
        <td>11</td>
        <td>fd427742-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-03-29 12:35:33</td>
        <td>2013-03-29 14:36:55</td>
        <td>20</td>
        <td>fd427b48-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>None</td>
        <td>2013-03-28 23:31:19</td>
        <td>2013-03-30 05:52:01</td>
        <td>20</td>
        <td>fd427d96-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-08-08 00:40:19</td>
        <td>2013-08-13 21:30:29</td>
        <td>14</td>
        <td>fd428124-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-06-25 23:55:21</td>
        <td>2013-06-26 00:10:42</td>
        <td>4</td>
        <td>fd4281f6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-04-12 23:29:07</td>
        <td>2013-05-09 23:59:12</td>
        <td>10</td>
        <td>fd428386-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-04-13 00:53:18</td>
        <td>2013-04-13 00:53:18</td>
        <td>1</td>
        <td>fd4283ea-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>None</td>
        <td>2013-03-29 20:45:05</td>
        <td>2013-03-29 22:35:34</td>
        <td>20</td>
        <td>fd428520-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-03-29 23:53:30</td>
        <td>2013-04-01 05:14:29</td>
        <td>20</td>
        <td>fd428714-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2014-01-13 18:31:17</td>
        <td>2015-07-08 02:18:53</td>
        <td>16</td>
        <td>fd428886-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2014-01-13 18:57:25</td>
        <td>2014-02-10 20:48:23</td>
        <td>11</td>
        <td>fd428a5c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-03-30 18:12:43</td>
        <td>2013-03-30 18:23:08</td>
        <td>4</td>
        <td>fd42906a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-04-01 23:26:36</td>
        <td>2013-04-21 17:24:42</td>
        <td>20</td>
        <td>fd429204-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-04-01 01:38:04</td>
        <td>2013-11-19 15:12:10</td>
        <td>20</td>
        <td>fd4292d6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-04-01 01:06:58</td>
        <td>2013-05-05 18:47:37</td>
        <td>20</td>
        <td>fd42939e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-04-01 00:46:21</td>
        <td>2013-04-06 01:59:25</td>
        <td>20</td>
        <td>fd4296d2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-10 06:22:47</td>
        <td>2013-05-12 02:17:59</td>
        <td>9</td>
        <td>fd429bf0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>10</td>
        <td>None</td>
        <td>2013-04-02 22:56:43</td>
        <td>2013-04-26 03:24:37</td>
        <td>20</td>
        <td>fd429cb8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-05-24 20:28:58</td>
        <td>2013-05-24 20:56:12</td>
        <td>11</td>
        <td>fd42a10e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-04-07 15:47:25</td>
        <td>2013-04-12 14:55:02</td>
        <td>20</td>
        <td>fd42a302-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-04-07 21:08:59</td>
        <td>2014-08-17 20:27:15</td>
        <td>45</td>
        <td>fd42a8c0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-04-07 15:30:44</td>
        <td>2013-04-25 22:56:40</td>
        <td>15</td>
        <td>fd42a992-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-04-07 21:40:49</td>
        <td>2013-04-08 03:15:53</td>
        <td>11</td>
        <td>fd42aac8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-04-09 04:05:23</td>
        <td>2013-12-02 17:33:45</td>
        <td>21</td>
        <td>fd42b32e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-04-13 16:23:54</td>
        <td>2013-04-14 18:19:46</td>
        <td>20</td>
        <td>fd42bc66-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-04-11 03:06:51</td>
        <td>2013-05-23 02:27:55</td>
        <td>20</td>
        <td>fd42c0e4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2014-06-10 21:02:06</td>
        <td>2014-06-11 01:10:42</td>
        <td>20</td>
        <td>fd42c7ec-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-04-16 21:54:40</td>
        <td>2014-09-01 17:49:56</td>
        <td>45</td>
        <td>fd42dd22-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-04-15 21:53:44</td>
        <td>2013-04-15 21:56:59</td>
        <td>2</td>
        <td>fd42dd90-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-04-23 22:05:52</td>
        <td>2013-04-23 22:12:41</td>
        <td>3</td>
        <td>fd42e060-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-06-04 16:34:05</td>
        <td>2013-06-04 16:55:36</td>
        <td>5</td>
        <td>fd42e204-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>None</td>
        <td>2013-04-17 06:21:30</td>
        <td>2014-01-31 22:47:59</td>
        <td>4</td>
        <td>fd42e39e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-04-16 23:28:17</td>
        <td>2014-02-08 02:51:47</td>
        <td>18</td>
        <td>fd42e4de-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-08-22 21:09:21</td>
        <td>2013-08-22 21:28:50</td>
        <td>4</td>
        <td>fd42e678-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>80</td>
        <td>None</td>
        <td>2013-11-02 04:57:22</td>
        <td>2013-11-02 05:22:51</td>
        <td>7</td>
        <td>fd42e74a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-04-20 15:40:19</td>
        <td>2013-06-02 19:09:03</td>
        <td>20</td>
        <td>fd42eb50-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-04-18 01:16:05</td>
        <td>2013-04-23 03:02:55</td>
        <td>20</td>
        <td>fd42f122-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-04-19 22:54:29</td>
        <td>2013-08-09 01:02:00</td>
        <td>20</td>
        <td>fd42f2f8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-04-19 23:09:21</td>
        <td>2013-08-09 00:54:42</td>
        <td>20</td>
        <td>fd42f38e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-07 23:28:14</td>
        <td>2013-05-11 20:08:43</td>
        <td>20</td>
        <td>fd42f51e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>None</td>
        <td>2013-04-28 16:42:09</td>
        <td>2013-05-04 20:29:36</td>
        <td>20</td>
        <td>fd42f5be-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-07 00:26:19</td>
        <td>2013-05-21 00:46:35</td>
        <td>20</td>
        <td>fd42f8c0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>40</td>
        <td>None</td>
        <td>2013-04-19 22:14:24</td>
        <td>2013-04-25 00:25:12</td>
        <td>20</td>
        <td>fd42f992-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-04-20 01:44:59</td>
        <td>2013-04-20 02:11:16</td>
        <td>7</td>
        <td>fd42fe06-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>60</td>
        <td>None</td>
        <td>2013-04-21 19:20:54</td>
        <td>2014-03-24 01:58:33</td>
        <td>20</td>
        <td>fd430068-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-04-21 20:52:51</td>
        <td>2013-04-21 21:08:16</td>
        <td>4</td>
        <td>fd4300d6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-06-14 03:07:01</td>
        <td>2013-06-14 03:59:01</td>
        <td>11</td>
        <td>fd43013a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-04-22 19:20:11</td>
        <td>2013-04-22 19:20:11</td>
        <td>1</td>
        <td>fd430536-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-04-22 23:10:47</td>
        <td>2013-04-23 00:06:12</td>
        <td>7</td>
        <td>fd43066c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-05-04 16:26:30</td>
        <td>2013-05-04 16:53:32</td>
        <td>6</td>
        <td>fd4308d8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-04-23 00:20:18</td>
        <td>2013-04-27 22:31:00</td>
        <td>7</td>
        <td>fd430e28-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-05-27 23:44:30</td>
        <td>2013-07-17 22:14:13</td>
        <td>20</td>
        <td>fd431102-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>40</td>
        <td>None</td>
        <td>2013-04-23 02:05:48</td>
        <td>2013-04-23 02:19:57</td>
        <td>4</td>
        <td>fd431170-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-04-24 04:04:48</td>
        <td>2013-05-14 04:34:59</td>
        <td>6</td>
        <td>fd431800-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-04-23 06:05:42</td>
        <td>2013-04-23 15:50:33</td>
        <td>5</td>
        <td>fd431904-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-04-23 06:32:28</td>
        <td>2013-05-30 05:51:15</td>
        <td>20</td>
        <td>fd4319e0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>1</td>
        <td>2013-12-22 23:39:48</td>
        <td>2014-02-08 23:36:49</td>
        <td>15</td>
        <td>fd431ddc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>80</td>
        <td>None</td>
        <td>2013-04-24 00:17:22</td>
        <td>2014-02-13 18:39:17</td>
        <td>23</td>
        <td>fd432bf6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2014-03-27 19:25:50</td>
        <td>2014-03-27 19:29:06</td>
        <td>2</td>
        <td>fd433ce0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-08-15 16:14:30</td>
        <td>2013-08-15 16:28:07</td>
        <td>4</td>
        <td>fd433d58-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-04-24 22:11:58</td>
        <td>2013-10-06 20:07:04</td>
        <td>13</td>
        <td>fd433dbc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-24 13:38:30</td>
        <td>2013-08-20 12:47:52</td>
        <td>20</td>
        <td>fd433e16-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-08-25 18:39:01</td>
        <td>2013-08-25 18:53:32</td>
        <td>4</td>
        <td>fd433fec-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-04-25 00:46:01</td>
        <td>2013-05-02 01:02:08</td>
        <td>16</td>
        <td>fd4341ea-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-07-08 22:52:37</td>
        <td>2013-07-28 01:49:30</td>
        <td>6</td>
        <td>fd43424e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-04-23 23:56:20</td>
        <td>2014-12-01 00:48:15</td>
        <td>16</td>
        <td>fd43458c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-04-23 17:11:32</td>
        <td>2013-05-05 22:39:55</td>
        <td>11</td>
        <td>fd4345f0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-04-23 22:40:00</td>
        <td>2013-04-23 22:49:49</td>
        <td>4</td>
        <td>fd434654-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-18 14:39:42</td>
        <td>2013-05-19 15:58:36</td>
        <td>7</td>
        <td>fd43471c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-27 22:41:44</td>
        <td>2013-06-26 19:37:09</td>
        <td>9</td>
        <td>fd4347ee-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-04-29 21:33:03</td>
        <td>2013-05-04 15:34:29</td>
        <td>6</td>
        <td>fd434bf4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-04-24 04:02:55</td>
        <td>2014-10-21 02:48:44</td>
        <td>24</td>
        <td>fd434d8e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>80</td>
        <td>None</td>
        <td>2013-04-27 01:49:45</td>
        <td>2013-06-14 21:28:49</td>
        <td>20</td>
        <td>fd434df2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>None</td>
        <td>2013-04-23 20:29:26</td>
        <td>2014-05-24 13:51:49</td>
        <td>31</td>
        <td>fd435568-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>40</td>
        <td>None</td>
        <td>2013-04-23 21:37:28</td>
        <td>2013-04-27 16:33:34</td>
        <td>14</td>
        <td>fd4357de-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-04-23 22:17:40</td>
        <td>2013-04-24 03:23:01</td>
        <td>14</td>
        <td>fd4359be-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>80</td>
        <td>None</td>
        <td>2013-05-05 19:51:33</td>
        <td>2013-10-27 17:45:40</td>
        <td>20</td>
        <td>fd435b8a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-04-23 23:17:27</td>
        <td>2013-04-28 00:17:16</td>
        <td>7</td>
        <td>fd435cca-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-04-23 23:53:55</td>
        <td>2013-04-28 00:35:58</td>
        <td>7</td>
        <td>fd435d2e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-02 00:50:08</td>
        <td>2013-05-02 01:02:33</td>
        <td>4</td>
        <td>fd435ed2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-04-27 03:40:54</td>
        <td>2013-04-27 03:53:02</td>
        <td>4</td>
        <td>fd435ffe-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-11 16:14:56</td>
        <td>2013-06-05 01:03:06</td>
        <td>17</td>
        <td>fd436210-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-04 17:16:51</td>
        <td>2013-05-13 00:17:27</td>
        <td>20</td>
        <td>fd43633c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-08-10 19:30:47</td>
        <td>2013-08-13 23:30:34</td>
        <td>4</td>
        <td>fd4363a0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>0</td>
        <td>None</td>
        <td>2013-04-25 00:30:19</td>
        <td>2014-03-29 15:11:18</td>
        <td>11</td>
        <td>fd436472-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-04-24 02:26:23</td>
        <td>2013-04-24 02:55:21</td>
        <td>6</td>
        <td>fd436616-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-04-25 02:24:39</td>
        <td>2013-05-06 02:54:02</td>
        <td>20</td>
        <td>fd4368dc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-08-12 00:03:44</td>
        <td>2013-08-12 00:15:34</td>
        <td>4</td>
        <td>fd436ae4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>90</td>
        <td>None</td>
        <td>2014-12-17 22:14:35</td>
        <td>2014-12-17 22:14:35</td>
        <td>1</td>
        <td>fd436d46-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-22 16:23:29</td>
        <td>2013-05-22 17:24:27</td>
        <td>6</td>
        <td>fd436daa-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-04-26 01:02:35</td>
        <td>2013-05-20 01:09:15</td>
        <td>20</td>
        <td>fd436f44-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-04-24 16:16:58</td>
        <td>2013-04-24 16:28:46</td>
        <td>4</td>
        <td>fd43723c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>100</td>
        <td>None</td>
        <td>2013-04-25 01:04:10</td>
        <td>2013-04-27 17:10:10</td>
        <td>11</td>
        <td>fd43744e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-04-24 17:06:25</td>
        <td>2013-05-01 17:31:36</td>
        <td>20</td>
        <td>fd437584-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>None</td>
        <td>2013-04-24 18:02:57</td>
        <td>2013-04-24 18:12:18</td>
        <td>4</td>
        <td>fd4378a4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-04-24 21:13:27</td>
        <td>2013-05-21 20:37:28</td>
        <td>14</td>
        <td>fd437e58-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-04-24 22:25:46</td>
        <td>2013-09-09 22:28:13</td>
        <td>28</td>
        <td>fd4385ec-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-08-02 23:53:13</td>
        <td>2013-08-03 00:07:01</td>
        <td>4</td>
        <td>fd4391d6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>None</td>
        <td>2013-04-25 01:24:13</td>
        <td>2013-04-25 01:34:50</td>
        <td>4</td>
        <td>fd439dfc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-04-24 23:21:11</td>
        <td>2014-05-11 23:37:14</td>
        <td>14</td>
        <td>fd439f3c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-05-05 15:56:38</td>
        <td>2013-05-05 16:31:52</td>
        <td>5</td>
        <td>fd43a004-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>1</td>
        <td>2013-04-25 02:05:40</td>
        <td>2014-05-31 01:01:56</td>
        <td>20</td>
        <td>fd43a202-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-04-25 13:17:37</td>
        <td>2013-04-25 15:20:29</td>
        <td>20</td>
        <td>fd43a464-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>None</td>
        <td>2013-04-25 14:41:35</td>
        <td>2013-06-17 00:03:40</td>
        <td>11</td>
        <td>fd43a536-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-04-26 21:09:12</td>
        <td>2013-08-04 19:23:02</td>
        <td>20</td>
        <td>fd43a5fe-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-04-25 17:27:27</td>
        <td>2013-08-27 17:30:54</td>
        <td>20</td>
        <td>fd43a78e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-04-26 00:17:11</td>
        <td>2013-05-11 17:04:42</td>
        <td>20</td>
        <td>fd43ad60-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>1</td>
        <td>2013-04-26 00:11:31</td>
        <td>2013-04-26 01:56:09</td>
        <td>20</td>
        <td>fd43aef0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-04-27 02:56:04</td>
        <td>2013-05-05 19:57:39</td>
        <td>6</td>
        <td>fd43afc2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-04-26 01:15:57</td>
        <td>2014-12-26 02:21:28</td>
        <td>20</td>
        <td>fd43b0ee-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-04-26 02:07:43</td>
        <td>2013-05-01 02:20:20</td>
        <td>7</td>
        <td>fd43b152-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>60</td>
        <td>None</td>
        <td>2013-04-27 03:54:47</td>
        <td>2013-06-23 23:36:38</td>
        <td>20</td>
        <td>fd43b210-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-04-26 02:58:05</td>
        <td>2013-04-30 01:42:35</td>
        <td>20</td>
        <td>fd43b27e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>80</td>
        <td>None</td>
        <td>2013-05-08 19:01:13</td>
        <td>2013-08-01 15:13:09</td>
        <td>12</td>
        <td>fd43b3aa-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2014-04-03 01:10:54</td>
        <td>2014-04-04 01:23:05</td>
        <td>4</td>
        <td>fd43b512-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-06 14:10:47</td>
        <td>2013-06-20 15:26:41</td>
        <td>14</td>
        <td>fd43b6b6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>1</td>
        <td>2013-05-06 14:18:38</td>
        <td>2013-06-20 15:21:17</td>
        <td>14</td>
        <td>fd43b756-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>None</td>
        <td>2013-04-28 14:15:56</td>
        <td>2013-06-01 20:24:27</td>
        <td>20</td>
        <td>fd43b896-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-04-29 16:37:51</td>
        <td>2013-05-04 16:18:14</td>
        <td>20</td>
        <td>fd43bfee-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-04-28 04:19:31</td>
        <td>2013-05-26 23:42:30</td>
        <td>20</td>
        <td>fd43c1f6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-04-27 13:18:49</td>
        <td>2013-04-27 13:29:17</td>
        <td>4</td>
        <td>fd43c386-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-04-28 22:07:15</td>
        <td>2013-04-28 22:41:40</td>
        <td>7</td>
        <td>fd43c3ea-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-04-27 18:53:52</td>
        <td>2013-04-27 21:08:15</td>
        <td>20</td>
        <td>fd43c70a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-04-28 10:29:07</td>
        <td>2013-08-05 18:29:40</td>
        <td>20</td>
        <td>fd43c76e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-04-27 21:56:14</td>
        <td>2013-04-30 02:57:15</td>
        <td>20</td>
        <td>fd43c890-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-04-27 21:59:21</td>
        <td>2013-04-28 23:43:42</td>
        <td>10</td>
        <td>fd43c8f4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-04-27 23:01:04</td>
        <td>2013-04-28 05:29:20</td>
        <td>20</td>
        <td>fd43c958-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-06 03:40:30</td>
        <td>2013-05-20 01:15:42</td>
        <td>4</td>
        <td>fd43ca84-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-08-09 00:32:37</td>
        <td>2013-08-09 01:13:35</td>
        <td>7</td>
        <td>fd43cd40-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-04-28 14:42:23</td>
        <td>2013-04-28 19:38:17</td>
        <td>11</td>
        <td>fd43cda4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-01 00:55:53</td>
        <td>2013-07-23 19:34:24</td>
        <td>30</td>
        <td>fd43ce08-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-04-28 18:16:49</td>
        <td>2013-05-03 00:20:38</td>
        <td>20</td>
        <td>fd43cf98-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-05-04 01:14:15</td>
        <td>2013-05-25 17:10:01</td>
        <td>5</td>
        <td>fd43d362-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-04-28 19:52:23</td>
        <td>2013-08-04 03:26:33</td>
        <td>20</td>
        <td>fd43d42a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>10</td>
        <td>None</td>
        <td>2013-08-10 15:00:03</td>
        <td>2013-08-10 15:00:03</td>
        <td>1</td>
        <td>fd43d4e8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-04-28 22:04:01</td>
        <td>2013-05-12 01:53:27</td>
        <td>5</td>
        <td>fd43d54c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-04-28 23:00:26</td>
        <td>2013-04-28 23:13:07</td>
        <td>4</td>
        <td>fd43d66e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-04-29 12:23:56</td>
        <td>2013-05-29 00:50:12</td>
        <td>22</td>
        <td>fd43d736-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-16 01:50:22</td>
        <td>2013-08-08 00:40:47</td>
        <td>7</td>
        <td>fd43d7a4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-04-29 04:10:58</td>
        <td>2013-04-29 04:22:42</td>
        <td>4</td>
        <td>fd43d862-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-04-29 03:39:43</td>
        <td>2013-04-29 04:00:47</td>
        <td>4</td>
        <td>fd43d8c6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>None</td>
        <td>2013-04-29 20:25:31</td>
        <td>2013-05-08 23:36:55</td>
        <td>20</td>
        <td>fd43da9c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-04-30 01:40:32</td>
        <td>2013-05-23 23:55:09</td>
        <td>16</td>
        <td>fd43db50-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-17 23:47:58</td>
        <td>2013-07-18 00:48:35</td>
        <td>11</td>
        <td>fd43e028-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-04-30 23:59:45</td>
        <td>2013-05-01 00:08:20</td>
        <td>2</td>
        <td>fd43e5c8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-01 02:50:16</td>
        <td>2013-05-02 04:02:22</td>
        <td>11</td>
        <td>fd43f608-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-01 01:34:45</td>
        <td>2013-05-02 00:07:39</td>
        <td>13</td>
        <td>fd43f8d8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-01 16:40:48</td>
        <td>2013-07-07 13:45:01</td>
        <td>7</td>
        <td>fd43fc02-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-02 18:47:29</td>
        <td>2013-06-28 21:37:47</td>
        <td>10</td>
        <td>fd4403c8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-07-18 20:35:32</td>
        <td>2013-07-18 20:38:57</td>
        <td>2</td>
        <td>fd44074c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-03 02:22:31</td>
        <td>2013-06-23 02:49:48</td>
        <td>20</td>
        <td>fd440882-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-05 20:29:06</td>
        <td>2013-05-25 16:05:27</td>
        <td>7</td>
        <td>fd4408e6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-10 17:13:07</td>
        <td>2013-05-10 22:12:08</td>
        <td>3</td>
        <td>fd440a12-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-06 22:34:22</td>
        <td>2013-05-06 23:46:08</td>
        <td>20</td>
        <td>fd440ba2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-04 18:28:28</td>
        <td>2013-05-04 20:12:57</td>
        <td>20</td>
        <td>fd440c9c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>1</td>
        <td>2013-05-03 21:03:36</td>
        <td>2013-06-10 00:19:57</td>
        <td>25</td>
        <td>fd441034-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-04 06:56:41</td>
        <td>2014-04-24 17:28:39</td>
        <td>11</td>
        <td>fd4410a2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-02 17:39:48</td>
        <td>2013-05-02 17:49:50</td>
        <td>4</td>
        <td>fd44135e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-12-14 22:02:34</td>
        <td>2013-12-14 22:13:53</td>
        <td>4</td>
        <td>fd4413c2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-02 18:25:16</td>
        <td>2013-05-04 19:28:35</td>
        <td>18</td>
        <td>fd441426-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>80</td>
        <td>None</td>
        <td>2013-06-10 22:11:31</td>
        <td>2013-06-10 22:40:49</td>
        <td>6</td>
        <td>fd44148a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>None</td>
        <td>2013-05-02 19:27:27</td>
        <td>2013-06-02 20:54:53</td>
        <td>19</td>
        <td>fd4414ee-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-02 20:14:51</td>
        <td>2013-05-02 20:25:08</td>
        <td>2</td>
        <td>fd44161a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>70</td>
        <td>None</td>
        <td>2013-05-02 21:22:06</td>
        <td>2013-05-02 21:26:29</td>
        <td>2</td>
        <td>fd4418f4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>None</td>
        <td>2013-05-03 00:38:26</td>
        <td>2013-05-17 01:36:02</td>
        <td>20</td>
        <td>fd441c3c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-02 23:22:19</td>
        <td>2013-05-02 23:22:19</td>
        <td>1</td>
        <td>fd441ea8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-16 02:03:45</td>
        <td>2013-08-13 03:04:00</td>
        <td>7</td>
        <td>fd441f3e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-05-02 23:50:49</td>
        <td>2013-05-16 23:56:43</td>
        <td>15</td>
        <td>fd441fde-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-03 23:37:34</td>
        <td>2013-07-12 23:17:44</td>
        <td>20</td>
        <td>fd442074-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-03 00:54:51</td>
        <td>2013-05-03 01:38:16</td>
        <td>10</td>
        <td>fd4421aa-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-05 20:40:53</td>
        <td>2013-09-08 16:00:30</td>
        <td>11</td>
        <td>fd442308-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-03 03:43:06</td>
        <td>2013-05-07 06:44:59</td>
        <td>18</td>
        <td>fd44256a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2014-09-19 14:07:37</td>
        <td>2014-09-19 15:17:36</td>
        <td>7</td>
        <td>fd442826-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-05 19:03:52</td>
        <td>2013-06-08 18:34:29</td>
        <td>14</td>
        <td>fd4428ee-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-03 17:37:14</td>
        <td>2015-01-29 19:54:10</td>
        <td>20</td>
        <td>fd442e66-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-03 23:32:06</td>
        <td>2013-07-18 20:50:34</td>
        <td>25</td>
        <td>fd442f38-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-04 20:01:29</td>
        <td>2013-05-04 20:08:15</td>
        <td>3</td>
        <td>fd442f9c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-03 20:06:18</td>
        <td>2013-05-16 01:31:49</td>
        <td>20</td>
        <td>fd443000-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>None</td>
        <td>2013-05-03 22:12:17</td>
        <td>2013-05-03 22:35:25</td>
        <td>6</td>
        <td>fd44319a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-04 20:51:31</td>
        <td>2013-05-23 16:44:26</td>
        <td>10</td>
        <td>fd4431fe-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-05-18 18:15:09</td>
        <td>2013-05-18 19:22:11</td>
        <td>4</td>
        <td>fd443262-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-04 01:02:57</td>
        <td>2013-05-04 01:07:26</td>
        <td>2</td>
        <td>fd44332a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>80</td>
        <td>None</td>
        <td>2013-05-04 01:04:45</td>
        <td>2013-07-12 01:32:16</td>
        <td>4</td>
        <td>fd44338e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-07 17:32:26</td>
        <td>2013-06-29 17:32:48</td>
        <td>20</td>
        <td>fd44344c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-04 07:45:18</td>
        <td>2013-08-22 13:18:09</td>
        <td>20</td>
        <td>fd44351e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-06 17:17:40</td>
        <td>2013-06-01 19:07:03</td>
        <td>8</td>
        <td>fd443ae6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-21 00:42:00</td>
        <td>2013-05-22 05:48:51</td>
        <td>20</td>
        <td>fd443b54-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-04 21:14:14</td>
        <td>2013-05-07 00:46:42</td>
        <td>7</td>
        <td>fd443c26-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-06-15 19:43:45</td>
        <td>2013-07-08 22:33:41</td>
        <td>20</td>
        <td>fd443c94-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-05 01:29:23</td>
        <td>2013-05-05 02:53:25</td>
        <td>20</td>
        <td>fd443e88-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-08 00:50:14</td>
        <td>2013-05-19 05:05:01</td>
        <td>16</td>
        <td>fd444202-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-05 21:11:27</td>
        <td>2013-05-06 23:43:18</td>
        <td>7</td>
        <td>fd444266-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-05-05 12:10:03</td>
        <td>2013-05-05 12:21:15</td>
        <td>4</td>
        <td>fd444432-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>90</td>
        <td>None</td>
        <td>2013-05-05 14:32:28</td>
        <td>2013-05-05 15:35:16</td>
        <td>7</td>
        <td>fd444892-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-05 17:42:03</td>
        <td>2013-05-05 17:56:28</td>
        <td>4</td>
        <td>fd445b7a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>90</td>
        <td>1</td>
        <td>2013-05-12 18:19:52</td>
        <td>2014-10-28 21:05:06</td>
        <td>14</td>
        <td>fd446890-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-05 23:56:17</td>
        <td>2013-05-12 23:02:46</td>
        <td>20</td>
        <td>fd446bc4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2015-05-31 01:00:09</td>
        <td>2015-05-31 01:00:09</td>
        <td>1</td>
        <td>fd446c82-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-06 03:44:55</td>
        <td>2013-05-06 03:59:57</td>
        <td>4</td>
        <td>fd446ce6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-06-23 19:45:55</td>
        <td>2013-06-23 19:54:41</td>
        <td>2</td>
        <td>fd446dae-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-06 11:18:10</td>
        <td>2013-05-06 11:45:48</td>
        <td>7</td>
        <td>fd446e08-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>100</td>
        <td>None</td>
        <td>2013-05-25 15:33:04</td>
        <td>2013-05-25 15:33:04</td>
        <td>1</td>
        <td>fd446e76-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-06-02 16:47:34</td>
        <td>2013-10-28 20:36:33</td>
        <td>20</td>
        <td>fd446ed0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-25 14:30:41</td>
        <td>2013-11-17 20:49:08</td>
        <td>20</td>
        <td>fd446f34-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>70</td>
        <td>None</td>
        <td>2013-05-07 23:01:41</td>
        <td>2014-01-02 21:38:46</td>
        <td>4</td>
        <td>fd446ffc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-07 15:07:41</td>
        <td>2013-05-28 20:06:28</td>
        <td>6</td>
        <td>fd447060-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-06-01 18:57:54</td>
        <td>2013-06-08 21:14:06</td>
        <td>20</td>
        <td>fd447308-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>30</td>
        <td>None</td>
        <td>2013-05-06 21:37:25</td>
        <td>2013-05-06 21:40:41</td>
        <td>2</td>
        <td>fd44736c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>60</td>
        <td>None</td>
        <td>2013-06-11 23:34:24</td>
        <td>2013-10-29 02:31:44</td>
        <td>11</td>
        <td>fd4473d0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-07-03 23:50:26</td>
        <td>2013-10-29 02:05:37</td>
        <td>20</td>
        <td>fd44754c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-05-07 02:55:16</td>
        <td>2013-06-03 05:17:43</td>
        <td>16</td>
        <td>fd4475b0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-07 06:33:30</td>
        <td>2013-06-10 04:53:30</td>
        <td>25</td>
        <td>fd44766e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>70</td>
        <td>None</td>
        <td>2013-05-08 05:12:23</td>
        <td>2013-05-08 05:31:23</td>
        <td>4</td>
        <td>fd447916-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>30</td>
        <td>None</td>
        <td>2013-05-07 23:30:47</td>
        <td>2013-09-14 16:20:22</td>
        <td>14</td>
        <td>fd447a9c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-07 22:59:06</td>
        <td>2015-07-18 18:06:19</td>
        <td>9</td>
        <td>fd447d9e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-08 02:27:28</td>
        <td>2013-05-14 00:35:54</td>
        <td>16</td>
        <td>fd44808c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-11 15:02:03</td>
        <td>2013-05-11 15:27:59</td>
        <td>7</td>
        <td>fd448122-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-08 01:25:10</td>
        <td>2013-05-08 01:39:32</td>
        <td>4</td>
        <td>fd4482ee-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-21 17:36:40</td>
        <td>2013-05-24 01:18:18</td>
        <td>7</td>
        <td>fd4485d2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-12 17:39:22</td>
        <td>2013-05-20 17:39:42</td>
        <td>11</td>
        <td>fd4486a4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-14 00:28:58</td>
        <td>2013-06-30 00:42:28</td>
        <td>20</td>
        <td>fd4487c6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-28 19:26:18</td>
        <td>2013-05-28 19:53:29</td>
        <td>5</td>
        <td>fd4488f2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-05-09 01:11:44</td>
        <td>2013-05-09 02:21:10</td>
        <td>6</td>
        <td>fd448a1e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-09 01:28:24</td>
        <td>2013-05-14 02:02:29</td>
        <td>20</td>
        <td>fd448a82-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-09 03:30:44</td>
        <td>2015-01-19 23:38:18</td>
        <td>7</td>
        <td>fd448ae6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-10 15:58:37</td>
        <td>2013-11-09 19:06:58</td>
        <td>20</td>
        <td>fd448b4a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-05-13 04:19:01</td>
        <td>2013-05-13 21:33:29</td>
        <td>20</td>
        <td>fd448cda-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-09 23:50:44</td>
        <td>2013-09-01 16:44:26</td>
        <td>18</td>
        <td>fd448e7e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-16 21:01:58</td>
        <td>2013-07-12 22:51:53</td>
        <td>11</td>
        <td>fd448f46-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-31 00:58:20</td>
        <td>2013-09-28 21:42:27</td>
        <td>5</td>
        <td>fd449266-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2014-01-18 15:58:02</td>
        <td>2014-01-18 16:24:40</td>
        <td>7</td>
        <td>fd449324-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>60</td>
        <td>None</td>
        <td>2013-06-12 00:18:47</td>
        <td>2013-06-12 00:18:47</td>
        <td>1</td>
        <td>fd4493e2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-07-06 14:23:29</td>
        <td>2013-09-29 19:55:53</td>
        <td>20</td>
        <td>fd4494aa-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-06-04 21:03:55</td>
        <td>2013-06-04 21:22:43</td>
        <td>4</td>
        <td>fd44963a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-12 23:40:04</td>
        <td>2013-05-13 00:31:01</td>
        <td>11</td>
        <td>fd449702-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-12 23:43:34</td>
        <td>2013-05-13 02:04:32</td>
        <td>5</td>
        <td>fd44975c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-05-10 17:23:29</td>
        <td>2014-05-18 16:02:28</td>
        <td>29</td>
        <td>fd44987e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-05-12 16:47:20</td>
        <td>2013-05-12 17:02:08</td>
        <td>4</td>
        <td>fd449c2a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-26 21:59:08</td>
        <td>2013-06-08 18:28:41</td>
        <td>13</td>
        <td>fd449d56-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-05-11 17:20:13</td>
        <td>2013-05-13 03:12:44</td>
        <td>7</td>
        <td>fd449dba-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-30 19:02:14</td>
        <td>2013-05-30 19:45:22</td>
        <td>4</td>
        <td>fd449edc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-12 03:02:04</td>
        <td>2014-04-05 06:09:38</td>
        <td>15</td>
        <td>fd44a012-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-17 01:56:48</td>
        <td>2013-05-17 02:15:27</td>
        <td>4</td>
        <td>fd44a2a6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-12 14:30:27</td>
        <td>2013-05-12 15:24:12</td>
        <td>14</td>
        <td>fd44a558-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-12 18:56:47</td>
        <td>2013-05-28 00:14:28</td>
        <td>10</td>
        <td>fd44a710-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-05-14 00:35:59</td>
        <td>2013-05-14 18:45:50</td>
        <td>4</td>
        <td>fd44ab02-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-07 13:08:08</td>
        <td>2013-07-07 14:36:23</td>
        <td>11</td>
        <td>fd44ab66-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-07 12:18:46</td>
        <td>2013-07-21 15:30:52</td>
        <td>15</td>
        <td>fd44abca-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-12 18:17:52</td>
        <td>2013-07-04 14:36:01</td>
        <td>20</td>
        <td>fd44ac24-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-12 18:47:20</td>
        <td>2013-07-07 18:41:21</td>
        <td>20</td>
        <td>fd44aec2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-12 14:41:40</td>
        <td>2013-05-12 15:35:35</td>
        <td>10</td>
        <td>fd44af58-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-12 22:37:53</td>
        <td>2014-06-25 03:00:21</td>
        <td>20</td>
        <td>fd44b034-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-08-19 23:48:09</td>
        <td>2013-08-20 00:00:05</td>
        <td>4</td>
        <td>fd44b386-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-20 10:16:20</td>
        <td>2013-05-20 10:20:57</td>
        <td>2</td>
        <td>fd44c088-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>10</td>
        <td>None</td>
        <td>2013-08-10 22:03:10</td>
        <td>2013-08-11 00:19:44</td>
        <td>3</td>
        <td>fd44c628-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-13 22:53:21</td>
        <td>2013-05-13 23:08:20</td>
        <td>4</td>
        <td>fd44c920-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-12 23:02:33</td>
        <td>2013-05-12 23:26:05</td>
        <td>7</td>
        <td>fd44c984-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-07-26 23:49:25</td>
        <td>2013-07-27 00:14:15</td>
        <td>4</td>
        <td>fd44c9e8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-16 23:08:00</td>
        <td>2013-07-30 00:27:33</td>
        <td>20</td>
        <td>fd44cb0a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-14 00:58:28</td>
        <td>2013-05-19 22:03:23</td>
        <td>14</td>
        <td>fd44ccfe-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-19 01:28:56</td>
        <td>2013-05-19 22:42:07</td>
        <td>10</td>
        <td>fd44cd62-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-14 01:09:06</td>
        <td>2013-07-02 02:32:08</td>
        <td>16</td>
        <td>fd44cdc6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-26 20:04:23</td>
        <td>2013-05-26 21:08:41</td>
        <td>20</td>
        <td>fd44d0d2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-24 03:54:26</td>
        <td>2013-05-24 04:24:44</td>
        <td>6</td>
        <td>fd44d320-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-10-24 00:05:58</td>
        <td>2013-10-24 01:59:19</td>
        <td>11</td>
        <td>fd44d44c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-14 09:04:16</td>
        <td>2014-02-04 15:53:28</td>
        <td>30</td>
        <td>fd44d5d2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-08-10 20:09:41</td>
        <td>2013-08-10 20:17:57</td>
        <td>4</td>
        <td>fd44d762-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>30</td>
        <td>None</td>
        <td>2013-05-14 17:38:05</td>
        <td>2013-05-14 17:54:34</td>
        <td>3</td>
        <td>fd44d834-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-20 00:26:07</td>
        <td>2014-11-26 22:16:21</td>
        <td>21</td>
        <td>fd44d898-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-08-20 02:42:49</td>
        <td>2013-08-23 03:07:18</td>
        <td>12</td>
        <td>fd44dafa-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-08-16 03:12:00</td>
        <td>2013-08-16 03:12:00</td>
        <td>1</td>
        <td>fd44e14e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-15 14:28:10</td>
        <td>2013-05-15 15:57:53</td>
        <td>20</td>
        <td>fd44e284-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-15 19:23:35</td>
        <td>2013-07-14 20:45:09</td>
        <td>6</td>
        <td>fd44e874-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-17 04:42:24</td>
        <td>2013-10-18 15:37:33</td>
        <td>4</td>
        <td>fd44e9d2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-11-16 22:51:19</td>
        <td>2013-11-16 23:04:48</td>
        <td>4</td>
        <td>fd44ea36-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-16 18:14:13</td>
        <td>2013-05-16 18:27:17</td>
        <td>4</td>
        <td>fd44ebbc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-16 18:33:48</td>
        <td>2013-05-16 18:42:41</td>
        <td>4</td>
        <td>fd44ec20-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>40</td>
        <td>None</td>
        <td>2013-06-13 22:36:24</td>
        <td>2013-09-03 23:13:03</td>
        <td>4</td>
        <td>fd44ed56-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2014-05-30 23:46:32</td>
        <td>2014-07-31 00:18:32</td>
        <td>4</td>
        <td>fd44ee14-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-19 03:49:18</td>
        <td>2013-05-26 19:35:05</td>
        <td>20</td>
        <td>fd44ef40-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-17 00:03:06</td>
        <td>2013-05-23 00:25:23</td>
        <td>6</td>
        <td>fd44f008-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-18 00:45:29</td>
        <td>2013-05-27 00:52:59</td>
        <td>7</td>
        <td>fd44f134-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-19 16:03:03</td>
        <td>2013-05-20 00:51:18</td>
        <td>20</td>
        <td>fd44f18e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-19 23:03:58</td>
        <td>2013-05-20 16:00:19</td>
        <td>4</td>
        <td>fd44f4fe-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-17 16:06:45</td>
        <td>2014-03-31 19:53:47</td>
        <td>31</td>
        <td>fd44f562-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td>2013-05-20 21:00:17</td>
        <td>2013-06-21 19:31:38</td>
        <td>10</td>
        <td>fd44f81e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-09-08 04:37:53</td>
        <td>2013-09-08 04:51:09</td>
        <td>4</td>
        <td>fd44f9ae-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-23 01:31:14</td>
        <td>2013-06-01 19:02:33</td>
        <td>7</td>
        <td>fd44fa6c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-18 14:41:32</td>
        <td>2013-05-18 22:17:06</td>
        <td>11</td>
        <td>fd44fe18-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-18 15:45:33</td>
        <td>2013-05-18 16:10:17</td>
        <td>6</td>
        <td>fd44ff44-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>10</td>
        <td>1</td>
        <td>2013-05-18 17:58:09</td>
        <td>2013-06-03 15:38:52</td>
        <td>15</td>
        <td>fd450002-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-26 17:18:44</td>
        <td>2013-05-26 18:50:43</td>
        <td>20</td>
        <td>fd4500ca-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-18 23:58:19</td>
        <td>2013-05-23 01:23:00</td>
        <td>20</td>
        <td>fd450138-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-05-24 21:52:04</td>
        <td>2013-05-25 01:51:54</td>
        <td>7</td>
        <td>fd45019c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-24 21:31:53</td>
        <td>2013-05-25 01:37:47</td>
        <td>7</td>
        <td>fd450200-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-05-19 20:00:00</td>
        <td>2013-05-22 01:27:49</td>
        <td>9</td>
        <td>fd4503cc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>70</td>
        <td>None</td>
        <td>2013-05-19 21:04:01</td>
        <td>2013-05-19 23:59:23</td>
        <td>20</td>
        <td>fd4507c8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>80</td>
        <td>None</td>
        <td>2013-05-20 00:17:31</td>
        <td>2013-06-18 01:51:02</td>
        <td>7</td>
        <td>fd45082c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-20 00:11:35</td>
        <td>2013-05-20 00:32:58</td>
        <td>6</td>
        <td>fd450886-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-05-20 00:46:51</td>
        <td>2013-05-21 00:24:30</td>
        <td>20</td>
        <td>fd4508ea-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2014-03-29 19:02:55</td>
        <td>2014-04-01 00:26:03</td>
        <td>9</td>
        <td>fd450cc8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-20 13:34:51</td>
        <td>2014-04-11 20:12:19</td>
        <td>6</td>
        <td>fd450dea-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-05-29 00:58:55</td>
        <td>2014-11-08 21:40:41</td>
        <td>20</td>
        <td>fd453068-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-21 23:38:16</td>
        <td>2013-05-22 00:05:15</td>
        <td>6</td>
        <td>fd453130-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-22 00:17:56</td>
        <td>2013-05-22 22:01:37</td>
        <td>20</td>
        <td>fd4533ce-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>30</td>
        <td>1</td>
        <td>2013-05-22 00:23:03</td>
        <td>2013-05-22 19:44:05</td>
        <td>20</td>
        <td>fd453496-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-25 13:31:43</td>
        <td>2014-04-11 20:12:26</td>
        <td>11</td>
        <td>fd4534fa-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-05-24 14:43:07</td>
        <td>2013-05-25 10:37:44</td>
        <td>5</td>
        <td>fd453748-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-05-22 19:57:57</td>
        <td>2014-07-16 04:29:31</td>
        <td>7</td>
        <td>fd4537a2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-23 18:14:22</td>
        <td>2013-05-23 18:33:33</td>
        <td>4</td>
        <td>fd453b08-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>None</td>
        <td>2013-05-26 02:52:12</td>
        <td>2014-06-27 21:28:38</td>
        <td>45</td>
        <td>fd453fa4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-24 21:44:37</td>
        <td>2013-05-24 21:54:04</td>
        <td>4</td>
        <td>fd45451c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-07-18 19:57:58</td>
        <td>2013-07-18 19:57:58</td>
        <td>1</td>
        <td>fd45463e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-26 14:47:31</td>
        <td>2013-07-01 23:35:31</td>
        <td>20</td>
        <td>fd45472e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-24 22:13:04</td>
        <td>2013-05-24 22:13:04</td>
        <td>1</td>
        <td>fd454792-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-12 20:29:48</td>
        <td>2013-09-30 21:13:25</td>
        <td>5</td>
        <td>fd4547f6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>None</td>
        <td>2013-06-04 23:37:19</td>
        <td>2014-03-16 22:59:47</td>
        <td>15</td>
        <td>fd45485a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-24 23:53:38</td>
        <td>2013-05-25 01:43:34</td>
        <td>20</td>
        <td>fd454922-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>80</td>
        <td>None</td>
        <td>2013-05-25 00:08:51</td>
        <td>2013-05-27 02:00:02</td>
        <td>11</td>
        <td>fd454a44-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>70</td>
        <td>None</td>
        <td>2013-06-15 00:40:56</td>
        <td>2013-08-18 21:40:43</td>
        <td>15</td>
        <td>fd454c88-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-25 19:30:16</td>
        <td>2013-06-02 20:08:22</td>
        <td>20</td>
        <td>fd454d3c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-27 01:29:59</td>
        <td>2013-12-22 01:18:16</td>
        <td>14</td>
        <td>fd454f9e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-26 01:23:30</td>
        <td>2013-06-02 02:54:42</td>
        <td>20</td>
        <td>fd455066-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-26 01:49:05</td>
        <td>2013-06-10 01:14:51</td>
        <td>20</td>
        <td>fd4550ca-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-26 14:54:12</td>
        <td>2014-04-11 20:12:42</td>
        <td>6</td>
        <td>fd4552be-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-08-31 16:04:32</td>
        <td>2013-09-01 18:00:42</td>
        <td>11</td>
        <td>fd455318-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-27 00:57:02</td>
        <td>2013-05-27 01:05:37</td>
        <td>4</td>
        <td>fd4553d6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-05-26 21:42:02</td>
        <td>2013-05-26 22:09:22</td>
        <td>7</td>
        <td>fd45543a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-26 22:01:31</td>
        <td>2013-05-27 00:35:53</td>
        <td>7</td>
        <td>fd455494-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>60</td>
        <td>None</td>
        <td>2013-08-24 18:12:06</td>
        <td>2013-09-15 01:49:59</td>
        <td>11</td>
        <td>fd4555b6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-05-27 19:12:09</td>
        <td>2013-05-27 19:34:47</td>
        <td>5</td>
        <td>fd45561a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-27 02:21:10</td>
        <td>2013-12-31 04:31:56</td>
        <td>25</td>
        <td>fd45567e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-27 01:25:54</td>
        <td>2013-05-27 01:42:42</td>
        <td>4</td>
        <td>fd45585e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>90</td>
        <td>None</td>
        <td>2013-05-27 03:34:20</td>
        <td>2013-06-11 03:09:46</td>
        <td>10</td>
        <td>fd4558c2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-27 20:09:51</td>
        <td>2013-05-27 20:38:50</td>
        <td>6</td>
        <td>fd455a3e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-27 17:07:05</td>
        <td>2013-05-27 17:42:17</td>
        <td>4</td>
        <td>fd455dea-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-05-27 19:49:36</td>
        <td>2013-07-19 17:59:59</td>
        <td>7</td>
        <td>fd455eb2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>1</td>
        <td>2013-06-02 14:29:47</td>
        <td>2013-07-13 13:04:07</td>
        <td>20</td>
        <td>fd4560f6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-27 23:42:26</td>
        <td>2013-06-11 03:36:20</td>
        <td>10</td>
        <td>fd4562ea-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-05-27 22:50:53</td>
        <td>2013-12-29 21:23:57</td>
        <td>26</td>
        <td>fd4563a8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-05-28 22:02:26</td>
        <td>2013-06-07 01:22:15</td>
        <td>20</td>
        <td>fd456db2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>1</td>
        <td>2013-05-28 17:35:19</td>
        <td>2013-08-05 16:22:33</td>
        <td>20</td>
        <td>fd456e16-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>10</td>
        <td>None</td>
        <td>2014-03-16 15:33:32</td>
        <td>2014-03-16 15:59:41</td>
        <td>6</td>
        <td>fd457190-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-05-28 21:28:41</td>
        <td>2013-05-28 22:49:42</td>
        <td>14</td>
        <td>fd457226-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-29 03:57:32</td>
        <td>2013-05-29 04:20:35</td>
        <td>6</td>
        <td>fd4572b2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-29 02:23:12</td>
        <td>2013-05-30 05:13:32</td>
        <td>20</td>
        <td>fd4575e6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-29 04:01:45</td>
        <td>2014-05-24 23:25:18</td>
        <td>13</td>
        <td>fd457988-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2014-11-15 01:41:04</td>
        <td>2014-11-15 02:23:41</td>
        <td>7</td>
        <td>fd457a1e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>1</td>
        <td>2013-05-29 18:25:56</td>
        <td>2013-05-31 13:42:55</td>
        <td>20</td>
        <td>fd458964-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-11-14 22:48:20</td>
        <td>2013-11-14 23:00:05</td>
        <td>4</td>
        <td>fd458af4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-06-09 20:59:59</td>
        <td>2013-09-01 22:01:44</td>
        <td>16</td>
        <td>fd458c16-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-05-30 10:15:21</td>
        <td>2013-05-30 10:34:53</td>
        <td>6</td>
        <td>fd458d38-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>70</td>
        <td>None</td>
        <td>2013-05-31 00:51:06</td>
        <td>2013-06-03 23:12:03</td>
        <td>13</td>
        <td>fd458d9c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-06-01 17:07:15</td>
        <td>2013-08-24 16:28:55</td>
        <td>20</td>
        <td>fd458e00-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-05-31 14:04:24</td>
        <td>2013-12-07 20:00:16</td>
        <td>20</td>
        <td>fd459166-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-05-31 15:10:54</td>
        <td>2013-05-31 15:42:21</td>
        <td>6</td>
        <td>fd4591ca-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-06-02 18:49:24</td>
        <td>2013-07-28 19:45:58</td>
        <td>11</td>
        <td>fd459292-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-05-31 20:38:38</td>
        <td>2013-05-31 21:09:46</td>
        <td>5</td>
        <td>fd459350-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-05-31 23:35:38</td>
        <td>2013-06-01 01:12:47</td>
        <td>20</td>
        <td>fd45949a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-06-01 00:57:38</td>
        <td>2013-07-13 20:43:48</td>
        <td>15</td>
        <td>fd4594fe-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-06-01 18:40:17</td>
        <td>2013-06-08 21:43:42</td>
        <td>20</td>
        <td>fd459684-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-06-01 23:15:13</td>
        <td>2013-06-18 23:49:04</td>
        <td>22</td>
        <td>fd4596e8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-06-04 00:12:05</td>
        <td>2013-06-18 23:57:34</td>
        <td>22</td>
        <td>fd45974c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-06-11 22:23:49</td>
        <td>2013-06-24 16:29:50</td>
        <td>9</td>
        <td>fd45986e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-06-02 17:39:01</td>
        <td>2013-07-03 23:29:44</td>
        <td>20</td>
        <td>fd459b84-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-06-02 18:25:51</td>
        <td>2014-06-07 18:52:54</td>
        <td>7</td>
        <td>fd459c88-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-06-03 01:01:00</td>
        <td>2013-06-03 01:17:28</td>
        <td>4</td>
        <td>fd45a0de-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-06-04 02:06:58</td>
        <td>2013-06-04 02:18:52</td>
        <td>4</td>
        <td>fd45a714-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-08-16 03:11:28</td>
        <td>2013-08-16 03:27:08</td>
        <td>4</td>
        <td>fd45a7aa-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>30</td>
        <td>None</td>
        <td>2013-06-05 02:44:07</td>
        <td>2013-06-07 01:48:48</td>
        <td>5</td>
        <td>fd45b0d8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-06-07 23:57:41</td>
        <td>2013-06-09 01:21:00</td>
        <td>15</td>
        <td>fd45b3ee-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>1</td>
        <td>2013-06-05 16:52:08</td>
        <td>2013-06-05 17:37:46</td>
        <td>20</td>
        <td>fd45b452-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-08-29 19:16:15</td>
        <td>2013-08-29 19:25:52</td>
        <td>3</td>
        <td>fd45b51a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-06-05 19:45:27</td>
        <td>2013-07-23 15:06:50</td>
        <td>20</td>
        <td>fd45b57e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>110</td>
        <td>None</td>
        <td>2014-06-25 05:45:34</td>
        <td>2014-06-25 05:56:12</td>
        <td>4</td>
        <td>fd45b768-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-06-05 23:36:54</td>
        <td>2013-06-10 01:20:40</td>
        <td>6</td>
        <td>fd45b88a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-06-18 19:24:56</td>
        <td>2013-06-27 17:52:41</td>
        <td>16</td>
        <td>fd45bfe2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-06-06 23:47:16</td>
        <td>2013-06-07 00:24:00</td>
        <td>6</td>
        <td>fd45c230-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-06-07 01:03:48</td>
        <td>2013-10-05 13:11:42</td>
        <td>20</td>
        <td>fd45c35c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-06-07 00:59:03</td>
        <td>2013-10-05 13:34:05</td>
        <td>20</td>
        <td>fd45c41a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-06-07 04:01:45</td>
        <td>2013-06-24 00:23:33</td>
        <td>20</td>
        <td>fd45c47e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-06-07 16:00:18</td>
        <td>2014-05-02 23:44:45</td>
        <td>20</td>
        <td>fd45c924-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-06-08 15:25:11</td>
        <td>2013-06-08 15:46:59</td>
        <td>5</td>
        <td>fd45cd66-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>60</td>
        <td>None</td>
        <td>2013-06-16 20:24:06</td>
        <td>2013-09-14 21:48:14</td>
        <td>20</td>
        <td>fd45d32e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-06-08 21:14:18</td>
        <td>2013-09-22 19:22:06</td>
        <td>7</td>
        <td>fd45e062-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-06-08 22:03:35</td>
        <td>2013-06-09 02:29:24</td>
        <td>20</td>
        <td>fd45e314-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>1</td>
        <td>2013-06-08 23:44:06</td>
        <td>2013-09-24 00:54:57</td>
        <td>20</td>
        <td>fd45ea44-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-06-09 18:37:54</td>
        <td>2013-06-09 18:45:21</td>
        <td>2</td>
        <td>fd45eea4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-06-10 23:43:32</td>
        <td>2013-06-11 00:03:44</td>
        <td>4</td>
        <td>fd45f278-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-06-10 15:09:16</td>
        <td>2013-06-10 16:07:07</td>
        <td>20</td>
        <td>fd45f340-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-06-10 19:42:17</td>
        <td>2013-06-11 02:12:12</td>
        <td>20</td>
        <td>fd45f656-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-06-10 21:57:44</td>
        <td>2013-06-10 22:32:09</td>
        <td>6</td>
        <td>fd45f7d2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-06-11 00:33:17</td>
        <td>2013-09-18 14:40:38</td>
        <td>6</td>
        <td>fd45f836-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-06-12 02:26:46</td>
        <td>2013-06-12 02:26:46</td>
        <td>1</td>
        <td>fd45f8fe-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-06-12 00:30:15</td>
        <td>2013-06-12 00:46:40</td>
        <td>4</td>
        <td>fd45fe08-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-06-13 15:07:55</td>
        <td>2013-06-15 02:22:13</td>
        <td>20</td>
        <td>fd45feda-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-06-13 15:26:45</td>
        <td>2013-06-15 03:15:45</td>
        <td>20</td>
        <td>fd45ff7a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-08-09 15:37:25</td>
        <td>2013-08-09 15:48:51</td>
        <td>4</td>
        <td>fd4601dc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-06-12 01:25:59</td>
        <td>2013-06-20 00:58:48</td>
        <td>7</td>
        <td>fd460272-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>1</td>
        <td>2013-06-12 17:16:26</td>
        <td>2013-08-13 20:39:04</td>
        <td>16</td>
        <td>fd4604d4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-06-13 02:07:12</td>
        <td>2014-02-02 22:03:49</td>
        <td>27</td>
        <td>fd460664-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-06-13 03:25:04</td>
        <td>2014-10-14 08:03:40</td>
        <td>16</td>
        <td>fd4606c8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>80</td>
        <td>None</td>
        <td>2013-06-16 23:58:13</td>
        <td>2013-06-24 00:31:15</td>
        <td>10</td>
        <td>fd460aa6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-06-14 00:35:49</td>
        <td>2013-08-29 00:12:50</td>
        <td>26</td>
        <td>fd460b00-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-06-22 13:57:47</td>
        <td>2015-08-01 18:51:23</td>
        <td>36</td>
        <td>fd460b6e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-02 15:03:50</td>
        <td>2013-09-29 19:34:50</td>
        <td>16</td>
        <td>fd460c36-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>None</td>
        <td>2013-06-16 00:36:11</td>
        <td>2013-06-16 00:47:10</td>
        <td>4</td>
        <td>fd46106e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-06-14 22:35:59</td>
        <td>2013-06-14 22:45:14</td>
        <td>4</td>
        <td>fd4610d2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-06-15 09:33:54</td>
        <td>2013-07-09 20:56:09</td>
        <td>16</td>
        <td>fd4611fe-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-06-15 09:39:56</td>
        <td>2013-06-15 09:54:29</td>
        <td>4</td>
        <td>fd461262-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-06-15 12:23:10</td>
        <td>2013-06-16 19:32:58</td>
        <td>20</td>
        <td>fd461320-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-06-15 18:22:59</td>
        <td>2013-07-30 23:57:59</td>
        <td>20</td>
        <td>fd46144c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-06-16 19:40:49</td>
        <td>2013-07-28 20:59:53</td>
        <td>20</td>
        <td>fd461640-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-06-29 21:39:52</td>
        <td>2013-07-06 01:54:12</td>
        <td>20</td>
        <td>fd461bd6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>40</td>
        <td>None</td>
        <td>2013-06-20 01:34:45</td>
        <td>2013-07-21 21:38:11</td>
        <td>22</td>
        <td>fd461d02-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-08-01 19:39:46</td>
        <td>2013-08-19 20:51:08</td>
        <td>2</td>
        <td>fd462784-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>None</td>
        <td>2013-06-17 19:56:48</td>
        <td>2013-06-19 21:05:06</td>
        <td>11</td>
        <td>fd4627e8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>None</td>
        <td>2013-06-22 20:37:03</td>
        <td>2013-10-15 18:35:18</td>
        <td>20</td>
        <td>fd462b08-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-06-17 21:34:41</td>
        <td>2013-06-17 23:33:39</td>
        <td>6</td>
        <td>fd462b6c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-06-23 00:14:49</td>
        <td>2013-06-24 02:12:32</td>
        <td>7</td>
        <td>fd463544-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-06-26 01:46:35</td>
        <td>2013-08-14 03:11:27</td>
        <td>20</td>
        <td>fd463896-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>None</td>
        <td>2013-07-09 17:03:02</td>
        <td>2013-07-09 19:04:11</td>
        <td>20</td>
        <td>fd463b52-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>60</td>
        <td>None</td>
        <td>2013-08-06 18:02:02</td>
        <td>2013-08-06 18:33:47</td>
        <td>2</td>
        <td>fd46485e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-06-22 15:43:13</td>
        <td>2013-07-18 20:29:01</td>
        <td>2</td>
        <td>fd4648c2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-08-10 14:27:01</td>
        <td>2013-08-10 14:27:01</td>
        <td>1</td>
        <td>fd464930-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-19 22:26:47</td>
        <td>2013-07-19 23:01:31</td>
        <td>7</td>
        <td>fd464e3a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-06-22 01:25:53</td>
        <td>2013-07-07 00:08:22</td>
        <td>7</td>
        <td>fd464e9e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-06-20 11:34:39</td>
        <td>2013-06-20 11:38:09</td>
        <td>2</td>
        <td>fd464f02-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2014-04-05 19:37:40</td>
        <td>2014-04-05 19:37:40</td>
        <td>1</td>
        <td>fd464fc0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>None</td>
        <td>2013-06-30 16:13:38</td>
        <td>2013-06-30 16:51:32</td>
        <td>6</td>
        <td>fd465218-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-06-20 23:03:34</td>
        <td>2014-05-07 02:41:16</td>
        <td>10</td>
        <td>fd46527c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-06-21 22:21:06</td>
        <td>2013-07-07 20:31:41</td>
        <td>14</td>
        <td>fd465538-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-06-21 15:00:14</td>
        <td>2013-09-08 16:44:27</td>
        <td>3</td>
        <td>fd46584e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>1</td>
        <td>2013-06-21 17:12:18</td>
        <td>2014-11-24 16:16:46</td>
        <td>21</td>
        <td>fd4658b2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-10-14 15:12:57</td>
        <td>2014-10-19 16:00:03</td>
        <td>5</td>
        <td>fd465a42-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-19 21:41:24</td>
        <td>2013-10-05 23:52:26</td>
        <td>6</td>
        <td>fd465f06-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-06-22 14:40:35</td>
        <td>2013-06-25 17:43:30</td>
        <td>20</td>
        <td>fd4661cc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-06-23 23:10:29</td>
        <td>2013-08-11 23:49:34</td>
        <td>11</td>
        <td>fd46626c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>90</td>
        <td>None</td>
        <td>2013-06-22 20:30:01</td>
        <td>2013-07-05 14:18:58</td>
        <td>6</td>
        <td>fd4665f0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-08-15 18:52:27</td>
        <td>2013-10-02 20:42:38</td>
        <td>16</td>
        <td>fd466690-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-06-23 04:38:28</td>
        <td>2013-07-08 00:22:17</td>
        <td>21</td>
        <td>fd4668de-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2014-05-01 01:33:59</td>
        <td>2014-05-01 02:06:56</td>
        <td>7</td>
        <td>fd466bb8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-06-29 05:13:30</td>
        <td>2013-07-21 06:51:46</td>
        <td>13</td>
        <td>fd466c1c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-06-23 09:52:58</td>
        <td>2013-06-23 09:56:53</td>
        <td>2</td>
        <td>fd466db6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-04 14:25:34</td>
        <td>2013-07-07 16:47:42</td>
        <td>20</td>
        <td>fd466e24-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-06-23 15:35:49</td>
        <td>2013-09-02 18:07:21</td>
        <td>7</td>
        <td>fd466e88-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>30</td>
        <td>None</td>
        <td>2013-07-14 21:10:39</td>
        <td>2013-07-14 21:18:28</td>
        <td>4</td>
        <td>fd466f5a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-06-24 00:44:45</td>
        <td>2013-06-24 00:57:33</td>
        <td>4</td>
        <td>fd46714e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-06-25 00:32:04</td>
        <td>2013-07-04 01:10:59</td>
        <td>5</td>
        <td>fd46720c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>1</td>
        <td>2013-06-23 23:39:36</td>
        <td>2013-11-23 06:02:38</td>
        <td>15</td>
        <td>fd46727a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2014-04-05 11:05:13</td>
        <td>2014-04-08 20:37:49</td>
        <td>7</td>
        <td>fd467716-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-06-25 21:30:11</td>
        <td>2013-06-25 22:03:26</td>
        <td>4</td>
        <td>fd4682ec-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-06-28 12:36:46</td>
        <td>2013-06-28 14:08:27</td>
        <td>7</td>
        <td>fd468346-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-02 22:51:50</td>
        <td>2013-07-04 20:15:23</td>
        <td>7</td>
        <td>fd468954-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-06-29 22:04:21</td>
        <td>2014-04-11 20:15:00</td>
        <td>10</td>
        <td>fd46a3bc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-09-29 01:23:37</td>
        <td>2013-10-03 00:18:55</td>
        <td>11</td>
        <td>fd46a9ac-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-06-27 17:21:57</td>
        <td>2013-08-22 19:39:53</td>
        <td>4</td>
        <td>fd46aa88-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-06-28 03:13:18</td>
        <td>2013-06-28 03:22:48</td>
        <td>4</td>
        <td>fd46aaec-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-06-27 03:55:55</td>
        <td>2014-02-11 20:11:00</td>
        <td>20</td>
        <td>fd46ab5a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-06-29 22:58:24</td>
        <td>2013-07-20 23:01:22</td>
        <td>20</td>
        <td>fd46b014-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>70</td>
        <td>None</td>
        <td>2013-06-30 01:12:55</td>
        <td>2013-07-02 00:54:26</td>
        <td>6</td>
        <td>fd46b3f2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-13 00:15:12</td>
        <td>2013-07-15 20:21:15</td>
        <td>20</td>
        <td>fd46b4ba-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-06-30 21:53:59</td>
        <td>2013-07-06 20:55:13</td>
        <td>20</td>
        <td>fd46b712-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-06-29 22:40:56</td>
        <td>2013-06-30 15:45:20</td>
        <td>20</td>
        <td>fd46b776-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-06-29 22:54:45</td>
        <td>2013-06-29 23:13:38</td>
        <td>4</td>
        <td>fd46b834-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-06-30 17:41:25</td>
        <td>2013-06-30 17:48:42</td>
        <td>2</td>
        <td>fd46b8fc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-09-03 01:22:09</td>
        <td>2013-11-26 00:11:32</td>
        <td>20</td>
        <td>fd46b9c4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-06-30 22:38:20</td>
        <td>2013-06-30 23:42:30</td>
        <td>4</td>
        <td>fd46c09a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-06-30 23:42:47</td>
        <td>2013-06-30 23:54:33</td>
        <td>2</td>
        <td>fd46c13a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-01 19:43:06</td>
        <td>2013-07-01 19:43:06</td>
        <td>1</td>
        <td>fd46c310-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>110</td>
        <td>None</td>
        <td>2013-07-10 02:58:41</td>
        <td>2015-06-21 21:34:46</td>
        <td>20</td>
        <td>fd46c446-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-06-30 19:23:03</td>
        <td>2013-06-30 19:58:35</td>
        <td>7</td>
        <td>fd46c4dc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-06-30 20:08:27</td>
        <td>2013-06-30 20:40:59</td>
        <td>7</td>
        <td>fd46cafe-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-06-30 20:28:31</td>
        <td>2014-06-16 03:21:38</td>
        <td>7</td>
        <td>fd46cc8e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-06-30 19:55:46</td>
        <td>2013-06-30 20:33:40</td>
        <td>6</td>
        <td>fd46cdba-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-07-01 10:53:34</td>
        <td>2013-07-01 11:08:21</td>
        <td>4</td>
        <td>fd46cf4a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-07-20 00:08:32</td>
        <td>2013-07-20 00:21:50</td>
        <td>4</td>
        <td>fd46cfae-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-08-11 21:41:58</td>
        <td>2013-08-11 22:15:10</td>
        <td>7</td>
        <td>fd46d526-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-08-11 22:21:14</td>
        <td>2013-08-11 22:43:53</td>
        <td>7</td>
        <td>fd46d58a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-07-03 16:51:12</td>
        <td>2013-07-04 12:01:32</td>
        <td>7</td>
        <td>fd46d71a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2014-02-05 21:13:27</td>
        <td>2014-02-05 21:45:29</td>
        <td>6</td>
        <td>fd46d8aa-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-01 18:49:51</td>
        <td>2013-07-19 19:09:34</td>
        <td>7</td>
        <td>fd46d90e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-01 13:05:12</td>
        <td>2013-07-01 21:03:41</td>
        <td>4</td>
        <td>fd46db66-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-01 01:19:49</td>
        <td>2013-07-01 01:19:49</td>
        <td>1</td>
        <td>fd46dbca-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-01 01:44:33</td>
        <td>2013-07-01 03:55:39</td>
        <td>4</td>
        <td>fd46ddfa-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-01 02:45:27</td>
        <td>2014-10-03 01:34:11</td>
        <td>23</td>
        <td>fd46df26-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-01 03:08:31</td>
        <td>2013-07-01 03:22:30</td>
        <td>4</td>
        <td>fd46dff8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-02 09:41:55</td>
        <td>2013-07-08 16:21:57</td>
        <td>7</td>
        <td>fd46e3ea-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-07-03 02:26:30</td>
        <td>2013-08-25 00:18:32</td>
        <td>4</td>
        <td>fd46e4a8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-07-07 22:29:30</td>
        <td>2013-07-07 22:33:55</td>
        <td>2</td>
        <td>fd46e9bc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-01 15:56:38</td>
        <td>2013-07-01 16:08:51</td>
        <td>4</td>
        <td>fd46eb56-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2014-04-03 08:30:18</td>
        <td>2014-04-03 09:13:47</td>
        <td>6</td>
        <td>fd46f740-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-01 21:21:23</td>
        <td>2013-07-01 21:36:42</td>
        <td>4</td>
        <td>fd46feca-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>70</td>
        <td>None</td>
        <td>2013-07-20 19:59:46</td>
        <td>2013-07-20 20:05:57</td>
        <td>2</td>
        <td>fd47046a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-07-02 02:27:07</td>
        <td>2013-07-02 03:06:04</td>
        <td>7</td>
        <td>fd470cc6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>70</td>
        <td>None</td>
        <td>2013-08-18 23:35:28</td>
        <td>2013-09-28 21:07:55</td>
        <td>11</td>
        <td>fd470d8e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-07-02 15:13:30</td>
        <td>2013-07-02 15:29:36</td>
        <td>4</td>
        <td>fd470f1e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>90</td>
        <td>None</td>
        <td>2013-07-08 02:04:34</td>
        <td>2013-07-09 03:41:11</td>
        <td>2</td>
        <td>fd47104a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>90</td>
        <td>None</td>
        <td>2013-07-03 00:14:44</td>
        <td>2013-07-03 00:25:15</td>
        <td>4</td>
        <td>fd4712a2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-02 22:12:01</td>
        <td>2013-07-02 22:21:50</td>
        <td>4</td>
        <td>fd471306-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-07-03 00:24:21</td>
        <td>2014-11-03 23:14:11</td>
        <td>20</td>
        <td>fd4713ce-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-08 02:31:45</td>
        <td>2013-07-08 02:44:32</td>
        <td>4</td>
        <td>fd471432-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-07-08 03:16:14</td>
        <td>2013-07-08 03:23:49</td>
        <td>4</td>
        <td>fd471496-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>1</td>
        <td>2013-07-03 02:56:22</td>
        <td>2013-07-03 03:40:18</td>
        <td>7</td>
        <td>fd471626-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-27 07:24:18</td>
        <td>2013-08-03 12:59:21</td>
        <td>7</td>
        <td>fd471752-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-03 16:42:14</td>
        <td>2013-08-07 19:16:37</td>
        <td>20</td>
        <td>fd47181a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-04 03:31:47</td>
        <td>2013-08-01 03:33:31</td>
        <td>7</td>
        <td>fd471a72-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-04 17:22:23</td>
        <td>2014-11-13 20:04:53</td>
        <td>35</td>
        <td>fd471c2a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-06 13:09:42</td>
        <td>2013-08-10 17:13:00</td>
        <td>2</td>
        <td>fd471fc2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-04 20:49:28</td>
        <td>2013-07-04 20:49:28</td>
        <td>1</td>
        <td>fd472094-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-07-20 15:55:54</td>
        <td>2013-07-28 15:48:06</td>
        <td>4</td>
        <td>fd47226a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-07-06 01:50:26</td>
        <td>2013-09-02 22:30:47</td>
        <td>16</td>
        <td>fd4723a0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-07-05 14:52:26</td>
        <td>2013-07-05 15:03:23</td>
        <td>4</td>
        <td>fd4726f2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-05 17:18:04</td>
        <td>2013-08-02 17:26:01</td>
        <td>11</td>
        <td>fd472a76-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-21 16:14:10</td>
        <td>2014-09-13 21:58:35</td>
        <td>20</td>
        <td>fd472ada-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-05 19:36:57</td>
        <td>2013-07-06 01:14:39</td>
        <td>7</td>
        <td>fd472b3e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-08-13 20:07:32</td>
        <td>2013-08-13 20:35:40</td>
        <td>7</td>
        <td>fd472ba2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-07-07 03:20:06</td>
        <td>2014-01-20 01:42:42</td>
        <td>20</td>
        <td>fd472cc4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-06 02:55:46</td>
        <td>2013-07-06 03:08:04</td>
        <td>4</td>
        <td>fd472d8c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-06 17:35:59</td>
        <td>2013-07-06 18:00:42</td>
        <td>7</td>
        <td>fd472f08-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-07-06 19:24:07</td>
        <td>2013-07-06 20:23:27</td>
        <td>7</td>
        <td>fd47302a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-07-06 20:07:39</td>
        <td>2013-07-06 20:39:50</td>
        <td>7</td>
        <td>fd47314c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>10</td>
        <td>None</td>
        <td>2013-08-15 09:42:36</td>
        <td>2013-08-16 09:40:36</td>
        <td>4</td>
        <td>fd47326e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-12-22 07:07:01</td>
        <td>2013-12-22 07:17:58</td>
        <td>4</td>
        <td>fd4732d2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-07-07 21:01:27</td>
        <td>2013-07-08 01:25:17</td>
        <td>20</td>
        <td>fd4734bc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2014-02-21 01:37:22</td>
        <td>2014-02-21 01:51:25</td>
        <td>4</td>
        <td>fd47357a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-17 23:15:28</td>
        <td>2013-07-17 23:19:51</td>
        <td>2</td>
        <td>fd473aca-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>1</td>
        <td>2013-07-09 03:54:42</td>
        <td>2013-07-09 04:07:14</td>
        <td>7</td>
        <td>fd473ec6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-07-09 14:17:36</td>
        <td>2013-07-09 14:27:19</td>
        <td>3</td>
        <td>fd4740ba-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-07-09 21:28:20</td>
        <td>2014-05-13 23:10:28</td>
        <td>45</td>
        <td>fd474240-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-07-09 20:51:55</td>
        <td>2013-10-21 04:32:49</td>
        <td>17</td>
        <td>fd474308-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-11 21:14:19</td>
        <td>2013-07-14 17:51:44</td>
        <td>20</td>
        <td>fd4743d0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-22 21:51:26</td>
        <td>2013-08-26 22:03:56</td>
        <td>20</td>
        <td>fd4744de-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-07-10 23:47:24</td>
        <td>2013-07-16 00:30:31</td>
        <td>7</td>
        <td>fd474542-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-10 03:43:03</td>
        <td>2013-07-10 03:56:32</td>
        <td>4</td>
        <td>fd47489e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-09-04 02:13:01</td>
        <td>2013-09-10 04:48:05</td>
        <td>6</td>
        <td>fd475456-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>70</td>
        <td>None</td>
        <td>2013-08-15 20:53:17</td>
        <td>2013-11-04 22:36:04</td>
        <td>11</td>
        <td>fd476cc0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>None</td>
        <td>2013-07-11 16:07:08</td>
        <td>2013-07-11 16:23:01</td>
        <td>4</td>
        <td>fd476fb8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-09-07 00:30:37</td>
        <td>2013-09-07 00:46:14</td>
        <td>4</td>
        <td>fd4771ca-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-08-17 16:24:20</td>
        <td>2013-08-17 17:05:16</td>
        <td>7</td>
        <td>fd4774a4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-12 18:10:23</td>
        <td>2014-08-07 20:14:46</td>
        <td>29</td>
        <td>fd47756c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>None</td>
        <td>2013-07-29 03:23:06</td>
        <td>2013-08-04 22:41:15</td>
        <td>4</td>
        <td>fd4777e2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-08-25 17:19:21</td>
        <td>2014-03-22 00:03:25</td>
        <td>20</td>
        <td>fd477b7a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>70</td>
        <td>None</td>
        <td>2013-07-12 01:09:55</td>
        <td>2013-09-09 20:00:53</td>
        <td>6</td>
        <td>fd4780fc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-11 21:40:21</td>
        <td>2013-11-12 23:29:26</td>
        <td>28</td>
        <td>fd478156-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>None</td>
        <td>2013-08-26 20:37:59</td>
        <td>2013-08-26 21:16:53</td>
        <td>7</td>
        <td>fd4789bc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-11 16:39:22</td>
        <td>2013-07-11 16:44:54</td>
        <td>2</td>
        <td>fd478c3c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-13 03:01:19</td>
        <td>2013-07-13 03:13:13</td>
        <td>4</td>
        <td>fd478fe8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-12 01:26:38</td>
        <td>2013-07-12 01:58:04</td>
        <td>7</td>
        <td>fd479664-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-07-21 04:13:03</td>
        <td>2013-08-31 02:38:01</td>
        <td>3</td>
        <td>fd47979a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-07-12 12:48:13</td>
        <td>2013-09-13 06:25:04</td>
        <td>2</td>
        <td>fd479baa-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-07-12 18:07:53</td>
        <td>2013-07-12 18:42:00</td>
        <td>7</td>
        <td>fd479e8e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-08-21 23:03:10</td>
        <td>2014-04-22 23:38:36</td>
        <td>7</td>
        <td>fd47a334-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>None</td>
        <td>2013-08-25 06:57:16</td>
        <td>2013-08-25 07:01:33</td>
        <td>2</td>
        <td>fd47a410-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-13 15:59:53</td>
        <td>2013-07-24 21:31:31</td>
        <td>23</td>
        <td>fd47a5aa-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-07-13 19:48:00</td>
        <td>2013-07-14 02:01:48</td>
        <td>7</td>
        <td>fd47a618-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-13 19:25:20</td>
        <td>2013-07-13 19:55:03</td>
        <td>7</td>
        <td>fd47b522-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-07-13 23:02:46</td>
        <td>2013-07-28 22:49:39</td>
        <td>7</td>
        <td>fd47b9c8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>70</td>
        <td>None</td>
        <td>2013-07-13 18:18:45</td>
        <td>2013-07-13 18:18:45</td>
        <td>1</td>
        <td>fd47d2f0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-10-14 19:02:13</td>
        <td>2013-10-14 19:15:22</td>
        <td>4</td>
        <td>fd47d462-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-13 22:32:28</td>
        <td>2013-07-13 22:58:07</td>
        <td>7</td>
        <td>fd47d80e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-07-18 17:42:37</td>
        <td>2013-07-25 01:40:41</td>
        <td>7</td>
        <td>fd47d872-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-14 02:03:20</td>
        <td>2013-07-14 02:14:41</td>
        <td>4</td>
        <td>fd47da16-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-14 01:02:24</td>
        <td>2013-07-14 01:36:55</td>
        <td>7</td>
        <td>fd47dbb0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-07-14 02:17:52</td>
        <td>2014-05-09 01:54:11</td>
        <td>22</td>
        <td>fd47dc82-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-14 16:15:54</td>
        <td>2013-07-14 16:19:49</td>
        <td>2</td>
        <td>fd47e042-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>80</td>
        <td>None</td>
        <td>2013-07-15 00:30:44</td>
        <td>2013-12-12 04:02:51</td>
        <td>20</td>
        <td>fd47e2b8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>100</td>
        <td>None</td>
        <td>2013-07-21 17:26:28</td>
        <td>2014-11-01 22:44:45</td>
        <td>7</td>
        <td>fd47e394-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-21 04:53:35</td>
        <td>2013-07-21 05:04:45</td>
        <td>2</td>
        <td>fd47e614-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2014-01-01 22:57:15</td>
        <td>2014-04-11 01:08:12</td>
        <td>7</td>
        <td>fd47e754-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-15 18:47:44</td>
        <td>2013-07-15 18:47:44</td>
        <td>1</td>
        <td>fd47e97a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-07-15 19:32:39</td>
        <td>2013-07-15 20:07:57</td>
        <td>7</td>
        <td>fd47eac4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>None</td>
        <td>2013-07-16 17:55:35</td>
        <td>2013-07-16 18:11:48</td>
        <td>4</td>
        <td>fd47eeb6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-07-16 23:57:16</td>
        <td>2013-07-20 00:17:28</td>
        <td>20</td>
        <td>fd47f05a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-07-16 14:38:17</td>
        <td>2013-07-16 15:00:03</td>
        <td>5</td>
        <td>fd47f12c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>90</td>
        <td>None</td>
        <td>2013-07-18 15:15:21</td>
        <td>2013-07-18 15:32:16</td>
        <td>4</td>
        <td>fd47f2d0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-07-16 19:43:25</td>
        <td>2013-07-16 20:11:14</td>
        <td>7</td>
        <td>fd47f4e2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-20 18:57:39</td>
        <td>2013-07-20 19:01:39</td>
        <td>2</td>
        <td>fd481a08-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-07-17 20:17:22</td>
        <td>2013-07-17 20:23:55</td>
        <td>4</td>
        <td>fd4837ae-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>None</td>
        <td>2014-05-01 21:53:32</td>
        <td>2014-05-01 22:28:34</td>
        <td>6</td>
        <td>fd483812-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-19 01:16:16</td>
        <td>2013-07-23 01:02:14</td>
        <td>19</td>
        <td>fd483c5e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2015-04-24 20:31:37</td>
        <td>2015-04-24 20:43:51</td>
        <td>4</td>
        <td>fd483ccc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2014-02-01 22:31:39</td>
        <td>2014-02-01 22:47:13</td>
        <td>3</td>
        <td>fd483e52-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-09-23 19:48:26</td>
        <td>2013-09-23 19:48:26</td>
        <td>1</td>
        <td>fd483f1a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-18 21:01:02</td>
        <td>2013-07-18 21:21:19</td>
        <td>7</td>
        <td>fd484618-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-18 23:31:58</td>
        <td>2013-07-18 23:35:09</td>
        <td>2</td>
        <td>fd484a1e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>60</td>
        <td>None</td>
        <td>2014-02-13 01:51:14</td>
        <td>2014-02-13 02:24:43</td>
        <td>7</td>
        <td>fd484bea-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>90</td>
        <td>None</td>
        <td>2014-06-08 17:24:38</td>
        <td>2015-09-24 02:35:02</td>
        <td>16</td>
        <td>fd484f64-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-07-19 12:34:44</td>
        <td>2013-07-19 12:48:07</td>
        <td>4</td>
        <td>fd4857fc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-07-19 15:47:16</td>
        <td>2013-07-19 15:55:49</td>
        <td>4</td>
        <td>fd4858c4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-07-19 14:37:47</td>
        <td>2013-07-21 15:28:07</td>
        <td>7</td>
        <td>fd485b1c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-19 15:24:04</td>
        <td>2013-07-19 16:22:04</td>
        <td>5</td>
        <td>fd485c48-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-07-30 01:36:15</td>
        <td>2013-07-30 01:51:09</td>
        <td>4</td>
        <td>fd485f68-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>80</td>
        <td>None</td>
        <td>2013-07-19 20:59:35</td>
        <td>2013-07-19 21:14:21</td>
        <td>4</td>
        <td>fd486094-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2014-09-20 18:44:33</td>
        <td>2014-09-21 23:16:27</td>
        <td>7</td>
        <td>fd486530-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-07-19 22:32:26</td>
        <td>2013-07-19 22:44:32</td>
        <td>4</td>
        <td>fd486594-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-19 23:06:23</td>
        <td>2013-07-19 23:17:29</td>
        <td>4</td>
        <td>fd486954-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>100</td>
        <td>1</td>
        <td>2013-07-19 23:12:09</td>
        <td>2013-09-26 16:16:17</td>
        <td>20</td>
        <td>fd486a1c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-07-26 08:37:46</td>
        <td>2013-08-15 22:12:32</td>
        <td>4</td>
        <td>fd486cf6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2014-06-14 02:39:59</td>
        <td>2014-06-14 02:39:59</td>
        <td>1</td>
        <td>fd486d64-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-07-23 19:47:54</td>
        <td>2013-08-09 19:04:23</td>
        <td>7</td>
        <td>fd486e7c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-20 05:44:27</td>
        <td>2013-07-20 05:59:33</td>
        <td>4</td>
        <td>fd486f44-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-09-01 10:54:12</td>
        <td>2013-09-01 10:58:19</td>
        <td>2</td>
        <td>fd4873b8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-07-20 17:21:17</td>
        <td>2013-07-20 18:44:56</td>
        <td>7</td>
        <td>fd487d90-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-07-20 19:03:48</td>
        <td>2014-05-18 23:37:11</td>
        <td>34</td>
        <td>fd4881fa-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-27 17:50:53</td>
        <td>2013-11-21 15:39:09</td>
        <td>13</td>
        <td>fd4885b0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2014-06-20 23:15:41</td>
        <td>2014-09-07 01:05:35</td>
        <td>25</td>
        <td>fd488e8e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-20 21:04:56</td>
        <td>2013-08-06 21:26:54</td>
        <td>4</td>
        <td>fd489596-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2014-04-03 02:29:54</td>
        <td>2014-04-03 02:35:36</td>
        <td>2</td>
        <td>fd4898f2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-07-21 00:17:17</td>
        <td>2013-07-21 00:34:03</td>
        <td>4</td>
        <td>fd489956-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-07-21 02:40:18</td>
        <td>2013-07-21 02:40:18</td>
        <td>1</td>
        <td>fd489b4a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-21 11:03:00</td>
        <td>2013-07-21 11:07:28</td>
        <td>2</td>
        <td>fd489bae-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-07-21 17:28:17</td>
        <td>2013-07-21 17:40:10</td>
        <td>4</td>
        <td>fd489d34-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-22 07:01:50</td>
        <td>2013-07-23 06:34:41</td>
        <td>10</td>
        <td>fd48a180-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-22 00:44:12</td>
        <td>2013-07-23 06:40:51</td>
        <td>5</td>
        <td>fd48a20c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-07-22 14:59:04</td>
        <td>2013-07-26 20:36:16</td>
        <td>20</td>
        <td>fd48a3a6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-07-22 07:53:46</td>
        <td>2013-08-13 13:49:50</td>
        <td>7</td>
        <td>fd48a46e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-23 12:09:31</td>
        <td>2013-08-20 04:07:54</td>
        <td>4</td>
        <td>fd48a4d2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-08-15 22:00:02</td>
        <td>2013-08-15 22:00:02</td>
        <td>1</td>
        <td>fd48a8ce-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-07-31 05:05:59</td>
        <td>2013-08-01 03:40:45</td>
        <td>6</td>
        <td>fd48b184-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-29 08:32:42</td>
        <td>2013-08-15 08:50:58</td>
        <td>23</td>
        <td>fd48b544-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>30</td>
        <td>None</td>
        <td>2013-08-31 02:47:10</td>
        <td>2015-03-03 04:52:59</td>
        <td>20</td>
        <td>fd48bac6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-07-29 18:42:59</td>
        <td>2013-09-02 01:50:17</td>
        <td>20</td>
        <td>fd48bbe8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-07-24 00:57:19</td>
        <td>2013-07-27 19:59:13</td>
        <td>7</td>
        <td>fd48c124-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-07-24 01:05:32</td>
        <td>2013-07-24 01:05:32</td>
        <td>1</td>
        <td>fd48c188-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-08-17 00:26:19</td>
        <td>2014-06-22 19:52:46</td>
        <td>20</td>
        <td>fd48c25a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-08-04 23:42:27</td>
        <td>2013-08-10 00:13:06</td>
        <td>20</td>
        <td>fd48c322-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-07-24 10:48:14</td>
        <td>2013-07-26 03:01:14</td>
        <td>20</td>
        <td>fd48c9a8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-24 14:29:26</td>
        <td>2013-07-24 14:50:15</td>
        <td>7</td>
        <td>fd48cade-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-24 15:52:57</td>
        <td>2013-07-24 16:10:37</td>
        <td>7</td>
        <td>fd48ccdc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-24 17:42:59</td>
        <td>2013-07-24 18:16:13</td>
        <td>7</td>
        <td>fd48d060-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>None</td>
        <td>2013-07-24 19:04:52</td>
        <td>2013-07-24 19:04:52</td>
        <td>1</td>
        <td>fd48d18c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>70</td>
        <td>None</td>
        <td>2013-07-24 20:28:47</td>
        <td>2013-07-24 20:28:47</td>
        <td>1</td>
        <td>fd48d498-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>130</td>
        <td>None</td>
        <td>2013-08-27 21:36:04</td>
        <td>2013-08-27 21:51:34</td>
        <td>4</td>
        <td>fd48f888-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-07-26 01:46:18</td>
        <td>2013-07-26 01:57:17</td>
        <td>4</td>
        <td>fd48f8ec-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-28 09:06:31</td>
        <td>2013-07-28 09:21:09</td>
        <td>4</td>
        <td>fd48fae0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>None</td>
        <td>2013-08-17 19:05:23</td>
        <td>2013-08-17 19:17:22</td>
        <td>4</td>
        <td>fd48fe5a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-08-04 15:46:46</td>
        <td>2013-09-22 15:50:44</td>
        <td>20</td>
        <td>fd49022e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-08-11 15:18:58</td>
        <td>2013-09-08 15:02:01</td>
        <td>20</td>
        <td>fd4902ec-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-26 23:29:04</td>
        <td>2013-07-26 23:34:18</td>
        <td>4</td>
        <td>fd490350-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-26 23:45:22</td>
        <td>2013-07-26 23:55:15</td>
        <td>4</td>
        <td>fd4903b4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-30 02:01:43</td>
        <td>2013-09-15 19:09:56</td>
        <td>7</td>
        <td>fd490472-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>80</td>
        <td>None</td>
        <td>2013-07-27 00:04:54</td>
        <td>2013-10-29 04:28:14</td>
        <td>20</td>
        <td>fd4904d6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-27 00:37:28</td>
        <td>2013-07-27 01:06:54</td>
        <td>4</td>
        <td>fd49053a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-09-28 17:45:44</td>
        <td>2013-09-28 17:57:50</td>
        <td>4</td>
        <td>fd491106-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-27 22:40:08</td>
        <td>2013-07-27 22:53:05</td>
        <td>4</td>
        <td>fd49123c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>80</td>
        <td>None</td>
        <td>2013-08-02 20:08:26</td>
        <td>2013-08-02 21:18:04</td>
        <td>4</td>
        <td>fd4913fe-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-08-23 17:49:20</td>
        <td>2013-08-23 18:04:40</td>
        <td>4</td>
        <td>fd49155c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>80</td>
        <td>None</td>
        <td>2013-07-28 16:50:23</td>
        <td>2013-07-28 17:03:09</td>
        <td>4</td>
        <td>fd491750-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-09-02 15:04:47</td>
        <td>2013-09-02 15:28:21</td>
        <td>5</td>
        <td>fd4917b4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-28 21:03:12</td>
        <td>2013-07-28 21:18:19</td>
        <td>4</td>
        <td>fd49199e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-07-29 03:48:37</td>
        <td>2013-07-29 03:59:42</td>
        <td>4</td>
        <td>fd491ac0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>70</td>
        <td>None</td>
        <td>2013-07-30 03:02:19</td>
        <td>2013-07-30 03:19:57</td>
        <td>4</td>
        <td>fd491b24-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-29 18:09:16</td>
        <td>2013-07-30 18:02:35</td>
        <td>5</td>
        <td>fd491ef8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-30 02:27:44</td>
        <td>2013-07-30 02:27:44</td>
        <td>1</td>
        <td>fd492326-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-08-23 18:50:37</td>
        <td>2013-09-12 01:11:55</td>
        <td>5</td>
        <td>fd49256a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-10-29 20:19:45</td>
        <td>2013-10-29 20:24:32</td>
        <td>2</td>
        <td>fd49295c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-08-10 14:41:35</td>
        <td>2013-08-10 14:52:47</td>
        <td>4</td>
        <td>fd492d4e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-31 02:00:07</td>
        <td>2013-07-31 17:45:52</td>
        <td>7</td>
        <td>fd492e66-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-31 01:34:13</td>
        <td>2013-08-01 00:23:10</td>
        <td>4</td>
        <td>fd492eca-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-31 21:40:00</td>
        <td>2013-07-31 22:42:52</td>
        <td>7</td>
        <td>fd492f24-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>80</td>
        <td>None</td>
        <td>2013-07-31 03:01:20</td>
        <td>2013-08-19 00:14:42</td>
        <td>7</td>
        <td>fd493046-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-07-31 21:46:02</td>
        <td>2013-07-31 21:46:02</td>
        <td>1</td>
        <td>fd49349c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-08-05 03:42:41</td>
        <td>2013-08-05 05:00:53</td>
        <td>7</td>
        <td>fd4956d4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>80</td>
        <td>None</td>
        <td>2013-07-31 12:24:29</td>
        <td>2013-07-31 12:36:49</td>
        <td>4</td>
        <td>fd495738-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-09-20 14:01:52</td>
        <td>2013-12-09 09:56:38</td>
        <td>15</td>
        <td>fd495b70-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-08-24 03:31:20</td>
        <td>2013-08-24 03:43:27</td>
        <td>4</td>
        <td>fd495d5a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-08-04 20:07:01</td>
        <td>2013-08-04 20:10:37</td>
        <td>2</td>
        <td>fd495e18-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-31 22:25:38</td>
        <td>2013-07-31 22:35:54</td>
        <td>4</td>
        <td>fd496070-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>20</td>
        <td>None</td>
        <td>2013-07-31 19:08:14</td>
        <td>2013-07-31 19:20:01</td>
        <td>4</td>
        <td>fd4961ec-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-09-06 13:55:53</td>
        <td>2013-09-06 13:55:53</td>
        <td>1</td>
        <td>fd4962b4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-09-07 00:01:20</td>
        <td>2013-09-07 00:09:33</td>
        <td>4</td>
        <td>fd49643a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-08-11 22:06:46</td>
        <td>2013-08-11 22:19:04</td>
        <td>4</td>
        <td>fd4968d6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2015-02-23 01:15:44</td>
        <td>2015-02-23 01:26:11</td>
        <td>4</td>
        <td>fd496c00-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-08-28 14:45:46</td>
        <td>2013-08-28 15:00:39</td>
        <td>4</td>
        <td>fd496c96-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>0</td>
        <td>None</td>
        <td>2013-07-31 22:29:42</td>
        <td>2013-07-31 22:41:45</td>
        <td>4</td>
        <td>fd497146-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>190</td>
        <td>None</td>
        <td>2013-07-31 21:56:33</td>
        <td>2013-07-31 22:09:48</td>
        <td>4</td>
        <td>fd4976dc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-31 18:45:57</td>
        <td>2013-07-31 19:35:05</td>
        <td>7</td>
        <td>fd497cea-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-08-01 02:04:06</td>
        <td>2013-08-01 02:35:52</td>
        <td>7</td>
        <td>fd497ff6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-31 18:26:51</td>
        <td>2013-07-31 18:32:56</td>
        <td>3</td>
        <td>fd49824e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-07-31 19:00:35</td>
        <td>2013-07-31 19:06:11</td>
        <td>4</td>
        <td>fd498b40-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>10</td>
        <td>None</td>
        <td>2013-07-31 20:07:00</td>
        <td>2013-07-31 20:07:00</td>
        <td>1</td>
        <td>fd498de8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-08-01 03:20:00</td>
        <td>2013-08-01 03:20:00</td>
        <td>1</td>
        <td>fd49a0d0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-08-12 00:40:11</td>
        <td>2013-08-12 01:05:59</td>
        <td>4</td>
        <td>fd49a828-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>None</td>
        <td>2013-07-31 20:23:53</td>
        <td>2013-07-31 21:02:13</td>
        <td>7</td>
        <td>fd49b6d8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-08-01 00:23:52</td>
        <td>2013-08-02 00:15:17</td>
        <td>20</td>
        <td>fd49ba3e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-07-31 20:47:50</td>
        <td>2013-07-31 21:05:11</td>
        <td>4</td>
        <td>fd49be12-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-07-31 21:12:40</td>
        <td>2013-07-31 21:48:40</td>
        <td>7</td>
        <td>fd49bed0-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Popular Hybrid</td>
        <td>50</td>
        <td>None</td>
        <td>2013-08-12 00:25:40</td>
        <td>2013-08-13 23:08:48</td>
        <td>2</td>
        <td>fd49bff2-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>70</td>
        <td>None</td>
        <td>2013-08-05 14:19:45</td>
        <td>2013-08-05 15:05:53</td>
        <td>7</td>
        <td>fd49c114-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-07-31 21:09:56</td>
        <td>2013-07-31 21:22:39</td>
        <td>4</td>
        <td>fd49c178-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>0</td>
        <td>None</td>
        <td>2013-07-31 22:43:13</td>
        <td>2013-07-31 23:31:33</td>
        <td>7</td>
        <td>fd49c1dc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-08-17 02:02:32</td>
        <td>2013-08-17 02:26:29</td>
        <td>6</td>
        <td>fd49ca7e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-08-08 00:51:33</td>
        <td>2013-11-27 20:44:32</td>
        <td>11</td>
        <td>fd49d6a4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>60</td>
        <td>None</td>
        <td>2013-11-08 03:53:20</td>
        <td>2015-08-02 23:58:01</td>
        <td>7</td>
        <td>fd49dca8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-08-24 22:20:40</td>
        <td>2013-08-24 22:25:15</td>
        <td>2</td>
        <td>fd49dd66-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-08-02 22:47:39</td>
        <td>2013-08-02 23:07:40</td>
        <td>4</td>
        <td>fd49e496-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>50</td>
        <td>None</td>
        <td>2013-08-15 20:49:09</td>
        <td>2013-08-15 20:56:34</td>
        <td>4</td>
        <td>fd49e8ec-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>40</td>
        <td>None</td>
        <td>2013-08-01 20:47:51</td>
        <td>2013-08-07 19:12:53</td>
        <td>7</td>
        <td>fd49ea18-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-08-02 12:30:28</td>
        <td>2013-11-01 14:59:56</td>
        <td>20</td>
        <td>fd49ead6-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>30</td>
        <td>None</td>
        <td>2013-08-02 15:15:15</td>
        <td>2013-08-02 15:15:15</td>
        <td>1</td>
        <td>fd49eb9e-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>20</td>
        <td>None</td>
        <td>2013-08-11 10:32:06</td>
        <td>2013-08-11 10:32:06</td>
        <td>1</td>
        <td>fd49ee46-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>60</td>
        <td>None</td>
        <td>2013-08-26 14:28:48</td>
        <td>2013-09-13 14:27:11</td>
        <td>5</td>
        <td>fd49f4b8-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>40</td>
        <td>None</td>
        <td>2013-08-01 19:34:16</td>
        <td>2013-08-01 22:49:58</td>
        <td>7</td>
        <td>fd49f9f4-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Pure Breed</td>
        <td>70</td>
        <td>None</td>
        <td>2013-08-02 01:02:34</td>
        <td>2013-09-04 01:13:44</td>
        <td>20</td>
        <td>fd4a028c-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Cross Breed</td>
        <td>50</td>
        <td>None</td>
        <td>2013-08-07 03:07:53</td>
        <td>2013-08-31 18:33:41</td>
        <td>20</td>
        <td>fd4a0c5a-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
    <tr>
        <td>Mixed Breed/ Other/ I Don&#x27;t Know</td>
        <td>110</td>
        <td>None</td>
        <td>2013-08-02 02:19:13</td>
        <td>2013-08-02 02:50:11</td>
        <td>7</td>
        <td>fd4a14fc-7144-11e5-ba71-058fbc01cf0b</td>
    </tr>
</table>
<span style="font-style:italic;text-align:center;">8816 rows, truncated to displaylimit of 1000</span>



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
