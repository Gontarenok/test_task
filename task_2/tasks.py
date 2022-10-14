import base64

import pandas

from celery import Celery

app = Celery('tasks')


@app.task
def add(excel_file_base64):
    excel_file = base64.b64decode(excel_file_base64)
    df = pandas.read_excel(excel_file)
    print("Contents of excel file:", df)
