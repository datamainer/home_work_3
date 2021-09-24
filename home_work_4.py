def generator():
    src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    # result = [12, 44, 4, 10, 78, 123]

    for src_index in range(1, len(src)):
        if src[src_index] > src[src_index - 1]:
            yield src[src_index]

    return


for result in generator():
    print(result)


