

```java
import java.util.Arrays;

public class trashQuestion {
  static double findGrantsCap(double[] arr, double bg) {
    // your code goes here
    Arrays.sort(arr);
    int idx = 0;
    double res = 0;
    while (idx < arr.length - 1) {
      double tmp = bg;
      for (int i = 0; i <= idx; i++) {
        tmp -= arr[i];
      }
      if (tmp < 0) { 
        idx++;
        continue;
      }
      tmp = tmp / (arr.length - idx - 1);
      // System.out.println(idx+":"+tmp);
      boolean flag = true;
      for (int i = idx + 1; i < arr.length; i++) {
        if (tmp > arr[i]) flag = false;
      }
      if (flag)
        res = Math.max(res, tmp);
      idx++;
    }
    
    return Math.max(res, bg / (arr.length));
    
  }

  public static void main(String[] args) {
    // double[] arr2 = new double[]{2, 50, 100, 120, 1000};
    double[][] testArr = new double[][]{{2,4,6}, {2,100,50,120,167}, {2,100,50,120,1000}, {21,100,50,120,130,110}, {210,200,150,193,130,110,209,342,117}};
    double[] bgArr = new double[]{3, 400, 190, 140, 1530};
    for (int i = 0; i <= testArr.length; i++) {
      double tmpRes = findGrantsCap(testArr[i], bgArr[i]);
      System.out.println(tmpRes);
    }

    /*
     *  Input: [2,4,6], 3,Expected: 1,Actual: 1.0
        Test Case #3
        Input: [2,100,50,120,167], 400,Expected: 128,Actual: 1.0
        Test Case #4
        Input: [2,100,50,120,1000], 190,Expected: 47,Actual: 1.0
        Test Case #5
        Input: [21,100,50,120,130,110], 140,Expected: 23.8,Actual: 1.0
        Test Case #6
        Input: [210,200,150,193,130,110,209,342,117], 1530,Expected: 211,Actual: 1.0
     * 
     */
  }
}
 
```
