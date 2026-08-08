import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
st.set_page_config(page_title = 'My Sales Dashboard', page_icon = ':bar-chart:', layout = 'wide')
df= pd.read_csv("/Users/prom1pro/dspy/learncode/00001/all_df.csv")
st.sidebar.header("Please Filter Here")
myselect_products = st.sidebar.multiselect(
    "SELECT PRODUCT",
    options = df["Product"].unique(),default= df["Product"].unique()[:5]
)
myselect_city = st.sidebar.multiselect(
    "SELECT CITY",
    options = df["City"].unique(),default= df["City"].unique()[:5]
)
myselect_month = st.sidebar.multiselect(
    "SELECT MONTH",
    options = df["Month"].unique(),default= df["Month"].unique()[:5])

st.title(" :bar_chart: My Sales Dashboard 2019")
st.markdown("##")
total_sales = df['Total'].sum()
no_of_unique_product = df["Product"].nunique()

left_col, right_col = st. columns(2)
with left_col:
    st.subheader("Total Sales")
    st.subheader(total_sales)

with right_col:
    st.subheader("No. of Product")
    st.subheader(f"{no_of_unique_product}")

df_select = df.query("City == @myselect_city and Month == @myselect_month and Product == @myselect_products")
sales_by_product = df_select.groupby("Product")["Total"].sum()
fig_sales_by_product = px.bar(
    sales_by_product,
    y = sales_by_product.index,
    x= sales_by_product.values,
    orientation= 'h',
    title = "Total Sales By Product"
)
sales_by_month = df_select.groupby("Month")["Total"].sum().sort_values()

fig_sales_by_month=px.bar(
    sales_by_month,
    x=sales_by_month.values,
    y=sales_by_month.index,
    orientation="h",
    title="Sales by Month"
        )

fig_sales_by_city=px.pie(
    df_select,
    values='Total',
    names='City',   
    title=" Sales by City "
        )

a,b,c = st.columns(3)
a.plotly_chart(fig_sales_by_product, use_container_width= True )
b.plotly_chart(fig_sales_by_city, use_container_width= True )
c.plotly_chart(fig_sales_by_month, use_container_width= True )

d, e = st.columns (2)
fig_sales_by_month_line = px.line(
    sales_by_product,
    y= sales_by_month.index,
    x =sales_by_month.values,
    title = "Total Sales By Month"
)

d.plotly_chart(fig_sales_by_month_line ,use_container_width= True)

fig_sales_by_scatter = px.scatter(
    df,
    y= "QuantityOrdered",
    x = "Total",
    title = "Total Sales By Item Amount"
)

e.plotly_chart(fig_sales_by_scatter ,use_container_width= True)