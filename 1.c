#include <stdio.h>
#include <stdlib.h>

// 1. Two Sum

int* twoSum(int* nums, int numsSize, int target)
{
    int *result;
    result = malloc(sizeof(int) * 2);

    int i, j;

    for (i = 0; i < numsSize; i++)
    	for (j = 0; j < numsSize && j != i; j++)
    		if ((nums[i] + nums[j]) == target)
    			goto done; // cuz easier to break from 2 loops
    
    done:
    	if (i < j)
    	{
    		result[0] = i;
    		result[1] = j;
    	}

    	else
    	{
    		result[0] = j;
    		result[1] = i;
    	}

    return result;
}

int main()
{
	int nums[4] = {3, 2, 4};
	int target = 6;

	int *p;
	p = twoSum(nums, 5, target);

	printf("nums[%d] = %d, nums[%d] = %d\n", p[0], nums[p[0]], p[1], nums[p[1]]);
	free(p);

	return 0;
}
