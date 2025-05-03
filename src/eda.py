import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Discribe the structure of the dataset:
def summarize(df):
    print(df.info())
    print(df.describe())
    
def missing_check(df):
    missing = df.isnull().sum()
    return missing

# data type classification

def get_variable_types(df, target=None, cat_threshold=0):
    if target:
        df = df.drop(columns=[target])
    
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    cat_cols = df.select_dtypes(include=["object", "category", "bool"]).columns.tolist()
    
    for col in num_cols.copy():
        if df[col].nunique() <= cat_threshold:
            cat_cols.append(col)
            num_cols.remove(col)
            
    return num_cols, cat_cols


# Visualize and summarize key variables:
    
def plot_distributions(df, num_cols):
    for col in num_cols:
        plt.figure()

        unique_vals = df[col].dropna().unique()
        if np.issubdtype(df[col].dtype, np.integer) and len(unique_vals) < 10: # check if the column is integer
            # ordinal measure
            sns.countplot(x=col, data=df)
        else:
            # continuous
            sns.histplot(df[col], kde=True)

        plt.title(f'Distribution of {col}')
        plt.tight_layout()
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

def drop_outliers_iqr(df, columns, multiplier=1.5):
    """
    Drop rows containing outliers based on IQR method for specified columns.

    Parameters:
        df: The dataframe to process.
        columns: List of column names to check for outliers.
        multiplier: The IQR multiplier (default = 1.5).
    """
    df_cleaned = df.copy()
    initial_shape = df_cleaned.shape

    for col in columns:
        Q1 = df_cleaned[col].quantile(0.25)
        Q3 = df_cleaned[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - multiplier * IQR
        upper = Q3 + multiplier * IQR
        df_cleaned = df_cleaned[(df_cleaned[col] >= lower) & (df_cleaned[col] <= upper)]

    final_shape = df_cleaned.shape
    dropped = initial_shape[0] - final_shape[0]
    print(f"Dropped {dropped} rows due to outliers in {columns}.")

    return df_cleaned


def skew_check(df, num_cols):
    skew_d = df[num_cols].skew()
    return skew_d


def one_hot_encode(df, cat_cols, drop_first=True):
    """
    Perform One-Hot Encoding on categorical columns.

    Parameters:
    - df: pandas DataFrame
    - cat_cols: list of categorical column names
    - drop_first: bool, whether to drop the first level to avoid multicollinearity (default: True)

    Returns:
    - encoded_df: DataFrame with one-hot encoded columns
    """
    encoded_df = pd.get_dummies(df, columns=cat_cols, drop_first=drop_first)
    return encoded_df


# VIF

from statsmodels.stats.outliers_influence import variance_inflation_factor

def calculate_vif(df, features):
    X = df[features].dropna().copy() 
    vif_data = pd.DataFrame()
    vif_data["feature"] = X.columns
    vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    return vif_data.sort_values(by="VIF", ascending=False)




