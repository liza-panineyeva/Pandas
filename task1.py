import pandas
"""In this method I consider that all parametrs will provided be correctly"""
def group_by(stream,field,success=None):
    i = 0
    j = 5
    if field == 'month':
        i=5
        j=9
    df =  pandas.read_fwf(stream, na_values=[])
    new_header = df.iloc[0]
    df = df[1:]
    df = df.fillna(method='ffill')
    df.rename(columns = new_header)
    if success==True:
        df = df[df["Suc"]=="S"]
    elif success==False:
        df = df[df["Suc"] == "F"]
    ld = df.groupby( [df["Launch Date"].str[i:j]]).agg({"Launch Date":"count"})
    return ld
"""I know that method should return a dict, but i like it that way more  :)"""
print(group_by(open('launchlog.txt'),"month",success=False))

