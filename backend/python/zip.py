import zipfile
with zipfile.ZipFile('task.zip', 'w') as zip:
     zip.write('task_1.py')