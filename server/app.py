from flask import Flask, jsonify, request, session, make_response

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

@app.route('/')
def index():
    return 'Welcome to the API!'

@app.route('/sessions/<string:key>', methods=['GET'])
def show_session(key):
    # Set session values if they don't already exist
    session["hello"] = session.get("hello") or "World"
    session["goodnight"] = session.get("goodnight") or "Moon"

    # Create a response with session and cookie information
    response = make_response(jsonify({
        'session': {
            'session_key': key,
            'session_value': session[key],
            'session_accessed': session.accessed,
        },
        'cookies': [{cookie: request.cookies[cookie]}
            for cookie in request.cookies],
    }), 200)

    # Set a new cookie
    response.set_cookie('mouse', 'Cookie')

    return response

if __name__ == '__main__':
    app.run(debug=True, port=5555)
