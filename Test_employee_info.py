import employee_info


def test_get_employee_age ():
    result=[]
    ageL=24
    ageH=30
    expected=[{'name':'Jane','age':25,'department':'Marketing','salary':60000}]
    result=employee_info.get_employees_by_age_range(ageL,ageH)
    assert(expected == result)


def test_calc_avg():
    result=employee_info.calculate_average_salary()
    expected=60166.666666666664
    assert('Average salary = ',expected == result)

def test_get_employee_dept():
    dept='Sales'
    expected=[{'name':'John','age':30,'department':'Sales','salary':50000},{'name':'Peter','age':40,'department':'Sales','salary':60000}]
    result=employee_info.get_employees_by_dept(dept)
    assert(expected==result)

    
    


    