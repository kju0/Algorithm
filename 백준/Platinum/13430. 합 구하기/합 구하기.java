import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static final int MODULO = 1_000_000_007;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int k = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        // 분자와 분모를 계산합니다.
        long num1 = 1;
        long num2 = 1;

        // 분자: n(n+1)(n+2)...(n+k)
        for (int i = 0; i <= k; i++) {
            num1 = num1 * (n + i) % MODULO;
        }

        // 분모: (k+1)!
        for (int i = 1; i <= k+1; i++) {
            num2 = num2 * i % MODULO;
        }

        // 분모의 모듈로 역원을 계산합니다.
        long result = num1 * modInverse(num2, MODULO) % MODULO;
        
        System.out.println(result);
    }

    // 모듈로 역원 계산을 위한 함수
    private static long modInverse(long a, long mod) {
        return power(a, mod - 2, mod);
    }

    // 거듭제곱 함수
    private static long power(long base, long exp, long mod) {
        long result = 1;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = result * base % mod;
            }
            base = base * base % mod;
            exp >>= 1;
        }
        return result;
    }
}
