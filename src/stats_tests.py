import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt
import os

def ttest(df, group1, group2):
    t_stat, p_val = stats.ttest_ind(group1, group2, equal_var=False)
    return print(f"T-test:\nT-statistic: {t_stat:.2f}\nP-value: {p_val}")

def anova(df, group: str):
    groups = [df[df[group] == level]["nightly_rate_log"].values for level in df[group].unique()]
    f_stat, p_val = stats.f_oneway(*groups)
    
    return print(f"ANOVA: {group}\nF-statistic: {f_stat:.2f}\nP-value: {p_val}")

def plot_group_distributions(df, target, column):
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=column, y=target, data=df)
    plt.title(f'Nightly Rate by {column}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()