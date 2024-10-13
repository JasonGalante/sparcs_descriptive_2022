import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

# set options 

## change default to not display exponential notation but float
pd.set_option('display.float_format', lambda x: '%.3f' % x)


df = pd.read_csv('C:\\Users\\grift\\sparcs_descriptive_2022\\Hospital_Inpatient_Discharges__SPARCS_De-Identified___2022_20241013.csv')


# First step: cleaning column names
# remove all white space, lower case, replace space with underscores
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('-', '_')
df_len = len(df)

## remove commas from total_charges and total_costs
df.total_charges = df.total_charges.apply(lambda x : x.replace(',',''))
df.total_costs = df.total_costs.apply(lambda x : x.replace(',',''))

## convert total_charges and total_costs to numeric
df['total_charges'] = pd.to_numeric(df['total_charges'], errors='coerce')
df['total_costs'] = pd.to_numeric(df['total_costs'], errors='coerce')

## count nan for total_charges and total_costs
df['total_charges'].isna().sum()
df['total_costs'].isna().sum()

#Remove unwanted columns
columns_to_keep = ['age_group', 'gender', 'length_of_stay','type_of_admission', 'total_charges', 'total_costs', 
    'discharge_year', 'ethnicity', 'race']

df = df[columns_to_keep]


# Calculate basic statistics for Length_Of_Stay, Total_Charges, and Total_Costs
df['length_of_stay'].describe()
df['total_costs'].describe()
df['total_charges'].describe()



# Count the distribution of age_group, gender, and type_of_admission
distribution = df.groupby(['age_group', 'gender', 'type_of_admission']).size().reset_index(name='Count')

print(distribution)

# create a bar plot for age_group, gender, and type_of_admission using matplotlib


# create histogram for length_of_stay
bins = range(1, 20)  # Bins from 1 to 10 (inclusive)

plt.figure(figsize=(10, 6))
plt.hist(df['length_of_stay'], bins=bins, color='skyblue', edgecolor='black', align='left')
plt.title('Histogram of Length of Stay')
plt.xlabel('Length of Stay')
plt.ylabel('Frequency')
plt.xticks(bins)  # Set x-ticks to match the bin edges
plt.xlim(1, 20)  # Set x-axis limits
plt.grid(axis='y', alpha=0.5)  # Optional: Add gridlines for better readability
plt.show()

# Create a box plot for total_charges
plt.figure(figsize=(10, 6))
plt.boxplot(df['total_charges'])
plt.title('Boxplot of Total Charges')
plt.ylabel('Total Charges')
plt.show()

# Create a bar plot for type_of_admission
plt.figure(figsize=(10, 6))
plt.bar(df['type_of_admission'].value_counts().index, df['type_of_admission'].value_counts().values)
plt.title('Bar Plot of Type of Admission')
plt.xlabel('Type of Admission')
plt.ylabel('Count')
plt.show()
