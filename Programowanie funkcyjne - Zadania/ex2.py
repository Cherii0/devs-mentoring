
class Solution:

    def __init__(self):
        self.to_sort = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

    def get_sorted_list(self):
        self.to_sort.sort(key = lambda tup : tup[-1], reverse = False)
        return self.to_sort

    def get_sorted_list_rev(self):
        return list(sorted(self.to_sort, key = lambda tup : tup[-1], reverse=True))


def main():
    solution = Solution()
    print(f"approach 1 : {solution.get_sorted_list()}")
    print(f"approach 2 : {solution.get_sorted_list_rev()}")

if __name__ == "__main__":
    main()