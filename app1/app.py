from flask import Flask, request, url_for, render_template, redirect
import redis

app = Flask(__name__)

# Connect using service name
r = redis.Redis(host='redis', port=6379, decode_responses=True)


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        message = request.form['message']

        # Store message permanently in Redis list
        r.rpush('messages', message)

        # redirect to GET to show updated counts and increment visits
        return redirect(url_for('home'))

    # Increment visit count
    r.incr('visit_count')

    message_count = r.llen('messages')
    visit_count = r.get('visit_count') or 0
    return render_template('message_collector.html', message_count=message_count, visit_count=visit_count)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)