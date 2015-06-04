def multiplication():
    for m in range(1, 13):
        singleline = []
        for n in range(1, 13):
            singleline.append(str(n*m))
        print " ".join(singleline)

multiplication()

