# import streamlit as st
# import mysql.connector
# import plotly.express as px
#
# # Database connection
# cnx = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='root',
#     database='financial_inclusion'
# )
#
# def fetch_data(search=None):
#     cursor = cnx.cursor()
#     if search:
#         query = "SELECT * FROM indicators WHERE `Financial inclusion indicator` LIKE %s"
#         cursor.execute(query, ('%' + search + '%',))
#     else:
#         query = "SELECT * FROM indicators"
#         cursor.execute(query)
#     data = cursor.fetchall()
#     columns = [column[0] for column in cursor.description]
#     cursor.close()
#     return columns, data
#
# def create_bar_chart(data):
#     fig = px.bar(data, x=['2008', '2012', '2016', '2020'], y=['2008', '2012', '2016', '2020'],
#                  barmode='group', title='Financial Inclusion Indicators')
#     return fig
#
# def main():
#     st.title('Financial Inclusion Indicators')
#
#     search = st.text_input('Enter search criteria:')
#     columns, data = fetch_data(search)
#
#     st.table(data)
#
#     fig = create_bar_chart(data)
#     st.plotly_chart(fig)
#
# if __name__ == '__main__':
#     main()



import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px

# Database connection
cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='financial_inclusion'
)

def fetch_data(search=None):
    cursor = cnx.cursor()
    if search:
        query = "SELECT * FROM indicators WHERE `Financial inclusion indicator` LIKE %s"
        cursor.execute(query, ('%' + search + '%',))
    else:
        query = "SELECT * FROM indicators"
        cursor.execute(query)
    data = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    cursor.close()
    return columns, data

def create_line_chart(data):
    df = pd.DataFrame(data)
    df.columns = ['Indicator', '2008', '2012', '2016', '2020']
    df = df.set_index('Indicator')  # Set 'Indicator' column as the index
    df = df.transpose()  # Transpose the DataFrame for line chart visualization

    fig = px.line(df, x=df.index, y=df.columns, title='Financial Inclusion Indicators over Time')
    return fig

def main():
    st.title('Financial Inclusion Indicators')

    search = st.text_input('Enter Indicator:')
    columns, data = fetch_data(search)

    st.table(data)

    fig = create_line_chart(data)
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()
