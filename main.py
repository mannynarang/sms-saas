from flask import Flask, request, json

app = Flask(__name__)


@app.route('/githubIssue', methods=['POST'])
def githubIssue():
    data = request.json
    print(f'Issue {data["issue"]["title"]} {data["action"]}')
    print(f'{data["issue"]["body"]}')
    print(f'{data["issue"]["url"]}')
    return data


@app.route('/webflow', methods=['POST'])
def webflow():
    data = request.json
    print(data)
    # print(f'Issue {data["issue"]["title"]} {data["action"]}')
    # print(f'{data["issue"]["body"]}')
    # print(f'{data["issue"]["url"]}')
    return data


@app.route('/')
def hello():
    return 'Webhooks with Python'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
