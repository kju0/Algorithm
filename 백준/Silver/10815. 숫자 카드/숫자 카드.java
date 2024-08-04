import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.Stream;

public class Main {
    static int N, M;
    static int[] sNumbers;
    static int[] checkNumbers;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // N과 상근이의 숫자 카드 배열 입력
        N = Integer.parseInt(br.readLine());
        sNumbers = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        // M과 확인해야 할 숫자 배열 입력
        M = Integer.parseInt(br.readLine());
        checkNumbers = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        // 상근이의 숫자 카드 배열 정렬
        Arrays.sort(sNumbers);

        // 정답을 저장할 StringBuilder
        StringBuilder sb = new StringBuilder();

        // 각 확인 숫자에 대해 이진 검색 수행
        for (int i = 0; i < M; i++) {
            if (binarySearch(sNumbers, checkNumbers[i])) {
                sb.append("1 ");
            } else {
                sb.append("0 ");
            }
        }

        // 결과 출력
        System.out.println(sb.toString().trim());
    }

    // 이진 검색 함수
    public static boolean binarySearch(int[] arr, int target) {
        int start = 0;
        int end = arr.length - 1;

        while (start <= end) {
            int mid = (start + end) / 2;

            if (arr[mid] == target) {
                return true;
            } else if (arr[mid] < target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        return false;
    }
}
