table_name = 'churn_records'
str = f'''
                CREATE TABLE IF NOT EXISTS {table_name} ('''
for i in ['1', '2', '3']:
    print(f"{i} DECIMAL NOT NULL", sep='/n')
    str += f"{i} DECIMAL NOT NULL, "
str = str[:-2]
str += ');' 
print(str)