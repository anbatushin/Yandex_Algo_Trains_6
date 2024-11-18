<div class="problem-statement"><div class="header"><h1 class="title">F. Сумма тройных произведений</h1><table><tr class="time-limit"><td class="property-title">Ограничение времени</td><td>2&nbsp;секунды</td></tr><tr class="memory-limit"><td class="property-title">Ограничение памяти</td><td>512Mb</td></tr><tr class="input-file"><td class="property-title">Ввод</td><td colspan="1">стандартный ввод или input.txt</td></tr><tr class="output-file"><td class="property-title">Вывод</td><td colspan="1">стандартный вывод или output.txt</td></tr></table></div><h2></h2><div class="legend">
    <p>
        Задана последовательность из n чисел aᵢ. Найдите число
<p>
    $$\sum_{1 \leq i < j < k \leq n} a_i * a_j * a_k$$
</p>


Поскольку число может получиться слишком большим, требуется посчитать его по модулю 1 000 000 007 (1000000007).
    </p></div><h2>Формат ввода</h2><div class="input-specification">
    <p>
    В первой строке дано одно целое число n (3 ≤ n ≤ 10⁶).

Во второй строке даны n целых чисел aᵢ (0 ≤ aᵢ ≤ 10⁶).
</p></div><h2>Формат вывода</h2><div class="output-specification"><p>
    Выведите требуемое число по модулю 1 000 000 007.
</p></p></div><h3>Пример 1</h3><table class="sample-tests"><thead><tr><th>Ввод</th><th>Вывод</th></tr></thead><tbody><tr><td><pre>3
1 2 3
</pre></td><td><pre>6
</pre></td></tr></tbody></table><h3>Пример 2</h3><table class="sample-tests"><thead><tr><th>Ввод</th><th>Вывод</th></tr></thead><tbody><tr><td><pre>4
0 5 6 7
</pre></td><td><pre>210
</pre></td></tr></tbody></table>
