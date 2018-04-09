/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

/**
 * This function is using two recrusions to find the sum
 * The time complexity is O(N^2). Runtime is 92 ms.
 * TODO: Using a hash table / map instead of two recrusions.
 * The time complexity can be improved to O(n).
 * @param  nums     [description]
 * @param  numsSize [description]
 * @param  target   [description]
 * @return          [description]
 */
int* twoSum(int* nums, int numsSize, int target) {
    int i, j;
    int* result = (int*)malloc(2 * sizeof(int));
    for ( i = 0; i < numsSize; i++)
    {
        for ( j = i + 1; j < numsSize; j++ )
        {
            if (target == nums[i] + nums[j])
            {
                result[0] = i;
                result[1] = j;
                return result;
            }
        }
    }
    return NULL;
}
