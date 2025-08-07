import string
import random
import sqlite3
from flask import Flask, request, redirect, render_template, flash, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'

DB = 'urls.db'

# Initialize DB
def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS urls (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            slug TEXT UNIQUE,
                            original_url TEXT NOT NULL
                        );''')

# Generate random slug
def generate_slug(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

# Check if slug exists
def slug_exists(slug):
    with sqlite3.connect(DB) as conn:
        result = conn.execute("SELECT 1 FROM urls WHERE slug = ?", (slug,)).fetchone()
        return result is not None

# Create a new shortened URL entry
def create_short_url(slug, original_url):
    with sqlite3.connect(DB) as conn:
        conn.execute("INSERT INTO urls (slug, original_url) VALUES (?, ?)", (slug, original_url))

# Retrieve original URL
def get_original_url(slug):
    with sqlite3.connect(DB) as conn:
        result = conn.execute("SELECT original_url FROM urls WHERE slug = ?", (slug,)).fetchone()
        return result[0] if result else None

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None

    if request.method == 'POST':
        long_url = request.form.get('long_url')
        title = request.form.get('title')  # Currently unused
        custom_slug = request.form.get('custom_slug')

        if not long_url or not long_url.startswith(('http://', 'https://')):
            flash("Please enter a valid URL (include http:// or https://).")
            return redirect(url_for('index'))

        if custom_slug:
            if slug_exists(custom_slug):
                flash("This custom link is already taken.")
                return redirect(url_for('index'))
            slug = custom_slug
        else:
            slug = generate_slug()
            while slug_exists(slug):
                slug = generate_slug()

        create_short_url(slug, long_url)
        short_url = request.host_url + slug

    return render_template('index.html', short_url=short_url)

@app.route('/<slug>')
def redirect_to_original(slug):
    original_url = get_original_url(slug)
    if original_url:
        return redirect(original_url)
    else:
        return "Invalid short URL.", 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
