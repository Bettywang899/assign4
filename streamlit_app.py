# Import necessary packages (Make sure to also include in "requirements.txt" in this repository.)
import streamlit as st
import pandas as pd

# Print Title for the App
st.title("Microsoft Stock Data Dashboard by Xiaobei Wang")

# Read CSV file with stock data (CSV file must be in 'main' folder for your assignment 4 repository) 
df = pd.read_csv("msft.csv")

# Set up the 4 tabs on the Dashboard
tabs = st.tabs(["📋 Raw Data", "📈 Price Chart", "📊 Volume Chart", "☀️ Fun Tab"])

# Tab 1: Raw Data
with tabs[0]:
    st.subheader(f"Raw Data for MSFT")
    st.dataframe(df, use_container_width=True)

# Tab 2: Closing Price Chart
with tabs[1]:
    st.subheader(f"Closing Price for MSFT")
    st.line_chart(df['Close'])

# Tab 3: Volume Chart
with tabs[2]:
    st.subheader(f"Volume for MSFT")
    st.bar_chart(df['Volume'])

# Tab 4: Volume Chart
with tabs[3]:
    st.subheader(f"Birthday Countdown")
    st.write("Find out how many days are left until your next birthday!")

    from datetime import datetime, date, timedelta
    from zoneinfo import ZoneInfo

    # Get today's date in Boston (Eastern Time)
    today = datetime.now(ZoneInfo("America/New_York")).date()

    # Select an upcoming birthday
    birthday = st.date_input(
        "🎁 Select your upcoming birthday:",
        value=today + timedelta(days=30),
        min_value=today,
        max_value=date(today.year + 5, 12, 31)
    )

    # Calculate days remaining
    days_left = (birthday - today).days

    # Display countdown
    if days_left == 0:
        st.success("🎉 Happy Birthday! Have an amazing day!")
        st.balloons()
    else:
        st.metric("🎈 Days Until Your Birthday", days_left)

        if days_left <= 7:
            st.write("🎁 Your birthday is almost here!")
        elif days_left <= 30:
            st.write("🎉 Less than a month to go!")
        else:
            st.write("✨ The countdown has begun!")

