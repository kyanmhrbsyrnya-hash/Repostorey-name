player_score={
}
while True:
    player=input('نام بازیکن را وارد کنید')
    score=int(input('لطفاامتیاز را وارد کنید'))
    player_score[player]=score
    print(player_score)
    if(player=='end'):
        break
    elif(player=='erase'):
       player_score.clear()
