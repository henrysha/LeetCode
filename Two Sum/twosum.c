/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int i, j;
    for (i = 0; i < numsSize; i++){
        for (j = 1; j < numsSize; j++){
            if (i == j){
                continue;
            }
            if (nums[i]+nums[j] == target){
                int* ret = malloc(2*sizeof(int));
                ret[0] = i;
                ret[1] = j;
                return ret;
            }
        }
    }
    return NULL;
}