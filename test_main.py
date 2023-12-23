from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def testmainApp_shouldHaveCorrectResponds_fromRussianToEndlish():
    responseGreetings = client.get("/translate?textToTranslate=Доброго времени суток!")
    responseGoodby = client.get("/translate?textToTranslate=Всего хорошего!")

    assert responseGoodby.status_code == 200
    assert responseGoodby.status_code == 200

    assert responseGreetings.text == '"Good times of the day!"'
    assert responseGoodby.text == '"Have a good day!"'
