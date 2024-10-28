from taylornet1 import RM
# from taylornet2 import TaylorLinearNet as TaylorNetShare
from taylornet2 import RMplus


def getRM(no_share=True,inputsize=None,outputsize=None,d=None):
    return RM(inputsize, outputsize, d) if no_share else RMplus(inputsize,outputsize,d)

