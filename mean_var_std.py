import numpy as np

def calculate(lst):
    if type(lst) is not list:
        raise TypeError("Input must be of list type.")
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    three_by_three = lambda x: [[x[0],x[1],x[2]],[x[3],x[4],x[5]],[x[6],x[7],x[8]]]
    data_arr = np.array(three_by_three(lst))
    print(data_arr)
    
    def apply_throughout(func):
        return ([np.apply_along_axis(func,0,data_arr).tolist(),np.apply_along_axis(func,1,data_arr).tolist(),np.apply_along_axis(func,0,lst).tolist()])

    mean = apply_throughout(np.mean)
    var = apply_throughout(np.var)
    sd = apply_throughout(np.std)
    highest = apply_throughout(np.amax)
    lowest = apply_throughout(np.amin)
    total = apply_throughout(np.sum)
    calculations = {
        'mean': mean,
        'variance': var,
        'standard deviation': sd,
        'max': highest,
        'min': lowest,
        'sum': total
    }

    
    return calculations
