import random


def random_access(nums):
    """Randomly access element"""
    random_index = random.randint(0, len(nums) - 1)
    return random_index


def extend(nums, e):
    """
    Ensuring the availability of memory space after an array for safe capacity 
    extension becomes challenging. Consequently, in most programming languages 
    the length of an array is immutable.
    To expand an array it's necessary to create a larger array and then copy
    the elements from the original array. Time: O(n)
    In python lists are dynamic but I will treat it as static arr.
    """
    res = [0] * (len(nums) + e)  # e is how much to extend the arr
    for i in range(len(nums)):
        res[i] = nums[i]
    return res


def insert(nums, element, index):
    """
    Array elements are tightly packed in memory, with no space to accomodate
    additional data between them. Elements need to be shifter to create room,
    unavoidably losing the last emenet due to the fixed size. One solution 
    widely implemented is resizing the array with larger capacity, copy elements
    add new element to array and replace references. (I know in python lists
    are dynamic). Time: O(n)
    """
    for i in range(len(nums) - 1, index, -1):
        nums[i] = nums[i-1]

    nums[index] = element
    # this is how you insert, to remove we shift elements to the left again


def traverse(nums):
    """Different ways to traverse a num (in python)"""
    for i in range(len(nums)):
        print(nums[i])

    for num in nums:
        print(num)

    for i, num in enumerate(nums):
        print(f"i = {i}\n n={num}")


if __name__ == "__main__":
    arr = [1, 3, 2, 5, 4]
    print(f"Arr = {arr}")

    # Random access an element, retrieval is constant since - contiguous mem
    i = random_access(arr)
    print(f"Randomly retrieved in nums: {arr[i]}")

    # extend arr
    arr = extend(arr, 5)
    print(f"Array has been extending by 5 {arr}")

    arr[-1] = 2
    print(f"adding 3 at index 0 arr = {arr}")
    insert(arr, 3, 0)
    print(f"added 3 at index 0 arr = {arr}")

    traverse(arr)
