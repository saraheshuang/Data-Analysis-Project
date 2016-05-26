
Copyright Jana Schaich Borg/Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)

# MySQL Queries that Test Relationships Between Test Completion and Testing Circumstances 

In this lesson, we are going to practice integrating more of the concepts we learned over the past few weeks to address whether issues in our Dognition sPAP are related to the number of tests dogs complete.  We are going to focus on a subset of the issues listed in the "Features of Testing Circumstances" branch of our sPAP.  You will need to look up new functions several times and the final queries at which we will arrive by the end of this lesson will be quite complex, but we will work up to them step-by-step.  


## 1. During which weekdays do Dognition users complete the most tests?

The first question we are going to address is whether there is a certain day of the week when users are more or less likely to complete Dognition tests.  If so, targeting promotions or reminder emails to those times of the week might increase the number of tests users complete.

At first, the query we need to address this question might seem a bit intimidating, but once you can describe what the query needs to do in words, writing the query won't seem so challenging.  

Ultimately, we want a count of the number of tests completed on each day of the week, with all of the dog_guids and user_guids the Dognition team flagged in their exclude column excluded.  To achieve this, we are going to have to use the GROUP BY clause to break up counts of the records in the completed_tests table according to days of the week.  We will also have to join the completed_tests table with the dogs and users table in order to exclude completed_tests records that are associated with dog_guids or user_guids that should be excluded.  First, though, we need a method for extracting the day of the week from a time stamp.  In MySQL Exercise 2 we used a function called "DAYNAME".  That is the most efficient function to use for this purpose, but not all database systems have this function, so let's try using a different method for the queries in this lesson.   Search these sites to find a function that will output a number from 1-7 for time stamps where 1 = Sunday, 2 = Monday, …, 7 = Saturday:

http://dev.mysql.com/doc/refman/5.7/en/func-op-summary-ref.html      
http://www.w3resource.com/mysql/mysql-functions-and-operators.php

**Question 1: Using the function you found in the websites above, write a query that will output one column with the original created_at time stamp from each row in the completed_tests table, and another column with a number that represents the day of the week associated with each of those time stamps.  Limit your output to 200 rows starting at row 50.**


```python
%sql select created_at, Dayofweek(created_at) from complete_tests limit 50, 200;
```

    200 rows affected.





<table>
    <tr>
        <th>created_at</th>
        <th>Dayofweek(created_at)</th>
    </tr>
    <tr>
        <td>2013-02-05 22:23:49</td>
        <td>3</td>
    </tr>
    <tr>
        <td>2013-02-05 22:26:36</td>
        <td>3</td>
    </tr>
    <tr>
        <td>2013-02-05 22:29:02</td>
        <td>3</td>
    </tr>
    <tr>
        <td>2013-02-05 22:32:25</td>
        <td>3</td>
    </tr>
    <tr>
        <td>2013-02-05 22:33:09</td>
        <td>3</td>
    </tr>
    <tr>
        <td>2013-02-05 22:36:11</td>
        <td>3</td>
    </tr>
    <tr>
        <td>2013-02-05 22:38:01</td>
        <td>3</td>
    </tr>
    <tr>
        <td>2013-02-05 22:48:58</td>
        <td>3</td>
    </tr>
    <tr>
        <td>2013-02-05 22:53:45</td>
        <td>3</td>
    </tr>
    <tr>
        <td>2013-02-05 22:59:45</td>
        <td>3</td>
    </tr>
    <tr>
        <td>2013-02-05 23:01:38</td>
        <td>3</td>
    </tr>
    <tr>
        <td>2013-02-05 23:04:43</td>
        <td>3</td>
    </tr>
    <tr>
        <td>2013-02-05 23:06:10</td>
        <td>3</td>
    </tr>
    <tr>
        <td>2013-02-05 23:35:48</td>
        <td>3</td>
    </tr>
    <tr>
        <td>2013-02-05 23:40:57</td>
        <td>3</td>
    </tr>
    <tr>
        <td>2013-02-05 23:45:30</td>
        <td>3</td>
    </tr>
    <tr>
        <td>2013-02-05 23:48:46</td>
        <td>3</td>
    </tr>
    <tr>
        <td>2013-02-05 23:54:40</td>
        <td>3</td>
    </tr>
    <tr>
        <td>2013-02-05 23:59:15</td>
        <td>3</td>
    </tr>
    <tr>
        <td>2013-02-06 00:05:31</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 00:12:23</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 00:16:59</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 00:20:04</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 00:24:26</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 00:34:56</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 00:41:07</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 00:45:05</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 02:00:27</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 02:04:21</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 02:07:04</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 02:11:28</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 02:19:33</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 02:25:46</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 02:32:33</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 02:39:41</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 02:43:36</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 02:46:34</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 02:51:18</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 02:57:10</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 03:02:47</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 03:08:57</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 03:12:09</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 03:17:13</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 03:22:53</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 03:25:20</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 03:32:08</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 03:37:57</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 03:42:35</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 03:49:31</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 03:55:52</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 04:00:08</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 04:05:42</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 04:06:40</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 04:11:51</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 04:16:18</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 04:21:38</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 04:23:24</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 04:31:32</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 04:33:53</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 04:40:04</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 04:44:50</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 04:45:28</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 04:47:51</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 04:48:29</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 04:48:52</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 04:53:53</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 05:00:40</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 05:03:59</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 05:22:26</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 05:27:00</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 05:32:58</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 05:39:04</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 05:52:28</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 06:04:01</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 06:10:28</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 06:17:25</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 06:23:00</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 06:47:43</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 06:52:29</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 06:57:38</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 06:59:09</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 07:00:46</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 07:02:46</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 07:03:43</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 13:47:07</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 13:51:15</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 13:53:20</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 13:56:08</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 18:07:18</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 18:10:23</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 18:12:05</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 18:14:05</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 18:16:13</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 18:16:17</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 19:18:07</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 19:19:06</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 19:20:46</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 19:23:40</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 19:23:52</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 19:24:34</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 19:24:54</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 19:30:09</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 19:38:16</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 20:14:43</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 20:19:34</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 21:56:44</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 21:57:45</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 21:59:35</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 22:03:51</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 22:04:10</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 22:04:57</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 22:08:02</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 22:09:52</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 22:12:11</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 22:14:00</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 22:16:28</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 22:17:58</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 22:19:13</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 22:22:09</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 22:22:38</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 22:28:22</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 22:31:59</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 22:35:27</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 22:38:31</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 22:40:18</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 22:41:28</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 22:48:21</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 22:54:06</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 22:59:24</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-06 23:05:10</td>
        <td>4</td>
    </tr>
    <tr>
        <td>2013-02-07 00:57:00</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 01:02:09</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 01:05:29</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 01:07:52</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 01:09:45</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 01:09:40</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 01:12:06</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 01:14:00</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 01:14:04</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 01:17:01</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 01:19:01</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 01:21:26</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 01:24:04</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 01:25:48</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 01:26:46</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 02:02:41</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 02:06:14</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 02:09:41</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 02:12:25</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 02:13:07</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 02:50:52</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 02:55:53</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 02:59:17</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 03:00:05</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 03:01:18</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 03:03:20</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 03:08:27</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 03:09:10</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 03:13:52</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 03:16:21</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 03:18:50</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 03:22:06</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 03:23:50</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 03:25:29</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 03:27:06</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 03:32:38</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 03:37:17</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 03:50:51</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 03:57:37</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 04:01:54</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 04:04:22</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 04:09:37</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 04:12:51</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 04:18:30</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 04:23:30</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 04:32:59</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 04:36:25</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 04:38:07</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 04:41:09</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 04:41:21</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 04:43:42</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 04:46:01</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 04:48:07</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 04:51:37</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 04:57:21</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 05:02:54</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 05:08:07</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 05:15:48</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 05:20:28</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 05:23:04</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 05:27:23</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 05:45:34</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 05:47:34</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 05:53:07</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 05:56:42</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 06:02:10</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 06:07:25</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 06:18:55</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 15:05:09</td>
        <td>5</td>
    </tr>
    <tr>
        <td>2013-02-07 15:13:43</td>
        <td>5</td>
    </tr>
</table>



Of course, the results of the query in Question 1 would be much easier to interpret if the output included the name of the day of the week (or a relevant abbreviation) associated with each time stamp rather than a number index.

**Question 2: Include a CASE statement in the query you wrote in Question 1 to output a third column that provides the weekday name (or an appropriate abbreviation) associated with each created_at time stamp.**


```python
%%sql select created_at, Dayofweek(created_at), case DayofWeek(created_at) when 1 then "Mon" when 2 then "Tues" when 3 then "Wed" 
when 4 then "Thur" when 5 then "Fri" when 6 then "Sat" when 7 then "Sun" end as weekday 
from complete_tests limit 50, 200;
```

    200 rows affected.





<table>
    <tr>
        <th>created_at</th>
        <th>Dayofweek(created_at)</th>
        <th>weekday</th>
    </tr>
    <tr>
        <td>2013-02-05 22:23:49</td>
        <td>3</td>
        <td>Wed</td>
    </tr>
    <tr>
        <td>2013-02-05 22:26:36</td>
        <td>3</td>
        <td>Wed</td>
    </tr>
    <tr>
        <td>2013-02-05 22:29:02</td>
        <td>3</td>
        <td>Wed</td>
    </tr>
    <tr>
        <td>2013-02-05 22:32:25</td>
        <td>3</td>
        <td>Wed</td>
    </tr>
    <tr>
        <td>2013-02-05 22:33:09</td>
        <td>3</td>
        <td>Wed</td>
    </tr>
    <tr>
        <td>2013-02-05 22:36:11</td>
        <td>3</td>
        <td>Wed</td>
    </tr>
    <tr>
        <td>2013-02-05 22:38:01</td>
        <td>3</td>
        <td>Wed</td>
    </tr>
    <tr>
        <td>2013-02-05 22:48:58</td>
        <td>3</td>
        <td>Wed</td>
    </tr>
    <tr>
        <td>2013-02-05 22:53:45</td>
        <td>3</td>
        <td>Wed</td>
    </tr>
    <tr>
        <td>2013-02-05 22:59:45</td>
        <td>3</td>
        <td>Wed</td>
    </tr>
    <tr>
        <td>2013-02-05 23:01:38</td>
        <td>3</td>
        <td>Wed</td>
    </tr>
    <tr>
        <td>2013-02-05 23:04:43</td>
        <td>3</td>
        <td>Wed</td>
    </tr>
    <tr>
        <td>2013-02-05 23:06:10</td>
        <td>3</td>
        <td>Wed</td>
    </tr>
    <tr>
        <td>2013-02-05 23:35:48</td>
        <td>3</td>
        <td>Wed</td>
    </tr>
    <tr>
        <td>2013-02-05 23:40:57</td>
        <td>3</td>
        <td>Wed</td>
    </tr>
    <tr>
        <td>2013-02-05 23:45:30</td>
        <td>3</td>
        <td>Wed</td>
    </tr>
    <tr>
        <td>2013-02-05 23:48:46</td>
        <td>3</td>
        <td>Wed</td>
    </tr>
    <tr>
        <td>2013-02-05 23:54:40</td>
        <td>3</td>
        <td>Wed</td>
    </tr>
    <tr>
        <td>2013-02-05 23:59:15</td>
        <td>3</td>
        <td>Wed</td>
    </tr>
    <tr>
        <td>2013-02-06 00:05:31</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 00:12:23</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 00:16:59</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 00:20:04</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 00:24:26</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 00:34:56</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 00:41:07</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 00:45:05</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 02:00:27</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 02:04:21</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 02:07:04</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 02:11:28</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 02:19:33</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 02:25:46</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 02:32:33</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 02:39:41</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 02:43:36</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 02:46:34</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 02:51:18</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 02:57:10</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 03:02:47</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 03:08:57</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 03:12:09</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 03:17:13</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 03:22:53</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 03:25:20</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 03:32:08</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 03:37:57</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 03:42:35</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 03:49:31</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 03:55:52</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 04:00:08</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 04:05:42</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 04:06:40</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 04:11:51</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 04:16:18</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 04:21:38</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 04:23:24</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 04:31:32</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 04:33:53</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 04:40:04</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 04:44:50</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 04:45:28</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 04:47:51</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 04:48:29</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 04:48:52</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 04:53:53</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 05:00:40</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 05:03:59</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 05:22:26</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 05:27:00</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 05:32:58</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 05:39:04</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 05:52:28</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 06:04:01</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 06:10:28</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 06:17:25</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 06:23:00</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 06:47:43</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 06:52:29</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 06:57:38</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 06:59:09</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 07:00:46</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 07:02:46</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 07:03:43</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 13:47:07</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 13:51:15</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 13:53:20</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 13:56:08</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 18:07:18</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 18:10:23</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 18:12:05</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 18:14:05</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 18:16:13</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 18:16:17</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 19:18:07</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 19:19:06</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 19:20:46</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 19:23:40</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 19:23:52</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 19:24:34</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 19:24:54</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 19:30:09</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 19:38:16</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 20:14:43</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 20:19:34</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 21:56:44</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 21:57:45</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 21:59:35</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 22:03:51</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 22:04:10</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 22:04:57</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 22:08:02</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 22:09:52</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 22:12:11</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 22:14:00</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 22:16:28</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 22:17:58</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 22:19:13</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 22:22:09</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 22:22:38</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 22:28:22</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 22:31:59</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 22:35:27</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 22:38:31</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 22:40:18</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 22:41:28</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 22:48:21</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 22:54:06</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 22:59:24</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-06 23:05:10</td>
        <td>4</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>2013-02-07 00:57:00</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 01:02:09</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 01:05:29</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 01:07:52</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 01:09:45</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 01:09:40</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 01:12:06</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 01:14:00</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 01:14:04</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 01:17:01</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 01:19:01</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 01:21:26</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 01:24:04</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 01:25:48</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 01:26:46</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 02:02:41</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 02:06:14</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 02:09:41</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 02:12:25</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 02:13:07</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 02:50:52</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 02:55:53</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 02:59:17</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 03:00:05</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 03:01:18</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 03:03:20</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 03:08:27</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 03:09:10</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 03:13:52</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 03:16:21</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 03:18:50</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 03:22:06</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 03:23:50</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 03:25:29</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 03:27:06</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 03:32:38</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 03:37:17</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 03:50:51</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 03:57:37</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 04:01:54</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 04:04:22</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 04:09:37</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 04:12:51</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 04:18:30</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 04:23:30</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 04:32:59</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 04:36:25</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 04:38:07</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 04:41:09</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 04:41:21</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 04:43:42</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 04:46:01</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 04:48:07</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 04:51:37</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 04:57:21</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 05:02:54</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 05:08:07</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 05:15:48</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 05:20:28</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 05:23:04</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 05:27:23</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 05:45:34</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 05:47:34</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 05:53:07</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 05:56:42</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 06:02:10</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 06:07:25</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 06:18:55</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 15:05:09</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
    <tr>
        <td>2013-02-07 15:13:43</td>
        <td>5</td>
        <td>Fri</td>
    </tr>
</table>



Now that we are confident we have the correct syntax for extracting weekday labels from the created_at time stamps, we can start building our larger query that examines the number of tests completed on each weekday.

**Question 3: Adapt the query you wrote in Question 2 to report the total number of tests completed on each weekday.  Sort the results by the total number of tests completed in descending order.  You should get a total of 33,190 tests in the Sunday row of your output.**


```python
%%sql select count(created_at) as total_tests, Dayofweek(created_at), case DayofWeek(created_at) when 2 then "Mon" when 3 then "Tues" when 4 then "Wed" 
when 5 then "Thur" when 6 then "Fri" when 6 then "Sat" when 1 then "Sun" end as weekday 
from complete_tests group by weekday order by total_tests desc;
```

    7 rows affected.





<table>
    <tr>
        <th>total_tests</th>
        <th>Dayofweek(created_at)</th>
        <th>weekday</th>
    </tr>
    <tr>
        <td>33190</td>
        <td>1</td>
        <td>Sun</td>
    </tr>
    <tr>
        <td>30195</td>
        <td>2</td>
        <td>Mon</td>
    </tr>
    <tr>
        <td>27989</td>
        <td>3</td>
        <td>Tues</td>
    </tr>
    <tr>
        <td>27899</td>
        <td>7</td>
        <td>None</td>
    </tr>
    <tr>
        <td>26473</td>
        <td>4</td>
        <td>Wed</td>
    </tr>
    <tr>
        <td>24420</td>
        <td>5</td>
        <td>Thur</td>
    </tr>
    <tr>
        <td>23080</td>
        <td>6</td>
        <td>Fri</td>
    </tr>
</table>



So far these results suggest that users complete the most tests on Sunday night and the fewest tests on Friday night.  We need to determine if this trend remains after flagged dog_guids and user_guids are excluded.  Let's start by removing the dog_guids that have an exclude flag.  We'll exclude user_guids with an exclude flag in later queries.

**Question 4: Rewrite the query in Question 3 to exclude the dog_guids that have a value of "1" in the exclude column (Hint: this query will require a join.)  This time you should get a total of 31,092 tests in the Sunday row of your output.**


```python
%%sql select case DayofWeek(c.created_at) when 2 then "Mon" when 3 then "Tues" when 4 then "Wed" 
when 5 then "Thur" when 6 then "Fri" when 6 then "Sat" when 1 then "Sun" end as weekday, count(c.created_at) as total_tests 
from complete_tests c join dogs d on c.dog_guid=d.dog_guid 
where d.exclude=0 or d.exclude is null
group by weekday order by total_tests desc;
```

    7 rows affected.





<table>
    <tr>
        <th>weekday</th>
        <th>total_tests</th>
    </tr>
    <tr>
        <td>Sun</td>
        <td>31092</td>
    </tr>
    <tr>
        <td>Mon</td>
        <td>28250</td>
    </tr>
    <tr>
        <td>None</td>
        <td>26231</td>
    </tr>
    <tr>
        <td>Tues</td>
        <td>25764</td>
    </tr>
    <tr>
        <td>Wed</td>
        <td>24501</td>
    </tr>
    <tr>
        <td>Thur</td>
        <td>22347</td>
    </tr>
    <tr>
        <td>Fri</td>
        <td>21028</td>
    </tr>
</table>



Now we need to exclude the user_guids that have a value of "1" in the exclude column as well.  One way to do this would be to join the completed_tests, dogs, and users table with a sequence of inner joins.  However, we've seen in previous lessons that there are duplicate rows in the users table.  These duplicates will get passed through the join and will affect the count calculations.  To illustrate this, compare the following two queries.

**Question 5: Write a query to count all the dog_guids for users common to the dogs and users table using the traditional inner join syntax (your output will be 950,331).**


```python
%sql select count(d.dog_guid) from users u join dogs d where d.user_guid=u.user_guid;
```

    1 rows affected.





<table>
    <tr>
        <th>count(d.dog_guid)</th>
    </tr>
    <tr>
        <td>950331</td>
    </tr>
</table>



**Question 6: Write a query to count all the *distinct* dog_guids common to the dogs and users table using the traditional inner join syntax (your output will be 35,048).**


```python
%sql select count(distinct d.dog_guid) from users u join dogs d where d.user_guid=u.user_guid;
```

    1 rows affected.





<table>
    <tr>
        <th>count(distinct d.dog_guid)</th>
    </tr>
    <tr>
        <td>35048</td>
    </tr>
</table>



The strategy we will use to handle duplicate rows in the users table will be to, first, write a subquery that retrieves the distinct dog_guids from an inner join between the dogs and users table with the appropriate records excluded.  Then, second, we will join the result of this subquery to the complete_tests table and group the results according to the day of the week.

**Question 7: Start by writing a query that counts distinct dog_guids common to the dogs and users table, excuding dog_guids and user_guids with a "1" in their respective exclude columns (your output will be 34,121).**


```python
%%sql select count(distinct d.dog_guid) from users u join dogs d 
where d.user_guid=u.user_guid and (u.exclude=0 or u.exclude is null) and (d.exclude=0 or d.exclude is null);
```

    1 rows affected.





<table>
    <tr>
        <th>count(distinct d.dog_guid)</th>
    </tr>
    <tr>
        <td>34121</td>
    </tr>
</table>



**Question 8: Now adapt your query from Question 4 so that it inner joins on the result of the subquery you wrote in Question 7 instead of the dogs table.  This will give you a count of the number of tests completed on each day of the week, excluding all of the dog_guids and user_guids that the Dognition team flagged in the exclude columns.**  


```python
%%sql
select case DayofWeek(c.created_at) when 2 then "Mon" when 3 then "Tues" when 4 then "Wed" 
when 5 then "Thur" when 6 then "Fri" when 6 then "Sat" when 1 then "Sun" end as weekday, count(c.created_at) as total_tests 
from complete_tests c join
(select distinct d.dog_guid as dogID
from users u join dogs d 
where d.user_guid=u.user_guid and (u.exclude=0 or u.exclude is null) and (d.exclude=0 or d.exclude is null)) as newdogs
on c.dog_guid=newdogs.dogID
group by weekday order by total_tests desc;
```

    7 rows affected.





<table>
    <tr>
        <th>weekday</th>
        <th>total_tests</th>
    </tr>
    <tr>
        <td>Sun</td>
        <td>31036</td>
    </tr>
    <tr>
        <td>Mon</td>
        <td>28138</td>
    </tr>
    <tr>
        <td>None</td>
        <td>26149</td>
    </tr>
    <tr>
        <td>Tues</td>
        <td>25696</td>
    </tr>
    <tr>
        <td>Wed</td>
        <td>24433</td>
    </tr>
    <tr>
        <td>Thur</td>
        <td>22323</td>
    </tr>
    <tr>
        <td>Fri</td>
        <td>21027</td>
    </tr>
</table>



These results still suggest that Sunday is the day when the most tests are completed and Friday is the day when the fewest tests are completed.  However, our first query suggested that more tests were completed on Tuesday than Saturday; our current query suggests that slightly more tests are completed on Saturday than Tuesday, now that flagged dog_guids and user_guids are excluded.

It's always a good idea to see if a data pattern replicates before you interpret it too strongly.  The ideal way to do this would be to have a completely separate and independent data set to analyze.  We don't have such a data set, but we can assess the reliability of the day of the week patterns in a different way.  We can test whether the day of the week patterns are the same in all years of our data set.

**Question 9: Adapt your query from Question 8 to provide a count of the number of tests completed on each weekday of each year in the Dognition data set.  Exclude all dog_guids and user_guids with a value of "1" in their exclude columns.  Sort the output by year in ascending order, and then by the total number of tests completed in descending order. HINT: you will need a function described in one of these references to retrieve the year of each time stamp in the created_at field:**

http://dev.mysql.com/doc/refman/5.7/en/func-op-summary-ref.html      
http://www.w3resource.com/mysql/mysql-functions-and-operators.php


```python
%%sql
select year(c.created_at) as Year, case DayofWeek(c.created_at) when 2 then "Mon" when 3 then "Tues" when 4 then "Wed" 
when 5 then "Thur" when 6 then "Fri" when 6 then "Sat" when 1 then "Sun" end as weekday, count(c.created_at) as total_tests 
from complete_tests c join
(select distinct d.dog_guid as dogID
from users u join dogs d 
where d.user_guid=u.user_guid and (u.exclude=0 or u.exclude is null) and (d.exclude=0 or d.exclude is null)) as newdogs
on c.dog_guid=newdogs.dogID
group by Year, weekday 
order by total_tests desc;
```

    21 rows affected.





<table>
    <tr>
        <th>Year</th>
        <th>weekday</th>
        <th>total_tests</th>
    </tr>
    <tr>
        <td>2015</td>
        <td>Sun</td>
        <td>13623</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>Mon</td>
        <td>13089</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>Tues</td>
        <td>11126</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>None</td>
        <td>11038</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>Thur</td>
        <td>10076</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>Wed</td>
        <td>9911</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>Fri</td>
        <td>9555</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Mon</td>
        <td>9309</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Sun</td>
        <td>9210</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Tues</td>
        <td>9177</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Wed</td>
        <td>8857</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>None</td>
        <td>8257</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>Sun</td>
        <td>8203</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Thur</td>
        <td>7286</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>None</td>
        <td>6854</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Fri</td>
        <td>6475</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>Mon</td>
        <td>5740</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>Wed</td>
        <td>5665</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>Tues</td>
        <td>5393</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>Fri</td>
        <td>4997</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>Thur</td>
        <td>4961</td>
    </tr>
</table>



These results suggest that although the precise order of the weekdays with the most to fewest completed tests changes slightly from year to year, Sundays always have a lot of completed tests, and Fridays always have the fewest or close to the fewest completed tests.  So far, it seems like it might be a good idea for Dognition to target reminder or encouragement messages to customers on Sundays.  However, there is one more issue our analysis does not address.  All of the time stamps in the created_at column are in Coordinated Universal Time (abbreviated UTC).  This is a time convention that is constant around the globe.  Nonetheless, as the picture below illustrates, countries and states have different time zones.  The same UTC time can correspond with local times in different countries that are as much as 24 hours apart:

<img src="https://duke.box.com/shared/static/0p8ee9az908soq1m0o4jst94vqlh2oh7.jpg" width=600 alt="TIME_ZONE_MAP" />


Therefore, the weekdays we have extracted so far may not accurately reflect the weekdays in the local times of different countries.  The only way to correct the time stamps for time zone differences is to obtain a table with the time zones of every city, state, or country.  Such a table was not available to us in this course, but we can run some analyses that approximate a time zone correction for United States customers.

**Question 10: First, adapt your query from Question 9 so that you only examine customers located in the United States, with Hawaii and Alaska residents excluded.  HINTS: In this data set, the abbreviation for the United States is "US", the abbreviation for Hawaii is "HI" and the abbreviation for Alaska is "AK".  You should have 5,860 tests completed on Sunday of 2013.**


```python
%%sql
select year(c.created_at) as Year, case DayofWeek(c.created_at) when 2 then "Mon" when 3 then "Tues" when 4 then "Wed" 
when 5 then "Thur" when 6 then "Fri" when 6 then "Sat" when 1 then "Sun" end as weekday, count(c.created_at) as total_tests 
from complete_tests c join
(select distinct d.dog_guid as dogID
from users u join dogs d 
where d.user_guid=u.user_guid and (u.exclude=0 or u.exclude is null) and (u.country="US" and u.state not in ("AK", "HI")) and (d.exclude=0 or d.exclude is null)) as newdogs
on c.dog_guid=newdogs.dogID
group by Year, weekday 
order by total_tests desc;
```

    21 rows affected.





<table>
    <tr>
        <th>Year</th>
        <th>weekday</th>
        <th>total_tests</th>
    </tr>
    <tr>
        <td>2015</td>
        <td>Mon</td>
        <td>8784</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>Sun</td>
        <td>8570</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Mon</td>
        <td>7278</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>Tues</td>
        <td>7218</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>None</td>
        <td>7116</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Tues</td>
        <td>6800</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Sun</td>
        <td>6632</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>Thur</td>
        <td>6343</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Wed</td>
        <td>6331</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>Wed</td>
        <td>6164</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>None</td>
        <td>6006</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>Sun</td>
        <td>5860</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>Fri</td>
        <td>5689</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Thur</td>
        <td>5271</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Fri</td>
        <td>4831</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>None</td>
        <td>4674</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>Mon</td>
        <td>3695</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>Wed</td>
        <td>3496</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>Tues</td>
        <td>3449</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>Fri</td>
        <td>3163</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>Thur</td>
        <td>3090</td>
    </tr>
</table>



The next step is to adjust the created_at times for differences in time zone. Most United States states (excluding Hawaii and Alaska) have a time zone of UTC time -5 hours (in the eastern-most regions) to -8 hours (in the western-most regions).  To get a general idea for how much our weekday analysis is likely to change based on time zone, we will subtract 6 hours from every time stamp in the complete_tests table.  Although this means our time stamps can be inaccurate by 1 or 2 hours, people are not likely to be playing Dognition games at midnight, so 1-2 hours should not affect the weekdays extracted from each time stamp too much. 

The functions used to subtract time differ across database systems, so you should double-check which function you need to use every time you are working with a new database.  We will use the date_sub function:

http://www.w3schools.com/sql/func_date_sub.asp

**Question 11: Write a query that extracts the original created_at time stamps for rows in the complete_tests table in one column, and the created_at time stamps with 6 hours subtracted in another column.  Limit your output to 100 rows.**


```python
%sql select created_at, date_sub(created_at, interval 6 hour) as new_date from complete_tests limit 100;
```

    100 rows affected.





<table>
    <tr>
        <th>created_at</th>
        <th>new_date</th>
    </tr>
    <tr>
        <td>2013-02-05 18:26:54</td>
        <td>2013-02-05 12:26:54</td>
    </tr>
    <tr>
        <td>2013-02-05 18:31:03</td>
        <td>2013-02-05 12:31:03</td>
    </tr>
    <tr>
        <td>2013-02-05 18:32:04</td>
        <td>2013-02-05 12:32:04</td>
    </tr>
    <tr>
        <td>2013-02-05 18:32:25</td>
        <td>2013-02-05 12:32:25</td>
    </tr>
    <tr>
        <td>2013-02-05 18:32:56</td>
        <td>2013-02-05 12:32:56</td>
    </tr>
    <tr>
        <td>2013-02-05 18:33:15</td>
        <td>2013-02-05 12:33:15</td>
    </tr>
    <tr>
        <td>2013-02-05 18:33:33</td>
        <td>2013-02-05 12:33:33</td>
    </tr>
    <tr>
        <td>2013-02-05 18:33:59</td>
        <td>2013-02-05 12:33:59</td>
    </tr>
    <tr>
        <td>2013-02-05 18:34:25</td>
        <td>2013-02-05 12:34:25</td>
    </tr>
    <tr>
        <td>2013-02-05 18:34:39</td>
        <td>2013-02-05 12:34:39</td>
    </tr>
    <tr>
        <td>2013-02-05 18:34:46</td>
        <td>2013-02-05 12:34:46</td>
    </tr>
    <tr>
        <td>2013-02-05 18:35:18</td>
        <td>2013-02-05 12:35:18</td>
    </tr>
    <tr>
        <td>2013-02-05 18:35:47</td>
        <td>2013-02-05 12:35:47</td>
    </tr>
    <tr>
        <td>2013-02-05 18:36:28</td>
        <td>2013-02-05 12:36:28</td>
    </tr>
    <tr>
        <td>2013-02-05 18:36:44</td>
        <td>2013-02-05 12:36:44</td>
    </tr>
    <tr>
        <td>2013-02-05 18:57:05</td>
        <td>2013-02-05 12:57:05</td>
    </tr>
    <tr>
        <td>2013-02-05 19:01:31</td>
        <td>2013-02-05 13:01:31</td>
    </tr>
    <tr>
        <td>2013-02-05 19:04:42</td>
        <td>2013-02-05 13:04:42</td>
    </tr>
    <tr>
        <td>2013-02-05 19:07:39</td>
        <td>2013-02-05 13:07:39</td>
    </tr>
    <tr>
        <td>2013-02-05 19:15:01</td>
        <td>2013-02-05 13:15:01</td>
    </tr>
    <tr>
        <td>2013-02-05 19:21:15</td>
        <td>2013-02-05 13:21:15</td>
    </tr>
    <tr>
        <td>2013-02-05 19:28:27</td>
        <td>2013-02-05 13:28:27</td>
    </tr>
    <tr>
        <td>2013-02-05 19:51:57</td>
        <td>2013-02-05 13:51:57</td>
    </tr>
    <tr>
        <td>2013-02-05 19:58:06</td>
        <td>2013-02-05 13:58:06</td>
    </tr>
    <tr>
        <td>2013-02-05 20:05:57</td>
        <td>2013-02-05 14:05:57</td>
    </tr>
    <tr>
        <td>2013-02-05 20:08:02</td>
        <td>2013-02-05 14:08:02</td>
    </tr>
    <tr>
        <td>2013-02-05 20:35:47</td>
        <td>2013-02-05 14:35:47</td>
    </tr>
    <tr>
        <td>2013-02-05 20:47:00</td>
        <td>2013-02-05 14:47:00</td>
    </tr>
    <tr>
        <td>2013-02-05 20:50:45</td>
        <td>2013-02-05 14:50:45</td>
    </tr>
    <tr>
        <td>2013-02-05 20:53:59</td>
        <td>2013-02-05 14:53:59</td>
    </tr>
    <tr>
        <td>2013-02-05 20:54:19</td>
        <td>2013-02-05 14:54:19</td>
    </tr>
    <tr>
        <td>2013-02-05 20:54:36</td>
        <td>2013-02-05 14:54:36</td>
    </tr>
    <tr>
        <td>2013-02-05 20:54:52</td>
        <td>2013-02-05 14:54:52</td>
    </tr>
    <tr>
        <td>2013-02-05 20:55:03</td>
        <td>2013-02-05 14:55:03</td>
    </tr>
    <tr>
        <td>2013-02-05 20:55:12</td>
        <td>2013-02-05 14:55:12</td>
    </tr>
    <tr>
        <td>2013-02-05 20:55:22</td>
        <td>2013-02-05 14:55:22</td>
    </tr>
    <tr>
        <td>2013-02-05 21:12:31</td>
        <td>2013-02-05 15:12:31</td>
    </tr>
    <tr>
        <td>2013-02-05 21:20:10</td>
        <td>2013-02-05 15:20:10</td>
    </tr>
    <tr>
        <td>2013-02-05 21:26:51</td>
        <td>2013-02-05 15:26:51</td>
    </tr>
    <tr>
        <td>2013-02-05 21:33:24</td>
        <td>2013-02-05 15:33:24</td>
    </tr>
    <tr>
        <td>2013-02-05 21:44:38</td>
        <td>2013-02-05 15:44:38</td>
    </tr>
    <tr>
        <td>2013-02-05 21:45:12</td>
        <td>2013-02-05 15:45:12</td>
    </tr>
    <tr>
        <td>2013-02-05 21:48:58</td>
        <td>2013-02-05 15:48:58</td>
    </tr>
    <tr>
        <td>2013-02-05 21:51:17</td>
        <td>2013-02-05 15:51:17</td>
    </tr>
    <tr>
        <td>2013-02-05 21:54:53</td>
        <td>2013-02-05 15:54:53</td>
    </tr>
    <tr>
        <td>2013-02-05 21:55:15</td>
        <td>2013-02-05 15:55:15</td>
    </tr>
    <tr>
        <td>2013-02-05 21:58:19</td>
        <td>2013-02-05 15:58:19</td>
    </tr>
    <tr>
        <td>2013-02-05 22:02:30</td>
        <td>2013-02-05 16:02:30</td>
    </tr>
    <tr>
        <td>2013-02-05 22:06:34</td>
        <td>2013-02-05 16:06:34</td>
    </tr>
    <tr>
        <td>2013-02-05 22:10:06</td>
        <td>2013-02-05 16:10:06</td>
    </tr>
    <tr>
        <td>2013-02-05 22:23:49</td>
        <td>2013-02-05 16:23:49</td>
    </tr>
    <tr>
        <td>2013-02-05 22:26:36</td>
        <td>2013-02-05 16:26:36</td>
    </tr>
    <tr>
        <td>2013-02-05 22:29:02</td>
        <td>2013-02-05 16:29:02</td>
    </tr>
    <tr>
        <td>2013-02-05 22:32:25</td>
        <td>2013-02-05 16:32:25</td>
    </tr>
    <tr>
        <td>2013-02-05 22:33:09</td>
        <td>2013-02-05 16:33:09</td>
    </tr>
    <tr>
        <td>2013-02-05 22:36:11</td>
        <td>2013-02-05 16:36:11</td>
    </tr>
    <tr>
        <td>2013-02-05 22:38:01</td>
        <td>2013-02-05 16:38:01</td>
    </tr>
    <tr>
        <td>2013-02-05 22:48:58</td>
        <td>2013-02-05 16:48:58</td>
    </tr>
    <tr>
        <td>2013-02-05 22:53:45</td>
        <td>2013-02-05 16:53:45</td>
    </tr>
    <tr>
        <td>2013-02-05 22:59:45</td>
        <td>2013-02-05 16:59:45</td>
    </tr>
    <tr>
        <td>2013-02-05 23:01:38</td>
        <td>2013-02-05 17:01:38</td>
    </tr>
    <tr>
        <td>2013-02-05 23:04:43</td>
        <td>2013-02-05 17:04:43</td>
    </tr>
    <tr>
        <td>2013-02-05 23:06:10</td>
        <td>2013-02-05 17:06:10</td>
    </tr>
    <tr>
        <td>2013-02-05 23:35:48</td>
        <td>2013-02-05 17:35:48</td>
    </tr>
    <tr>
        <td>2013-02-05 23:40:57</td>
        <td>2013-02-05 17:40:57</td>
    </tr>
    <tr>
        <td>2013-02-05 23:45:30</td>
        <td>2013-02-05 17:45:30</td>
    </tr>
    <tr>
        <td>2013-02-05 23:48:46</td>
        <td>2013-02-05 17:48:46</td>
    </tr>
    <tr>
        <td>2013-02-05 23:54:40</td>
        <td>2013-02-05 17:54:40</td>
    </tr>
    <tr>
        <td>2013-02-05 23:59:15</td>
        <td>2013-02-05 17:59:15</td>
    </tr>
    <tr>
        <td>2013-02-06 00:05:31</td>
        <td>2013-02-05 18:05:31</td>
    </tr>
    <tr>
        <td>2013-02-06 00:12:23</td>
        <td>2013-02-05 18:12:23</td>
    </tr>
    <tr>
        <td>2013-02-06 00:16:59</td>
        <td>2013-02-05 18:16:59</td>
    </tr>
    <tr>
        <td>2013-02-06 00:20:04</td>
        <td>2013-02-05 18:20:04</td>
    </tr>
    <tr>
        <td>2013-02-06 00:24:26</td>
        <td>2013-02-05 18:24:26</td>
    </tr>
    <tr>
        <td>2013-02-06 00:34:56</td>
        <td>2013-02-05 18:34:56</td>
    </tr>
    <tr>
        <td>2013-02-06 00:41:07</td>
        <td>2013-02-05 18:41:07</td>
    </tr>
    <tr>
        <td>2013-02-06 00:45:05</td>
        <td>2013-02-05 18:45:05</td>
    </tr>
    <tr>
        <td>2013-02-06 02:00:27</td>
        <td>2013-02-05 20:00:27</td>
    </tr>
    <tr>
        <td>2013-02-06 02:04:21</td>
        <td>2013-02-05 20:04:21</td>
    </tr>
    <tr>
        <td>2013-02-06 02:07:04</td>
        <td>2013-02-05 20:07:04</td>
    </tr>
    <tr>
        <td>2013-02-06 02:11:28</td>
        <td>2013-02-05 20:11:28</td>
    </tr>
    <tr>
        <td>2013-02-06 02:19:33</td>
        <td>2013-02-05 20:19:33</td>
    </tr>
    <tr>
        <td>2013-02-06 02:25:46</td>
        <td>2013-02-05 20:25:46</td>
    </tr>
    <tr>
        <td>2013-02-06 02:32:33</td>
        <td>2013-02-05 20:32:33</td>
    </tr>
    <tr>
        <td>2013-02-06 02:39:41</td>
        <td>2013-02-05 20:39:41</td>
    </tr>
    <tr>
        <td>2013-02-06 02:43:36</td>
        <td>2013-02-05 20:43:36</td>
    </tr>
    <tr>
        <td>2013-02-06 02:46:34</td>
        <td>2013-02-05 20:46:34</td>
    </tr>
    <tr>
        <td>2013-02-06 02:51:18</td>
        <td>2013-02-05 20:51:18</td>
    </tr>
    <tr>
        <td>2013-02-06 02:57:10</td>
        <td>2013-02-05 20:57:10</td>
    </tr>
    <tr>
        <td>2013-02-06 03:02:47</td>
        <td>2013-02-05 21:02:47</td>
    </tr>
    <tr>
        <td>2013-02-06 03:08:57</td>
        <td>2013-02-05 21:08:57</td>
    </tr>
    <tr>
        <td>2013-02-06 03:12:09</td>
        <td>2013-02-05 21:12:09</td>
    </tr>
    <tr>
        <td>2013-02-06 03:17:13</td>
        <td>2013-02-05 21:17:13</td>
    </tr>
    <tr>
        <td>2013-02-06 03:22:53</td>
        <td>2013-02-05 21:22:53</td>
    </tr>
    <tr>
        <td>2013-02-06 03:25:20</td>
        <td>2013-02-05 21:25:20</td>
    </tr>
    <tr>
        <td>2013-02-06 03:32:08</td>
        <td>2013-02-05 21:32:08</td>
    </tr>
    <tr>
        <td>2013-02-06 03:37:57</td>
        <td>2013-02-05 21:37:57</td>
    </tr>
    <tr>
        <td>2013-02-06 03:42:35</td>
        <td>2013-02-05 21:42:35</td>
    </tr>
    <tr>
        <td>2013-02-06 03:49:31</td>
        <td>2013-02-05 21:49:31</td>
    </tr>
    <tr>
        <td>2013-02-06 03:55:52</td>
        <td>2013-02-05 21:55:52</td>
    </tr>
</table>



**Question 12: Use your query from Question 11 to adapt your query from Question 10 in order to provide a count of the number of tests completed on each day of the week, with approximate time zones taken into account, in each year in the Dognition data set. Exclude all dog_guids and user_guids with a value of "1" in their exclude columns. Sort the output by year in ascending order, and then by the total number of tests completed in descending order. HINT: Don't forget to adjust for the time zone in your DAYOFWEEK statement and your CASE statement.** 


```python
%%sql
select year(date_sub(c.created_at, interval 6 hour)) as Year, case DayofWeek(date_sub(c.created_at, interval 6 hour)) when 2 then "Mon" when 3 then "Tues" when 4 then "Wed" 
when 5 then "Thur" when 6 then "Fri" when 7 then "Sat" when 1 then "Sun" end as weekday, count(c.created_at) as total_tests 
from complete_tests c join
(select distinct d.dog_guid as dogID
from users u join dogs d 
where d.user_guid=u.user_guid and (u.exclude=0 or u.exclude is null) and (d.exclude=0 or d.exclude is null)) as newdogs
on c.dog_guid=newdogs.dogID
group by Year, weekday 
order by total_tests asc;
```

    21 rows affected.





<table>
    <tr>
        <th>Year</th>
        <th>weekday</th>
        <th>total_tests</th>
    </tr>
    <tr>
        <td>2013</td>
        <td>Thur</td>
        <td>4881</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>Fri</td>
        <td>4913</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>Tues</td>
        <td>5185</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>Wed</td>
        <td>5648</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>Mon</td>
        <td>5953</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Fri</td>
        <td>6020</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Thur</td>
        <td>6729</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>Sat</td>
        <td>6825</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Wed</td>
        <td>8046</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>Sun</td>
        <td>8413</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Sat</td>
        <td>8432</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>Fri</td>
        <td>8844</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Tues</td>
        <td>8987</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>Thur</td>
        <td>9745</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>Wed</td>
        <td>9983</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Sun</td>
        <td>10215</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Mon</td>
        <td>10247</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>Tues</td>
        <td>10515</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>Sat</td>
        <td>11086</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>Mon</td>
        <td>12364</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>Sun</td>
        <td>15771</td>
    </tr>
</table>



You can try re-running the query with time-zone corrections of 5, 7, or 8 hours, and the results remain essentially the same.  All of these analyses suggest that customers are most likely to complete tests around Sunday and Monday, and least likely to complete tests around the end of the work week, on Thursday and Friday. This is certainly valuable information for Dognition to take advantage of.

If you were presenting this information to the Dognition team, you might want to present the information in the form of a graph that you make in another program.  The graph would be easier to read if the output was ordered according to the days of the week shown in standard calendars, with Monday being the first day and Sunday being the last day.  MySQL provides an easy way to do this using the FIELD function in the ORDER BY statement:

https://www.virendrachandak.com/techtalk/mysql-ordering-results-by-specific-field-values/

**Question 13: Adapt your query from Question 12 so that the results are sorted by year in ascending order, and then by the day of the week in the following order: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.**


```python
%%sql
select year(date_sub(c.created_at, interval 6 hour)) as Year, case DayofWeek(date_sub(c.created_at, interval 6 hour)) when 2 then "Mon" when 3 then "Tues" when 4 then "Wed" 
when 5 then "Thur" when 6 then "Fri" when 7 then "Sat" when 1 then "Sun" end as weekday, count(c.created_at) as total_tests 
from complete_tests c join
(select distinct d.dog_guid as dogID
from users u join dogs d 
where d.user_guid=u.user_guid and (u.exclude=0 or u.exclude is null) and (d.exclude=0 or d.exclude is null)) as newdogs
on c.dog_guid=newdogs.dogID
group by Year, weekday
order by year asc, field(weekday,"Mon","Tues","Wed","Thur","Fri","Sat","Sun");
```

    21 rows affected.





<table>
    <tr>
        <th>Year</th>
        <th>weekday</th>
        <th>total_tests</th>
    </tr>
    <tr>
        <td>2013</td>
        <td>Mon</td>
        <td>5953</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>Tues</td>
        <td>5185</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>Wed</td>
        <td>5648</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>Thur</td>
        <td>4881</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>Fri</td>
        <td>4913</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>Sat</td>
        <td>6825</td>
    </tr>
    <tr>
        <td>2013</td>
        <td>Sun</td>
        <td>8413</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Mon</td>
        <td>10247</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Tues</td>
        <td>8987</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Wed</td>
        <td>8046</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Thur</td>
        <td>6729</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Fri</td>
        <td>6020</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Sat</td>
        <td>8432</td>
    </tr>
    <tr>
        <td>2014</td>
        <td>Sun</td>
        <td>10215</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>Mon</td>
        <td>12364</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>Tues</td>
        <td>10515</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>Wed</td>
        <td>9983</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>Thur</td>
        <td>9745</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>Fri</td>
        <td>8844</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>Sat</td>
        <td>11086</td>
    </tr>
    <tr>
        <td>2015</td>
        <td>Sun</td>
        <td>15771</td>
    </tr>
</table>



Unfortunately other database platforms do not have the ORDER BY FIELD functionality.  To achieve the same result in other platforms, you would have to use a CASE statement or a more advanced solution:

http://stackoverflow.com/questions/1309624/simulating-mysqls-order-by-field-in-postgresql

The link provided above is to a discussion on stackoverflow.com.  Stackoverflow is a great website that, in their words, "is a community of 4.7 million programmers, just like you, helping each other."  You can ask questions about SQL queries and get help from other experts, or search through questions posted previously to see if somebody else has already asked a question that is relevant to the problem you are trying to solve.  It's a great resource to use whenever you run into trouble with your queries.

## 2. Which states and countries have the most Dognition users?

You ended up with a pretty long and complex query in the questions above that you tested step-by-step.  Many people save these types of queries so that they can be adapted for similar queries in the future without having to redesign and retest the entire query.  
    
In the next two questions, we will practice repurposing previously-designed queries for new questions.  Both questions can be answered through relatively minor modifications of the queries you wrote above.

**Question 14: Which 5 states within the United States have the most Dognition customers, once all dog_guids and user_guids with a value of "1" in their exclude columns are removed?  Try using the following general strategy: count how many unique user_guids are associated with dogs in the complete_tests table, break up the counts according to state, sort the results by counts of unique user_guids in descending order, and then limit your output to 5 rows. California ("CA") and New York ("NY") should be at the top of your list.**


```python
%%sql 
select count(distinct n.UserID) as total_users, u.state as state 
from  (select d.user_guid as UserID, d.exclude
       from dogs d join complete_tests c
       where d.dog_guid=c.dog_guid and (d.exclude is null or d.exclude=0)) 
        as n join users u 
        on u.user_guid=UserID
        where u.state is not null and u.country="US"
        and (u.exclude is null or u.exclude=0)
        group by u.state 
        order by total_users desc
        limit 5;
```

    5 rows affected.





<table>
    <tr>
        <th>total_users</th>
        <th>state</th>
    </tr>
    <tr>
        <td>1363</td>
        <td>CA</td>
    </tr>
    <tr>
        <td>628</td>
        <td>NY</td>
    </tr>
    <tr>
        <td>536</td>
        <td>TX</td>
    </tr>
    <tr>
        <td>502</td>
        <td>FL</td>
    </tr>
    <tr>
        <td>467</td>
        <td>NC</td>
    </tr>
</table>



The number of unique Dognition users in California is more than two times greater than any other state.  This information could be very helpful to Dognition.  Useful follow-up questions would be: were special promotions run in California that weren't run in other states?  Did Dognition use advertising channels that are particularly effective in California?  If not, what traits differentiate California users from other users?  Can these traits be taken advantage of in future marketing efforts or product developments?

Let's try one more analysis that examines testing circumstances from a different angle.

**Question 15: Which 10 countries have the most Dognition customers, once all dog_guids and user_guids with a value of "1" in their exclude columns are removed? HINT: don't forget to remove the u.country="US" statement from your WHERE clause.**


```python
%%sql 
select count(distinct n.UserID) as total_users, u.country as Country 
from  (select d.user_guid as UserID, d.exclude
       from dogs d join complete_tests c
       where d.dog_guid=c.dog_guid and (d.exclude is null or d.exclude=0)) 
        as n join users u 
        on u.user_guid=UserID
        where (u.exclude is null or u.exclude=0) and u.country is not null
        group by u.country 
        order by total_users desc
        limit 10;
```

    10 rows affected.





<table>
    <tr>
        <th>total_users</th>
        <th>Country</th>
    </tr>
    <tr>
        <td>8936</td>
        <td>US</td>
    </tr>
    <tr>
        <td>5466</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>484</td>
        <td>CA</td>
    </tr>
    <tr>
        <td>142</td>
        <td>AU</td>
    </tr>
    <tr>
        <td>123</td>
        <td>GB</td>
    </tr>
    <tr>
        <td>40</td>
        <td>DE</td>
    </tr>
    <tr>
        <td>38</td>
        <td>NZ</td>
    </tr>
    <tr>
        <td>34</td>
        <td>DK</td>
    </tr>
    <tr>
        <td>30</td>
        <td>NO</td>
    </tr>
    <tr>
        <td>23</td>
        <td>FR</td>
    </tr>
</table>



The United States, Canada, Australia, and Great Britain are the countries with the most Dognition users.  N/A refers to "not applicable" which essentially means we have no usable country data from those rows.  After Great Britain, the number of Dognition users drops quite a lot.  This analysis suggests that Dognition is most likely to be used by English-speaking countries.  One question Dognition might want to consider is whether there are any countries whose participation would dramatically increase if a translated website were available.

## 3. Congratulations!

You have now written many complex queries on your own that address real analysis questions about a real business problem.  You know how to look up new functions, you know how to troubleshoot your queries by isolating each piece of the query until you are sure the syntax is correct, and you know where to look for help if you get stuck.  You are ready to start using SQL in your own business ventures.  Keep learning, keep trying new things, and keep asking questions.  Congratulations for taking your career to the next level!

There is another video to watch, and of course, more exercises to work through using the Dillard's data set.  
    
**In the meantime, enjoy practicing any other queries you want to try here:**


```python

```
