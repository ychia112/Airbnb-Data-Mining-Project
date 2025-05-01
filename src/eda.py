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

# data type classification

def get_variable_types(df, target=None, id_column=None, cat_threshold=0):
    if target:
        df = df.drop(columns=[target])
    if id_column:
        df = df.drop(columns=id_column)
    
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    cat_cols = df.select_dtypes(include=["object", "category", "bool"]).columns.tolist()
    
    for col in num_cols.copy():
        if df[col].nunique() <= cat_threshold:
            cat_cols.append(col)
            num_cols.remove(col)
            
    return num_cols, cat_cols


# Visualize and summarize key variables:
    
def plot_distributions(df, num＿cols):
    for col in num_cols:
        plt.figure()
        sns.histplot(df[col], kde=True)
        plt.title(f'Distribution of {col}')
        plt.show()
        
def plot_correlations(df):
    corr = df.corr(numeric_only=True)
    plt.figure(figsize=(10,8))
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.tight_layout()
    plt.show()
    
def plot_boxplots(df, cat_cols, target):
    for col in cat_cols:
        plt.figure(figsize=(8, 4))
        sns.boxplot(x=col, y= target, data= df)
        plt.title(f'Boxplot of {col}')
        plt.tight_layout()
        plt.show()

    
# Outliers, skew, or transformations:

def skew_check(df, num_cols):
    skew_d = df[num_cols].skew()
    return skew_d







