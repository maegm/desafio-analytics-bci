def select_countries(df):
    df1 = df.copy()
    df1.drop(df1[~df1['Country'].isin(['us', 'gb'])].index, inplace=True)
    return df1


def define_east_and_west_coast(df):
    df1 = df.copy()
    # west coast: California (CA), Oregon (OR), Washington (WA)
    # east coast: Maine (ME), Nuevo Hampshire (NH), New York (NY), Massachusetts (MA),
    #             Rhode Island (RI), Connecticut (CT), New Jersey (NJ), Delaware (DE), Maryland (MD), Virgina (VA),
    #             North Carolina (NC), South Carolina (NC), Georgia (GA), Florida (FL), Delaware (DE)

    states = {
        'west coast': ['CA', 'OR', 'WA'],
        'east coast': ['ME', 'NH', 'NY', 'MA', 'RI', 'CT', 'NJ', 'DE', 'MD', 'VA', 'NC', 'SC', 'GA', 'FL']
    }
    for coast in states.keys():
        f1 = df1['Country'] == 'us'
        f2 = df1['Region'].isin(states[coast])
        df1.loc[f1 & f2, 'Coast'] = coast
    df1.loc[df1['Country'] == 'gb', 'Coast'] = 'united kingdom'
    df1.drop(df1[df1['Coast'].isna()].index, inplace=True)
    df1.reset_index(drop=True, inplace=True)
    return df1


def usa_cities_in_uk(df):
    dfp = (
        df.groupby(['Coast', 'City'], as_index=False)['Region'].count()
        .rename(columns={'Region': 'N Cities'})
        .pivot(index='City', columns='Coast', values='N Cities')
    )
    f1 = dfp['united kingdom'] >= 1
    f2 = (dfp['west coast'] >= 1) | (dfp['east coast'] >= 1)
    dfp.drop(dfp[~(f1 & f2)].index, inplace=True)
    return dfp
