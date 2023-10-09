class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int p1 = 0;
        int size = nums.size();
        int p2 = size - 1;
        vector<pair<int, int>> newNums = {};
        
        for (int i = 0; i < size; i++) {
            newNums.push_back({nums[i], i});
        }
        sort(newNums.begin(), newNums.end());

        while (p2 > p1) {
            int sum = newNums[p2].first + newNums[p1].first;
            if (sum == target) {
                vector<int> ans = {newNums[p1].second, newNums[p2].second};
                return ans;
            } else if (sum < target) {
                p1 = p1 + 1;
            } else {
                p2 = p2 - 1;
            }
        }

        // Handle the case when no valid pair is found
        return {}; // Return an empty vector to indicate no solution
    }
};
