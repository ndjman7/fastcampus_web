def histogram(elements):
    # 0. hist 초기화
    hist = {}
    for key in elements:
        hist[key] = 0

    # 1. hist 데이터 생성
    for key in elements:
        hist[key] += 1

    # 2. 출력
    # 2-1. for문
    for key, value in hist.items():
        print("{key}{space}{histogram}".format(
            key=key,
            space=" " * (10-len(key)),
            histogram="="*value,
        ))

    # 2-2. list comprehension
    print ("\n".join([
        "{key}{space}{histogram}".format(
            key=key,
            space=" " * (10-len(key)),
            histogram="="*value,
        )
        for key, value
        in hist.items()
    ]))

    # 2-3. lambda
    print ("\n".join(
        list(map(
            lambda key : "{key}{space}{histogram}".format(
                key = key,
                space = " "*(10-len(key)),
                histogram= "="*hist[key],
            ),
            hist,
        ))
    ))


histogram(["fast","fast","campus","campus","fast","fast","school"])

