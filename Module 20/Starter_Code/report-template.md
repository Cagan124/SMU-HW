# Module 20 Report Template

## Overview of the Analysis

In this section, describe the analysis you completed for the machine learning models used in this Challenge. This might include:

* Explain the purpose of the analysis.

The purpose of the analysis is to test models to determine whether borrowers should or should not receive loans

* Explain what financial information the data was on, and what you needed to predict.

The lending data was information regarding borrower's loan status and we need to predict if they are eligible for the loan they are applying for.

* Provide basic information about the variables you were trying to predict (e.g., `value_counts`).

Value counts is a great example of what we were trying to predict, which was how many people will/will not default on their loan

* Describe the stages of the machine learning process you went through as part of this analysis.

After reading in the data and adding the imports, I reviewed the loan status column and assigned variables. After this, I checked the balance of the data to seee what our models should be aiming for.I then split the data into training sets and adding a function from a previous activity. I then created a logistic regression and made predictions. Once this was completed, I evaluated the model's performance.

* Briefly touch on any methods you used (e.g., `LogisticRegression`, or any resampling method).

I used a logistic regression to show our results as a ROC curve and created a confusion matrix to show our False Positives/False Negatives

## Results

Using bulleted lists, describe the balanced accuracy scores and the precision and recall scores of all machine learning models.

* Machine Learning Model 1:
  * Description of Model 1 Accuracy, Precision, and Recall scores.

*Precision was 85%
*Recall was 91% 
* Overall, we would prefer this to be a little bit more accurate, but it is not a terrible model


* Machine Learning Model 2:
  * Description of Model 2 Accuracy, Precision, and Recall scores.
  
*Precision was 85% 
*Recall was 89%
*Overall, this was slightly worse with higher false negatives. 

## Summary

Summarize the results of the machine learning models, and include a recommendation on the model to use, if any. For example:
* Which one seems to perform best? How do you know it performs best?
* Does performance depend on the problem we are trying to solve? (For example, is it more important to predict the `1`'s, or predict the `0`'s? )

Out of the 2 models tested, I would recommend the linear regression model. This model performed slightly better than the random forest model, however, neither model was perfect. For this specific activity, I do not think that performance depended on the problem we were trying to solve. With that being said, it would be more important to predict 0's accurately as those are going to be approved loans. We would rather have more false positives than false negatives. 

If you do not recommend any of the models, please justify your reasoning.
