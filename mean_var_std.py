import numpy as np

def calculate(element_list:list):
    
    if len(element_list) < 9 or len(element_list) > 9:
        raise Exception("List must contain nine numbers.") 
    
    shape = 3
    array = np.array(element_list)
    array = np.reshape(array,(shape,shape))
    
    dict = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }
    
    functions = [[],[],[],[],[],[]]
    for ax in [0,1,None]:
        for idx,f in enumerate([np.mean(array,axis=ax),np.var(array,axis=ax),np.std(array,axis=ax),np.max(array,axis=ax),np.min(array,axis=ax),np.sum(array,axis=ax)]):
            if type(f) == np.ndarray:
                functions[idx].append(list(f))
            else:
                functions[idx].append(f)
            
    for idx,results in enumerate(functions):
        dict.update({list(dict.keys())[idx]:results})
        
    return dict
    
    
print(calculate([0,1,2,3,4,5,6,7,8]))


