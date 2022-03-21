import pandas as pd
from datetime import datetime
"""القراءة من excel بشرط وبدون شرط"""

Machine_date = datetime.today().strftime('%d-%m')

df = pd.read_excel('Salah-Calendar2.xlsx', sheet_name='Table 1', usecols='A:L')
# اول براميتر تضع اسم الملف
# sheet_name اسم ورقة العمل
# useclos يعني من اي عامود الى اي عامود
for row in range(len(df)):
    print(df.loc[row]['Date'].strftime('%m-%d'))
    print(df.loc[row]['Fajr'])
    print(df.loc[row]['Fajr Iqama'].strftime('%I:%M'))
    print(df.loc[row]['Sunrise'])
    print(df.loc[row]['Zuhr'])
    print(df.loc[row]['Zuhr Iqama'].strftime('%I:%M'))

# الان سنضع شرط يجلب البيانات حسب تاريخ الحالي و تاريخ الموجود في الملف
print('____________________________________________')
for row in range(len(df)):
    if df.loc[row]['Date'].strftime('%d-%m') == Machine_date:
        print(df.loc[row]['Date'].strftime('%m-%d'))
        print(df.loc[row]['Fajr'])
        print(df.loc[row]['Fajr Iqama'].strftime('%I:%M'))
        print(df.loc[row]['Sunrise'])
        print(df.loc[row]['Zuhr'])
        print(df.loc[row]['Zuhr Iqama'].strftime('%I:%M'))
