#
#
# Regression and Classification programming exercises
#
#


#
#   In this exercise we will be taking a small data set and computing a linear function
#   that fits it, by hand.
#   

#   the data set

import numpy as np

sleep = [5,6,7,8,10]
scores = [65,51,75,75,86]


def compute_regression(sleep,scores):

    #   First, compute the average amount of each list

    avg_sleep = np.average(sleep)
    avg_scores = np.average(scores)


    #   Then normalize the lists by subtracting the mean value from each entry

    normalized_sleep = [(5-avg_sleep),(6-avg_sleep),(7-avg_sleep),(8-avg_sleep),(10-avg_sleep)]
    normalized_scores = [(65-avg_scores),(51-avg_scores),(75-avg_scores),(75-avg_scores),(86-avg_scores)]


    #   Compute the slope of the line by taking the sum over each student
    #   of the product of their normalized sleep times their normalized test score.
    #   Then divide this by the sum of squares of the normalized sleep times.

    my_sum = normalized_sleep[0] * normalized_scores[0] + \
    normalized_sleep[1] * normalized_scores[1] + \
    normalized_sleep[2] * normalized_scores[2] + \
    normalized_sleep[3] * normalized_scores[3] + \
    normalized_sleep[4] * normalized_scores[4]

    my_div = normalized_sleep[0] * normalized_sleep[0] + \
        normalized_sleep[1] * normalized_sleep[1] + \
        normalized_sleep[2] * normalized_sleep[2] + \
        normalized_sleep[3] * normalized_sleep[3] + \
        normalized_sleep[4] * normalized_sleep[4]

    slope = my_sum / my_div
    

    #   Finally, We have a linear function of the form
    #   y - avg_y = slope * ( x - avg_x )
    #   Rewrite this function in the form
    #   y = m * x + b
    #   Then return the values m, b
    m = slope
    b = -slope * avg_sleep + avg_scores

    return m,b


if __name__=="__main__":
    m,b = compute_regression(sleep,scores)
    print "Your linear model is y={}*x+{}".format(m,b)