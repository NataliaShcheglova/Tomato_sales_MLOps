#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import click
import pandas as pd


@click.command()
@click.option("--input-path", type=click.Path(exists=True), required=True)
@click.option("--output-path", type=click.Path(), required=True)
def featured_data(input_path: str, output_path: str):
    """Function make features for time series DataFrame from a CSV file
    :param input_path: Path to read original DataFrame with all listings
    :param output_path: Path to save clean DataFrame
    :return:
    """
    df = pd.read_csv(input_path, index_col=[0], parse_dates=[0])

    # Check if the 'Average' column exists in the input DataFrame
    if 'Average' not in df.columns:
        # Create the 'Average' column if it doesn't exist
        df['Average'] = df.mean(axis=1)

    # Convert the index to an integer index
    df.index = df.index.astype(int)

    # Convert the index to a DatetimeIndex
    df.index = pd.to_datetime(df.index)

    def make_features(data, max_lag, rolling_mean_size):
        # Extract the month and day attributes from the DatetimeIndex
        data['month'] = data.index.month
        data['day'] = data.index.day

        for lag in range(1, max_lag + 1):
            data['lag_{}'.format(lag)] = data['Average'].shift(lag)

        data['rolling_mean'] = data['Average'].shift().rolling(rolling_mean_size).mean()

        return data

    df_prepared = make_features(df, 4, 4)
    df_prepared.to_csv(output_path, index=False)


if __name__ == "__main__":
    featured_data()
