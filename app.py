from flask import Flask, redirect, abort
import json, os

app = Flask(__name__)

# 1) Leer el JSON de URLs completas
with open(os.path.join(os.path.dirname(__file__), 'tag_urls.json'), 'r') as f:
    url_map = json.load(f)

@app.route('/nfc/<tag_id>')
def nfc_redirect(tag_id):
    # 2) Buscar la URL completa para este tag
    final_url = url_map.get(tag_id)
    if not final_url:
        abort(404, description="Etiqueta NFC no registrada")
    # 3) Redirigir (HTTP 302)
    return redirect(final_url, code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
