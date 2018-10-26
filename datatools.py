def one_hot_code(source,keywords=[]):
    new= []
    for i in keywords:
        for j in source:
            if i in j:
               new.append(i)
        
    return  new
