import flask
import os

app = flask.Flask(__name__)

@app.route('/sbotify', methods=['GET, POST'])
def sbotify(m):
	print m

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 8888))
	app.run(host = '0.0.0.0', port = port, debug = True)