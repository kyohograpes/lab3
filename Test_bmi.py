import Lab2.bmi as bmi
def testbmiover():
    assert(bmi.calc_bmi(1.7,90)==1)
    
def testbmiunder():
    assert(bmi.calc_bmi(3.0,20)==-1)


def testbminormal():
    assert(bmi.calc_bmi(1.5,44)==0)
  
    
