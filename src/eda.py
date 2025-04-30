import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Discribe the structure of the dataset:
def summarize(df):
    print(df.info())
    print(df.describe())
    
def missing_check(df):
    missing = df.isnull().sum()
    return missing

# Visualize and summarize key variables:
    
def plot_distributions(df, num＿cols):
    for col in num_cols:
        plt.figure()
        sns.histplot(df[col], kde=True)
        plt.title(f'Distribution of {col}')
        plt.close()
        
def plot_correlations(df):
    corr = df.corr(numeric_only=True)
    plt.figure(figsize=(10,8))
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.tight_layout()
    plt.close()
    
def plot_boxplots(df, num_cols):
    for col in num_cols:
        plt.figure()
        sns.boxplot()(x=df[col])
        plt.title(f'Boxplot of {col}')
        plt.tight_layout()
        plt.show()

    
# Outliers, skew, or transformations:

def skew_check(df, num_cols):
    skew_d = df[num_cols].skew()
    return skew_d






