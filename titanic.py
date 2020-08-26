#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from src import preprocess, build_features, train

# paths:
data_dir = "./data/"

# data for training:
train_csv = data_dir + "train.csv"
train_df_csv = data_dir + "train_df.csv"
train_df2_csv = data_dir + "train_df2.csv"

# data for validation:
val_csv = data_dir + "val.csv"
val_df_csv = data_dir + "val_df.csv"

model_path = data_dir + "model.pkl"

if __name__ == '__main__':

    # 1. preprocess
    preprocess.execute(train_csv, train_df_csv)

    # 2. build features
    build_features.execute(train_df_csv, train_df2_csv)

    # 3. train
    train.execute(train_df2_csv, model_path)

    # 4. predict