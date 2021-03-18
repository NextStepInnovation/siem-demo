import re
import logging

from flask import Flask, request

count_re = re.compile(r'count\(\)=(?P<count>\d+\.\d+)')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.json.get('event', {}).get('message', '')
        match = count_re.search(message)
        if match:
            app.logger.error(f'Brute Force! count: {match.groupdict()["count"]}')
        else:
            print(request.json)
    return ''

