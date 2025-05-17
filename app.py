from flask import Flask, render_template, request
import requests
import json  # para exibir o JSON formatado

app = Flask(__name__)

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
                
               
                
                

                if data.get("fetch", {}).get("status") == "Success":
                    weights = data.get("weights", {})
                    general = data.get("general", {})
                    aircraft = data.get("aircraft", {})
                    origin = data.get("origin", {})
                    destination = data.get("destination", {})
            
                

                    flight_plan = {
                        "flight_number": general.get("flight_number", "N/A"),
                        "aircraft": aircraft.get("type", "N/A"),
                        "departure": origin.get("icao_code", "N/A"),
                        "arrival": destination.get("icao_code", "N/A"),
                        "route": general.get("route", "N/A"),
                        "flight_level": general.get("initial_altitude", "N/A"),
                        "nBLOCK FUEL": weights.get("nBLOCK FUEL", "N/A"),
                        "fuel_burn": general.get("enroute_burn", "N/A"),
                        "payload": weights.get("payload", "N/A"),
                        "cargo": weights.get("cargo", "N/A"),
                        "empty_weight": weights.get("empty_weight", "N/A"),
                        "zfw_est": weights.get("est_zfw", "N/A"),
                        "tow_est": weights.get("est_tow", "N/A"),
                        "lw_est": weights.get("est_lw", "N/A"),
                        "max_zfw": weights.get("max_zfw", "N/A"),
                        "max_tow": weights.get("max_tow", "N/A"), 
                        "max_lw": weights.get("max_lw", "N/A"),
                        "metar_departure": origin.get("metar", "N/A"),
                        "metar_arrival": destination.get("metar", "N/A"),
                        
                        
                       
        
                    }
                else:
                    error_message = "Erro ao processar os dados do plano de voo. Verifique se há um voo recente gerado."
            except Exception as e:
                error_message = f"Erro ao acessar a API: {str(e)}"

    return render_template("index.html", flight_plan=flight_plan, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
