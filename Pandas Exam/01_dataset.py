import pandas as pd

# Check version
print(pd.__version__)

# pandas.Series
data1 = ['a', 'b', 'c', 'd', 'e']
sr1 = pd.Series(data1)
print('자료형 : {}'.format(type(sr1)))
print()

# print Series
print('print Series')
print(sr1)
print()

# print with index (Use loc)
print('print with index (Use loc)')
print(sr1.loc[1])
print()

# loc can also slicing
print('loc can also slicing (but not same of lists indexing)')
print(sr1.loc[1:3])
print()

# if data is int, dtype is float64
print('int type')
data2 = [1, 3, 4, 13, 12.1, -100]
sr2 = pd.Series(data2)
print(sr2)
print()

# Make DataFrame
dict_data = {'c0': sr1, 'c1': sr2}
df1 = pd.DataFrame(dict_data)
print(df1)
print()
