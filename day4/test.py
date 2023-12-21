# NOTE: this was a file used for sketching in order to refresh my recursive brain.

test = {
    1: [2, 3],
    2: [3, 4],
    3: [4],
    4: [],
}
# required number: 14

# step 1: understanding the recursive problem
# for og_id, copy_array in test.items():
#     count += 1
#     # recursion should start here
#     for item in copy_array:
#         count += 1
#         for copy_id in test[item]:
#             count +=1
#             for copy_id2 in test[copy_id]:
#                 count += 1
# print(count)

# step 2: implementing recursive way
def recursion(array, rec_count) -> int:
    for item in array:
        rec_count = recursion(test[item], rec_count + 1)
    return rec_count

if __name__ == '__main__':
    count = 0
    for og_id, copy_array in test.items():
       rec_count = recursion(copy_array, 0)
       count += rec_count
    print (count + len(test))