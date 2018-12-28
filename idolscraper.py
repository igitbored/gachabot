import json
import requests
import csv
from os import path

def query():
    endpoint = "http://schoolido.lu/api/cards/"
    page_num = 1

    while endpoint:
        page = []
        request = requests.get(endpoint, params = { "idol_main_unit": "μ's,Aqours" })
        request_json = json.loads(request.text)
        endpoint = request_json["next"]
        results = request_json["results"]

        for result in results:
            idol = [str(result["id"]), result["idol"]["name"], result["rarity"], 
            result["card_idolized_image"], result["card_image"]]
            
            page.append([(col or "") for col in idol])

        if page_num == 0:
            page = ["id" , "name" , "rarity", "card_idolized_image" , "card_image"] + page
        
        serialize(page)

        print("Page " + str(page_num) + " completed", end = "\r")
        page_num += 1

    print(str(page_num) + " page(s) completed!")

def serialize(arr):
    with open("idols.csv", "a", newline = "") as csvfile:
        writer = csv.writer(csvfile)

        for idol in arr:
            writer.writerow(idol)

if __name__ == "__main__":
    query()