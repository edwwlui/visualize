import pandas as pd
import matplotlib.pyplot as plt
import sys

def main(argv1):
    name=argv1
    #single col of values

    data=pd.read_csv(name,header=None)
    #data.plot(kind='hist',range=[0,40],bins=20)
    data.plot(kind='hist')
    #plt.xlabel('Length')
    plt.title(name,fontsize=15)
    plt.show()
    #fig = plt.figure(figsize=(4,3))
    #fig.savefig(name+'.png', dpi = 300)

if __name__=='__main__':
    main(sys.argv[1])
