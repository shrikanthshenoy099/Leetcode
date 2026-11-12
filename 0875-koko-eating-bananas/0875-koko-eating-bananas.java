class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int low = 1;
        int high = getMax(piles);
        int ans = high;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            if (canFinish(piles, mid, h)) {
                ans = mid;          // Valid speed, try to find a smaller one on the left
                high = mid - 1;     
            } else {
                low = mid + 1;      // Too slow, need a higher speed on the right
            }
        }
        
        return ans;
    }
    
    // Helper to find the maximum pile size
    private int getMax(int[] piles) {
        int max = 0;
        for (int pile : piles) {
            if (pile > max) {
                max = pile;
            }
        }
        return max;
    }
    
    // Helper to check if Koko can finish all piles within h hours at speed k
    private boolean canFinish(int[] piles, int k, int h) {
        long totalHours = 0; // Use long to prevent potential integer overflow
        for (int pile : piles) {
            totalHours += (pile + k - 1) / k; // Ceiling division formula
        }
        return totalHours <= h;
    }
}