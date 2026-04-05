import requests

def lay_truyen_cuoi():
    duong_dan = "https://api.chucknorris.io/jokes/random"
    
    try:
        phan_hoi = requests.get(duong_dan)
        phan_hoi.raise_for_status()
        
        du_lieu = phan_hoi.json()
        print(du_lieu["value"])
        
    except requests.exceptions.RequestException:
        print("Loi")

    
lay_truyen_cuoi()