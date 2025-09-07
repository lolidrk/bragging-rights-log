
class Solution {
public:
    int romanToInt(string s) {
        // unordered_map<char, int> character_dict = {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};
        int character_dict[256] = {};
        character_dict['I'] = 1;
        character_dict['V'] = 5;
        character_dict['X'] = 10;
        character_dict['L'] = 50;
        character_dict['C'] = 100;
        character_dict['D'] = 500;
        character_dict['M'] = 1000;

        char current_char, next_char;
        int curr, nex, num, final_num = 0;
        for (int i = 0; i < s.size(); i++){
            // current_char = s[i];
            // next_char = s[i+1];
            // auto it = character_dict.find(current_char); 
            // curr = it -> second;

            curr = character_dict[s[i]];
            nex = (i + 1 < s.size() ? character_dict[s[i+1]] : 0);

            // if ( i + 1 < s.size()){
            //     it = character_dict.find(next_char);
            //     nex = it -> second;
            // }
            // else nex = 0;
            if (curr < nex){
                num = nex - curr;
                i++;
            }
            else num = curr;

            final_num += num;
        }
        
        return final_num;
    }
};
