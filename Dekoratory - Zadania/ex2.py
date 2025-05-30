
class OuterLines:
    def __init__(self, func):
        self.func = func

    def __call__(self, *, text):
        line = "*"
        print(line * 50)
        self.func(text=text)
        print(line * 50)

def outer_lines(func):
    def inner_func(*, text):
        line = "*"
        print(line * 50)
        func(text = text)
        print(line * 50)
    return inner_func

#@outer_lines
@OuterLines
def show_text(*, text):
    print(text)


show_text(text = "Total 4 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)")
show_text(text ="remote: Resolving deltas: 100% (1/1), completed with 1 local object.")
show_text(text = "   71c4658..f83cf0c  main -> main.")
show_text(text = "remote: Resolving deltas: 100% (1/1), completed with 1 local object.")
show_text(text = r"PS C:\Users\zygmu\PycharmProjects\devs-mentoring>.")