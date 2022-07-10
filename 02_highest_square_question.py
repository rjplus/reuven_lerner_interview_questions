def highest_square_under(max_num):

    if max_num <= 0:
        return 0

    highest_square = 0

    for i in range(max_num):
        square = i ** 2
        if square > max_num:
            break
        highest_square = square

    return i, highest_square

highest_square_under(500)
