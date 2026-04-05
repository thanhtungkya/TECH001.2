import requests

def lay_thoi_tiet():
    thanh_pho = input("Nhap ten thanh pho: ")
    api_key = "3bbd7269c48517eeffb27a0e8fc40c8f"
    
    duong_dan = f"https://api.openweathermap.org/data/2.5/weather?q={thanh_pho}&appid={api_key}&units=metric"
    
    try:
        phan_hoi = requests.get(duong_dan)
        du_lieu = phan_hoi.json()
        
        mo_ta = du_lieu["weather"][0]["description"]
        nhiet_do_K = du_lieu["main"]["temp"]
        
        print(mo_ta)
        print(nhiet_do_K)
        print(f"nhiet do C: {nhiet_do_K - 273}")
        
    except :
        print("Loi")


lay_thoi_tiet()