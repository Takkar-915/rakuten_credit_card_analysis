"""
csvファイルへの処理を書く。
"""
import pandas as pd
import os
from django.http import HttpResponse
from regex import B
from credit_card.settings import BASE_DIR


def process_csv():
    csv_file = pd.read_csv(os.path.join(BASE_DIR, 'app/static/files/rakuten.csv'),encoding='UTF-8')
    df = pd.DataFrame(df)
    df_payment_per_category = df.groupby('利用店名・商品名')['支払総額'].sum().sort_values(ascending=False)
    df_payment_per_category = pd.DataFrame(df_payment_per_category)

    len = len(df_payment_per_category)
    list = []
    for i in range(1,len+1):
        list.append(i)

    df_result = df_payment_per_category.assign(総額順位=list)
    


    return df_result


def convert_csv(df):
    response = HttpResponse(content_type='text/csv; charset=UTF-8')
    response['Content-Disposition'] = 'attachment; filename="result.csv"'
    df.to_csv(path_or_buf = response, encoding = 'UTF-8', index=False)

    return response
