from flask import Flask, render_template, request
import qrcode
from io import BytesIO
from base64 import b64encode

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')
	
@app.route('/', methods=['POST'])
def gen_qr():
	memory = BytesIO()
	data = request.form.get('link')
	img = qrcode.make(data)
	img.save(memory)
	memory.seek(0)
	
	base64 = 'data:image/png;base64,' +b64encode(memory.getvalue()).decode('ascii')
	
	return render_template('index.html', data=base64)


if __name__ == '__main__':
	app.run(debug=True)