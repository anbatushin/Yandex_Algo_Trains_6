<div class="problem-statement"><div class="header"><h1 class="title">E. Значение арифметического выражения</h1><table><tr class="time-limit"><td class="property-title">Ограничение времени</td><td>1&nbsp;секунда</td></tr><tr class="memory-limit"><td class="property-title">Ограничение памяти</td><td>256Mb</td></tr><tr class="input-file"><td class="property-title">Ввод</td><td colspan="1">стандартный ввод или input.txt</td></tr><tr class="output-file"><td class="property-title">Вывод</td><td colspan="1">стандартный вывод или output.txt</td></tr></table></div><h2></h2><div class="legend">
<p>
Задано числовое выражение. Необходимо вычислить его значение или установить, что оно содержит ошибку. В выражении могут встречаться знаки сложения, вычитания, умножения, скобки и пробелы (пробелов внутри чисел быть не должно). Приоритет операций стандартный. Все числа в выражении целые и по модулю не превосходят 2 × 10⁹. Также гарантируется, что все промежуточные вычисления также не превосходят 2 × 10⁹.

</p>
</div><h2>Формат ввода</h2><div class="input-specification">
<p>
В первой строке вводится выражение. Его длина не превосходит 100 знаков. После выражения идет переход на новую строчку.

</p>
</div><h2>Формат вывода</h2><div class="output-specification">
<p>
Выведите значение этого выражения или слово "WRONG", если значение не определено.

</p></div><h3>Пример 1</h3><table class="sample-tests"><thead><tr><th>Ввод</th><th>Вывод</th></tr></thead><tbody><tr><td><pre>1+(2*2 - 3)
</pre></td><td><pre>2
</pre></td></tr></tbody></table><h3>Пример 2</h3><table class="sample-tests"><thead><tr><th>Ввод</th><th>Вывод</th></tr></thead><tbody><tr><td><pre>1+a+1
</pre></td><td><pre>WRONG
</pre></td></tr></tbody></table><h3>Пример 3</h3><table class="sample-tests"><thead><tr><th>Ввод</th><th>Вывод</th></tr></thead><tbody><tr><td><pre>1 1 + 2
</pre></td><td><pre>WRONG
</pre></td></tr></tbody></table>
