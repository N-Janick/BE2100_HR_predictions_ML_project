# BE2100 Home Run Prediction Machine Learning Project

## Overview
This group project for BE2100 aims to explore statistical analysis and machine learning by developing a machine learning model that predicts the number of home runs a player will hit in a season based on various features derived from historical MLB data. The project is structured to support collaborative data analysis, feature engineering, model training, and evaluation.

## Repository Structure
```
    BE2100_HR_predictions_ML_project/
    |-- data/                                   
    |   |-- raw/                # Raw unprocessed data
    |   |-- cleaned/            # Cleaned data sets
    |   |-- processed/          # Processed datasets that are ready for engineered features
    |   |-- predictions/        # output datasets
    |
    |-- notebooks/
    |   |-- exploration/        # individual notebooks for each team member to explore and analyze data as well as work on engineering features
    |       |-- busrah_k_notebook.ipynb
    |       |-- jawad_e_notebook.ipynb
    |       |-- justin_t_notebook.ipynb
    |       |-- kamran_h_notebook.ipynb
    |       |-- karl_s_notebook.ipynb
    |       |-- miles_l_notebook.ipynb
    |       |-- nick_j_notebook.ipynb
    |       |-- nick_l_notebook.ipynb
    |   |-- modeling
    |       |-- proposed_features.ipynb         # shared notebook where memebers can propose feature to be included in the model
    |       |-- model_training.ipynb            # shared notebook for training the model
    |-- scripts/
    |   |-- data_cleaning.py            # Script to clean raw data
    |   |-- feature_engineering.py      # Script to apply selected features to data
    |   |-- prepare_predictions.py      # Script to prepare input for model predictions
    |   |-- train_model.py              # Script to train and evaluate final model
    │-- models/                 # Trained models and serialized versions
    │-- reports/                # Model performance reports and analysis
    │-- README.md               # Project documentation
    |-- setup_environment.bat   # Script to set up virtual environment windows
    |-- setup_environment.sh    # Script to set up virtual environment mac/linux
    |-- requirements.txt          
```

## The Data
I downloaded a couple of datasets from fangraphs.com. One is player batting stats, including advanced statistics, for the 2005 - 2024 season. The other is team batting statistics for the same date range. I pulled more than we may need in case we find the model is not very accurate. This way we can add additional data if needed. I started with 2005 as that is generally accepted as the end of the steroid era of baseball. In 2015, MLB started tracking 
"Statcast" cast stats, which consist of new advanced statistics that relate to batted balls such as exit velocity. This seems like a good place to split the data, as we will have to figure out how to deal with the missing Statcast data pre 2015.

## Instructions
Clone repo and create a branch for yourself when working on project. Please do not work on main branch. When creating pull request that involves anything other than your personal data exploration notebook, please request a review from someone working on that part of the project.

To set up and run a virtual environment for working on the project you can open a command prompt and run the appropriate setup_environment script for your os

`setup_environment.bat`

or

`setup_environment.sh`

Once the virtual environment is running you can enter the following command to open Jupyter notebooks and work on the project:

`Jupyter notebook`

This should open Jupyter notebooks in a browser and you will be able to access your files and notebooks from there.

Alternatively, you can work on and IDE with extensions supporting notebooks, such as VS Code.

## Individual Notebooks for exloration
I have added individual notebooks for everyone to explore and analyze data with, as well as experiment with code. Anyone who is not officially working on the model training portion but wants some hands on with machine learning can use their notebook to experiment with feature engineering. Please just communicate with the rest of the team any possible features you are exploring so we don't have people doing duplicate work. Once you have a feature you feel is ready, you can add the python code and a short justification for why you think it will be an impactful feature to the proposed_features notebook. Create a pull request and assign it to anyone on the "model training" team so they can look it over and work it into the feature engineering and model training scripts.

## Naming conventions
I have set up some import statements and aliases in all of the notebooks to get us started and all on the same page, such as:
```python
    import matplotlib.pyplot as plt
    import pandas as pd

    raw_data = '../../data/raw/fangraphs_2005-2024_batting_stats_raw.csv' 
    data_source = raw_data

    /# creates a dataframe from a dataset to work with the data
    df = pd.read_csv(data_source)
```

When creating new variables please use `snake_case` for consistency.

## Helpful links
[pandas documentation](https://pandas.pydata.org/docs/)

[numpy documentation](https://numpy.org/doc/)

[matplotlib documentation](https://matplotlib.org/stable/index.html)

[scipy documentation](https://docs.scipy.org/doc/scipy/)

[scikit-learn documentation](https://scikit-learn.org/stable/)

[seaborn documentation](https://seaborn.pydata.org/)

Baseball links

[Baseball statistics and how to analyze them](https://library.fangraphs.com/getting-started/)

[Article on exit velocity interpretation](https://blogs.fangraphs.com/the-doomed-search-for-a-perfect-way-to-interpret-exit-velocity-data/)

[Article about the different eras of baseball](https://imaginesports.com/bball/reference/eras/popup)

[Article about Statcast stats (available 2015 - present)](https://www.mlb.com/news/statcast-primer-baseball-will-never-be-the-same/c-119234412)

[Additional Statcast article](https://www.si.com/mlb/2016/08/26/statcast-era-data-technology-statistics)
