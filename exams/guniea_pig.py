def check_pig_happiness():
    food = float(input())
    hay = float(input())
    cover = float(input())
    weight = float(input())

    for day in range(1, 31):

        food -= 0.3

        if day % 2 == 0:
            hay -= food * 0.05

        if day % 3 == 0:
            cover -= 1 / 3 * weight

        if round(food, 2) <= 0 or round(hay, 2) <= 0 or round(cover, 2) <= 0:
            print(f'Merry must go to the pet store!')
            break
    else:
        print(f'Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.')


check_pig_happiness()

