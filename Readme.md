Brief comparison of three sorting methods on different data sets.

<table class="table">
<thead><tr class="firstrow"><th>Time</th><th>QuickSort</th><th>HeapSort</th><th>BubbleSort</th></tr></thead><tbody>
 <tr><td>Random[]   </td><td>0.037</td><td>0.171</td><td>1.987</td></tr>
 <tr><td>Sorted[]   </td><td>7.549</td><td>0.102</td><td>1.829</td></tr>
 <tr><td>Rev-Sorted[]  </td><td>4.420</td><td>0.098</td><td>2.032</td></tr>
</tbody></table>

This quick experiment lets us pick out the best and worst cases.
Especially for QuickSort we could prove that it is very ineffective with sorted or reverse-sorted data sets. 

Each function was run with list of 5k elements. Time count by cProfile, displayed in seconds.
