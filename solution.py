import pandas
import re

"""
    Recruitment project for Junior Data Engineer role
    Author: Dawid Boratyński
    Date: 2026-02-11
    Chcek out my another projects on Website: https://bit.ly/dawidboratynski
"""

def add_virtual_column(df: pandas.DataFrame, rule: str, new_column: str) -> pandas.DataFrame:
    
    rule = rule.strip()
    
    # split the rule by the operator
    if '+' in rule:
        operator = '+'
        columns = rule.split('+')
    elif '-' in rule:
        operator = '-'
        columns = rule.split('-')
    elif '*' in rule:
        operator = '*'
        columns = rule.split('*')
    else:
        return pandas.DataFrame([])
    
    columns = [col.strip() for col in columns]
    
    # only letters and underscores
    if not re.match(r'^[a-zA-Z_]+$', new_column):

        return pandas.DataFrame() 
    
    # check if the columns exist in the DataFrame
    if not all(col in df.columns for col in columns):
        return pandas.DataFrame([])
    
    if operator == '+':
        df[new_column] = df[columns[0]] + df[columns[1]]
    elif operator == '-':
        df[new_column] = df[columns[0]] - df[columns[1]]
    elif operator == '*':
        df[new_column] = df[columns[0]] * df[columns[1]]
    
    return df