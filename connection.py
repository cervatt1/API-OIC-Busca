import requests
import sqlite3
import time

# Função para criar o banco de dados e a tabela
def create_db():
    conn = sqlite3.connect('status.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS status (
            id TEXT,
            servidor TEXT,
            workflow TEXT,
            contabilidade TEXT,
            empresa TEXT,
            tipo TEXT,
            data TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id, timestamp)
        )
    ''')
    conn.commit()
    conn.close()

# Função para obter o status da API
def get_status():
    response = requests.get("https://api-status-server.herokuapp.com/status")
    if response.status_code == 200:
        return response.json()
    return None

# Função para salvar o status no banco de dados
def save_status(data):
    conn = sqlite3.connect('status.db')
    cursor = conn.cursor()

    for server_key, status_list in data.items():
        for status in status_list:
            cursor.execute('''
                INSERT INTO status (id, servidor, workflow, contabilidade, empresa, tipo, data) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (status['id'], status['servidor'], status['workflow'], status['contabilidade'], 
                  status['empresa'], status['tipo'], status['data']))

            # Limitar a 5 últimas entradas por id
            cursor.execute('''
                DELETE FROM status
                WHERE id = ?
                AND timestamp NOT IN (
                    SELECT timestamp
                    FROM status
                    WHERE id = ?
                    ORDER BY timestamp DESC
                    LIMIT 5
                )
            ''', (status['id'], status['id']))

    conn.commit()
    conn.close()

# Função para verificar se o status é diferente do que está no banco de dados
def is_status_different(data):
    conn = sqlite3.connect('status.db')
    cursor = conn.cursor()
    different_status = []

    for server_key, status_list in data.items():
        for status in status_list:
            cursor.execute('''
                SELECT empresa FROM status 
                WHERE id = ? 
                ORDER BY timestamp DESC 
                LIMIT 1
            ''', (status['id'],))
            db_status = cursor.fetchone()
            if db_status:
                if db_status[0] != status['empresa']:
                    different_status.append(status)
            else:
                different_status.append(status)

    conn.close()
    return different_status

# Função para buscar informações pelo campo "contabilidade"
def search_by_contabilidade(contabilidade):
    conn = sqlite3.connect('status.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM status WHERE contabilidade = ? ORDER BY timestamp DESC
    ''', (contabilidade,))
    results = cursor.fetchall()
    conn.close()
    return results

# Função principal para executar o loop de verificação e salvamento
def main():
    create_db()
    while True:
        status_data = get_status()
        if status_data:
            different_status = is_status_different(status_data)
            if different_status:
                save_status({key: [status for status in value if status in different_status] for key, value in status_data.items()})
        time.sleep(15)

if __name__ == '__main__':
    main()