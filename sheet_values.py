import pandas as pd
import statistics

df = pd.read_excel('./Okko. Июнь-август.xlsx')


# Add subscribers count to list.
def subscribers_count():
    col_subscribers_list = df['Подписчиков'].to_list()
    return col_subscribers_list[len(col_subscribers_list)-2]


# Add likes count to list and calculating the average.
def likes_mean():
    col_likes_list = df['Unnamed: 7'].to_list()
    col_likes_list = col_likes_list[1:len(col_likes_list)-1]
    likes_average = round(statistics.fmean(col_likes_list))
    return likes_average


# Add comments count to list and calculating the average.
def comments_mean():
    col_comments_list = df['Unnamed: 8'].to_list()
    col_comments_list = col_comments_list[1:len(col_comments_list)-1]
    comments_average = round(statistics.fmean(col_comments_list))
    return comments_average


# Add reposts count to list and calculating the average.
def reposts_mean():
    col_reposts_list = df['Unnamed: 9'].to_list()
    col_reposts_list = col_reposts_list[1:len(col_reposts_list)-1]
    reposts_average = round(statistics.fmean(col_reposts_list))
    return reposts_average


# Create a list for means of key values.
def means_list():
    means = []

    like_mean = likes_mean()
    comment_mean = comments_mean()
    repost_mean = reposts_mean()

    means.append(like_mean)
    means.append(comment_mean)
    means.append(repost_mean)

    return means
