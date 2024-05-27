import pandas as pd
import streamlit as st

from functions import *


# st.markdown('## Analysis')
# st.code('''
#         df = pd.read_csv('nebenan.csv')
#         print(df)''', language='python')

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
