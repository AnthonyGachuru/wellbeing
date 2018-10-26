keywords = ['4D', '2D', 'SEDAN', 'V6', 'V8', '4C',
            'FWD','RWD','2WD','4WD','AWD',
            'CAB','MINIVAN','SUV','UTILITY',
            'PICKUP','COUPE','SUV','SPORT',
            'PASSENGER','WAGON','LIMITED']
keywords1 = ['4D','2D','V6','V8']

def test_one_hot_code():
    expected = keywords1
    source = keywords
    output = one_hot_code(source,keywords1)
    if len(set(output).difference(set(expected))) == 0:
        return True
    return False, output
