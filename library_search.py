library = [
    {"title": "python crash course", "status": "available"},
    {"title": "harry potter", "status": "borrowed"}
]

user_choice = input("کدام کتاب را می‌خواهید؟ ").lower()

found = False
for book in library:
    if book["title"] == user_choice:
        found = True
        if book["status"] == "borrowed":
            print("متأسفم، این کتاب در حال حاضر امانت داده شده است.")
        else:
            print("بله، این کتاب موجود است. می‌توانید آن را بردارید.")
        break

if not found:
    print("این کتاب در کتابخانه ما وجود ندارد.")
  
