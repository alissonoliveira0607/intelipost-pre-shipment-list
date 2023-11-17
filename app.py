from flask import Flask, request, jsonify
import uuid
import logging
import os

# Garante que o diretório de log existe
log_dir = './log/'
os.makedirs(log_dir, exist_ok=True)

# Configuração do logging
log_file = os.path.join(log_dir, 'app.log')
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route('/api/v1/pre_shipment_list', methods=['POST'])
def intelipost_endpoint():
    try:
        # Obter dados do corpo da requisição
        payload = request.get_json()

        # Log dos cabeçalhos da requisição
        logging.info("Request Headers: %s", request.headers)
        
        # Log do corpo da requisição
        logging.info("Request Body: %s", payload)

        # Exemplo de criação de hash aleatória
        hash_value = str(uuid.uuid4())

        # Construir a resposta com base nos dados da solicitação
        response = {
            "intelipost_pre_shipment_list": payload.get("intelipost_pre_shipment_list"),
            "shipper_pre_shipment_list": payload.get("shipper_pre_shipment_list"),
            "logistics_provider_shipment_list": payload.get("logistics_provider_shipment_list"),
            "shipment_list_creation_date": payload.get("shipment_list_creation_date"),
            "orders_array": [
                {
                    "order_number": order.get("order_number"),
                    "shipment_order_volume_array": [
                        {
                            "shipment_order_volume_number": volume.get("shipment_order_volume_number"),
                            "tracking_code": volume.get("tracking_code")
                        } for volume in order.get("shipment_order_volume_array", [])
                    ]
                } for order in payload.get("shipment_order_array", [])
            ],
            "status": "OK",
            "messages": [
                {
                    "type": "SUCCESS",
                    "text": "Operação realizada com sucesso.",
                    "key": "success.message"
                }
            ],
            "hash": hash_value
        }

        # Log da resposta
        logging.info("Response: %s", response)

        return jsonify(response)

    except Exception as e:
        # Em caso de erro, log do erro e retornar um código de status 400 com mensagem de erro
        logging.error("Error: %s", str(e))
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
