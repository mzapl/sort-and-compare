<table class="table">
<thead><tr class="firstrow"><th>Time</th><th>QuickSort</th><th>HeapSort</th><th>BubbleSort</th></tr></thead><tbody>
 <tr><td>Random[]   </td><td>0.037</td><td>0.171</td><td>1.987</td></tr>
 <tr><td>Sorted[]   </td><td>7.549</td><td>0.102</td><td>1.829</td></tr>
 <tr><td>Rev-Sorted[]  </td><td>4.420</td><td>0.098</td><td>2.032</td></tr>
</tbody></table>

<h1> example output </h1>

Recursion limit set:  10000
 ------------------------------ 
quickSort(example, 0, size) sortedArr
         12517500 function calls (12507502 primitive calls) in 7.549 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    7.549    7.549 <string>:1(<module>)
 12502499    1.264    0.000    1.264    0.000 funcs.py:1(swap)
     4999    6.277    0.001    7.540    0.002 funcs.py:24(partition)
   9999/1    0.009    0.000    7.549    7.549 funcs.py:34(quickSort)
        1    0.000    0.000    7.549    7.549 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 ------------------------------ 
 ------------------------------ 
heapSort(example, size) sortedArr
         190253 function calls (134335 primitive calls) in 0.102 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.101    0.101 <string>:1(<module>)
    63416    0.010    0.000    0.010    0.000 funcs.py:4(left)
63416/7498    0.078    0.000    0.098    0.000 funcs.py:41(heapify)
        1    0.001    0.001    0.011    0.011 funcs.py:56(heapBuild)
        1    0.002    0.002    0.101    0.101 funcs.py:61(heapSort)
    63416    0.010    0.000    0.010    0.000 funcs.py:7(right)
        1    0.000    0.000    0.102    0.102 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 ------------------------------ 
 ------------------------------ 
bubbleSort(example) sortedArr
         5 function calls in 1.829 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.829    1.829 <string>:1(<module>)
        1    1.829    1.829    1.829    1.829 funcs.py:13(bubbleSort)
        1    0.000    0.000    1.829    1.829 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 ------------------------------ 
 ------------------------------ 
quickSort(example, 0, size) reversedArr
         6270004 function calls (6260004 primitive calls) in 4.420 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    4.420    4.420 <string>:1(<module>)
  6255000    0.646    0.000    0.646    0.000 funcs.py:1(swap)
     5000    3.765    0.001    4.411    0.001 funcs.py:24(partition)
  10001/1    0.009    0.000    4.420    4.420 funcs.py:34(quickSort)
        1    0.000    0.000    4.420    4.420 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 ------------------------------ 
 ------------------------------ 
heapSort(example, size) reversedArr
         190304 function calls (134371 primitive calls) in 0.098 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.098    0.098 <string>:1(<module>)
    63433    0.011    0.000    0.011    0.000 funcs.py:4(left)
63433/7500    0.074    0.000    0.095    0.000 funcs.py:41(heapify)
        1    0.001    0.001    0.012    0.012 funcs.py:56(heapBuild)
        1    0.002    0.002    0.098    0.098 funcs.py:61(heapSort)
    63433    0.010    0.000    0.010    0.000 funcs.py:7(right)
        1    0.000    0.000    0.098    0.098 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 ------------------------------ 
 ------------------------------ 
bubbleSort(example) reversedArr
         5 function calls in 2.032 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    2.032    2.032 <string>:1(<module>)
        1    2.032    2.032    2.032    2.032 funcs.py:13(bubbleSort)
        1    0.000    0.000    2.032    2.032 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 ------------------------------ 
 ------------------------------ 
quickSort(example, 0, size) randomArr
         50326 function calls (43554 primitive calls) in 0.037 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.037    0.037 <string>:1(<module>)
    40164    0.004    0.000    0.004    0.000 funcs.py:1(swap)
     3386    0.027    0.000    0.032    0.000 funcs.py:24(partition)
   6773/1    0.005    0.000    0.037    0.037 funcs.py:34(quickSort)
        1    0.000    0.000    0.037    0.037 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 ------------------------------ 
 ------------------------------ 
heapSort(example, size) randomArr
         189398 function calls (133765 primitive calls) in 0.171 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.171    0.171 <string>:1(<module>)
    63131    0.011    0.000    0.011    0.000 funcs.py:4(left)
63131/7498    0.144    0.000    0.168    0.000 funcs.py:41(heapify)
        1    0.001    0.001    0.012    0.012 funcs.py:56(heapBuild)
        1    0.003    0.003    0.171    0.171 funcs.py:61(heapSort)
    63131    0.013    0.000    0.013    0.000 funcs.py:7(right)
        1    0.000    0.000    0.171    0.171 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 ------------------------------ 
 ------------------------------ 
bubbleSort(example) randomArr
         5 function calls in 1.987 seconds
   Ordered by: standard name
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.987    1.987 <string>:1(<module>)
        1    1.987    1.987    1.987    1.987 funcs.py:13(bubbleSort)
        1    0.000    0.000    1.987    1.987 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 ------------------------------ 
