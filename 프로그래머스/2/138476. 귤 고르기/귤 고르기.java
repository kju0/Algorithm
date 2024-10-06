import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int N = tangerine.length;
        int answer = 0;
        HashMap<Integer, Integer> cnt = new HashMap<>();
        
        for (int i=0; i<N; i++) {
            if (cnt.containsKey(tangerine[i])){
                cnt.replace(tangerine[i], cnt.get(tangerine[i])+1);
            }
            else cnt.put(tangerine[i], 1);
        }
        // 우선순위 큐 생성 (value 기준 내림차순)
        PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>(
            new Comparator<Map.Entry<Integer, Integer>>() {
                @Override
                public int compare(Map.Entry<Integer, Integer> a, Map.Entry<Integer, Integer> b) {
                    return Integer.compare(b.getValue(), a.getValue());  // value 기준 내림차순
                }
            }
        );

        // HashMap의 모든 Entry를 우선순위 큐에 추가
        pq.addAll(cnt.entrySet());

        // 우선순위 큐에서 값 꺼내기 (value가 큰 순서대로 출력됨)
        while (!pq.isEmpty()) {
            if (k<=0) break;
            
            Map.Entry<Integer, Integer> entry = pq.poll();
            //System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
            answer += 1;
            k -= entry.getValue();
        }
        
        
        

        return answer;
    }
}