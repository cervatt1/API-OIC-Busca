from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

def search_by_contabilidade(contabilidade):
    conn = sqlite3.connect('status.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, servidor, workflow, contabilidade, empresa, tipo, data, timestamp 
        FROM status 
        WHERE contabilidade = ? 
        ORDER BY timestamp DESC
    ''', (contabilidade,))
    results = cursor.fetchall()
    conn.close()
    return results

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    contabilidade = request.args.get('contabilidade')
    if contabilidade:
        results = search_by_contabilidade(contabilidade)
        return jsonify(results)
    else:
        return jsonify({"error": "Please provide a contabilidade parameter"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)
