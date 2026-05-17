"""
Range sum query Immutable:
    For an array, arr = [2,5,1,6,4,3,8], we are given Q queries l, r.
    2,4 = 11 1,5=19, 4,6=15

    Optimized approach:
        Prefix array : P[i]= sum(arr[0..i-1])
        Prefix array = [0, 2, 7, 8, 14, 18, 21, 29]
        P[r+1] - P[l]
        2,4 = 18-7 = 11, 1,5 = 21-2=19

Range sum query Mutable (Single Element): Segment tree.

Range sum query Mutable (Entire range): Segment tree + Lazy propagation.
"""
