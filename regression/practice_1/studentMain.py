#!/usr/bin/python

import numpy
import matplotlib
matplotlib.use('agg')

import matplotlib.pyplot as plt
from studentRegression import studentReg
from class_vis import prettyPicture, output_image

from ages_net_worths import ageNetWorthData

ages_train, ages_test, net_worths_train, net_worths_test = ageNetWorthData()
# ages_test =  [[38,47,60,61,34,24,23,30,35,50]]
# net_worths_test = [[270.37610018,306.3198933, 373.56695844, 444.41851262, 226.965441, 131.57444916,  84.60912039, 184.61959514, 223.18690359, 207.71019584]]
# ages_train = [[36, 61, 30, 21, 47, 35, 44, 64, 24, 55]]
# net_worths_train = [[154.47839379,360.51919127,182.8740687,152.95240174,282.08225001,221.45112819,285.44221089,378.22469102,165.02792073,397.99960114]]

reg = studentReg(ages_train, net_worths_train)

plt.clf()
plt.scatter(ages_train, net_worths_train, color="b", label="train data")
plt.scatter(ages_test, net_worths_test, color="r", label="test data")
plt.plot(ages_test, reg.predict(ages_test), color="black")
plt.legend(loc=2)
plt.xlabel("ages")
plt.ylabel("net worths")


plt.savefig("test.png")
output_image("test.png", "png", open("test.png", "rb").read())
