from flask import Flask, request
import redis

app = Flask(__name__)

# Connect using service name
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/', methods=['GET', 'POST'])
def home():

    # Increment visit count
    r.incr('visit_count')

    if request.method == 'POST':
        message = request.form['message']

        # Store message permanently in Redis list
        r.rpush('messages', message)

        return f"Message submitted: {message}"

    return '''
        <h1>Message Collector</h1>
        <form method="POST">
            <input type="text" name="message">
            <button type="submit">Submit</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)