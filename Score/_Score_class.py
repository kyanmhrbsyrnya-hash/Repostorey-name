scores_class={
}
choice=input('شروع کنید')
while(choice!='exite'):
    choice1=input('لطفا چه میخواهید،show/Add/serch/erase/exite')
    if(choice1=='Add'):
        name=input('نام رو وارد کنید')
        score=int(input('نمره را وارد کنید'))
        scores_class["name":"score"]=name,score
    elif(choice=='show'):
        print(scores_class)
    elif(choice=='serch'):
        name1=input('serch')
        scores_class.get(name1,'یافت نشد')
    elif(choice=='erase'):
         score_class.clear()
