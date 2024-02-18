import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def percentage(orders_df):
    """
    This function calculates the percentage of missing values in each column of the given DataFrame.
    It then plots these percentages in a bar chart.

    Parameters:
    orders_df (pd.DataFrame): The DataFrame to analyze.

    Returns:
    None
    """
    # Calculate the percentage of missing values in each column
    missing = orders_df.isnull().sum() * 100 / len(orders_df)

    # Create a DataFrame with the results
    percentage_missing = pd.DataFrame({
        'column': orders_df.columns,
        'missing_percentage %': missing.values
    })

    # Round the percentages to two decimal places
    percentage_missing['missing_percentage %'] = percentage_missing['missing_percentage %'].round(2)

    # Sort the DataFrame by percentage in descending order
    percentage_missing = percentage_missing.sort_values('missing_percentage %', ascending=False)

    # Reset the index and drop the old index
    percentage_missing = percentage_missing.reset_index().drop('index', axis=1)

    # Plot the missing value percentages
    plt.figure(figsize=(10, 5))
    ax = sns.barplot(x='missing_percentage %', y='column', data=percentage_missing, color='#E1341E')

    # Annotate the bars with the percentage values
    for p in ax.patches:
        ax.annotate("%.2f" % p.get_width() + '%', xy=(p.get_width(), p.get_y() + p.get_height() / 2),
                    xytext=(8, 0), textcoords='offset points', ha="left", va="center", fontsize=10)

    # Set the title and labels
    plt.title('Missing values Percentage for Each Column', fontsize=17, fontweight='bold')
    plt.ylabel('Column', fontsize=12)
    plt.xlabel('Missing percentage %', fontsize=12)

    # Set the x-axis limit
    plt.xlim(0, 50)

    # Display the plot
    plt.show()