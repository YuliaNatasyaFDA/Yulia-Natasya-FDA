from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "<p>Nama : Yulia Natasya Farah Diba Arifin</p><p>Tempat, tanggal lahir : Sampang, 09 Juli 2004</p><p>Alamat : Jln. Raya Krampon Barat</p><p>Jenis Kelamin : Perempuan</p><p>Umur : 19 tahun</p>"


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
