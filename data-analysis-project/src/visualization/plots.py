import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(data, column):
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], kde=True)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid()
    plt.show()

def plot_correlation_matrix(data):
    plt.figure(figsize=(12, 8))
    correlation = data.corr()
    sns.heatmap(correlation, annot=True, fmt=".2f", cmap='coolwarm', square=True)
    plt.title('Correlation Matrix')
    plt.show()

def plot_boxplot(data, x_column, y_column):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=data[x_column], y=data[y_column])
    plt.title(f'Boxplot of {y_column} by {x_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.grid()
    plt.show()