for num in range(1, 21):
    if num == 4 or num == 13:
        state = "UNLOCKY!!"
    else:
        if num % 2 == 0:
            state = "even"
        else:
            state = "odd"
    print(f"{num} is {state}")
