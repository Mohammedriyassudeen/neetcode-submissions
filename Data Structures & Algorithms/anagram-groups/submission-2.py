class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output_list = {}
        for i , word in enumerate(strs):
            sorted_word = sorted(word)
            output_list[i] = (sorted_word)
            # print(output_list)
        # return output_list
        # for keys, val in output_list.items():
        #     print(keys, val,)

        groups = {}

        for index, chars in output_list.items():

            key = tuple(chars)

            if key not in groups:
                groups[key] = []

            groups[key].append(index)
            
            outer_list = []
        for key, val in groups.items():
            final_list = []
            for size in range(len(val)):
                final_list.append(strs[val[size]])
                # print(final_list)
            outer_list.append(final_list)
            # print(outer_list)
        return outer_list

        