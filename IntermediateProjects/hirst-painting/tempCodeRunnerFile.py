for _ in range(1, 11):
    for _ in range(9):
        hirst.dot(20)
        hirst.penup()
        hirst.forward(50)
        hirst.pendown()
        hirst.dot(20)
    hirst.penup()
    hirst.goto(0, gap)
    hirst.pendown()
    gap += 50