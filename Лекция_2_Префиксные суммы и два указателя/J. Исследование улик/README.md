<div class="problem-statement"><div class="header"><h1 class="title">J. Исследование улик*</h1><table><tr class="time-limit"><td class="property-title">Ограничение времени</td><td>2&nbsp;секунды</td></tr><tr class="memory-limit"><td class="property-title">Ограничение памяти</td><td>256Mb</td></tr><tr class="input-file"><td class="property-title">Ввод</td><td colspan="1">стандартный ввод или input.txt</td></tr><tr class="output-file"><td class="property-title">Вывод</td><td colspan="1">стандартный вывод или output.txt</td></tr></table></div><h2></h2><div class="legend">
<p>
    Бенуа Бланк взялся за расследование загадочного преступления и теперь активно ищет улики, которые помогут ему выйти на настоящего преступника. Как любой уважающий себя детектив, Бенуа Бланк имеет собственный метод поиска истины. Как он любит повторять, его философия заключается в том, что можно просто быть пассивным наблюдателем, и жизнь сама выведет тебя к правде.

Всего Бенуа Бланк собрал n улик и расположил перед собой в ряд; i-я улика в ряду имеет весомость, равную aᵢ. Детектив считает, что наиболее интересными могут оказаться наименее весомые улики, и разработал следующий процесс их исследования.

Сперва Бланк выбирает какую-то улику с номером x и начинает перебирать улики слева от нее. Пока слева от текущей улики находится улика меньшей или равной весомости, Бенуа Бланк перемещается к ней. При этом эксцентричному детективу быстро надоедает однообразие, поэтому он не будет делать больше k перемещений между уликами с одинаковой весомостью.

Например, если весомости улик равны ⟨3, 3, 3, 4, 4, 5⟩, k = 2, и детектив начинает с последней улики, он совершит четыре перемещения влево, после чего остановится.

Улики требуют тщательного изучения, поэтому Бенуа Бланк повторяет процесс m раз, в i-й раз начиная с улики с номером xᵢ. Помогите ему побыстрее определить, на какой улике он остановится в каждом из случаев.

</p>
</div><h2>Формат ввода</h2><div class="input-specification">
<p>
В первой строке дано целое число n — количество улик (1 ≤ n ≤ 4⋅10⁵). Во второй строке через пробел перечислены n целых чисел aᵢ — значения весомости улик в порядке их следования в ряду (1 ≤ aᵢ ≤ 10⁹).

В следующей строке через пробел даны два целых числа m и k — количество экспериментов и максимальное число перемещений между уликами равной весомости (1 ≤ m ≤ 4⋅10⁵; 0 ≤ k ≤ n).

В последней строке через пробел перечислены m целых чисел xᵢ — номера улик, с которых Бенуа Бланк будет начинать исследование (1 ≤ xᵢ ≤ n).

</p>
</div><h2>Формат вывода</h2><div class="output-specification">
<p>
Выведите через пробел m целых чисел от 1 до n — номера улик, на которых остановится детектив в каждом из экспериментов.
</p></div><h3>Пример 1</h3><table class="sample-tests"><thead><tr><th>Ввод</th><th>Вывод</th></tr></thead><tbody><tr><td><pre>6
3 3 3 4 4 5
4 2
3 4 5 6
</pre></td><td><pre>1 1 2 2 
</pre></td></tr></tbody></table><h3>Пример 2</h3><table class="sample-tests"><thead><tr><th>Ввод</th><th>Вывод</th></tr></thead><tbody><tr><td><pre>7
1 5 7 2 10 10 6
7 0
1 2 3 4 5 6 7
</pre></td><td><pre>1 1 1 4 4 6 7 
</pre></td></tr></tbody></table>
