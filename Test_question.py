
quiz_questions = []
quantity = int(input('لطفا تعداد سوالات آزمون رو وارد کنید: '))

for i in range(quantity):
    print(f"\n--- طراحی سوال شماره {i+1} ---")
    
    question_text = input('سوال را وارد کنید: ')
    opt1 = input('گزینه ۱ را وارد کنید: ')
    opt2 = input('گزینه ۲ را وارد کنید: ')
    opt3 = input('گزینه ۳ را وارد کنید: ')
    opt4 = input('گزینه ۴ را وارد کنید: ')
    correct_answer = input('شماره گزینه درست کدام است؟ (۱ تا ۴
    new_question = {
        "question": question_text,
        "options": [opt1, opt2, opt3, opt4],
        "answer": correct_answer
    }
    quiz_questions.append(new_question)

print("\n--- آزمون شما با موفقیت ذخیره شد! ---")
print(quiz_questions)
