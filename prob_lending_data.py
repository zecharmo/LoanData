import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

# access lending data

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# remove rows with null values

loansData.dropna(inplace=True)

# generate and save a boxplot of the data

loansData.boxplot(column='Amount.Requested')
plt.savefig("loans_boxplot.png")
plt.show()

# generate and save a histogram of the data

loansData.hist(column='Amount.Requested')
plt.savefig("loans_histogram.png")
plt.show()

# generate and save a QQ-plot of the data

plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.savefig("loans_qqplot.png")
plt.show()