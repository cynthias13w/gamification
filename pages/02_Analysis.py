import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

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


df = pd.read_csv('nebenan.csv')
# st.write(df)
df.fillna(0, inplace=True)

df_4weeks = df[df['LAST_X_WEEKS'] == 4].set_index('USER_ID')
df_6weeks = df[df['LAST_X_WEEKS'] == 6].set_index('USER_ID')
df_8weeks = df[df['LAST_X_WEEKS'] == 8].set_index('USER_ID')
df_12weeks = df[df['LAST_X_WEEKS'] == 12].set_index('USER_ID')

# One month ago
one_month = df_4weeks
# 6 weeks ago
one_month_and_half = df_6weeks - df_4weeks
# Two months ago
two_months = df_8weeks - (one_month_and_half + one_month)
# Three months ago
three_months = df_12weeks - (two_months + one_month_and_half + one_month)



st.set_option('deprecation.showPyplotGlobalUse', False)

def page_event_planner():
    st.markdown('## 📆 EVENT PLANNER')
    st.write('''Example of how to read this graph:''')
    st.write('631 users created 1 event the last four weeks')
    st.write('131 users created 2 events the last four weeks, etc.')
    st.pyplot(visualize_columns(one_month, ['EVENTS_CREATED']))

    st.markdown("""📆 Event Planner: At least **6** events with a minimum of **3** participants in **12** weeks

There are 20k users and 849 have at least 1 event created the last month (4 weeks).

I visualised the users by the number of events created per month

I analyzed percentages of active users (users who have created one event or more):

1 event - 631 = 74.4%
2 events - 131 = 15.6%
3+ events - 10%

I decided to focus on the top 25% in order to strike a balance between ease and difficulty to obtain the badge, therefore, top 25% would equal to roughly 2+ events/months

2 events/ month *  3 months = 6 events during 12 weeks

Total number of participants = 67% Events have 2 or fewer so we will focus on 3 participants at least (not to make it too hard)

Organizing events takes time and effort

                """)

def page_conversation_starter():
    st.markdown('## 🗣️ Conversation Starter')
    st.write('''Example of how to read this graph:''')
    st.write('4217 users created 1 post the last four weeks')
    st.write('679 users received 1 reply the last four weeks, etc.')
    st.pyplot(visualize_columns(one_month, ['POSTS_CREATED']))

    st.write('''Example of how to read this graph:''')
    st.write('822 users received 1 reply the last four weeks')
    st.write('644 users received 1 reply the last four weeks, etc.')
    st.pyplot(visualize_columns(one_month, ['REPLIES_RECEIVED']))

def page_philanthropist():
    st.markdown('## 🎁 Philanthropist')
    st.write('''Example of how to read this graph:''')
    st.write('1374 users gifted once the last four weeks')
    st.write('298 users gifted twice the last four weeks, etc.')
    st.pyplot(visualize_columns(one_month, ['ITEMS_GIFTED']))

def page_helping_hand():
    st.markdown('## 🫱🏻 Helping Hand')
    st.write('''Example of how to read this graph:''')
    st.write('1028 users received 1 thankyou the last four weeks')
    st.write('412 users received 2 thankyous the last four weeks, etc.')
    st.pyplot(visualize_columns(one_month, ['THANKYOUS_RECEIVED']))

def page_local_guide():
    st.markdown('## 🧳 Local Guide')
    st.write('''Example of how to read this graph:''')
    st.write('638 users recommended 1 place the last four weeks')
    st.write('169 users recommended 2 places the last four weeks, etc.')
    st.pyplot(visualize_columns(one_month, ['PLACES_RECOMMENDED']))


def main():
    st.sidebar.title("Badges")
    selection = st.sidebar.radio("Please select:", ["📆 Event Planner", "🗣️ Conversation Starter", "🎁 Philanthropist", "🫱🏻 Helping Hand", "🧳 Local Guide"])

    if selection == "📆 Event Planner":
        page_event_planner()
    elif selection == "🗣️ Conversation Starter":
        page_conversation_starter()
    elif selection == "🎁 Philanthropist":
        page_philanthropist()
    elif selection == "🫱🏻 Helping Hand":
        page_helping_hand()
    elif selection == "🧳 Local Guide":
        page_local_guide()


if __name__ == "__main__":
    main()
