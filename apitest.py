import requests

url = "http://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

def test_verify_status_code_200():
    esperado = 200
    actual = response.status_code
    assert esperado == actual, f"FAIL: actual:{actual}, esperado:{esperado}"

def test_verify_name():
    esperado = "margarita"
    json_respuesta = response.json()
    actual = json_respuesta["drinks"][0]["strDrink"].lower() 
    assert esperado == actual, f"FAIL: actual:{actual}, esperado:{esperado}"
    
def test_verify_ingredient_tequila():
    esperado = "Tequila"
    actual = response.json()["drinks"][0]["strIngredient1"]  # Asegúrate de que este índice sea correcto
    assert esperado == actual, f"FAIL: actual:{actual}, esperado:{esperado}"



print(response.text)