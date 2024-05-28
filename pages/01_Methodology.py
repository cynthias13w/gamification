import streamlit as st

st.markdown("""<h3 style="color: #FE9DE1;">How did I do data exploration?</h3>""", unsafe_allow_html=True)
st.markdown("""
To conduct this analysis, I proceeded with the following assumptions:

1. **Missing Values Handling**: I assumed that missing values indicated zero activity, given their consistent occurrence. For instance, if a user had no posts represented by ‘NaN’, it was treated as zero activity.
2. **Zero Data Points Exclusion**: I did not use data points where the value equaled zero because zero data points do not provide insights about *activity*. This is to ensure that my analysis focused on active users and avoided inactive/almost inactive participants in order to make predictions that will also engage those less active users.""")

st.markdown("""<h3 style="color: #FE9DE1;">How did I come up with a strategy?</h3>""", unsafe_allow_html=True)
st.markdown("""I started with different approaches:""")

st.markdown("""1. I isolated data per data frame in order to look at visualisations of individual months (three months of data) which I found similar.""")
st.markdown("""2. I looked at statistics of unique values to understand the spread of the data (maximum values, median)""")
st.markdown("""3. I analysed top users in order to gain insights regarding outliers. (see .ipynb notebook)""")

st.markdown("""<h3 style="color: #FE9DE1;">What strategy did I focus on in the end?</h3>""", unsafe_allow_html=True)

st.markdown("""
In the end, the strategy that I decided to focus on is as follows:

1. **Top Performers**: To strike a balance between making earning the badges not too easy and not too difficult, I concentrated on metrics that fell within the top 25% per month.
2. **Consistent Timeframe for Analysis**: I analysed the one month timeframe because it is a common timeframe used by anyone and easy to understand for users and internally. Also, after visualising the other months, the data did not appear to be widely different.
One other approach would have been to take an aggregation of three months.
3. **Consistent Timeframe for Predictions**: For coherence and simplicity, I opted for a consistent timeframe of 12 weeks across all badge categories.
This duration is recognized in the industry (for e.g., TK Fit Challenge) and provides users with a reasonable period to track their progress and keeps users engaged for a longer period of time.
""")
