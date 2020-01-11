# def reverse(data):
#     for index in range(len(data) - 1, -1, -1):
#         result = yield data[index]
#         print(result)
#
#
# print(''.join(reverse("hello")))


# def gen():
#     num = -1
#     while True:
#         result = yield num + 1
#         num += 1
#         print(result)


def echo(value=None):
    print("Execution starts when 'next()' is called for the first time.")
    try:
        while True:
            try:
                value = yield value
                # print(value)
            except Exception as e:
                value = e
                # print("exception:", value)
    finally:
        print("Don't forget to clean up when 'close()' is called.")


gen = echo(1)
print(next(gen))
print(next(gen))
gen.throw(TypeError, 'spam')
gen.close()
