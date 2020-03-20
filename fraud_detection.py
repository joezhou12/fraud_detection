#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 17:31:02 2020

@author: Yichun Zhou

PROG for BI HWK5
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import random
import math
import codecs
############
###    Part1
############

#############################    Problem 1   #################################
# The function takes a filename and a list of names of columns and return a 
# list of numbers
# in the PDF file, it suggests to use csv.DictReader, however I failed to use 
# it, instead I used pandas read_csv, used a thousands=r',' parameter to clean
# the file and returned a correct list 
def extract_election_vote_counts(filename, column_names):
    #initiate a new list to store value 
    vote_count = []
    # read the csv file into correct format
    df = pd.read_csv(filename, thousands=r',',usecols = column_names)
    #For loop using index to iterate the csv file
    for i in range(len(df)):
        #another for loop to iterate through the columns needed
        for j in column_names:
            #store the vote counts to the list initiated earlier
            vote_count.append(df.at[i,j])
    #return the list
    return vote_count

#Test with election-iran-2009.csv file, uncomment the line below
# extract_election_vote_counts("election-iran-2009.csv", ["Ahmadinejad", "Rezai", "Karrubi", "Mousavi"])
#output should be: [1131111, 16920, 7246, 837858, 623946, 12199, 21609, 656508, ...

'''Report
I use pandas to read the csv file, set to the right format use thousands=r','
and set usecols with the column wanted, I spent a some time doing research, 
finally find out the way using thousands=r',' to delete the comma in numbers
'''

#############################    Problem 2   #################################
# The function takes a list numbers and return the percentage of the frequency
# of ones and tens digit as a histogram
def ones_and_tens_digit_histogram(numbers):
    # initiate a histogram list to store return result
    histogram = []
    # initiate a list to store the ones and tens digit
    two_digit = []
    # initiate a dictionary, key is 0-9 digit, value is the frequency
    percentage = {}
    # For loop iterate in the number list 
    for num in numbers:
        # get the tens digit by divide by 10 then mode by 10
        tens_digit = int((num/10)%10)
        # store each tens digit into the list
        two_digit.append(tens_digit)
        # get the ones digit by mode by 10
        ones_digit = num % 10
        # store each ones digit into the list
        two_digit.append(ones_digit)
    # for loop iterate in the list of ones and tens digit
    for i in two_digit:
        # use a count function to count the number of occurence of each number
        occurance_count = two_digit.count(i)
        # store the histogram percentage of each number into the dictionary
        percentage[i] = occurance_count/len(two_digit)        
    # for loop iterate in in digit 0 to 9        
    for j in range(0,10):
        #if the any digit from 0-9 is not in the key, means no existance
        if j not in percentage:
            #set the value of the key to 0
            percentage[j] = 0
        # get the value in the dictionary
        histogram.append(percentage[j])
    # return the histogram list
    return histogram
#assertion test for the function above, provided by HKW5 PDF
assert ones_and_tens_digit_histogram([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,144, 
  233, 377, 610, 987, 1597, 2584, 4181, 6765]) == [0.21428571428571427, 0.14285714285714285, 0.047619047619047616,0.11904761904761904, 
  0.09523809523809523, 0.09523809523809523,0.023809523809523808, 0.09523809523809523, 0.11904761904761904,0.047619047619047616]

'''Report:
I used 3 for loop to complete this function
first for loop get the tens and ones digit of each number in the list and 
store into a list, second for loop count the frequency of each number and
store into a dictionary, thrid for loop is used to return the histogram as 
a list
'''
                                                                                                  
#############################    Problem 3   #################################
# function take a list of histogram percentage number to plot the elction data
# used matplotlib package and used the pyplot as plt
def plot_iranian_least_digits_histogram(histogram):
    #plot the ideal line which is a staight line = 0.1, with blue color
    plt.plot([0.1 for _ in range(10)], label='Ideal',color='blue')
    # plot the Iran election data give the line green color
    plt.plot(histogram, label='Iran',color='green')
    # locate the legend of each line at upper right
    plt.legend(loc='upper right')
    #make x-axis from 0 - 9 
    plt.xlim(0, 9)
    #make y - axis from 0.06 to 0.16
    plt.ylim(0.06, 0.16)
    # get the y-axis lable as Frequency
    plt.ylabel('Frequency')
    # get the x-axis lable as Digit
    plt.xlabel('Digit')
    #save the plot figure name iran-digits.png
    plt.savefig('iran-digits.png')
    #show the plot after save the figure
    plt.show()
    #return nothing, will show the plot if call the function
    return None

'''Report:
This problem wants us to plot a line graph of Ideal histogram and Iran histram
I spent some time learning how to make the plot look nice and how to show the 
axis lable and legend
'''

#############################    Problem 4   #################################
# the main purpose of this function is to plot the distribution of 
# 10, 50, 100, 1000, 10000 sample sizes
# used a similar plot technique from question 3
def plot_distribution_by_sample_size():
    # set the plot figure size
    plt.figure(figsize=(15,10))
    # iterate in list [10, 50, 100, 1000, 10000], these are the number of 
    # sample sizes 
    for i in [10, 50, 100, 1000, 10000]:
        # get a list of random numbers from 0 - 99
        random_list = [random.randint(0,99) for _ in range(i)]
        # call the ones_and_tens_digit_histogram function to get histogram
        his = ones_and_tens_digit_histogram(random_list)
        #line legend name
        plot_lable = str(i) + ' random numbers'
        #plot the line of the specific histogram
        plt.plot(his, label=plot_lable)  

    #plot the ideal line which is a staight line = 0.1, with blue color

    plt.plot([0.1 for _ in range(10)], label='Ideal',color='blue') 
    # locate the legend of each line at upper right
    plt.legend(loc='upper right')
    # get the y-axis lable as Frequency
    plt.ylabel('Frequency')
    # get the x-axis lable as Digit
    plt.xlabel('Digit')
    plt.xlim(0, 9)

    #save the plot figure name random-digits.png
    plt.savefig('random-digits.png')
    #show the plot after save the figure
    plt.show()
    #return nothing, will show the plot if call the function
    return None

'''Report:
I did some research for this problem, find the ramdom,randint function which
can help me generate random numers, also it is very interesting to find the 
line is closer to the ideal histogram when the number of counts get larger
'''
#############################    Problem 5   #################################
# given two lists of numbers, same length, the function would computes the mean 
# squared error between the lists
def mean_squared_error(numbers1, numbers2):
    # initiate a int value to future store use 
    error_sum = 0
    # iterate as index in the range length of first number list
    for i in range(len(numbers1)):
        #caculation of mean_squared_error
        #use number from two list, in the same index to subtract, then square 
        # the difference
        error_sum += (numbers1[i] - numbers2[i]) ** 2
    #return the square error
    return error_sum
#assertion test for the function above, provided by HKW5 PDF
assert mean_squared_error([1, 4, 9], [6, 5, 4]) == 51

'''Report:
To caculate the mean square error, the hard part is to for loop use index, I 
forget how to set i as index, finally found out using google
'''
#############################    Problem 6   #################################
#takes a histogram and returns the mean squared error of the given histogram 
#with the uniform distribution.
def calculate_mse_with_uniform(histogram):
    #initiate a new list to store unifrom list data
    uniform = []
    #for loop iterate from 0-9 cause we need 10 numbers
    for i in range(10):
        #set each index in the list to 0.1
        uniform.append(0.1)
    #use mean_squared_error function to get the mse between the input histogram
    # list and the unifrom list
    return mean_squared_error(histogram, uniform)
#call the calculate_mse_with_uniform function to get the iran_histogram mse
# calculate_mse_with_uniform(iran_histogram)
#output: 0.007395833333333335

#takes the Iranian MSE and compares it to the MSE to the uniform distribution 
#for 10000 groups of random numbers
def compare_iranian_mse_to_samples(mse):
    iran_histogram = ones_and_tens_digit_histogram(extract_election_vote_counts("election-iran-2009.csv", ["Ahmadinejad","Rezai", "Karrubi", "Mousavi"]))
    # initiate two counter int variable
    # this one store the number of mse larger than iran mse
    larger_equal_Iran_count = 0
    # this one store the number of mse smaller than iran mse
    smaller_Iran_count = 0
    #for loop iterate through 10000 numbers, generate 10000 mse
    for i in range(10000):
        # use ones_and_tens_digit_histogram function to get histogram
        # use calculate_mse_with_uniform to get mse 
        #  use the last two digits of the random numbers
        # where each group is the same size as the Iranian election data (120 numbers)
        test_mse = calculate_mse_with_uniform(ones_and_tens_digit_histogram(
                [random.randint(0,99) for _ in range(120)]))
        # if test mse larger than iran mse, the counter for larger add one
        if test_mse >= calculate_mse_with_uniform(iran_histogram):
            # larger_equal_Iran_count add one if condition satisfied
            larger_equal_Iran_count += 1
        # if test mse smaller than iran mse, smaller counter add one
        elif test_mse < calculate_mse_with_uniform(iran_histogram):
            # smaller_Iran_count add one if condition satisfied
            smaller_Iran_count += 1
    # print out number of tse mse larger and than iran mse
    print("Quantity of MSEs larger than or equal to the 2009 Iranian election MSE: ",larger_equal_Iran_count)
    # print out number of tse mse smaller and than iran mse
    print("Quantity of MSEs smaller than the 2009 Iranian election MSE: ",smaller_Iran_count)
    # caculate and print null hypothesis level useing larger_equal_Iran_count/10000
    print("2009 Iranian election null hypothesis rejection level p: ",larger_equal_Iran_count/10000)
    # Return nothing, print out the result
    return None

# Output:
# Quantity of MSEs larger than or equal to the 2009 Iranian election MSE:  364
# Quantity of MSEs smaller than the 2009 Iranian election MSE:  9636
# 2009 Iranian election null hypothesis rejection level p:  0.0364

'''Report:
I found this problem very interesting that how you compare the number of mse 
generated by random number compare with the iran data, it found the p-value is 
very small, which the iran data is very likely not genuine
'''
#############################    Problem 7   #################################
# Please view Answer.txt or below 
# The value 0.007 is larger than 9636 of the random MSEs, and is
# smaller than 364 of the random MSEs. If the election results were genuine, then
# there would only be a 3.64% chance of such a lopsided choice. This
# is unlikely, and we could say that we are 96.36% confident that the data are
# fraudulent (we reject the null hypothesis at the p=.0364 level).

'''Report:
I learnt how to write the analysis from the PDF file provided for the HWK
assignment, it is very informative, show the percentage of it is being a 
lopsided choice and show the p-value, finally determine whether it is 
fraudulent or not.
'''
#############################    Problem 8   #################################
# The function takes a filename and a list of names of columns and return a 
# list of numbers，thousands=r',' and encoding='latin-1' are two important 
# parameters that require for reading the data
def us_extract_election_vote_counts(filename, column_names):
    #initiate a new list to store value 
    vote_count = []
    #use pandas to read the csv file, set to the right format use thousands=r','
    #and for reading US data encoding='latin-1'is needed set usecols with the 
    # column wanted
    df = pd.read_csv(filename, thousands=r',',usecols = column_names, encoding='latin-1')
    #For loop using index to iterate the csv file
    for i in range(len(df)):
        #another for loop to iterate through the columns needed
        for j in column_names:
            #store the vote counts to the list initiated earlier
            vote_count.append(df.at[i,j])
    # When a datum is missing ignore that datum
    cleanedList = [x for x in vote_count if str(x) != 'nan']   
    #return the list
    return cleanedList

#takes the US MSE and compares it to the MSE to the uniform distribution 
#for 10000 groups of random numbers
def compare_us_mse_to_samples(mse):
    # set us_2008_candidates list with the name of all candidates
    us_2008_candidates = ["Obama", "McCain", "Nader", "Barr", "Baldwin", "McKinney"]
    # 
    us_histogram = ones_and_tens_digit_histogram((us_extract_election_vote_counts("election-us-2008.csv", us_2008_candidates)))

    #get the length the list of US extract election vote counts
    us_random_range = len(us_extract_election_vote_counts("election-us-2008.csv", us_2008_candidates))
    # initiate two counter int variable
    # this one store the number of mse larger than US mse
    larger_equal_US_count = 0
    # this one store the number of mse smaller than US mse
    smaller_US_count = 0
    #for loop iterate through 10000 numbers, generate 10000 mse
    for i in range(10000):
        #to get the mse for random generated numbers
        test_mse = calculate_mse_with_uniform(ones_and_tens_digit_histogram(
                [random.randint(0,99) for _ in range(us_random_range)]))
        # if test mse larger than iran mse, the counter for larger add one
        if test_mse >= calculate_mse_with_uniform(us_histogram):
            # larger_equal_Iran_count add one if condition satisfied
            larger_equal_US_count += 1
        # if test mse smaller than iran mse, smaller counter add one
        elif test_mse < calculate_mse_with_uniform(us_histogram):
            # smaller_Iran_count add one if condition satisfied
            smaller_US_count += 1
    # print out number of tse mse larger and than US mse
    print("Quantity of MSEs larger than or equal to the 2008 US election MSE: ",larger_equal_US_count)
    # print out number of tse mse smaller and than US mse
    print("Quantity of MSEs smaller than the 2008 US election MSE: ",smaller_US_count)
    # caculate and print null hypothesis level useing larger_equal_US_count/10000
    print("2008 US election null hypothesis rejection level p: ",larger_equal_US_count/10000)
    # Return nothing, print out the result
    return None

# Answer to Problem 8:
# null hypothesis:  observed sample (the US election data) is not fraudulent
# compare_us_mse_to_samples(0.001410025876058068)
# Quantity of MSEs larger than or equal to the 2008 US election MSE:  4776
# Quantity of MSEs smaller than the 2008 US election MSE:  5224
# 2008 US election null hypothesis rejection level p:  0.4776

# The value 0.0014 is larger than 5224 of the random MSEs, and is
# smaller than 4776 of the random MSEs. If the election results were genuine, then
# there would be a 47.76% chance of such a lopsided choice. It is not suprising
# at all; it provides no evidence regarding the null hypothesis.
    
'''Report:
This problem is very tricky, especially when I trying to get the mse for 
randomly generated numbers, I firstly used ones_and_tens_digit_histogram 
function to get histogram, then used calculate_mse_with_uniform to get mse, 
and used the last two digits of the random numbers, where each group is the 
same size as the US election data
'''
############
###    Part2
############

#############################    Problem 9,10，11  ###########################
# Problem 9 helper function
# This function return the benfold law result, uses a for loop and log10 
# function to get the benford numbers
def benfold_dist_list():
    # initiate a new list to store benfold law 
    benfold_list = []
    # for loop iterate through 1 to 9
    for i in range(1,10):
        # use math log function to caculate for benfold law numbers
        benfold_list.append(math.log10(1+1/i))
    # return the benfold_list
    return benfold_list

# Problem 10 helper function
# This function requires a number and return a list of numbers, uses a for loop 
# and math pow, e and random function to generate random numbers caculation
def benfold_artificial_data_list(range_number):
    # initiate a new list to store numbers
    a_list = []
    # for loop iterate through 0 to range number
    for i in range(range_number):
        # use math pow, e and random function to caculate for random numbers
        a = math.pow(math.e,random.uniform(0, 30))
        # store number to list
        a_list.append(a)
    # return the list
    return a_list
# benfold_artificial_data_list(1000)

# Problem 11 helper function
# This function return a list of numbers, uses a for loop and math pow, e, pi and 
# random function to generate random numbers caculation
def benfold_e_data_list():
    # initiate a new list to store numbers
    e_list = []
    # for loop iterate through 0 to 1000
    for i in range(1000):
        # use math pow, e and random function to caculate for random numbers
        # multiply with pi
        e = math.pi * math.pow(math.e,random.uniform(0, 30))
        # store number to list
        e_list.append(e)
    # return the list   
    return e_list
# benfold_e_data_list()

# Helper function to get the histogram of most significant number
def most_sig_digits_histogram(numlist):
    # initiate a new list to store numbers
    most_sig_digits_list = []
    # initiate a new dictionary to store digit as key, histogram as value
    percentage = {}
    # initiate a new list to store numbers
    histogram = []
    # for loop iterate through the first number in numlist to the last 
    for i in numlist:
        # get the most significant digit of each number 
        digit = i/int(math.pow(10, len(str(int(i)))-1))
        # store the most significant digit into a list
        most_sig_digits_list.append(int(digit)) 
    # # for loop iterate through the first digit in most_sig_digits_list to 
    # the last
    for j in most_sig_digits_list:
        # use a count function to count the number of occurence of each digit
        occurance_count = most_sig_digits_list.count(j)
        # store the histogram percentage of each digit into the dictionary
        percentage[j] = occurance_count/len(most_sig_digits_list)        
    # for loop iterate in in digit 1 to 9  
    for n in range(1,10):
        #if the any digit from 0-9 is not in the key, means no existance
        if n not in percentage:
            #set the value of the key to 0
            percentage[n] = 0
        # get the value in the dictionary, and store to list
        histogram.append(percentage[n])
    # return the histogram list    
    return histogram
#assertion test for the function above
assert most_sig_digits_histogram([1,20,300,4000]) == [0.25, 0.25, 0.25, 0.25, 0, 0, 0, 0, 0]

# function plot the benfold data
# used matplotlib package and used the pyplot as plt
# 3 line is ploted in the function, Benfold ideal line, 1000 random line caculated
# by benfold_artificial_data_list function and benfold_e_data_list function
def plot_scale_invariance():
    #the list of x values
    d = [1,2,3,4,5,6,7,8,9]
    #plot the ideal line of benfold, use the benfold_dist_list function
    plt.plot(d,benfold_dist_list(), label='Benfold')
    # plot the line of the result of most_sig_digits_histogram and
    # benfold_artificial_data_list function with 1000 as number range
    plt.plot(d,most_sig_digits_histogram(benfold_artificial_data_list(1000)), label='1000 samples')
    # plot the line of the result of most_sig_digits_histogram and
    # benfold_e_data_list function
    plt.plot(d,most_sig_digits_histogram(benfold_e_data_list()), label='1000 samples, scaledby $\pi$')
    
    # locate the legend of each line at upper right
    plt.legend(loc='upper right')
    #make x-axis from 1 - 9 
    plt.xlim(1, 9)
    #make y - axis from 0.060 to 0.35
    plt.ylim(0.00, 0.35)
    # get the y-axis lable as Frequency    
    plt.ylabel('Frequency')
    # get the x-axis lable as Digit
    plt.xlabel('First Digit')
    #save the plot figure name scale-invariance.png
    plt.savefig('scale-invariance.png')
    #show the plot after save the figure
    plt.show()
    #return nothing, will show the plot if call the function
    return None

'''Report:
I created 3 helper function, one for each problems 9, 10, 11.
I found the most_sig_digits_histogram is most interesting function to code,
The function takes a list numbers and return the percentage of the frequency
of most significant digit as a histogram. Also, I used 3 for loop to complete 
this function, first for loop get the most significant digit of each number 
in the list and store into a list, second for loop count the frequency of each 
number and store into a dictionary, thrid for loop is used to return the 
histogram as a list 
'''

#############################     Problem 12, 13    ##########################
# Problem 12 helper function
# This function take a list of data, uses a for loop and two conditions to
# get the number we need, store and return the number list
def clean_list_p12(data):
    # initiate a new list to store numbers
    new_list = []
    # for loop iterate through the first item in data to the last     
    for i in data:
        # make sure the item value is not X
        if i != "X":
            # make sure the item value is not 0
            if int(i) != 0:
                #store the number into the list 
               new_list.append(int(i)) 
    #return the list of numbers
    return new_list

# Problem 13 helper function
# This function read the literature population file, uses a for loop to
# get the number we need, store and return the number list
def clean_list_literature():
    # read the literature population file
    lit_pop = open('literature-population.txt')
    # initiate a new list to store numbers
    l_line = []
    # for loop iterate through the first item in lit_pop to the last 
    for line_of_text in lit_pop:
        # split the line with\t and get the second value in the line
        a = line_of_text.split('\t')[1]
        # replace the comma with empty
        a = a.replace(',', '')
        # store as an integer to list
        l_line.append(int(a))
    #return the list 
    return l_line

# function plot the benfold graph for us and litratrue population
# used matplotlib package and used the pyplot as plt
# 3 line is ploted in the function, Benfold ideal line, us population benfold
# by most_sig_digits_histogram function and use clean_list_literature function
# to get the litratrue population benford
def plot_us_and_litrature_pop():
    
    # get the raw_us_pop_data using the extract_election_vote_counts function
    raw_us_pop_data = extract_election_vote_counts('SUB-EST2009_ALL.csv', ["POPCENSUS_2000"])
    # get the cleaned us data using clean_list_p12 function
    us_pop_data = clean_list_p12(raw_us_pop_data)
    
    #the list of x values
    d = [1,2,3,4,5,6,7,8,9]
    #plot the ideal line of benfold, use the benfold_dist_list function
    plt.plot(d,benfold_dist_list(), label='Benfold')
    # plot the line of the result of most_sig_digits_histogram of us population
    plt.plot(d,most_sig_digits_histogram(us_pop_data),label='US (all)')
    # plot the line of the result of most_sig_digits_histogram of litrature population
    plt.plot(d,most_sig_digits_histogram(clean_list_literature()),label='Literature Places')
    # locate the legend of each line at upper right
    plt.legend(loc='upper right')
    #make x-axis from 1 - 9 
    plt.xlim(1, 9)
    #make y - axis from 0.00 to 0.35
    plt.ylim(0.00, 0.35)
    # get the y-axis lable as Frequency 
    plt.ylabel('Frequency')
    # get the x-axis lable as First Digit
    plt.xlabel('First Digit')
    #save the plot figure name population-data.png
    plt.savefig('population-data.png')
    #show the plot after save the figure
    plt.show()
    #return nothing, will show the plot if call the function
    return None

'''Report:
I used some functions in part 1, and the other codes in part also helped me to
solve this probelm.
The most trouble I got from this question is how to set the x-axis from 1 to 9,
I used so many ways, however all of them did not work out, finally I found a 
Youtube video wich shows me how to plot it, Thanks Youtube.
'''
#############################     Problem 14    ##############################
# the main purpose of this function is to plot the distribution of 
# 10, 50, 100, 10000 number range for benfold_artificial_data_list function
def plot_more_benford():
    #the list of x values
    d = [1,2,3,4,5,6,7,8,9]
    #plot the ideal line of benfold, use the benfold_dist_list function    
    plt.plot(d,benfold_dist_list(), label='Benfold',linestyle='dashed')
    # plot the line of the result of most_sig_digits_histogram and
    # benfold_artificial_data_list function with 10 as number range
    plt.plot(d,most_sig_digits_histogram(benfold_artificial_data_list(10)), label='10 samples')
    # plot the line of the result of most_sig_digits_histogram and
    # benfold_artificial_data_list function with 50 as number range
    plt.plot(d,most_sig_digits_histogram(benfold_artificial_data_list(50)), label='50 samples')
    # plot the line of the result of most_sig_digits_histogram and
    # benfold_artificial_data_list function with 100 as number range
    plt.plot(d,most_sig_digits_histogram(benfold_artificial_data_list(100)), label='100 samples')
    # plot the line of the result of most_sig_digits_histogram and
    # benfold_artificial_data_list function with 1000 as number range
    plt.plot(d,most_sig_digits_histogram(benfold_artificial_data_list(10000)), label='10000 samples')

    # locate the legend of each line at upper right
    plt.legend(loc='upper right')
    #make x-axis from 1 - 9    
    plt.xlim(1, 9)
    #make y - axis from 0.00 to 0.35
    plt.ylim(0.00, 0.35)
    # get the y-axis lable as Frequency 
    plt.ylabel('Frequency')
    # get the x-axis lable as First Digit
    plt.xlabel('First Digit')
    #save the plot figure name benford-samples.png
    plt.savefig('benford-samples.png')
    #show the plot after save the figure
    plt.show()
    #return nothing, will show the plot if call the function
    return None

'''Report:
The helper function from question 10 did a great work for this problem, I 
called the function several time with different passing variable to plot the 
lines, very interesting result just like problem 4, the larger the number of 
random numbers, the closer to the ideal line
'''
        
#############################     Problem 15    ##############################
#takes the 10000 groups of random numbers US poluation and benford MSE and 
# compares it to the MSE of literature population and benford 
def compare_us_mse_to_literature_mse():
    # get the MSE of literature population and benford by calling most_sig_digits_histogram
    # benfold_dist_list and mean_squared_error function
    ben_lit_mse = mean_squared_error(benfold_dist_list(),most_sig_digits_histogram(clean_list_literature()))
    # output: 0.006089412520813688
    
    # get the raw_us_pop_data using the extract_election_vote_counts function
    raw_us_pop_data = extract_election_vote_counts('SUB-EST2009_ALL.csv', ["POPCENSUS_2000"])
    # get the cleaned us data using clean_list_p12 function
    us_pop_data = clean_list_p12(raw_us_pop_data)
    
    #get the length the list of clean_list_literature
    lit_range = len(clean_list_literature())
    # initiate two counter int variable
    # this one store the number of mse larger than US mse
    larger_equal_US_count = 0
    # this one store the number of mse smaller than US mse
    smaller_US_count = 0
    #for loop iterate through 10000 numbers, generate 10000 mse
    for i in range(10000):
        # randomly selected numbers in the us_pop_data, select size equals
        # the length of the list of clean_list_literature
        us_random_sample = random.sample(us_pop_data, lit_range)
        # use ones_and_tens_digit_histogram function to get histogram
        # use mean_squared_error to get mse 
        # use the lmost significant digit of the random numbers
        us_random_mse = mean_squared_error(most_sig_digits_histogram(us_random_sample),benfold_dist_list())
        # if test mse larger than us population mse, the counter for larger 
        # add one
        if us_random_mse >= ben_lit_mse:
            # larger_equal_US_count add one if condition satisfied
            larger_equal_US_count += 1
        # if test mse smaller than us population mse, smaller counter add one
        elif us_random_mse < ben_lit_mse:
            # smaller_US_count add one if condition satisfied
            smaller_US_count += 1
    # print lines
    print("Comparison of US MSEs to literature MSE: ")
    # print out number of US mse larger or equal and than literature mse
    print("larger/equal: ",larger_equal_US_count)
    # print out number of US mse smaller and than literature mse
    print("smaller: ",smaller_US_count)
    # Return nothing, print out the result
    return None
# Comparison of US MSEs to literature MSE: 
# larger/equal:  8947
# smaller:  1053

'''Report:
Very confusing but interesting problem, used so many functions defined 
previously, such as most_sig_digits_histogram, mean_squared_error, one small
detial is you have to use the length of the cleaned dataset to help generate 
the randon number, hard code the range is not smart way to do it
'''
#############################     Problem 16    ##############################
# Answer to Problem 16:
# null hypothesis:  observed sample (the US Cities Population data) is not 
# fraudulent

# The Literature MSE is around 0.006089412520813688
# 8947 of random US MSEs is larger or equal to the Literature MSE, and 1053 is 
# smaller than the Literature MSE. If the Population data were genuine, then
# there would be a 10.53% chance of such a lopsided choice. This is somewhat 
# unlikely, but not so very surprising. It does not provide any statistically 
# significant evidence against the null hypothesis.

'''Report:
I did some study on hypothesis testing which I was not very good at, I learnt 
adbout what is alpha, what is p-vlaue, finally I can write the analysis,
after this question, I actually went back and did some modification for 
problem 7 and 8.
'''
#####################################
# The code in this function is executed when this file is run as a Python
# program
def main():
    # use the ones_and_tens_digit_histogram function defined earlier to get the 
    # histogram list of iran last two digit election digitsdata
    iran_histogram = ones_and_tens_digit_histogram(extract_election_vote_counts("election-iran-2009.csv", ["Ahmadinejad",
    "Rezai", "Karrubi", "Mousavi"]))
    # plot the iran histogram graph use the plot_iranian_least_digits_histogram function
    plot_iranian_least_digits_histogram(iran_histogram)
    #run the plot_distribution_by_sample_size function to get the plot
    plot_distribution_by_sample_size()
    # call the compare_iranian_mse_to_samples to get printout results
    compare_iranian_mse_to_samples(0.00739583333333)
    # list to store 2008 us candidate
    us_2008_candidates = ["Obama", "McCain", "Nader", "Barr", "Baldwin", "McKinney"]
    # use us_extract_election_vote_counts and ones_and_tens_digit_histogram function
    # to get us histogram
    us_histogram = ones_and_tens_digit_histogram((us_extract_election_vote_counts("election-us-2008.csv", us_2008_candidates)))
    # call the calculate_mse_with_uniform to get the mse between us histogram and 
    # uniform list
    calculate_mse_with_uniform(us_histogram)
    # call the compare_us_mse_to_samples to get printout results
    compare_us_mse_to_samples(0.001410025876058068)
    
    # plot the Benfold graph use the plot_scale_invariance function
    plot_scale_invariance()
    # plot the US population and litrature population Benfold graph use the 
    # plot_us_and_litrature_pop function
    plot_us_and_litrature_pop()
    # plot the 10, 50, 100, 10000 number range Benfold graph use the
    # plot_more_benford function
    plot_more_benford()
    # call the compare_us_mse_to_literature_mse to get printout results
    compare_us_mse_to_literature_mse()
if __name__ == "__main__":
 main()
 
 
 