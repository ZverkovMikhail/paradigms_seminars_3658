import sys


def sort_list_imperative(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    return nums


def sort_list_declarative(nums):
    return sorted(nums, reverse=True)


if __name__ == '__main__':
    nums = [2, 3, 6, 7, 9, 12, 34, 1, 8, 42]
    print(sort_list_imperative(nums))
    print(sort_list_declarative(nums))
