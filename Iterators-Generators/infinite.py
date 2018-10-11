# def current_beat():
#     max = 100
#     nums = (1, 2, 3, 4)
#     i = 0
#     results = []
#     while len(results) > max:
#         if i >= len(nums):
#             i = 0
#         results.append(nums[i])
#     return results


def current_beat():
    nums = (1, 2, 3, 4)
    i = 0
    while True:
        if i >= len(nums): i = 0
        yield nums[i]
        i += 1


beat = current_beat()
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))
