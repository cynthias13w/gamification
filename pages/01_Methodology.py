import streamlit as st


st.markdown("""
### How did I do data exploration?

To conduct this analysis, I proceeded with the following assumptions:

1. **Missing Values Handling**: I assumed that missing values indicated zero activity, given their consistent occurrence. For instance, if a user had no posts represented by ‘NaN’, it was treated as zero activity.
2. **Zero Data Points Exclusion**: I did not use data points where the value equaled zero because zero data points do not provide insights about *activity*. This is to ensure that my analysis focused on active users and avoided inactive/almost inactive participants in order to make predictions that will also engage those less active users.

To decide on a strategy, I started with different approaches such as isolating data per data frame in order to look at individual months, or looking at statistics of unique values or focusing on top users. (see .ipynb notebook)

### What did I focus on?

In the end, the strategy that I decided to focus on is as follows:

1. **Top Performers**: To strike a balance between making earning the badges not too easy and not too difficult, I concentrated on metrics that fell within the top 25% per month.
2. **Consistent Timeframe for Analysis**: I analysed the one month timeframe because it is a common timeframe used by anyone and easy to understand for users and internally
3. **Consistent Timeframe for Predictions**: For coherence and simplicity, I opted for a consistent timeframe of 12 weeks across all badge categories.
This duration is recognized in the industry (for e.g., TK Fit Challenge) and provides users with a reasonable period to track their progress and keeps users engaged for a longer period of time.""")
