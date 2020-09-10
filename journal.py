import pandas as pd 
import numpy as np
from datetime import date
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import os

DIRNAME = os.path.dirname(os.path.abspath("__file__"))
PATH_TO_CSV = os.path.join(DIRNAME, 'daylio_export.csv')


def gen_baseline_metrics(path_to_csv = PATH_TO_CSV):

    ugly_df = pd.read_csv(path_to_csv, index_col=False)
    df = clean_df(ugly_df)

    entries_over_time = gen_entries_over_time_hist(df)
    wordcloud = gen_wordcloud(df)

    pass

def clean_df(df):

    df.full_date = pd.to_datetime(df.full_date)
    clean_df = convert_activities_to_categorical(df)
    
    return(clean_df)

def convert_activities_to_categorical(df):

    all_activities = []

    for index, row in df.iterrows():
        if type(row['activities']) == str:
            activities_list = row['activities'].split(" | ")
            for activity in activities_list:
                if activity not in all_activities:
                    all_activities.append(activity)

    categorical_activity_matrix = []

    for index, row in df.iterrows():
        activity_list_binary = []
        for activity in all_activities:
                if type(row['activities']) != str:
                    activity_list_binary = [False] * len(all_activities)
                else:
                    if activity in row['activities']:
                        activity_list_binary.append(True)
                    else: 
                    activity_list_binary.append(False)
        categorical_activity_matrix.append(activity_list_binary)

    categorical_df = pd.DataFrame(categorical_activity_matrix, columns = all_activities)

    full_df = pd.concat([df, categorical_df], axis=1)

    return(categorical_df)




def gen_entries_over_time_hist(df):

    df._month = pd.to_datetime(df.full_date).dt.to_period('M').dt.to_timestamp()

    earliest_entry = min(df._month)
    start_year = earliest_entry.year
    start_month = earliest_entry.month

    latest_entry = max(df._month)
    end_year = latest_entry.year
    end_month = latest_entry.month

    all_months = [date(m//12, m%12+1, 1) for m in range(start_year*12+start_month-1, end_year*12+end_month)]
    num_entries = []

    for month in all_months:
        num_entries.append(len(df[df._month == month]))

    ax = plt.subplot(111)
    ax.bar(all_months, num_entries, width = 25, color = "darkorange")
    ax.xaxis_date()
    plt.title("# journal entries written, by month")

    return(plt)

def gen_wordcloud(df):

    all_words = ''
    stopwords = set(STOPWORDS)

    for note in df.note:
        val = str(val)
        tokens = val.split()

    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
        all_words += " ".join(tokens) + " "

    wordcloud = WordCloud(width = 800, height = 800, 
        background_color ='white', 
        stopwords = stopwords, 
        min_font_size = 10).generate(all_words_words)

    plt.figure(figsize = (8,8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)

    return(plt)
