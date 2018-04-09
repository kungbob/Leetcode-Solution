/* This question ask to find an maximum subarray which contain at least
** one number. It causes small difference with tradiontal maximum continous
** subsequence problem.
*/

int maxSubArray(int* nums, int numsSize) {
    int current_sum, max_sum, i;

    current_sum = 0;
    max_sum = nums[0];

    for( i = 0; i < numsSize; i++)
    {
        current_sum += nums[i];

        if (current_sum > max_sum)
            max_sum = current_sum;
        if (current_sum < 0)
            current_sum = 0;
    }
    return max_sum;
}
