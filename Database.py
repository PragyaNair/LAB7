import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('people.db')
cursor = conn.cursor()

# Execute the SQL query to get old people (age >= 50)
cursor.execute('''
    SELECT name, age
    FROM people
    WHERE age >= 50
''')

# Fetch all the query results
results = cursor.fetchall()

# Print the name and age of each old person
for name, age in results:
    print(f"{name} is {age} years old.")

# Save the results to a CSV file
df = pd.DataFrame(results, columns=['Name' ,  'Age'])
df.to_csv('old_people.csv', index=False)

# Close the connection
conn.close()
