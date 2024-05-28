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
    st.markdown("""At least **6** events with a minimum of **3** participants in **12** weeks""")
    st.caption('''Example of how to read the following graph:''')
    st.caption('631 users created 1 event the last four weeks')
    st.caption('131 users created 2 events the last four weeks, etc.')
    st.pyplot(visualize_columns(one_month, ['EVENTS_CREATED']))

    st.markdown("""

*Explanation:*

849 (out of 20k users) have at least 1 event created the last month (4 weeks).

I visualised the users by the number of events created per month and analyzed percentages of active users (users who have created one event or more):

1 event - 631 = 74.4%

2 events - 131 = 15.6%

3+ events - 10%

I decided to focus on the top 25% of users in order to strike a balance between ease and difficulty to obtain the badge, therefore, top 25% would equal to roughly 2+ events/months

2 events/ month *  3 months = 6 events during 12 weeks
""")
    st.write('-'*20)
    st.caption('''Example of how to read the following graph:''')
    st.caption('370 users welcomed 1 participant the last four weeks')
    st.caption('184 users received 2 participants the last four weeks, etc.')
    st.pyplot(visualize_columns(one_month, ['EVENT_PARTICIPANTS']))
    st.markdown('*Explanation:*')
    st.markdown('67% of users have 1 or 2 participants.')
    st.markdown("""
                44.85% of users - 1 participant

                22.30% of users - 2 participants

                12.85% of users - 3 participants (falls into top 25%)""")
    st.markdown("""Therefore, I chose 3 participants to not make it too hard but still make it encouraging
            since there are 6 events to organise for 12 weeks and organizing events takes time and effort.
                """)

def page_conversation_starter():
    st.markdown('## 🗣️ Conversation Starter')
    st.markdown(""" At least **6** posts with a minimum of **5** replies in **12** weeks.""")
    st.caption('''Example of how to read the following graph:''')
    st.caption('4217 users created 1 post the last four weeks')
    st.caption('679 users received two posts the last four weeks, etc.')
    st.pyplot(visualize_columns(one_month, ['POSTS_CREATED']))
    st.markdown("""
        *Explanation*

        Considering the users who created at least one post

        80% of users created 1 post per month

        20% of users created 2 posts or more per month

        2 posts/ month falls into the top 25% users.
        """
    )
    st.write('-'*20)

    st.caption('''Example of how to read the following graph:''')
    st.caption('822 users received 1 reply the last four weeks')
    st.caption('644 users received 2 replies the last four weeks, etc.')
    st.pyplot(visualize_columns(one_month, ['REPLIES_RECEIVED']))
    st.markdown("""For the replies to get into the top 25% of posts with the most replies, the posts need to have at least 5 replies revealed as follows:

    1 reply - 27% of posts

    2 replies - 20% of posts

    3 replies - 14% of posts

    4 replies - 11% of posts

    5 replies - 6% of posts (breaking into the top 25 %)""")

def page_philanthropist():
    st.markdown('## 🎁 Philanthropist')
    st.markdown(""" At least **6** items gifted on the marketplace in **12** weeks.""")

    st.caption('''Example of how to read the following graph:''')
    st.caption('1374 users gifted once the last four weeks')
    st.caption('298 users gifted twice the last four weeks, etc.')
    st.pyplot(visualize_columns(one_month, ['ITEMS_GIFTED']))
    st.markdown("""
                *Explanation:*

                69% of users who have gifted - 1 item gifted

                15% of users who have gifted - 2 items gifted (breaking into the top 25%)

                2 * 3 months (12 weeks) = 6 items gifted per user """)

def page_helping_hand():
    st.markdown('## 🫱🏻 Helping Hand')
    st.markdown("""At least **10** thank-you messages received in **12** weeks.""")
    st.caption('''Example of how to read the following graph:''')
    st.caption('1028 users received 1 thankyou the last four weeks')
    st.caption('412 users received 2 thankyous the last four weeks, etc.')
    st.pyplot(visualize_columns(one_month, ['THANKYOUS_RECEIVED']))
    st.markdown("""
                *Explanation*

                Users with at least X thank you reaction per month:

                1 thank you reaction - 48%

                2 thank you reactions - 19%

                3 thank you reactions - 8%

                It takes 3 thank you reactions to break into the top 25% of the users with the most thank you reactions per month

                3 * 3 months (12 weeks) = 9 -> rounding up to 10 thank you reactions
                """)

def page_local_guide():
    st.markdown('## 🧳 Local Guide')
    st.markdown("""At least **10** places recommended in **12** weeks.""")
    st.caption('''Example of how to read the following graph:''')
    st.caption('638 users recommended 1 place the last four weeks')
    st.caption('169 users recommended 2 places the last four weeks, etc.')
    st.pyplot(visualize_columns(one_month, ['PLACES_RECOMMENDED']))
    st.markdown("""
                *Explanation*

                Users with one recommendation - 61%

                Users with 2 recommendations - 16%

                Users with 3 recommendations - 5% (breaking the into 25%)

                3 recommendations per month * 3 months (12 weeks) = 9 recommendations -> rounding it up to 10 recommendations

                """)

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
