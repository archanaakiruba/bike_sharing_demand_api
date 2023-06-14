import pandas as pd
import numpy as np
import holidays
from datetime import date

# Function for Holiday Flag
def is_holiday(data: pd.DataFrame):
    """
    Performs feature engineering on the input data.

    Args:
        data (pd.DataFrame): The input DataFrame.

    Returns:
        DataFrame: A DataFrame containing the Holiday Flags.
    """
    df = data.copy()
    df['rent_date_hour'] = pd.to_datetime(df['rent_date_hour'])

    # Extract date from rent_date_hour
    date_column = df['rent_date_hour'].dt.date

    # Checking for the Bayern Holidays
    bay_holidays = holidays.CountryHoliday('DE', prov='BY')

    df['is_holiday'] = date_column.apply(lambda x: 1 if x in bay_holidays else 0)

    return df[['rent_date_hour', 'is_holiday']]


# Function for Weekend Flag
def is_weekend(data: pd.DataFrame):
    """
    Performs feature engineering on the input data.

    Args:
        data (pd.DataFrame): The input DataFrame.

    Returns:
        DataFrame: A DataFrame containing the Weekend Flags.
    """
    df = data.copy()
    df['rent_date_hour'] = pd.to_datetime(df['rent_date_hour'])

    # Extract date from rent_date_hour
    date_column = data['rent_date_hour'].dt.date

    # Checking if Day is a Weekend or not
    df["is_weekend"] = date_column.apply(lambda x: 1 if x.weekday() >= 5 else 0)

    return df[['rent_date_hour', 'is_weekend']]


def feature_selection(data, list):
    '''
    Performs feature selection on the input data.

    Args:
        data (pd.DataFrame): The input DataFrame.
        list: List containing features

    Returns:
        DataFrame: A DataFrame containing the Features from the List.
    '''
    df = data[[c for c in data.columns if c in list]]

    return df
