## A/B Test on Udacity's Enrollment Page's UI Change

``#a/b testing #effective size analysis #bonferroni test #sample size


##Project Summary

This project designs an A/B test and analyze the result related to Udacity's UI change related to the page of starting free trial. It defines the test metric (invariants and metric), measures the variability, determines the size and duration of A/B test and analyze the results. It recommends launching the change as it will increase the customers retention and net conversion rate and help Udacity to utilize its coarching resources at the most needed students.

## Project Background

At the time of this experiment, Udacity courses currently have two options on the home page: "start free trial", and "access course materials". If the student clicks "start free trial", they will be asked to enter their credit card information, and then they will be enrolled in a free trial for the paid version of the course. After 14 days, they will automatically be charged unless they cancel first. If the student clicks "access course materials", they will be able to view the videos and take the quizzes for free, but they will not receive coaching support or a verified certificate, and they will not submit their final project for feedback.

In the experiment, Udacity tested a change where if the student clicked "start free trial", they were asked how much time they had available to devote to the course. If the student indicated 5 or more hours per week, they would be taken through the checkout process as usual. If they indicated fewer than 5 hours per week, a message would appear indicating that Udacity courses usually require a greater time commitment for successful completion, and suggesting that the student might like to access the course materials for free. At this point, the student would have the option to continue enrolling in the free trial, or access the course materials for free instead. [This screenshot](https://drive.google.com/file/d/0ByAfiG8HpNUMakVrS0s4cGN2TjQ/view?usp=sharing) shows what the experiment looks like.

The hypothesis was that this might set clearer expectations for students upfront, thus 1) reducing the number of frustrated students who left the free trial because they didn't have enough time; 2) without significantly reducing the number of students to continue past the free trial and eventually complete the course. 

- Hypothesis 1: the number of enrolled peope will be significantly reduced;
- Hypothesis 2: the number of people making the payment will not decrease. 

If this hypothesis held true, Udacity could improve the overall student experience and improve coaches' capacity to support students who are likely to complete the course.

The unit of diversion is a cookie, although if the student enrolls in the free trial, they are tracked by user-id from that point forward. The same user-id cannot enroll in the free trial twice. For users that do not enroll, their user-id is not tracked in the experiment, even if they were signed in when they visited the course overview page.

## Experiment Design

### Metric Choice

#### Metrics

I chose the following metrics: gross conversion rate, retention rate and/or net conversion rate for evaluation. To validate the hypotheis above, the metric should include the gross conversion rate (which is expected to **decrease**), retention rate (which is expected to **increase**) and/OR net conversion rate (which is expected to be **unchanged**). Comparing net conversion rate and retention rate, it seems that net conversion rate is a better choice since it is unit of diversion is click instead of user ID, therefore the number of total pageviews it requires will likely be fewer.

- Gross conversion: That is, number of user-ids to complete checkout and enroll in the free trial divided by number of unique cookies to click the "Start free trial" button. 

- Retention: That is, number of user-ids to remain enrolled past the 14-day boundary (and thus make at least one payment) divided by number of user-ids to complete checkout. 

- Net conversion: That is, number of user-ids to remain enrolled past the 14-day boundary (and thus make at least one payment) divided by the number of unique cookies to click the "Start free trial" button. 


#### Sanity Check and Invariants
To do the experiment, I suggest take the sanity check with the following invariants. 

- Number of cookies: That is, number of unique cookies to view the course overview page. 
(since number of cookies will not be changed. It is the unit of diversion )

- Number of clicks: That is, number of unique cookies to click the "Start free trial" button (which happens before the free trial screener is trigger). 
(It happens beofre the triger, so the number of clicks should not change as much)

- Click-through-probability: That is, number of unique cookies to click the "Start free trial" button divided by number of unique cookies to view the course overview page. (Click happens before the UI change, so the click through probability should not change)

Number of user-ids will change as the UI change might affect the number of users who enroll in the free trial. 


###Measuring Standard Deviation
This section list the standard deviation of each of your evaluation metrics. 

- Gross Conversion Rate (Probability of enrolling at given click )


```
Probability of enrolling (Poe), given click is 0.20625
Standard Deviation at 5000 pageviews is 0.02023060414
sqrt(*(1-Poe)/(5000*0.08))	
```
- Retention Rate (Probability of payment at enrollment)

```
Probability of payment (Pop) at enrollment is 0.53	
Standard Deviation at 5000 pageviews is 0.05494901218, 
sqrt(Pop*(1-Pop)/(5000*0.08*0.20625))
```
- Net conversion rate (Probability of payment at given click)

```
Probability of payment(Popa) at given click	0.1093125
Standard Deviation at 5000 pageviews is 0.01560154458
sqrt(Popa*(1-Popa)/(5000*0.08))

```
Analysis: when the unit of analysis = unit of diversion, variability tend to be lower and closer to analytical estimate. The Pop has largest variability, which indicates it require much larger sample size than the other two indicators. Therefore, it might not be a good idea to include it in the metric. Therefore, the final metrics are

- Gross converstion rate

	Null hypothesis: GC(e)=GC(c)
	
	Alternative hypothese: GC(e)<GC(c)
	
- Net converstion rate

	Null hypothesis: NC(e)=NC(c)
	
	Alternative hypothese: NC(e)>=NC(c)
	
###Sizing

####Number of Samples vs. Power
Bonferroni correction will not be used as the metircs are correlated. 

```
Sample size for Poe is 25835/0.08*2=645875
Sample size for Popa is 27413/0.08*2=685325

```

####Duration vs. Exposure

Since no one will be hurt in this experiment and no sensitive information will be collected, it is fine to conduct the experiement without user consent form.

I will divert 0.856 traffic to experiment end, since this change is safe so the large exposure would not not be that dangerous. On the other hand, I would like the period cover the entire week so it would capture the user activities over the weekdays and weekends. So I chose 0.856 and the total will take 21 days.


##Experiment Analysis
###Sanity Checks

Sanity check for pageviews

```
n=total number of pageviews
se=sqrt(0.5*(1-0.5)*n)
m=se*1.96
d hat=0.5
The confidence interval is (0.4988,0.5011)
The observed pageview ratio 
(experiement pageviews/total pageviews)=0.5006. 
It falls into the confidence interval

```

Sanity check for clicks

```
n=total number of clicks
se=sqrt(0.5*(1-0.5)*n)
m=se*1.96
d hat=0.5
The confidence interval is (0.4959,0.5041)
The observed click ratio 
(experiement clicks/total clicks)=0.5005. 
It falls into the confidence interval
```
Sanity check for click through probability

```
n1=total number of pageviews in the experiment group
n2=total number of pageviews in the control group
p=average click through probability
p(pool)=0.082
n1=34660
n2=345543
se=sqrt(p*(1-p)*(1/n1+1/n2))
m=se*1.96
The confidence interval is (-m,m) which is (-0.0013,0.0013)
The real click through rate difference (experienment click through rate - control click through rate) is 0.0001
It falls into the confidence interval

```
The Sanity check is passed, we can continue to result analysis.

###Result Analysis

####Effect Size Tests

- Gross conversion (GC)

```
GC_diff=GC(e)-GC(c)=-0.02055
n_e=17260
n_c=17293
n_e_count=3423
n_c_count=3785
GC_pool=(n_c_count+n_c_count)/(n_e+n_c)
SE=sqrt(GC_pool*(1-GC_pool)*(1/n_e+1/n_c))
M=SE*1.96
CI is (GC_hat-M, GC_hat+M) which is (-0.029,-0.012)

```
Since the confidence interval is below 0 and the absolut(-0.012)>0.01, the result is statistically significant and practically significant.

- Net conversion

```
NC_diff=NC(e)-NC(c)=-0.0049
n_e=17260
n_c=17293
n_e_count=3423
n_c_count=3785
NC_pool=(n_c_count+n_c_count)/(n_e+n_c)
SE=sqrt(NC_pool*(1-NC_pool)*(1/n_e+1/n_c))
M=SE*1.96
CI is (NC_pool-M, NC_pool+M) which is (-0.0116,0.0019)

```
Since the confidence interval includes 0, the result is statistically insignificant and practically insignificant.


####Sign Tests

- Gross Conversion

	23 experiments, 19 are success. the p value for two-tail test is 0.0026

- Net Conversion

	23 experiments, 10 are success. the p value for two-tail test is 0.6776 

####Summary

I did not use Bonferroni correction since there are only two metrics, the risk of typeII error is relatively small. Therefore, we will only launch the change if all the metric are significantly changed. 

Based on the results, the gross conversion rate's decrease is statistically and practically significant. However, the null hypothesis of net conversion is not rejected since it is unclear whether it will increase or decrease based on our results.

###Recommendation

I recommend not launch the change. 

Based on the results, the gross conversion's reduction is statistically and practicaly significant (which is what we expected) while the net conversion rate's positive change is statistically insignificant. Since only one metric meets the requirement, the overall experiment is not successful, therefore launching the test is not worthwhile.

##Follow-Up Experiment: How to Reduce Early Cancellations

Experiement: when use choose to cancel the subscription, pop up a window of reminder showing the lessons that the user has completed and the upcoming session in the course, and ask them again whether to cancel or continue. 

We expect this will encourage more student to continue subscribing.

Hypothesis is that the reminder window at the cancel page will encourage more students to continue the subscription, which increases the retention rate and decreases the cancellation rate. 

The metrics are the retention rate -total number of payments over the total number of enrollments, and cancellation rate- the total cancellation over the enrollment. 

The unit of diversion is userID. Since the payment and cancellation information are specific to particular users.

The invariants could inlcude pageviews, click-through-probability (start free trial clicks over the pageviews) and the enrollment rates, since the pop up window will only pop up when the subscribed users want to cancel, these rate should not change that much.

