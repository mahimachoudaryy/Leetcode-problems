"""
Group Anagrams
Time Complexity: O(n^2 * k log k)
Space Complexity: O(n * k)
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr=[]
        for i in strs:
            arr.append(sorted(i))
        st=[]
        visited=[0]*len(strs)
        for j in range(len(arr)):
            if(visited[j]==1):
                continue
            ans=[]
            for k in range(j,len(arr)):
                if(arr[j]==arr[k] and visited[k]==0):
                    ans.append(strs[k])
                    visited[k]=1
            st.append(ans)
        return st
