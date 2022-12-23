import java.util.Arrays;
import java.util.HashMap;

public class SmallestWindow
{
    //Function to find the smallest window in the string s consisting
    //of all the characters of string p.
    public static String smallestWindowSol(String s, String p)
    {
        Integer result = Integer.MAX_VALUE;
        Integer resultLeftPointer = 0;
        Integer resultRightPointer = 0;
        char[] testChars = p.toCharArray();
        char[] sourceChars = s.toCharArray();
        HashMap<Character, Integer> testCounterMap = new HashMap<Character, Integer>();
        HashMap<Character, Integer> windowMap = new HashMap<Character, Integer>();
        if (p.equals("")){
            return "-1";
        }
        // Populate the test string char count map
        for (char testChar : testChars) {
            testCounterMap.put(testChar, testCounterMap.getOrDefault(testChar, 0) + 1);
        }
        // the count of substring we have with equal length
        Integer have = 0;
        Integer need = testCounterMap.size();
        Integer leftIndex = 0;
        // iterrate the window
        for (int rightIndex = 0; rightIndex < sourceChars.length; rightIndex++) {
            char curr = sourceChars[rightIndex];
            // log the char count map in window string chars
            windowMap.put(curr, windowMap.getOrDefault(curr, 0) + 1);

            // if the count of the item (char) in the test str map is equals the item (char) in the window 
            // update the have, since the string chars we need is meet already
            if (testCounterMap.containsKey(curr) && windowMap.containsKey(curr) && windowMap.get(curr).equals(testCounterMap.get(curr))){
                have += 1;
            }

            // if the have same substring amount we need
            // we will pop from the left
            while (have == need) {
                if (rightIndex - leftIndex + 1 < result) {
                    result = rightIndex - leftIndex + 1;
                    resultLeftPointer = leftIndex;
                    resultRightPointer = rightIndex;
                }
                windowMap.replace(sourceChars[leftIndex], windowMap.get(sourceChars[leftIndex]) - 1);
                // if the poping item is in the test substring, and if it is having a length less than need reduce have
                if (testCounterMap.containsKey(sourceChars[leftIndex]) && windowMap.get(sourceChars[leftIndex]) < testCounterMap.get(sourceChars[leftIndex])){
                    have -= 1;
                }
                leftIndex += 1;
            }

        }

        return result != Integer.MAX_VALUE  ? String.copyValueOf(Arrays.copyOfRange(sourceChars, resultLeftPointer, resultRightPointer + 1)) : "-1";
    }

    public static void main(String[] args) {
        System.out.println(SmallestWindow.smallestWindowSol("zoomlazapzo", "oza"));
    }
}