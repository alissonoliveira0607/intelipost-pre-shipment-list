# Mock server PLP

Este projeto tem como objetivo mapear um endpoint que receberá um POST com dados de PLP - Pré lista de postagem.

## Configuração do Ambiente

### Requisitos

- Python 3.x
- Docker
- Docker Compose

### Configuração Local

```bash
git clone https://github.com/seu-usuario/minha-aplicacao.git
cd minha-aplicacao
python -m venv venv
source venv/bin/activate  # no Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Construindo e Executando com Docker Compose
### Requisitos
- Docker
- Docker Compose

```bash	
git clone https://github.com/alissonoliveira0607/intelipost-pre-shipment-list.git
cd minha-aplicacao

# Construindo a imagem Docker
docker build -t label/image:tag .
```

### Alterar o arquivo docker-compose.yaml:
```yaml

version: '3'

services:
  minha-aplicacao:
    image: label/image:tag  # Imagem construída
    ports:
      - "80:5000"
    volumes:
      - ./log:/app/log  # Mapeia a pasta de logs do container para ./logs na máquina local

```

### Rodando a aplicação:
```bash
docker-compose up -d
```

### Outra opção seria utilizar o seguinte compose que já constrói a imagem a partir do Dockerfile:

```yaml

version: '3'

services:
  minha-aplicacao:
    build:
      context: .
      dockerfile: Dockerfile
      args:
        - TAG=qa
    ports:
      - "80:5000"  # Mapeia a porta 80 do host para a 5000 do container - aplicação
    volumes:
      - ./log:/app/log  # Mapeia a pasta de logs do container para ./logs na máquina local

```

```bash
docker-compose up -d
```
### Endpoint:

- http://localhost/api/v1/pre_shipment_list

### Requisição API:
Body da Requisição:
```json
{
  "intelipost_pre_shipment_list": 2970,
  "origin_name": "CD_SP",
  "origin_federal_tax_payer_id": "XXXXXXXXXXXXXX",
  "origin_state_tax_payer_id": "cc",
  "origin_customer_phone": "XXXXXXXXXX",
  "origin_customer_email": "cd@cd.com",
  "origin_street": "amancio de carvalho",
  "origin_number": 182,
  "origin_additional": "ssss",
  "origin_reference": "ABCD",
  "origin_zip_code": "04012090",
  "origin_city": "São Paulo",
  "origin_quarter": "Vila Mariana",
  "origin_state_code": "SP",
  "shipment_order_array": [
    {
      "order_number": "9613344",
      "sales_channel": "MEU_CANAL_DE_VENDAS",
      "sales_order_number": "9613344",
      "scheduled": false,
      "scheduling_window_start": null,
      "scheduling_window_end": null,
      "shipment_order_type": "NORMAL",
      "shipment_order_sub_type": null,
      "delivery_method_id": 18,
      "logistic_provider_id": 9,
      "payment_type": "CIF",
      "end_customer": {
        "first_name": "PRIMEIRONOME",
        "last_name": "SOBRENOME",
        "phone": "XXXXXXXXXX",
        "is_company": false,
        "federal_tax_payer_id": "XXXXXXXXXXXX",
        "shipping_address": "RUA X",
        "shipping_number": "50",
        "shipping_quarter": "PETROPOLIS",
        "shipping_city": "NATAL",
        "shipping_zip_code": "59012-310",
        "shipping_state": "RN",
        "shipping_state_code": "RN",
        "shipping_country": "BRASIL",
        "shipping_additional": "AP 101",
        "shipping_reference": "PROXIMO AO MERCADO"
      },
      "shipment_order_volume_array": [
        {
          "shipment_order_volume_number": "467778",
          "weight": 1.646,
          "volume_type_code": "BOX",
          "width": 29,
          "height": 15,
          "length": 38,
          "products_nature": "30043290",
          "products_quantity": 41,
          "is_icms_exempt": false,
          "tracking_code": "SEP7231564",
          "shipment_order_volume_invoice_array": [
            {
              "invoice_series": "1",
              "invoice_number": "12345",
              "invoice_key": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
              "invoice_date": 1498767939000,
              "invoice_date_iso": "2017-06-29T17:25:39.000-03:00",
              "invoice_total_value": 1874.33,
              "invoice_products_value": 1874.33,
              "already_insured": true
            }
          ]
        },
        {
          "shipment_order_volume_number": "888472",
          "weight": 12.5,
          "volume_type_code": "BOX",
          "width": 30,
          "height": 10,
          "length": 15,
          "products_nature": "30043290",
          "products_quantity": 1,
          "is_icms_exempt": false,
          "tracking_code": "SEP7231565",
          "shipment_order_volume_invoice_array": [
            {
              "invoice_series": "1",
              "invoice_number": "123457",
              "invoice_key": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
              "invoice_date": 1498767939000,
              "invoice_date_iso": "2017-06-29T17:25:39.000-03:00",
              "invoice_total_value": 1414.33,
              "invoice_products_value": 1414.33,
              "already_insured": true
            }
          ]
        }
      ]
    }
  ]
}

```

### Para parar a execução, pressione Ctrl+C e execute:
```bash
docker-compose down
```