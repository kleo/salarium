#!/usr/bin/env python
import requests
import json
import datetime
import holidays
from fake_useragent import UserAgent

email_address = '<email>'
password = '<password>'

ua = UserAgent()

ph_holidays = holidays.PH()

if datetime.datetime.today() in ph_holidays:
  print('Today is a holiday', ph_holidays.get(datetime.datetime.today().isoformat()), datetime.datetime.today().strftime('%a, %b %d, %Y'), 'at', datetime.datetime.today().strftime('%X'))
else:
  headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://app.salarium.com',
    'Referer': 'https://app.salarium.com/users/login',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': ua.chrome,
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="104", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
  }

  data = {
      'email': email_address,
      'password': password
  }

  login = requests.post('https://app.salarium.com/users/login', headers=headers, data=data)

  data2 = {
      'email': email_address,
      'password': password,
      'log_type': 'TIME OUT'
  }

  time_out = requests.post('https://app.salarium.com/employees/ebundy_clock', headers=headers, cookies=login.cookies, data=data2)

  time = json.loads(time_out.content)
  print(time['message'])