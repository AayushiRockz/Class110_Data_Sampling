from numpy import mod
import pandas as pd 
import csv
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("data.csv")

data = df["temp"].tolist()
# population_mean = statistics.mean(data)
# std_dev = statistics.stdev(data)
# print("The population mean is {} and the standard deviation is {}".format(population_mean,std_dev))


# data_set =[]
# for i in range(0,100):
#     random_index = random.randint(0,len(data))
#     value = data[random_index]
#     data_set.append(value)

# mean = statistics.mean(data_set)
# std = statistics.stdev(data_set)
# print("The sample's mean is {} and standard deviation is {}".format(mean,std))


# fig = ff.create_distplot([data],["temp"],show_hist=False)
# fig.show()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
       random_index = random.randint(0,len(data)-1)
       value = data[random_index]
       dataset.append(value)
     
    mean = statistics.mean(dataset)
    return mean  

def show_fig(mean_list):
    df = mean_list
    mean  = statistics.mean(mean_list)
    print("mean of the sampling distribution is ",mean)
    fig = ff.create_distplot([df],["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode = "lines",name="Mean"))
    fig.show()

def main():
    mean_list =[]
    for i in range(0,1000):
        set_of_mean = random_set_of_mean(144)
        mean_list.append(set_of_mean)
    show_fig(mean_list)
   
main()

def std_Dev():
    mean_list = []
    for i in range(0,1000):
        set_of_mean = random_set_of_mean(144)
        mean_list.append(set_of_mean)
    std_Dev = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution is {}".format(std_Dev))

std_Dev()

# The population mean is 35.05393111079237 and the standard deviation is 5.699825337585306
