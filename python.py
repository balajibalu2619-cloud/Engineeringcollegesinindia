import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Basic Data Cleaning
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df['Established Year'] = pd.to_numeric(df['Established Year'], errors='coerce')
df['Average Fees'] = pd.to_numeric(df['Average Fees'], errors='coerce')

# 1. Distribution of Average Fees
fig1 = px.histogram(df, x='Average Fees', nbins=20, title='Distribution of Average Fees')

# 2. Top 10 Cities with Most Colleges
city_count = df['City'].value_counts().nlargest(10).reset_index()
city_count.columns = ['City', 'Count']
fig2 = px.bar(city_count, x='City', y='Count', title='Top 10 Cities with Most Engineering Colleges')

# 3. Colleges by Established Year
year_count = df['Established Year'].value_counts().sort_index().reset_index()
year_count.columns = ['Year', 'Count']
fig3 = px.line(year_count, x='Year', y='Count', title='Number of Colleges Established Over Years')

# 4. Average Fees by College Type
fig4 = px.box(df, x='College Type', y='Average Fees', title='Average Fees by College Type')

# Save visualizations as HTML dashboard
from plotly.subplots import make_subplots
from plotly.offline import plot

dashboard_html = """
<html>
<head><title>Engineering Colleges in India - Dashboard</title></head>
<body>
<h1>Engineering Colleges in India - Data Analysis Dashboard</h1>
""" + \
plot(fig1, output_type='div') + \
plot(fig2, output_type='div') + \
plot(fig3, output_type='div') + \
plot(fig4, output_type='div') + \
"""
</body>
</html>
"""

dashboard_path = "/mnt/data/engineering_colleges_dashboard.html"
with open(dashboard_path, "w") as f:
    f.write(dashboard_html)

dashboard_path