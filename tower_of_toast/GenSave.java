import java.math.BigInteger;
import java.util.ArrayList;


public class GenSave {

    static final int GAME_SIZE = 40;

    public static ArrayList<BigInteger> getPrimes(int n) {
        ArrayList<BigInteger> primes = new ArrayList<BigInteger>();
        BigInteger currentNumber = BigInteger.ONE.add(BigInteger.ONE);		
        while (primes.size() < n) {
            if (currentNumber.isProbablePrime(1000000)) {
                primes.add(currentNumber);
            }
            currentNumber = currentNumber.add(BigInteger.ONE);
        }
        return primes;
    }


    public static BigInteger genSaveWin() 
    {
        ArrayList<BigInteger> primes = getPrimes(GAME_SIZE);
        BigInteger output = BigInteger.ONE;

        for (int i = 0; i < primes.size(); i++) {
            output = output.multiply(primes.get(i));
        }

        return output;
    }

    public static void main(String[] args) {
        BigInteger win_pole = genSaveWin();

        System.out.println(win_pole);
    }


}
 

