import streamlit as st
from text import *

import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def print_badge_associations(column_name):
    """
    Print the names of badges associated with the given column name.

    Parameters:
        column_name (str): The column name for which to print badge associations.
    """
    badge_associations = {
        "EVENTS_CREATED": "📆 Event Planner",
        "EVENT_PARTICIPANTS": "📆 Event Planner",
        "POSTS_CREATED": "🗣️ Conversation Starter",
        "REPLIES_RECEIVED": "🗣️ Conversation Starter",
        "ITEMS_GIFTED": "🎁 Philanthropist",
        "THANKYOUS_RECEIVED": "🫱🏻 Helping Hand",
        "PLACES_RECOMMENDED": "🧳 Local Guide"
    }

    if column_name in badge_associations:
        print(f"{badge_associations[column_name].upper()}")
    else:
        print(f"No badge association found for '{column_name}'.")

def visualize_columns(df, column_names):
    """
    Visualize specified columns from the DataFrame using seaborn countplot.

    Parameters:
        df (DataFrame): The DataFrame containing the data.
        column_names (list): A list of column names to visualize.
    """

    for column_name in column_names:
        # Print associated badge name
        # print_badge_associations(column_name)

        plt.figure(figsize=(8, 6))
        ax = sns.countplot(x=df[column_name])
        #plt.title(f"Countplot of {column_name}")

        # Set integer x-axis tick labels
        plt.xticks(rotation=45)  # Rotate labels for better visibility
        plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: int(x)))

        # Add count labels to the bars
        for p in plt.gca().patches:
            plt.gca().annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom', fontsize=10, color='black', xytext=(0, 5), textcoords='offset points')

        sns.despine(bottom=True, right=True, left=True)
        #ax.set(yticklabels=[])

        plt.tick_params(axis='both', which='both', bottom=False, left=False)
        plt.xlim(1, 25)
        plt.ylim(0, df[column_name].value_counts()[1.0])
        # plt.ylim(0, 169)
        plt.show()

        ax.set_ylabel(None)

def page_home():
    st.title("Nebenan Challenge")
    st.markdown("## My recommendations for each badge's criteria:")
    st.write(predictions)

if __name__ == "__main__":
    page_home()
