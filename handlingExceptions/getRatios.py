def getRatios(vect1, vect2):
    """Assumes vect1 and vect2 are equal length lists
    of numbers, returns a ist containing the meaningful values of 
    vect[i]1/vect2[i]"""
    ratios = []
    for index,_ in enumerate(vect1):
        try:
            ratios.append(vect1[index]/vect2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) #nan = not a number
        except:
            raise ValueError('getRatios called with bad arguments')
    return ratios
