# 骰子函數
def dice_fun():
    from random import choice
    dice = ["1", "2", "3", "4", "5", "6"]
    flip = []
    flip.append(choice(dice))
    return flip

# 三個六投擲函數
def six_for_three_times():
    from random import choice
    dice = [1, 2, 3, 4, 5, 6]
    flip = []
    while flip.count(6) < 3:
        flip.append(choice(dice))
    return flip, len(flip)

#print(dice_fun())

flip, cnt = six_for_three_times()
print("投擲紀錄: %s\n投擲次數: %s 次"%(flip, cnt), sep="")
