class Solution
{
public:
  int removeDuplicates(vector<int> &nums)
  {
    if (nums.size() == 0)
      return 0;
    int curr = nums[0];
    int idx = 1;
    for (int i = 1; i < nums.size(); i++)
    {
      if (nums[i] > curr)
      {
        nums[idx] = nums[i];
        curr = nums[i];
        idx++;
      }
    }
    return idx;
  }
};