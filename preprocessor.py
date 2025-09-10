import pandas as pd



def preprocess(df,region_df):
    # filtering for summer olympics
    df = df[df['Season'] == 'Summer']
    # Merge with region_df
    # region_df = region_df[ [ 'NOC', 'region' ] ]  # keep only what you need
    df = df.merge(region_df, on='NOC', how='left')

    # Dropping duplicates
    df.drop_duplicates(inplace=True)
    # one hot encoding medals
    df = pd.concat([df, pd.get_dummies(df[ 'Medal' ], dtype=int) ], axis=1)
    return df
