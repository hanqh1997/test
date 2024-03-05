from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=BhPfyo9Ac7LbNaVdEeipto6Q&client_secret=HBHc8oKAqmKtCvgb1lo16WvaoSO3GzR7'
    response = requests.get(host)
    if response:
        access_token=response.json()['access_token']
    token = access_token
    url = 'https://aip.baidubce.com/rpc/2.0/mt/texttrans/v1?access_token=' + token
    text= request.form['text']
    q = text; # example: hello
    # For list of language codes, please refer to "https://ai.baidu.com/ai-doc/MT/4kqryjku9"
    from_lang = 'zh'; # example: en
    to_lang = 'en'; # example: zh
    term_ids = ''; #术语库id，多个逗号隔开


    # Build request
    headers = {'Content-Type': 'application/json'}
    payload = {'q': q, 'from': from_lang, 'to': to_lang, 'termIds' : term_ids}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()

    # Show response
    result = result['result']['trans_result'][0]['dst']

    return render_template('index.html', translation=result)

if __name__ == '__main__':
    app.run(debug=True)
