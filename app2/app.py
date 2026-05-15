from flask import Flask, render_template
import redis

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def dashboard():

    message_count = r.llen('messages')
    visit_count = r.get('visit_count') or 0

    return render_template(
        'dashboard.html',
        message_count=message_count,
        visit_count=visit_count
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
