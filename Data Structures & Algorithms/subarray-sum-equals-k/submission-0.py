from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Map to store the frequency of each prefix sum seen so far: {prefix_sum: frequency}
        # Base case {0: 1}: represents an empty prefix before index 0.
        # This handles cases where a valid subarray starts right at index 0 (curr_sum == k).
        prefix_map = {0: 1}
        
        curr_sum = 0  # Running sum from index 0 to the current index
        total_subarrays = 0  # Count of subarrays that sum to k

        for num in nums:
            # 1. Expand the running total to include the current element
            curr_sum += num

            # 2. Check if there is an earlier prefix we can "chop off".
            # Equation: earlier_prefix + k = curr_sum  ==>  earlier_prefix = curr_sum - k
            needed_prefix = curr_sum - k
            
            # If that earlier prefix exists, every occurrence of it marks the start of
            # a distinct valid subarray ending at the current index.
            if needed_prefix in prefix_map:
                total_subarrays += prefix_map[needed_prefix]

            # 3. Record the current running prefix sum into the map for future iterations
            # (Always do this AFTER checking step 2 so we don't match an empty subarray when k == 0)
            prefix_map[curr_sum] = prefix_map.get(curr_sum, 0) + 1

        return total_subarrays

        