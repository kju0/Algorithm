import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int[] elements) {
        List<Integer> arr = Arrays.stream(elements)
                                    .boxed()
                                    .collect(Collectors.toList());
        
        for (int i=0; i<elements.length; i++){
            arr.add(elements[i]);
        }
        
        Set<Integer> sumSet = new HashSet<>();
        for (int size=1; size<elements.length+1; size++){
            for (int target=0; target<elements.length; target++){
                int sum = arr.subList(target, target+size).stream()
                      .mapToInt(Integer::intValue)
                      .sum();
                sumSet.add(sum);
            }
        }
        
        return sumSet.size();
    }
}