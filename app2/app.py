from flask import Flask
import redis

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def dashboard():

    message_count = r.llen('messages')
    visit_count = r.get('visit_count')

    if visit_count is None:
        visit_count = 0

    return f"""
        <h1>Dashboard</h1>
        <p>Total Messages: {message_count}</p>
        <p>Total Visits: {visit_count}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)