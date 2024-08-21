import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

# Define the file path
csv_file_path = r'C:\Users\SMART SPACE STORE\Documents\Business\US_Accidents_March23.csv'

# Load the dataset
df = pd.read_csv(csv_file_path)

# Step 1: Basic Data Exploration
print(df.head())  # Display the first few rows of the dataset
print(df.info())  # Display a summary of the dataset
print(df.describe())  # Display basic statistical details

# Step 2: Handle Missing Values (if any)
missing_values = df.isnull().sum()
print(missing_values)  # Check for missing values

# Optionally, you can drop rows or fill missing values
# df = df.dropna()  # Drop rows with missing values
# df.fillna(method='ffill', inplace=True)  # Forward fill missing values

# Step 3: Analyze Traffic Accidents by Time of Day
df['Start_Time'] = pd.to_datetime(df['Start_Time'])  # Convert to datetime
df['Hour'] = df['Start_Time'].dt.hour  # Extract the hour
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Hour', palette='viridis')
plt.title('Traffic Accidents by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Accidents')
plt.show()

# Step 4: Analyze Traffic Accidents by Weather Conditions
plt.figure(figsize=(10, 6))
sns.countplot(data=df, y='Weather_Condition', order=df['Weather_Condition'].value_counts().iloc[:10].index, palette='coolwarm')
plt.title('Top 10 Weather Conditions During Accidents')
plt.xlabel('Number of Accidents')
plt.ylabel('Weather Condition')
plt.show()

# Step 5: Analyze Traffic Accidents by Road Conditions
plt.figure(figsize=(10, 6))
sns.countplot(data=df, y='Road_Condition', order=df['Road_Condition'].value_counts().iloc[:10].index, palette='magma')
plt.title('Top 10 Road Conditions During Accidents')
plt.xlabel('Number of Accidents')
plt.ylabel('Road Condition')
plt.show()

# Step 6: Visualize Accident Hotspots Using Folium
# For demonstration, we'll plot accidents in a specific city (e.g., Los Angeles)
df_la = df[df['City'] == 'Los Angeles']  # Filter accidents in Los Angeles
map_la = folium.Map(location=[34.0522, -118.2437], zoom_start=10)

# Add accident markers to the map
for index, row in df_la.iterrows():
    folium.CircleMarker(
        location=(row['Start_Lat'], row['Start_Lng']),
        radius=2,
        color='red',
        fill=True,
        fill_opacity=0.6
    ).add_to(map_la)

# Save the map as an HTML file
map_la.save('LA_Accident_Hotspots.html')

print("Analysis complete. Check the LA_Accident_Hotspots.html file for the map.")

