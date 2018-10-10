import sqlite3
import pandas as pd


timeframes = ['2005-12']

for timeframe in timeframes:
    connection = sqlite3.connect('{}.db'.format(timeframe))
    cursor = connection.cursor()
    limit = 5000
    last_unix = 0
    cur_length = limit
    counter = 0
    test_done = False
    while cur_length == limit:
        #print("kaan")
        df = pd.read_sql("SELECT * FROM parent_reply WHERE unix > {} "
                         "AND parent_id NOT NULL AND score > 0 "
                         "ORDER BY unix ASC LIMIT {}".format(last_unix, limit), connection)
        print(df)
        last_unix = df.tail(1)['unix'].values[0]
        #print(df.tail(1)['unix'].values[0])
        cur_length = len(df)
        #print(len(df))
        #print(cur_length)
        if not test_done:
            with open("test.from", 'a', encoding='utf8') as f:
                for content in df['parent'].values:
                    f.write(str(content)+"\n")
            with open("test.to", 'a', encoding='utf8') as f:
                for content in df['comment'].values:
                    f.write(str(content)+"\n")

            test_done = True
        else:
            with open("train.from", 'a', encoding='utf8') as f:
                for content in df['parent'].values:
                    f.write(str(content)+'\n')
            with open("train.to", 'a', encoding='utf8') as f:
                for content in df['comment'].values:
                    f.write(str(content)+'\n')

        counter += 1
        #print(counter)
        if counter % 20 == 0:
            print(counter*limit,'rows completed so far')

