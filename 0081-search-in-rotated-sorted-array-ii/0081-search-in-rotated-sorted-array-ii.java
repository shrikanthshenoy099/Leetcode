class Solution {
    public boolean search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            // If target is found, return true
            if (nums[mid] == target) {
                return true;
            }

            // Handle duplicates: when left, mid, and right all have the same value,
            // we cannot determine which half is sorted. Shrink the search space.
            if (nums[left] == nums[mid] && nums[mid] == nums[right]) {
                left++;
                right--;
            } 
            // Check if the left half is sorted
            else if (nums[left] <= nums[mid]) {
                // Check if the target lies within the sorted left half
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } 
            // Otherwise, the right half must be sorted
            else {
                // Check if the target lies within the sorted right half
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        return false;
    }
}