import matplotlib.pyplot as plt
import seaborn as sns

def plot_data(df):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True)