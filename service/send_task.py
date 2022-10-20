import pandas as pd
from service.celery_jd_category import app as jd_category


def send_data(tt, sku):
    app = jd_category
    task = {
       'sku': sku
    }
    app.send_task(f'{tt}.{tt}', [task])


if __name__ == '__main__':
    df = pd.read_excel(r'./urls.xlsx')
    sku_id = df['sku_id']
    for sku in sku_id:
        send_data('jd_category', sku)
