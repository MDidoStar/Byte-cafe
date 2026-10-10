# Functions
def new_zero_list(l):
    p = []
    for u in l:
        p.append(set_zero(round(u, 2)))
    return p       
def len_num(i):
    l = []
    s = f"{i}"
    for o in s:
        l.append(s)
    return len(l)
def set_zero(n):
    if f"{int(n)}" == f"{n}":
        n = f"{n}.00 $"
    elif (len_num(int(n)) + 2) == len_num(n):
        n = f"{n}0 $"
    else:
        n = f"{n} $"
    return n
def sales_statistics(pa):
    mean = round(stat.mean(pa), 2)
    mean = set_zero(mean)
    median = round(stat.median(pa), 2)
    median = set_zero(median)
    mode = round(stat.mode(pa), 2)
    mode = set_zero(mode)
    sum_s = round(sum(pa), 2)
    sum_s = set_zero(sum_s)
    length = len(pa)
    return mean, median, mode, sum_s, length
def get_purchase(p):
    if p > 200:
        f = "Premium Purchase"
    elif p > 100:
        f = "Large Purchase" 
    elif p > 50:
        f = "Medium Purchase"
    else:
        f = "Small Purchase" 

    return f
def get_purchase_data(p):
    s = 0 
    m = 0
    l = 0
    pr = 0 
    for t in p:
        if get_purchase(t) == "Small Purchase":
            s += 1
        elif get_purchase(t) == "Medium Purchase":
            m += 1
        elif get_purchase(t) == "Large Purchase":
            l += 1
        else:
            pr += 1
    return s, m, l, pr
