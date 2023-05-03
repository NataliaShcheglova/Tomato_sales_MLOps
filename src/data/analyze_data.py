git #!/usr/bin/env python
# coding: utf-8

# In[1]:


import click
import pandas as pd
import seaborn as sns


@click.command()
@click.option("--input-path", type=click.Path(exists=True), required=True)
@click.option("--output-path", type=click.Path(), required=True)
def analyze_data(input_path: str, output_path: str):
    """Function analyze time series data from a CSV file, print the graphs
    and general information and rebuild missed data.
    :param input_path: Path to read original DataFrame with all listings
    :param output_path: Path to save clean DataFrame
    :return:
    """
    df = pd.read_csv(input_path, index_col=[0], parse_dates=[0])
    # Display general information about dataset
    print(df.head())
    print(df.info())
    # Check if we have different markets and units
    print(df["Market"].value_counts())
    print(df["Unit"].value_counts())
    # Drop market and unit columns
    df = df.drop("Market", axis=1)
    df = df.drop("Unit", axis=1)
    # Check and display the number of missing dates
    df = df.asfreq("D")
    missing_values = df.isnull().sum()
    missed_percentage = missing_values / len(df)
    print("Количество отстутствующийх дней", missing_values)
    print(
        "Процент отстутствующийх дней от всего датасета",
        round(missed_percentage, 2),
        "%",
    )
    # Check and display missing dates
    mask = df["Average"].isnull()
    missing_dates = df.index[mask]
    print("Пропущенные даты:\n", missing_dates)
    # Display one graph with a few missing dates
    df["2013-06-15":"2013-07-30"].plot(
        figsize=(20, 3), title="Пробел в данных - Июнь 2013", color="#FF00FF"
    )
    # Fill in the missing dates
    df = df.interpolate(method="slinear")
    # Display one graph with filled in missing dates
    df["2013-06-15":"2013-07-30"].plot(
        figsize=(20, 3), title="Missing dates - June 2013", color="#FF00FF"
    )
    # Display dataset graphs
    sns.set(style="darkgrid")
    df.plot(subplots=True, figsize=(20, 10))
    # Drop Minimum and Maximum columns
    df = df.drop("Minimum", axis=1)
    df = df.drop("Maximum", axis=1)
    # Resampling by one week
    df = df.resample("1W").mean()
    print(df.info())
    df.plot(subplots=True, figsize=(20, 10))

    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    analyze_data()
