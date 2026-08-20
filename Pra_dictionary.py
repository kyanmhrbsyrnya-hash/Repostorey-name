####حذف و نگه داری
game_scores = {
    "Player1": 150,
    "Player2": 200,
    "Player3": 50,
    "Player4": 300
}
som=game_scores.pop("Player1")
print("امتیازهای باقی‌مانده در بازی:")
print(som)



####حذف مطلق)
phone={
"brand":"samsung",
"model":"galexy s23",
"price":2000000
}
print(phone.get("storbage","پیدا نشد !"))




####
game_scores = {
    "Player1": 150,
    "Player2": 200,
    "Player3": 50,
    "Player4": 300
}
del game_scores["player1"]
print("امتیازهای باقی‌مانده در بازی:")
print(game_scores)



####
phone={
"brand":"samsung",
"model":"galexy s23",
"price":2000000
}
phone["color"]="black"
print(phone)



####
