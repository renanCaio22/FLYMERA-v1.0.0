from flask import Flask, render_template, request
from random import random
import requests
import json
import re  # Importe a biblioteca de expressões regulares

app = Flask(__name__)
app.jinja_env.globals['random'] = random

@app.route('/', methods=['GET', 'POST'])
def index():
    flight_plan = None
    error_message = None

    if request.method == 'POST':
        pilot_id = request.form.get('pilot_id')
        if pilot_id:
            url = f"https://www.simbrief.com/api/xml.fetcher.php?userid={pilot_id}&json=1"
            try:
                response = requests.get(url)
                data = response.json()

                # ✅ Print do JSON completo no terminal
                print(json.dumps(data, indent=4))

                if data.get("fetch", {}).get("status") == "Success":
                    weights = data.get("weights", {})
                    general = data.get("general", {})
                    aircraft = data.get("aircraft", {})
                    origin = data.get("origin", {})
                    destination = data.get("destination", {})
                    text_data = data.get("text", {})
                    plan_html = text_data.get("plan_html", "")
                    alternate_data = {} # <-- Correção: inicialize aqui

                    # Use regex para encontrar a linha que contém "ALTN" seguido pelo código do aeroporto
                    altn_match = re.search(r"ALTN\s+([A-Z]{4})", plan_html)
                    alternate_airport = altn_match.group(1) if altn_match else "N/A"

                    # Use regex para encontrar a linha que contém "BLOCK FUEL" e extrair o valor
                    block_fuel_match = re.search(r"BLOCK FUEL\s+\w+\s+(\d+)", plan_html)
                    block_fuel = block_fuel_match.group(1) if block_fuel_match else "N/A"

                    # ✅ Imprima os valores extraídos para depuração
                    print(f"Aeroporto Alternativo (ALTN) extraído: {alternate_airport}")
                    print(f"Valor de block_fuel extraído: {block_fuel}")
                    print("Conteúdo do dicionário 'general':", general)
                    print("Conteúdo do dicionário 'weights':", weights)
                    print(f"Valor de plan_html: {data.get('text', {}).get('plan_html', '')}")
                    print(f"Pista do alternado: {alternate_data.get('plan_rwy', 'N/A')}")

                    

                    flight_plan = {
                        "flight_number": general.get("flight_number", "N/A"),
                        "aircraft": aircraft.get("icao_code", "N/A"),
                        "plan_rwy": origin.get("plan_rwy", "N/A"),
                        "plan_rwy_landing": destination.get("plan_rwy", "N/A"),
                        "plan_rwy_alternate": alternate_data.get("plan_rwy", "N/A"),
                        "departure": origin.get("icao_code", "N/A"),
                        "arrival": destination.get("icao_code", "N/A"),
                        "alternate": alternate_airport,  # ✅ Adicionando o aeroporto alternativo
                        "route": general.get("route", "N/A"),
                        "flight_level": general.get("initial_altitude", "N/A"),
                        "block_fuel": block_fuel,
                        "fuel_burn": general.get("total_burn", "N/A"),
                        "payload": weights.get("payload", "N/A"),
                        "cargo": weights.get("cargo", "N/A"),
                        "empty_weight": weights.get("oew", "N/A"),
                        "zfw_est": weights.get("est_zfw", "N/A"),
                        "tow_est": weights.get("est_tow", "N/A"),
                        "lw_est": weights.get("est_ldw", "N/A"),
                        "max_zfw": weights.get("max_zfw", "N/A"),
                        "max_tow": weights.get("max_tow", "N/A"),
                        "max_ldw": weights.get("max_ldw", "N/A"),  # Chave CORRIGIDA para Máx LW
                        "CI": general.get("costindex", "N/A"),  # Adicionando o Cost Index
                        "pax": general.get("passengers", "N/A"),
                        "metar_departure": origin.get("metar", "N/A"),
                        "metar_arrival": destination.get("metar", "N/A"),
                    }

                else:
                    error_message = "Erro ao processar os dados do plano de voo. Verifique se há um voo recente gerado."
            except Exception as e:
                error_message = f"Erro ao acessar a API: {str(e)}"

    return render_template("index.html", flight_plan=flight_plan, error_message=error_message) #se conecta com o html

if __name__ == '__main__':
    app.run(debug=True)