import price_info


def test_total_cost_shopping():
    test=[]
    cost=(46.75)
    test=price_info.total_cost_shopping()
    assert(cost == test)


def test_cost_of_fruit():
    test=[]
    cost=12
    test=price_info.cost_of_fruits("apple",10)
    assert(cost ==  test)


