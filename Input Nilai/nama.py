from flask import Flask, render_template, request, send_file
import pandas as pd
import io

app = Flask(__name__)

data = {
    "Kelas": [],
    "Mata Pelajaran": [],
    "Nama Siswa": [],
    "Nilai": []
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    kelas = request.form['kelas']
    mata_pelajaran = request.form['mata_pelajaran']
    nama_siswa = request.form['nama_siswa']
    nilai = request.form['nilai']

    data['Kelas'].append(kelas)
    data['Mata Pelajaran'].append(mata_pelajaran)
    data['Nama Siswa'].append(nama_siswa)
    data['Nilai'].append(nilai)

    return "Data berhasil disimpan! <a href='/'>Kembali</a>"

@app.route('/download')
def download():
    df = pd.DataFrame(data)
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Nilai')
    output.seek(0)

    return send_file(output, as_attachment=True, download_name='nilai.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

if __name__ == '__main__':
    app.run(debug=True)

# Create a folder named 'templates' and add the following file as 'index.html'
# index.html content:
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Input Nilai</title>
# </head>
# <body>
#     <h1>Input Data Nilai</h1>
#     <form action="/submit" method="post">
#         <label for="kelas">Kelas:</label><br>
#         <input type="text" id="kelas" name="kelas" required><br><br>
#         
#         <label for="mata_pelajaran">Mata Pelajaran:</label><br>
#         <input type="text" id="mata_pelajaran" name="mata_pelajaran" required><br><br>
#         
#         <label for="nama_siswa">Nama Siswa:</label><br>
#         <input type="text" id="nama_siswa" name="nama_siswa" required><br><br>
#         
#         <label for="nilai">Nilai:</label><br>
#         <input type="number" id="nilai" name="nilai" required><br><br>
#         
#         <button type="submit">Submit</button>
#     </form>
#     <br>
#     <a href="/download">Download Data Nilai</a>
# </body>
# </html>
