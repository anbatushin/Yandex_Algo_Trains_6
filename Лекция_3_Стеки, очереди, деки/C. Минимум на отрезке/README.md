<div class="problem-statement"><div class="header"><h1 class="title">C. Минимум на отрезке</h1><table><tr class="time-limit"><td class="property-title">Ограничение времени</td><td>1&nbsp;секунда</td></tr><tr class="memory-limit"><td class="property-title">Ограничение памяти</td><td>64Mb</td></tr><tr class="input-file"><td class="property-title">Ввод</td><td colspan="1">стандартный ввод или input.txt</td></tr><tr class="output-file"><td class="property-title">Вывод</td><td colspan="1">стандартный вывод или output.txt</td></tr></table></div><h2></h2><div class="legend">
<p>
    Рассмотрим последовательность целых чисел длины n. По ней с шагом 1 двигается «окно» длины k, то есть сначала в «окне» видны первые k чисел, на следующем шаге в «окне» уже будут находиться k чисел, начиная со второго, и так далее до конца последовательности. Требуется для каждого положения «окна» определить минимум в нём.

</p>
</div><h2>Формат ввода</h2><div class="input-specification">
<p>
В первой строке входных данных содержатся два натуральных числа n и k (n ≤ 150000, k ≤ 10000, k ≤ n) — длины последовательности и «окна», соответственно. На следующей строке находятся n чисел — сама последовательность.

</p>
</div><h2>Формат вывода</h2><div class="output-specification">
<p>
Выходные данные должны содержать n − k + 1 строк — минимумы для каждого положения «окна».
</p></div><h2>Пример</h2><table class="sample-tests"><thead><tr><th>Ввод</th><th>Вывод</th></tr></thead><tbody><tr><td><pre>7 3
1 3 2 4 5 3 1
</pre></td><td><pre>1
2
2
3
1
</pre></td></tr></tbody></table><h2>Примечания</h2><div class="notes"><p>Обратите внимание, что решение с непосредственным подсчётом минимума для каждого положения окна не пройдёт по времени.</p></div>
