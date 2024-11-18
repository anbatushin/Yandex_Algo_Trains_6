<div class="problem-statement"><div class="header"><h1 class="title">A. Префиксные суммы</h1><table><tr class="time-limit"><td class="property-title">Ограничение времени</td><td>1&nbsp;секунда</td></tr><tr class="memory-limit"><td class="property-title">Ограничение памяти</td><td>256Mb</td></tr><tr class="input-file"><td class="property-title">Ввод</td><td colspan="1">стандартный ввод или input.txt</td></tr><tr class="output-file"><td class="property-title">Вывод</td><td colspan="1">стандартный вывод или output.txt</td></tr></table></div><h2></h2><div class="legend">
<p>По данной последовательности <i>a<sub>1</sub>, a<sub>2</sub>, …, a<sub>n</sub></i> вычислите последовательность её префиксных сумм <i>b<sub>1</sub>, b<sub>2</sub>, …, b<sub>n</sub></i>, где</p>

<p>
    $$b_j = \sum_{i=1}^j a_i$$
</p>
    
</p></div><h2>Формат ввода</h2><div class="input-specification">
    <p>В первой строке дано целое число <i>n</i> (<i>1 &le; n &le; 10<sup>3</sup></i>) — количество элементов в последовательности <i>a</i>. Во второй строке дано <i>n</i> целых чисел <i>a<sub>1</sub>, a<sub>2</sub>, …, a<sub>n</sub></i> (<i>|a<sub>i</sub>| &le; 10<sup>6</sup></i>) — элементы последовательности.</p>
    
</p></div><h2>Формат вывода</h2><div class="output-specification">
<p>Выведите <i>n</i> целых чисел <i>b<sub>1</sub>, b<sub>2</sub>, …, b<sub>n</sub></i> — последовательность префиксных сумм для последовательности <i>a</i>.</p>

</p></div><h2>Пример</h2><table class="sample-tests"><thead><tr><th>Ввод</th><th>Вывод</th></tr></thead><tbody><tr><td><pre>5
10 -4 5 0 2
</pre></td><td><pre>10 6 11 11 13 
</pre></td></tr></tbody></table>
