from flask import Flask, request, url_for
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

        return f"Message submitted: {message}"

    # Increment visit count
    r.incr('visit_count')

    message_count = r.llen('messages')
    visit_count = r.get('visit_count') or 0

    return f'''
    <!doctype html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Message Collector</title>
        <link rel="stylesheet" href="{url_for('static', filename='style.css')}">
    </head>
    <body>
        <main class="dashboard">
            <header class="dashboard-header">
                <div>
                    <p class="eyebrow">Messages</p>
                    <h1>Submit Message</h1>
                </div>
                <a class="refresh-link" href="/">Refresh</a>
            </header>

            <section class="stats-grid" aria-label="Application statistics">
                <article class="stat-card">
                    <p class="stat-label">Total Messages</p>
                    <p class="stat-value">{message_count}</p>
                </article>

                <article class="stat-card stat-card-accent">
                    <p class="stat-label">Total Visits</p>
                    <p class="stat-value">{visit_count}</p>
                </article>
            </section>

            <section style="margin-top:24px;">
                <form method="POST" class="stat-card" style="display:flex;gap:8px;align-items:center;">
                    <input type="text" name="message" style="flex:1;padding:8px;border:1px solid var(--border);border-radius:6px;">
                    <button type="submit" class="refresh-link" style="min-height:44px;">Submit</button>
                </form>
            </section>
        </main>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)