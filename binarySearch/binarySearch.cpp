//
//  binarySearch.cpp
//  letcode
//
//  Created by haizhi on 2017/12/3.
//  Copyright © 2017年 haizhihaizhihaizhi. All rights reserved.
//

#include "binarySearch.hpp"
#include <iostream>

int binarySearch::binarySearch_recursive(int* a, int left, int right, int target){

    if (!a) return -1;
    if (left>right) return -1;
    int mid = left+((right-left)>>1);
    if (a[mid]>target)
        return binarySearch_recursive(a, left, mid-1, target);
    else if (a[mid]<target)
        return binarySearch_recursive(a, mid+1, right, target);
    else
        return mid;
}

int binarySearch::binarySearch_nonrecursive(int* a, int lef, int rig, int target){
    if (!a) return -1;
    int left = lef;
    int right = rig;
        while(left<=right){
            int mid = left + ((right-left)>>1);
            if (a[mid]>target)
                right = mid-1;
            else if (a[mid]<target)
                left = mid+1;
            else
                return mid;
    }
    
    return -1;
}