/* way more to do, just started. Seems like 
C++ would be better too */ 
class Solution {
    public int reverse(int x) {
        // 2^31 = 2147483648
        
        String x_string = String.valueOf(x)
        int length = x_string.length();

        if (length > 10) {
            return 0;
        }
        else if (length == 10) {
            if (x % 10 > 2) {
                return 0;
            }
            else if (x % 10 == 2) {
                for (int i = length - 1; i >= 0; i--) {
                    if x_string
                }
            }
        }
    }
}